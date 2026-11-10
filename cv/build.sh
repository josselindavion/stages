#!/usr/bin/env bash
# Compile toutes les versions du CV dans cv/pdf/ et signale les \todo restants.
# Usage : ./build.sh            (toutes les versions)
#         ./build.sh finance_en (une seule)
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p pdf build
versions=("${@:-finance_fr finance_en defense_fr}")
for v in ${versions[@]}; do
  latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build "cv_$v.tex" >/dev/null \
    || { echo "ERREUR de compilation : cv_$v (voir build/cv_$v.log)"; exit 1; }
  cp "build/cv_$v.pdf" "pdf/cv_$v.pdf"
  pages=$(pdfinfo "pdf/cv_$v.pdf" 2>/dev/null | awk '/^Pages/{print $2}')
  echo "ok  pdf/cv_$v.pdf  (${pages:-?} page(s))"
  [ "${pages:-1}" -gt 1 ] && echo "    ATTENTION : plus d'une page"
done
n=$(grep -o '\\todo{' blocs/*.tex | wc -l)
echo "Champs \\todo restants dans blocs/ : $n"
