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
Prérequis : ImageMagick (commande « convert »).
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
    "Intro 1": "Le renard roux : c'est toi, l'apprenant !",
    "Intro 3": "Le lièvre variable : c'est Andrea",
    "Intro 4": "La marmotte siffle pour prévenir les autres",
    "Intro 5": "Des moutons à compter, un par un",
    "Kit 2": "Léa la marmotte grignote une fleur",
    "Kit 3": "Andrea le lièvre, en robe d'hiver",
    "Kit 4": "Hugo le bouquetin sur son rocher",
    "Rodina 1": "Une famille de marmottes",
    "Rodina 2": "Des marmottes dans le parc national de la Vanoise",
    "Rodina 3": "Des bouquetins : frères et sœurs",
    "Rodina 4": "Des chamois dans les Alpes françaises",
    "Rodina 5": "Un chalet d'alpage : chez Mamie Odile",
    "Rodina 6": "Les Alpes françaises au lever du soleil",
    "Doma 2": "L'intérieur d'un chalet en bois",
    "Doma 3": "Des bottes et un sac, prêts pour la rando",
    "Doma 4": "Une marmotte dans l'herbe, près de son terrier",
    "Jedlo 1": "Le petit déjeuner en plein air",
    "Jedlo 2": "Une vache qui broute dans l'alpage",
    "Jedlo 3": "Des myrtilles sauvages",
    "Jedlo 4": "Des crêpes : miam !",
    "Jedlo 5": "De la pâte dans un saladier : on prépare les crêpes de Hugo",
    "Jedlo 6": "Un pique-nique : croissants, fromage et fruits",
    "Dedina 1": "Un village de montagne dans sa vallée",
    "Dedina 3": "Un bus sur une route de montagne",
    "Dedina 4": "Un panneau de directions à un carrefour",
    "Dedina 5": "Monsieur Hérisson dans l'herbe",
    "Dedina 6": "La basilique de Fourvière, à Lyon",
    "Zvieratá 1": "Un chamois dans l'herbe",
    "Zvieratá 2": "Un chien de berger qui rassemble des moutons",
    "Zvieratá 3": "Une marmotte debout, qui guette",
    "Zvieratá 4": "Les sommets enneigés vus de Sallanches",
    "Zvieratá 5": "Un aigle royal dans les montagnes",
    "Zvieratá 6": "Des poules : cot cot !",
    "Hry 1": "Un ballon dans l'herbe",
    "Hry 2": "Un télésiège au-dessus de la neige",
    "Hry 3": "Des marmottes qui jouent",
    "Hry 4": "Des marmottes ensemble sur l'herbe",
    "Hry 5": "Un jeu de cartes sur une table en bois",
    "Hry 6": "Un village sous la neige : c'est l'heure de la luge !",
    "Čas 1": "Des moutons au bord d'un lac : combien en vois-tu ?",
    "Čas 2": "Des pièces d'euros posées sur du bois",
    "Čas 3": "Un troupeau sur la route",
    "Čas 4": "L'horloge d'un clocher de village",
    "Čas 5": "Un train dans la gare de Chamonix",
    "Čas 6": "Un village de montagne au crépuscule",
}


def get(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    return data if binary else data.decode("utf-8", "replace")


def og_image(html):
    m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', html) \
        or re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html)
    return m.group(1).replace("&amp;", "&") if m else None


def direct_url(page):
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
            if not os.path.exists(dst):
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
                        open(raw, "wb").write(get(url, binary=True))
                        if "à lire" in author:
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
