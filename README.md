# Líštička 🦊 🇸🇰 🇫🇷

**Apprendre le français en s'amusant — pour les enfants slovaques de 8 à 12 ans**

Un cours de français pour enfants slovaquophones, construit sur le framework [Slovingo](https://github.com/lstux/Slovingo). C'est la version « enfants » du cours adulte [Slovingo-fr-sk](https://github.com/lstux/Slovingo-fr-sk), et la cousine du cours de slovaque pour enfants [Slovingo-sk-fr-kids](https://github.com/lstux/Slovingo-sk-fr-kids) (même univers, sens inverse).

L'app s'appelle **Líštička**, le petit nom affectueux slovaque du renard (*líška* est le mot courant, *líštička* le diminutif). Dans le cours cousin, la hase Andrea porte de son côté le petit nom *zajka*. 🦊

## Le monde

Tout se passe dans les **Alpes françaises**, avec la région lyonnaise en arrière-plan. Toi, tu es une petite *líška* (renard ou renarde : le texte ne le précise jamais) qui vient d'arriver dans la montagne. Tu apprends le français avec tes nouveaux voisins, qui sont des animaux.

## Les personnages

| Avatar | Personnage |
|---|---|
| 🦊 | Toi, la *líška* qui vient d'arriver dans les Alpes (prénom saisi au début du cours) |
| 🐰 | Andrea, une hase (*zajačica*), ton amie. Même duo qu'en sk-fr-kids |
| 🐹 | Léa, une marmotte (*svišť*) |
| 🐐 | Hugo, un bouquetin (*kozorožec*), l'ami de Léa |

*Prénoms de Léa et Hugo : propositions, à valider. D'autres animaux pourront rejoindre la bande (adultes, commerçants, gardien du parc…).*

## Les séries

| N° | Série | Thème |
|---|---|---|
| 00 | Kit prežitia | Bonjour, merci, se présenter |
| 01 | Rodina | La famille |
| 02 | Doma | Chez soi |
| 03 | Jedlo | Les repas |
| 04 | Dedina | Le village |
| 05 | Zvieratá | Les animaux des Alpes |
| 06 | Hry | Les jeux |
| 07 | Čas a čísla | Les heures et les nombres |

## Règles de ce cours (sens inverse de sk-fr-kids)

- Les explications sont en **slovaque** : on les met en `{{sk:…}}`, lues par la voix slovaque. Le français, lui, n'a pas de préfixe (langue apprise).
- Aucun mot français dans un `{{sk:…}}`, et aucune lettre isolée en `{{…}}` (la voix lirait son nom).
- Le **genre de 🦊** reste neutre : en slovaque, pas de participe passé ni d'adjectif accordé pour l'enfant ; en français, pas d'adjectif ou de participe accordé non plus.
- Chaque fiche a son « 🇫🇷 Francúzsky kútik » (un fait vérifiable sur la France).
- Le tutoiement entre enfants ; le *vous* arrive avec les adultes.
- Les noms de fichiers des séries sont en français (comme dans Slovingo-fr-sk).

## Structure

```
slovingo-fr-sk-kids/
├── docs/        # Relectures et notes de travail
├── md/          # Fiches (SMD, Slovingo Markdown)
├── exercises/   # Exercices écrits à la main (JSON), à venir
├── img/         # Illustrations
└── lang.json    # Configuration (français ← slovaque)
```

## État

Pilote relu : Introduction (5 fiches) et Kit prežitia (3 fiches + extra). Voir [docs/Relecture-pilote-2026-10.md](./docs/Relecture-pilote-2026-10.md). Les images sont encore des `TODO_img`, et le slovaque est à faire relire par un locuteur natif.

## Dépôts liés

- [lstux/Slovingo](https://github.com/lstux/Slovingo) : le framework
- [lstux/Slovingo-fr-sk](https://github.com/lstux/Slovingo-fr-sk) : le cours adulte
- [lstux/Slovingo-sk-fr-kids](https://github.com/lstux/Slovingo-sk-fr-kids) : le cours de slovaque pour enfants
