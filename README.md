# Stages de césure — mai 2027 → sept. 2028

Année de césure avant la 3A (Mines de Paris). Deux stages d'environ 6 mois :

| Créneau | Secteur | Période visée | Candidatures |
|---|---|---|---|
| S1 | Finance / quant / IA | mai–juin 2027 → oct.–nov. 2027 | **maintenant → janv. 2027** |
| S2 | Ingénierie défense | nov. 2027–janv. 2028 → mai–juin 2028 | printemps 2027 (≥ 6 mois avant, à cause de l'habilitation) |

Retour aux Mines (3A) : septembre 2028.

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
