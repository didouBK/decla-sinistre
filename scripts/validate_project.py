"""Vérifie identifiants, liens, couverture et concordance référentiel/CSV."""
import csv,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'data/referentiel.json').read_text(encoding='utf8'))
ids=[]
for group in ('stories','rules','requirements','tests'):
 ids += [x['id'] for x in d[group]]
assert len(ids)==len(set(ids)), 'Identifiant dupliqué'
for expected,group in [('US-', 'stories'),('RG-','rules'),('REQ-','requirements'),('TC-','tests')]:
 assert all(x['id'].startswith(expected) for x in d[group])
known=set(ids)
for t in d['tests']:
 for link in t['links'].split(';'):
  assert link in known, f"Lien invalide {t['id']} -> {link}"
for r in d['requirements']:
 if r['testable']:
  assert any(r['id'] in t['links'].split(';') for t in d['tests']),f"Exigence sans test: {r['id']}"
assert len(list((ROOT/'tests/features').glob('*.feature')))==8
stories_doc=(ROOT/'docs/ba/user-stories.md').read_text(encoding='utf8')
assert len(re.findall(r'^## US-\d{3}',stories_doc,re.M))==8
assert stories_doc.count('```gherkin')==8
with (ROOT/'docs/qa/matrice-tracabilite.csv').open(encoding='utf8') as f:
 csvtests=list(csv.DictReader(f))
assert [(t['id'],t['title'],t['links']) for t in d['tests']]==[(x['test_id'],x['intitule'],x['liens']) for x in csvtests]
with (ROOT/'docs/pilotage/backlog.csv').open(encoding='utf8') as f: assert sum(x['type']=='Story' for x in csv.DictReader(f))==8
print(f"OK: {len(ids)} identifiants uniques; {len(d['tests'])} tests; {len(d['requirements'])} exigences testables liées; 8 stories et exports cohérents.")
