# Illustrations IA de Líštička — prompts Gemini

Même univers que Zajko (`Slovingo-sk-fr-kids`), en sens inverse : le renard et Andrea sont les mêmes, et on les retrouve dans les **Alpes françaises**. On réutilise leurs planches ; on ajoute **Léa**, **Hugo**, **Mamie Odile** et **Monsieur Hérisson**.

Style : dessin animé 2D classique, animaux debout qui portent des vêtements, formes rondes et douces (enfants de 8 à 11 ans), décors peints reconnaissables.

## Méthode (comme pour Zajko, mais avec Gemini)

1. **Planche des héros** : nouvelle conversation Gemini, joindre les images indiquées, coller le prompt. Garder la meilleure et la déposer dans `docs/illustrations/planche-heros.jpg`. Même chose pour la planche des seconds rôles (`planche-seconds-roles.jpg`).
2. **Défauts à surveiller** : Andrea qui redevient une lapine (oreille gauche pliée, bande blanche, pas de cils), un animal du cours qui redevient « un personnage connu », des yeux réduits à de gros points noirs, des humains plus réalistes que les animaux. Si un personnage dérive : « Keep the characters exactly as in the attached model sheet. »
3. **Si Gemini refuse** : nouvelle conversation et on enlève la phrase qui coince. Ne jamais citer de film, de studio ou de personnage connu.
4. **Ensuite** : les prompts des scènes (une couverture, une image par série), écrits sur le même modèle que dans `Slovingo-sk-fr-kids/docs/Prompts-illustrations.md`, avec ces planches jointes.

**Fichiers de référence** (dans les autres repos) : `Slovingo-sk-fr-friends/esp32/zajko-quest/art/characters/fox-reference.png` et `andrea-reference.png` ; `Slovingo-sk-fr-kids/docs/illustrations/planche-heros.jpg` et `planche-seconds-roles.jpg`.

## Les personnages

| | Personnage | Description à garder |
|---|---|---|
| 🦊 | Le renard (toi) | **identique à Zajko** : sweat bleu roi, sac à dos aux bretelles jaunes, jean, baskets blanches |
| 🐰 | Andrea, 11 ans | **identique à Zajko** : hase tachetée, oreille gauche pliée, T-shirt vert menthe |
| 🐹 | Léa, 9 ans | marmotte, fourrure sable à ventre crème, veste jaune moutarde, écharpe rouge, legging vert. Différente de Katka (violette, écouteurs) |
| 🐐 | Hugo, 8 ans | bouquetin, petit frère de Léa, le plus petit ; petites cornes courbées, casquette rouge à l'envers, T-shirt rayé bleu et blanc |
| 🦌 | Mamie Odile | chamois âgée, gilet lavande à col de dentelle, tablier à carreaux, panier |
| 🦔 | Monsieur Hérisson | hérisson et facteur, casquette et veste bleu foncé, besace en cuir (sans logo) |

*Les âges de Léa (9 ans) et Hugo (8 ans) viennent de la fiche `Rodina_02`. Les vêtements sont des propositions.*

---

## Planche des héros (renard, Andrea, Léa, Hugo)

**À joindre** : `fox-reference.png`, `andrea-reference.png` (dossier `esp32/zajko-quest/art/characters/` du repo friends), puis `docs/illustrations/planche-heros.jpg` de ce repo (validée).

