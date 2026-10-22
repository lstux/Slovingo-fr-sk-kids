#!/usr/bin/env python3
"""Installe d'un coup toutes les photos listées dans docs/Images-a-telecharger.md.

Pour chaque ligne des tableaux :
  1. récupère la photo (dossier --manual s'il contient le fichier, sinon
     téléchargement depuis la page Pexels / Unsplash / Pixabay) ;
  2. la réduit à 1200 px de large (ratio conservé, pas de recadrage) dans img/ ;
  3. remplace la ligne « @ TODO_img/... » de la fiche par « @ img/<fichier> | légende » ;
  4. ajoute une ligne dans img/credits.md.

Relançable à volonté : ce qui est déjà fait est ignoré.
Les photos qui échouent (Pixabay bloque souvent les robots) sont listées à la fin :
télécharge-les à la main, nomme-les comme indiqué, mets-les dans un dossier
et relance avec --manual <dossier>.

Usage : python3 tools/install_images.py [--manual DIR] [--only Rodina] [--dry-run]
Prérequis : ImageMagick (« convert ») et curl.
Optionnel (recommandé si les sites répondent 403) : clés API gratuites, en variables d'environnement
  PEXELS_API_KEY, UNSPLASH_ACCESS_KEY, PIXABAY_API_KEY
"""
import argparse, glob, os, re, shutil, subprocess, sys, tempfile, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC = os.path.join(ROOT, "docs", "Images-a-telecharger.md")
CREDITS = os.path.join(ROOT, "img", "credits.md")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"

# Préfixe du tableau -> préfixe du nom de fiche dans md/
PREFIX = {
    "Intro": "00_Introduction_0", "Kit": "10_Series_00_KitSurvie_0",
    "Rodina": "10_Series_01_Rodina_0", "Doma": "10_Series_02_Doma_0",
    "Jedlo": "10_Series_03_Jedlo_0", "Dedina": "10_Series_04_Dedina_0",
    "Zvieratá": "10_Series_05_Zvierata_0", "Hry": "10_Series_06_Hry_0",
    "Čas": "10_Series_07_Cas_0",
}

CAPTIONS = {
    "Intro 1": "{{sk:Líška obyčajná – to si ty!}}",
    "Intro 3": "{{sk:Zajac belavý – to je Andrea}}",
    "Intro 4": "{{sk:Svišť stojí a pískaním varuje ostatných}}",
    "Intro 5": "{{sk:Ovce na počítanie – jedna po druhej}}",
    "Kit 2": "{{sk:Svišť Léa si pochutnáva na kvetine}}",
    "Kit 3": "{{sk:Zajac Andrea v zimnom kožúšku}}",
    "Kit 4": "{{sk:Kozorožec Hugo na skale}}",
    "Rodina 1": "{{sk:Rodina svišťov}}",
    "Rodina 2": "{{sk:Svište v národnom parku Vanoise}}",
    "Rodina 3": "{{sk:Kozorožce: súrodenci}}",
    "Rodina 4": "{{sk:Kamzíky vo francúzskych Alpách}}",
    "Rodina 5": "{{sk:Horská chata: u babky Odile}}",
    "Rodina 6": "{{sk:Francúzske Alpy pri východe slnka}}",
    "Doma 2": "{{sk:Vnútro drevenej chaty}}",
    "Doma 3": "{{sk:Topánky a batoh pripravené na túru}}",
    "Doma 4": "{{sk:Svišť v tráve pri svojej nore}}",
    "Jedlo 1": "{{sk:Raňajky pod holým nebom}}",
    "Jedlo 2": "{{sk:Krava sa pasie na alpskej lúke}}",
    "Jedlo 3": "{{sk:Divoké čučoriedky}}",
    "Jedlo 4": "{{sk:Palacinky – mňam!}}",
    "Jedlo 5": "{{sk:Cesto v miske: Hugo robí palacinky}}",
    "Jedlo 6": "{{sk:Piknik: croissanty, syr a ovocie}}",
    "Dedina 1": "{{sk:Horská dedina v údolí}}",
    "Dedina 3": "{{sk:Autobus na horskej ceste}}",
    "Dedina 4": "{{sk:Ukazovateľ smerov na križovatke}}",
    "Dedina 5": "{{sk:Monsieur Hérisson v tráve}}",
    "Dedina 6": "{{sk:Bazilika Fourvière v Lyone}}",
    "Zvieratá 1": "{{sk:Kamzík v tráve}}",
    "Zvieratá 2": "{{sk:Pastiersky pes zháňa ovce}}",
    "Zvieratá 3": "{{sk:Svišť stojí a stráži}}",
    "Zvieratá 4": "{{sk:Zasnežené vrcholy pri Sallanches}}",
    "Zvieratá 5": "{{sk:Orol skalný v horách}}",
    "Zvieratá 6": "{{sk:Sliepky: kvok, kvok!}}",
    "Hry 1": "{{sk:Lopta v tráve}}",
    "Hry 2": "{{sk:Sedačková lanovka nad snehom}}",
    "Hry 3": "{{sk:Svište sa hrajú}}",
    "Hry 4": "{{sk:Svište spolu v tráve}}",
    "Hry 5": "{{sk:Karty na drevenom stole}}",
    "Hry 6": "{{sk:Dedina pod snehom: čas na sánkovanie!}}",
    "Čas 1": "{{sk:Ovce pri jazere: koľko ich vidíš?}}",
    "Čas 2": "{{sk:Euromince na dreve}}",
    "Čas 3": "{{sk:Stádo na ceste}}",
    "Čas 4": "{{sk:Hodiny na zvonici v dedine}}",
    "Čas 5": "{{sk:Vlak na stanici v Chamonix}}",
    "Čas 6": "{{sk:Horská dedina za súmraku}}",
}


