import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def test_reference_has_expected_counts():
 d=json.loads((ROOT/'data/referentiel.json').read_text(encoding='utf8'))
 assert len(d['stories'])==8 and len(d['rules'])==12 and len(d['tests'])==15
def test_requirement_coverage():
 d=json.loads((ROOT/'data/referentiel.json').read_text(encoding='utf8'))
 for r in d['requirements']:
  assert any(r['id'] in t['links'].split(';') for t in d['tests'])
def test_feature_files_exist():
 assert len(list((ROOT/'tests/features').glob('*.feature')))==8
