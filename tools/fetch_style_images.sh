#!/bin/sh
# Réduit des photos de bannière à 1200 px de large (ratio conservé, pas de recadrage).
# Usage : tools/fetch_style_images.sh <dossier-de-telechargements>
# Cherche dans le dossier des fichiers style_<clé>.* et écrit img/style_<clé>.jpg
set -e
SRC="${1:?dossier source}"
mkdir -p img
for key in default basics family house food city animals games time; do
  f=$(ls "$SRC"/style_"$key".* 2>/dev/null | head -n1 || true)
  [ -n "$f" ] || { echo "manquant : style_$key"; continue; }
  convert "$f" -auto-orient -resize 1200x -strip -quality 82 "img/style_$key.jpg"
  echo "ok : img/style_$key.jpg"
done