BROWSER_HEADERS = [
    "User-Agent: " + UA,
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language: fr-FR,fr;q=0.9,en;q=0.8",
    "Upgrade-Insecure-Requests: 1",
    "Sec-Fetch-Dest: document", "Sec-Fetch-Mode: navigate", "Sec-Fetch-Site: none", "Sec-Fetch-User: ?1",
]


def get(url, binary=False, headers=None):
    """Téléchargement via curl (moins bloqué que urllib). Erreur détaillée avec URL + code HTTP."""
    with tempfile.NamedTemporaryFile(delete=False) as t:
        out = t.name
    cmd = ["curl", "-sL", "--compressed", "--max-time", "90", "-o", out, "-w", "%{http_code}", url]
    for h in (headers if headers is not None else BROWSER_HEADERS):
        cmd += ["-H", h]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True)
        code = r.stdout.strip()
        if r.returncode != 0 or not code.startswith("2"):
            raise RuntimeError(f"HTTP {code or '?'} (curl {r.returncode}) pour {url}")
        data = open(out, "rb").read()
    finally:
        os.unlink(out)
    return data if binary else data.decode("utf-8", "replace")


def last_number(page):
    m = re.search(r"(\d+)/?$", page.rstrip("/"))
    return m.group(1) if m else None


def via_api(page):
    """Utilise l'API du site si une clé est donnée par variable d'environnement.
    Retourne (url_image, auteur) ou None."""
    import json
    if "pexels.com" in page and os.environ.get("PEXELS_API_KEY"):
        j = json.loads(get(f"https://api.pexels.com/v1/photos/{last_number(page)}",
                           headers=["Authorization: " + os.environ["PEXELS_API_KEY"]]))
        return j["src"].get("large2x") or j["src"]["original"], j.get("photographer")
    if "unsplash.com" in page and os.environ.get("UNSPLASH_ACCESS_KEY"):
        pid = page.rstrip("/").split("/")[-1][-11:]
        h = ["Authorization: Client-ID " + os.environ["UNSPLASH_ACCESS_KEY"]]
        j = json.loads(get(f"https://api.unsplash.com/photos/{pid}", headers=h))
        try:
            get(j["links"]["download_location"], headers=h)  # exigé par les règles de l'API
        except Exception:
            pass
        return j["urls"]["raw"] + ("&" if "?" in j["urls"]["raw"] else "?") + "w=1600&q=80", j["user"]["name"]
    if "pixabay.com" in page and os.environ.get("PIXABAY_API_KEY"):
        j = json.loads(get(f"https://pixabay.com/api/?key={os.environ['PIXABAY_API_KEY']}&id={last_number(page)}",
                           headers=["Accept: application/json"]))
        hit = j["hits"][0]
        return hit["largeImageURL"], hit.get("user")
    return None


def og_image(html):
    m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', html) \
        or re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html)
    return m.group(1).replace("&amp;", "&") if m else None


def direct_url(page):
    api = via_api(page)
    if api:
        return api[0], "AUTEUR:" + (api[1] or "")
    html = get(page)
    img = og_image(html)
    if not img:
        raise RuntimeError("pas d'image trouvée dans la page")
    if "pexels.com" in page:
        img = img.split("?")[0] + "?auto=compress&cs=tinysrgb&w=1600"
    elif "unsplash.com" in page:
        img = re.sub(r"([?&])w=\d+", r"\1w=1600", img)
    return img, html


