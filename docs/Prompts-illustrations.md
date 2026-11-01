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
