#!/usr/bin/env python3
"""Vue rapide : pipeline des candidatures + échéances proches."""
import argparse
import csv
import re
from collections import Counter, defaultdict
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORDRE = ["cible", "a_envoyer", "envoyee", "test", "entretiens", "offre", "refus", "abandon"]
LIGNE_DEADLINE = re.compile(r"^- \[( |x)\] (\d{4}-\d{2}-\d{2}) — (.+)$")


def parse_date(s):
    try:
        return date.fromisoformat(s.strip()) if s and s.strip() else None
    except ValueError:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jours", type=int, default=21, help="horizon des échéances")
    args = ap.parse_args()
    today = date.today()
    horizon = today + timedelta(days=args.jours)

    with open(ROOT / "candidatures.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    print(f"=== Pipeline ({len(rows)} candidatures) — {today} ===")
    par_secteur = defaultdict(Counter)
    for r in rows:
        par_secteur[r["secteur"]][r["statut"]] += 1
    for secteur, c in sorted(par_secteur.items()):
        detail = "  ".join(f"{s}:{c[s]}" for s in ORDRE if c[s])
        print(f"  {secteur:<8} {detail}")

    actives = [r for r in rows if r["statut"] in ("test", "entretiens", "offre")]
    if actives:
        print("\n=== En cours ===")
        for r in actives:
            print(f"  {r['id']} {r['boite']} — {r['statut']}")

    echeances = []
    for r in rows:
        d = parse_date(r["deadline"])
        if d and r["statut"] in ("cible", "a_envoyer") and d <= horizon:
            echeances.append((d, f"Deadline candidature {r['id']} {r['boite']}"))
    dl = ROOT / "deadlines.md"
    if dl.exists():
        for line in dl.read_text(encoding="utf-8").splitlines():
            m = LIGNE_DEADLINE.match(line.strip())
            if m and m.group(1) == " ":
                d = parse_date(m.group(2))
                if d and d <= horizon:
                    echeances.append((d, m.group(3)))

    print(f"\n=== Échéances d'ici {args.jours} jours (et retards) ===")
    if not echeances:
        print("  rien")
    for d, quoi in sorted(echeances):
        tag = "RETARD " if d < today else ""
        print(f"  {tag}{d}  {quoi}")


if __name__ == "__main__":
    main()