def author_from_page(html):
    if html.startswith("AUTEUR:"):
        return html[7:] or None
    m = re.search(r"Photo by ([^<\"|]+?) on Pexels", html)
    return m.group(1).strip() if m else None


def resize(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    subprocess.run(["convert", src, "-auto-orient", "-resize", "1200x>", "-strip",
                    "-quality", "82", dst], check=True)


def licence(page):
    if "pexels.com" in page: return "Licence Pexels"
    if "pixabay.com" in page: return "Licence Pixabay"
    if "unsplash.com" in page: return "Licence Unsplash"
    return "à compléter"


def parse_rows():
    rows = []
    for line in open(DOC, encoding="utf-8"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or not re.search(r"`[^`]+\.jpg`", cells[1]) or not cells[2].startswith("http"):
            continue
        m = re.match(r"(\S+)\s+(\d+)$", cells[0])
        label = f"{m.group(1)} {int(m.group(2))}" if m else cells[0]
        rows.append(dict(label=label, file=cells[1].strip("`"), page=cells[2],
                         author=cells[3], note=cells[4]))
    return rows


def sheet_for(label):
    m = re.match(r"(\S+)\s+(\d+)$", label)
    if not m or m.group(1) not in PREFIX:
        return None
    hits = glob.glob(os.path.join(ROOT, "md", PREFIX[m.group(1)] + m.group(2) + "_*.md"))
    return hits[0] if len(hits) == 1 else None


def credit_row(usage, file, page, author, lic):
    return f"| {usage} | `{file}` | [page]({page}) | {author} | {lic} |\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manual", help="dossier où tu as mis des photos téléchargées à la main")
    ap.add_argument("--only", help="ne traiter que les fiches dont le nom commence ainsi (ex. Rodina)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    credits = open(CREDITS, encoding="utf-8").read()
    failed, done = [], 0
    for r in parse_rows():
        label, fname, page = r["label"], r["file"], r["page"]
        is_banner = fname.startswith("style_")
        if a.only and not label.startswith(a.only) and not (is_banner and a.only == "style"):
            continue
        sheet = None if is_banner else sheet_for(label)
        caption = None if is_banner else CAPTIONS.get(label)
        if not is_banner and (not sheet or not caption):
            failed.append((label, "fiche ou légende introuvable"))
            continue
        dst = os.path.join(ROOT, "img", fname)
        author = r["author"]
        try:
            if os.path.exists(dst):
                # photo déjà déposée dans img/ (à la main) : on la réduit si elle dépasse 1200 px
                w = subprocess.run(["identify", "-format", "%w", dst], capture_output=True, text=True).stdout
                if w.strip().isdigit() and int(w) > 1200 and not a.dry_run:
                    resize(dst, dst)
            else:
                manual = os.path.join(a.manual, fname) if a.manual else None
                if a.dry_run:
                    print("à faire :", label, fname)
                    continue
                with tempfile.TemporaryDirectory() as tmp:
                    raw = os.path.join(tmp, "raw")
                    if manual and os.path.exists(manual):
                        shutil.copy(manual, raw)
                    else:
                        url, html = direct_url(page)
                        open(raw, "wb").write(get(url, binary=True, headers=["User-Agent: " + UA, "Accept: image/*,*/*;q=0.8"]))
                        if html.startswith("AUTEUR:") and html[7:]:
                            author = html[7:]  # nom exact donné par l'API
                        elif "à lire" in author:
                            author = author_from_page(html) or "à compléter"
                    resize(raw, dst)
            if "à lire" in author:
                author = "à compléter"
            if a.dry_run:
                continue
            if sheet:
                text = open(sheet, encoding="utf-8").read()
                new = re.sub(r"^@ TODO_img/\S+ \| TODO.*$", f"@ img/{fname} | {caption}",
                             text, count=1, flags=re.M)
                if new != text:
                    open(sheet, "w", encoding="utf-8").write(new)
            if f"`{fname}`" not in credits:
                usage = f"Bannière {fname[6:-4]}" if is_banner else f"{label} · {os.path.basename(sheet)[:-3]}"
                credits += credit_row(usage, fname, page, author, licence(page))
            done += 1
            print("ok :", label, fname)
        except Exception as e:  # réseau, protection anti-robot, etc.
            failed.append((label, f"{fname} : {e}"))
    if not a.dry_run:
        open(CREDITS, "w", encoding="utf-8").write(credits)
    print(f"\n{done} photo(s) installée(s).")
    if failed:
        print("\nÀ télécharger à la main (nomme le fichier comme indiqué, puis --manual DIR) :")
        for label, why in failed:
            print(" -", label, "→", why)


if __name__ == "__main__":
    main()
