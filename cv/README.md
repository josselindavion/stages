# CV

Sources LaTeX, une seule mise en page, trois versions.

```
cvstyle.sty        mise en page commune (ne pas toucher pour le contenu)
blocs/fr.tex       contenu FR, partagé par finance_fr et defense_fr
blocs/en.tex       contenu EN (finance)
cv_finance_fr.tex  banques à Paris
cv_finance_en.tex  Londres / Amsterdam / Zurich / fonds
cv_defense_fr.tex  défense
pdf/               PDF compilés (ceux qu'on envoie)
lettres/           une lettre par candidature, nommée par id (ex. F05_CFM.md)
retours/           revues du CV (recherche + relectures simulées) et plans d'action
```

## Modifier

- Le contenu se change uniquement dans `blocs/fr.tex` et `blocs/en.tex`.
- Dans `fr.tex` : `\pourfinance{...}` ou `\pourdefense{...}` pour du texte présent dans une seule version.
  La section Projets n'apparaît que dans la version finance.
- `\todo{...}` s'affiche en rouge. Il ne doit plus en rester avant l'envoi.
- Macros : `\entree{Organisation}{Dates}{Rôle}{Lieu}`, puis un environnement `points` pour les puces ; `\ligne{Catégorie}{contenu}`.

## Compiler

```bash
./build.sh             # les 3 versions -> pdf/, indique le nb de pages et de \todo restants
./build.sh finance_en  # une seule
```

Il faut `latexmk` (TeX Live). Sinon, Overleaf : importer le dossier `cv/`.

## Règles

- Une page, pas de photo, pas de paragraphe d'accroche.
- Des chiffres dans chaque puce quand c'est possible.
- Quand on envoie une candidature, noter dans `candidatures.csv` la version envoyée (ou le commit).