```
Character model sheet for a friendly animated film for children, on a plain light background. Four young animal characters standing side by side at the same scale, each shown front view and three-quarter view, full body, with a few facial expressions (smiling, surprised, shy). They are friends living in the French Alps.

The first attached image is the design reference for the fox; the second is the design reference for Andrea; the third attached image is an existing model sheet that shows these two characters, plus a bear cub and a marmot, redrawn as young children. Keep the fox and Andrea EXACTLY as in the third image (same species, colours, clothes, proportions, style). Do NOT draw the bear cub or the marmot from the third image: they are replaced by the two new characters below, drawn in the same style and at the same level of roundness.

1. The red fox, a 10-year-old (exactly as in the attached sheet): royal-blue hoodie, backpack with yellow straps, navy jeans, white sneakers.
2. Andrea, an 11-year-old hare girl (a real hare, not a rabbit): exactly as in the attached sheet — speckled brown-grey fur, white blaze, long ears with black tips where her LEFT ear is folded down, no eyelashes, mint-green T-shirt, yellow cross-body bag, denim shorts, red sneakers.
3. Léa, a 9-year-old alpine marmot girl, a bit smaller than the fox: sandy-brown fur with a cream belly, small round ears, a broad flat face with two visible front teeth, a short bushy tail in plain sandy-brown (no stripes), a lively, chatty look, wearing a mustard-yellow hooded jacket, a red scarf and green leggings with brown boots.
4. Hugo, an 8-year-old young alpine ibex (bouquetin), Léa's little brother, the smallest of the four (he reaches the fox's shoulder): a grey-tan coat with a pale belly, short stocky legs with small dark hooves, two short backward-curved horns just starting to grow, a mischievous grin, wearing a red cap turned backwards, a blue-and-white striped T-shirt and grey shorts.

Height: the hare's ears aside, the fox and Andrea are about the same height; Léa is slightly shorter; Hugo is the smallest.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Warm, natural light. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

## Planche des seconds rôles (Mamie Odile, Monsieur Hérisson)

**À joindre** : `docs/illustrations/planche-seconds-roles.jpg` de ce repo (validée, sans le groupe du milieu), pour le style seulement.

```
Character model sheet for a friendly animated film for children, on a plain light background. Two adult animal characters standing side by side, each shown front view and three-quarter view, full body, kind and warm. The attached image is an existing model sheet of other adult characters: use it ONLY as the reference for the drawing style (line, colours, shading, level of detail), and do not draw any of its characters.

1. Mamie Odile, an elderly chamois (a goat-antelope of the Alps: tan-brown coat, a dark stripe on each side of the face, short slim horns hooked backwards at the tip, a white muzzle and chin), the children's grandmother, wearing a lavender knitted cardigan with a white lace collar and a checked apron, holding a woven basket. Warm, welcoming smile.
2. Monsieur Hérisson, a middle-aged hedgehog and village postman (brown spines, round belly, a small moustache, round friendly face), wearing a dark-blue peaked cap and jacket, a brown leather postal satchel across his chest (no logo, no text) and holding a letter. Polite and a bit formal.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. No text, no letters, no logos, no watermark.
```

---

## Scènes des séries (fiche 05 de chaque série, plus le kit 03)

Une illustration par série, dans la fiche 05 (le dialogue), comme pour Zajko. Chaque prompt est complet. **Joindre la planche des héros** (et la planche des seconds rôles quand elle est indiquée), **puis la photo de référence** : soit une image déjà dans `img/`, soit le lien Commons de la fiche.

### Kit 03 · Salut, Andrea ! ✅ faite le 8 novembre (Gemini)

Fiche `10_Series_00_KitSurvie_03_dialogue.md` → `img/illus_00_kit.jpg`

**À joindre** : planche des héros + photo de référence : img/kit-02-marmotte-fleurs.jpg

```
Use the attached model sheet for the characters (keep them exactly as designed). Use the attached photo as the reference for the place.

Scene: A bright mountain path in summer, flanked by flowers and spruce trees. The young fox, with his backpack, meets Andrea the hare for the first time: they stand face to face, a little shy, the fox waving, Andrea smiling with her long ears upright. Léa the marmot peeks from behind a rock, curious.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, rounded friendly shapes. Soft, painterly background with few small details, so the characters stand out, but the place stays recognisable. Landscape format 16:9. No text, no letters, no logos, no watermark. Andrea wears her mint-green T-shirt; Léa wears her mustard-yellow jacket, red scarf and green leggings.
```

### Rodina 05 · Chez Mamie Odile ✅ faite le 8 novembre (Gemini ; cornes de Mamie à revoir si besoin : trop longues pour une chamois)

Fiche `10_Series_01_Rodina_05_chez-mamie.md` → `img/illus_01_rodina.jpg`

**À joindre** : planche des héros + planche des seconds rôles + photo de référence : img/rodina-05-chalet-alpage.jpg

```
Use the attached model sheets for the characters (keep them exactly as designed). Use the attached photo as the reference for the place.

