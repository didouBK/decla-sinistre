import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def test_trace_export_matches_json():
 d=json.loads((ROOT/'data/referentiel.json').read_text(encoding='utf8'))
 with (ROOT/'docs/qa/matrice-tracabilite.csv').open(encoding='utf8') as f: rows=list(csv.DictReader(f))
 assert [(x['id'],x['title'],x['links']) for x in d['tests']]==[(x['test_id'],x['intitule'],x['liens']) for x in rows]
