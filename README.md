# Stages de césure — juin 2027 → août 2028

Année de césure avant la 3A (Mines de Paris). Deux stages d'environ 6 mois :

| Priorité | Secteur | Période | Candidatures |
|---|---|---|---|
| 1 | Finance de marché et finance quantitative (3 familles, voir ci-dessous) | **1re ou 2e moitié de la césure**, selon les offres | **dès maintenant**, en continu |
| 2 | Ingénierie défense | l'autre moitié | ≥ 6 mois avant le début (habilitation) |

« Finance d'abord » est une **priorité, pas un ordre dans le temps** (décision du 15/11) : un stage finance de
janvier à juin 2028 convient aussi bien qu'un stage de juin à novembre 2027 ; la défense prend l'autre créneau.
Retour aux Mines (3A) : septembre 2028.

## Cible finance : trois familles de métiers (décision du 15/11)

Les trois l'intéressent ; on candidate dans les trois, avec cette priorité :

| Priorité | Famille | Exemples | Métier | Maths et entretiens | Format |
|---|---|---|---|---|---|
| 1 | **Activités de marché en banque** (sell side) | SG, BNP Paribas, Natixis, CA-CIB ; banques US et UK à Paris / Londres ; Leonteq et Vontobel (produits structurés, Zurich) | Structuration, trading, strats / quant de desk, sales | Pricing, grecques, Monte Carlo ; entretiens : probas, options, marchés et actualité | Césure de 6 mois standard à Paris |
| 2 | **Recherche quant en fonds** (buy side) | CFM, QRT, Squarepoint, Citadel | Chercher des signaux dans les données, backtester, mettre en production | Statistiques, ML, code ; entretiens : probas, stats, ML, code | Stages longs possibles à Paris (à vérifier par offre) |
| 3 | **Market makers** | Jane Street, Optiver, IMC | Coter en continu et gérer le risque en temps réel | Probas, théorie des jeux, calcul mental rapide ; tests chronométrés | Souvent des stages d'été courts : retenir seulement les offres de ~6 mois |

Ce qui le différencie : la culture financière (produits, marchés, actualité) pour la famille 1, le programme ML de
`quant-ml` pour la famille 2, les probabilités d'entretien quotidiennes pour les trois.
Les appels avec les anciens servent aussi à choisir entre les familles (« à quoi ressemble ta journée ? »).

## Structure

```
candidatures.csv   une ligne par entreprise ciblée : famille, format, calendrier, statut
calendrier_finance.md  quand postuler selon le type d'entreprise (recherche du 15/11) + sources
annuaire_mpa.md    ordre des recherches dans l'annuaire des anciens + personnes trouvées
contacts.csv       recruteurs, alumni, profs, référents
contacts/suivi_anciens.csv  suivi des 126 messages aux anciens (statut, réponse, appel)
deadlines.md       échéances datées + administratif (césure, conventions)
prep/              prépa entretiens (quant, technique défense)
cv/                CV en LaTeX (finance FR/EN, défense FR) + lettres — voir cv/README.md
scripts/status.py  vue rapide : pipeline + deadlines proches
```

## Conventions

- **Statuts** (`candidatures.csv`, colonne `statut`) :
  `cible` → `a_envoyer` → `envoyee` → `test` → `entretiens` → `offre` | `refus` | `abandon`
- **Dates** au format `AAAA-MM-JJ`. Laisser vide si inconnue.
- `nationalite` : exigence connue ou supposée (`FR`, `UE`, `aucune`, `?`). En défense, à vérifier pour chaque offre.
- Le champ `notes` est libre. Pas de virgule nue : mettre la valeur entre guillemets si besoin.

## Usage

```bash
python3 scripts/status.py            # pipeline + deadlines à 21 jours
python3 scripts/status.py --jours 7  # horizon plus court
```
