# Exercices écrits à la main — séries 01 à 07

42 fiches (6 par série) ont un fichier `exercises/<fiche>.exercises.json`
(mode `replace`, `sync: full`). Ils s'ajoutent aux 5 fichiers de l'introduction.
Total : 799 exercices pour les séries, soit 15 à 23 par fiche.

| Type | Nombre | Rôle |
|------|--------|------|
| listen | 206 | on entend le français, on choisit le sens slovaque parmi 4 phrases proches |
| fill-blank | 179 | un mot manque, avec des pièges choisis à la main |
| order | 187 | remettre la phrase dans l'ordre |
| qcm | 152 | vocabulaire de la fiche |
| match | 75 | associer 4 mots slovaque / français |

## Principes

- Les mots et les phrases viennent de la fiche elle-même (tableaux de vocabulaire
  et cartes). Les bonnes réponses ne testent que ce que l'enfant a vu ; les fausses réponses peuvent contenir un mot courant pas encore enseigné (par exemple l'impératif « choď »), ce qui ne gêne pas.
  La commande `src/sync_exercises.py --lang-dir .` ne signale rien d'obsolète.
- Les fausses réponses ne sont pas tirées au hasard : elles reprennent
  les pièges du cours.
  - Genre et accord : `mon école` / `ma clé`, `grand` / `grande`, `gentil` / `gentille`.
  - Articles partitifs et contractés : `du`, `de la`, `de l'`, `au`, `aux`, `à la`.
  - Prépositions : `en bus` / `à vélo` / `à pied`, `ou` / `où`.
  - Verbes : `je cours` / `ils courent`, `je viens` / `tu viens`.
  - Nombres : 70 à 99, `pol štvrtej` / `et demie`.
- Une fausse réponse n'apparaît jamais déjà dans la phrase à compléter
  (contrôle automatique fait sur les 799 exercices).
- Pas de `[USER_NAME]` dans les exercices : on utilise les phrases
  qui n'en contiennent pas.
- Le renard reste neutre : aucune forme masculine ou féminine pour `[USER_NAME]`.

## À savoir pour la relecture

- Comme le reste du cours, ces exercices n'ont pas été relus par un locuteur natif
  du slovaque. Les phrases erronées des choix (listen, fill-blank) doivent être
  fausses, mais bien formées : c'est à vérifier en priorité.
- Pour modifier une fiche : éditer `md/…`, puis lancer
  `python3 src/sync_exercises.py --lang-dir . --apply` depuis le moteur
  (met à jour les exercices touchés, supprime les exercices périmés).