Scene: A high alpine pasture on a sunny afternoon, with an old wooden chalet with flowers on its windowsill. Madame Odile, the elderly chamois grandmother, opens her arms to welcome the young fox, who waves; Léa the marmot and Hugo the young ibex stand beside them, smiling. Mountain peaks in the background.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, rounded friendly shapes. Soft, painterly background with few small details, so the characters stand out, but the place stays recognisable. Landscape format 16:9. No text, no letters, no logos, no watermark. Léa wears her mustard-yellow jacket, red scarf and green leggings; Hugo wears his blue-and-white striped T-shirt and red cap worn backwards.
```

### Doma 05 · Chez Andrea ✅ faite le 8 novembre (Gemini, sans photo ; baskets du renard rouges, sacoche d'Andrea absente)

Fiche `10_Series_02_Doma_05_chez-andrea.md` → `img/illus_02_doma.jpg`

**À joindre** : planche des héros + photo de référence : European_Hare.jpg (Commons, lien dans la fiche)

```
Use the attached model sheet for the characters (keep them exactly as designed). Use the attached photo as the reference for the place.

Scene: At the edge of a sunny meadow, a cosy wooden house with a round door stands under a big tree. Andrea the hare, in her mint-green T-shirt, stands in the doorway and invites the young fox in with a smile; Léa the marmot is behind her, waving. Wildflowers in the grass.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, rounded friendly shapes. Soft, painterly background with few small details, so the characters stand out, but the place stays recognisable. Landscape format 16:9. No text, no letters, no logos, no watermark. Andrea wears her mint-green T-shirt; Léa wears her mustard-yellow jacket, red scarf and green leggings.
```

### Jedlo 05 · Les crêpes de Hugo ✅ faite le 8 novembre (Gemini, sans photo)

Fiche `10_Series_03_Jedlo_05_les-crepes-de-hugo.md` → `img/illus_03_jedlo.jpg`

**À joindre** : planche des héros + photo de référence : img/jedlo-05-pate-saladier.jpg

```
Use the attached model sheet for the characters (keep them exactly as designed). Use the attached photo as the reference for the place.

Scene: Inside a warm wooden kitchen of a mountain chalet. Hugo the young ibex, in his striped T-shirt and red cap, stands proudly on a small stool at the table and flips a golden pancake in a pan. A stack of golden pancakes on a plate, and next to it two small jars: one of chocolate spread and one of jam (no labels). The fox, Andrea and Léa sit at the table and watch with excitement; the fox licks his lips. A window showing snowy peaks.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, rounded friendly shapes. Soft, painterly background with few small details, so the characters stand out, but the place stays recognisable. Landscape format 16:9. No text, no letters, no logos, no watermark. Andrea wears her mint-green T-shirt; Léa wears her mustard-yellow jacket, red scarf and green leggings; Hugo wears his blue-and-white striped T-shirt and red cap worn backwards.
```

### Dedina 05 · Pardon, Monsieur ! ✅ faite le 8 novembre (Gemini)

Fiche `10_Series_04_Dedina_05_pardon-monsieur.md` → `img/illus_04_dedina.jpg`

**À joindre** : planche des héros + planche des seconds rôles + photo de référence : img/dedina-05-herisson.jpg

```
Use the attached model sheets for the characters (keep them exactly as designed). Use the attached photo as the reference for the place.

