# Stages de césure — juin 2027 → août 2028

Année de césure avant la 3A (Mines de Paris). Deux stages d'environ 6 mois :

| Créneau | Secteur | Période visée | Candidatures |
|---|---|---|---|
| S1 | Finance de marché (3 familles, voir ci-dessous) | juin 2027 → oct.–nov. 2027 | **maintenant → janv. 2027** |
| S2 | Ingénierie défense | nov. 2027–janv. 2028 → mai–juin 2028 | printemps 2027 (≥ 6 mois avant, à cause de l'habilitation) |

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
candidatures.csv   une ligne par candidature (pipeline)
contacts.csv       recruteurs, alumni, profs, référents
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