Scene: A small mountain village street with wooden chalets, a stone fountain, a church with a small bell tower, and, further down the street, a bakery with fresh bread in its window. Monsieur Hérisson, the hedgehog postman in his dark-blue cap and satchel, stops to answer and points down the street to the left with a calm, polite gesture; the young fox, hungry and polite, listens with a hand on his tummy, and Andrea the hare stands next to him, listening.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, rounded friendly shapes. Soft, painterly background with few small details, so the characters stand out, but the place stays recognisable. Landscape format 16:9. No text, no letters, no logos, no watermark. Andrea wears her mint-green T-shirt.
```

### Zvieratá 05 · Regarde, un aigle !

Fiche `10_Series_05_Zvierata_05_regarde-un-aigle.md` → `img/illus_05_zvierata.jpg`

**À joindre** : planche des héros + photo de référence : img/zvierata-05-aigle.jpg

```
Use the attached model sheet for the characters (keep them exactly as designed). Use the attached photo as the reference for the place.

Scene: On a rocky mountain ridge with snowy peaks behind, a golden eagle spreads its huge wings above the valley. In the foreground on a grassy slope, the fox points up to the sky while Andrea, Léa and Hugo look up with excitement; Hugo grins and nudges Léa, teasing her, and Léa pretends to be offended. On a rocky slope in the background, a wild chamois jumps from rock to rock (natural coat, no clothes). The eagle is majestic, not scary.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, rounded friendly shapes. Soft, painterly background with few small details, so the characters stand out, but the place stays recognisable. Landscape format 16:9. No text, no letters, no logos, no watermark. Andrea wears her mint-green T-shirt; Léa wears her mustard-yellow jacket, red scarf and green leggings; Hugo wears his blue-and-white striped T-shirt and red cap worn backwards.
```

### Hry 05 · Une partie de cartes

Fiche `10_Series_06_Hry_05_une-partie-de-cartes.md` → `img/illus_06_hry.jpg`

**À joindre** : planche des héros + photo de référence : img/hry-05-cartes.jpg

```
Use the attached model sheet for the characters (keep them exactly as designed). Use the attached photo as the reference for the place.

Scene: Inside a wooden mountain chalet, around a low wooden table in the warm light of a window. The fox, Andrea, Léa and Hugo sit together playing cards. Hugo points at Andrea with a suspicious frown, as if shouting "you cheat!", while Andrea proudly shows her winning card with an innocent smile; Léa laughs, and the fox holds only a few cards and shrugs with a cheerful grin. Cosy, funny mood.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, rounded friendly shapes. Soft, painterly background with few small details, so the characters stand out, but the place stays recognisable. Landscape format 16:9. No text, no letters, no logos, no watermark. Andrea wears her mint-green T-shirt; Léa wears her mustard-yellow jacket, red scarf and green leggings; Hugo wears his blue-and-white striped T-shirt and red cap worn backwards.
```

### Čas 05 · Dépêche-toi !

Fiche `10_Series_07_Cas_05_depeche-toi.md` → `img/illus_07_cas.jpg`

**À joindre** : planche des héros + photo de référence : img/cas-05-train-chamonix.jpg

```
Use the attached model sheet for the characters (keep them exactly as designed). Use the attached photo as the reference for the place.

Scene: A small mountain railway station with a red train waiting on the platform, mountains behind. The fox, Andrea the hare and Léa the marmot stand on the platform next to the open train door, anxious but cheerful; Léa points at the round station clock, which shows ten to three. Hugo the young ibex runs along the platform from the far end, out of breath, with his red cap and a small backpack, waving.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, rounded friendly shapes. Soft, painterly background with few small details, so the characters stand out, but the place stays recognisable. Landscape format 16:9. No text, no letters, no logos, no watermark. Andrea wears her mint-green T-shirt; Léa wears her mustard-yellow jacket, red scarf and green leggings; Hugo wears his blue-and-white striped T-shirt and red cap worn backwards.
```
