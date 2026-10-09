#!/usr/bin/env python3
from __future__ import annotations
import csv,gzip,hashlib,json,re,sys
from collections import Counter
from pathlib import Path
LEVELS=['beginner', 'intermediate', 'advanced', 'expert', 'compiler', 'runtime', 'optimization', 'validation', 'certification', 'deployment']
EXPECTED={'positive': 400, 'negative': 150, 'boundary': 100, 'integration': 100, 'security': 75, 'performance': 50, 'determinism': 50, 'interoperability': 25, 'recovery': 25, 'certification': 25}
def sha(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()
def balance(src):
    clean=re.sub(r'"(?:\\.|[^"\\])*"','""',src)
    return clean.count("{")-clean.count("}")
def main():
    root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
    errors=[]
    corpus=root/"corpus/technical/JA21_JAOPS_TECHNICAL_CORPUS_10000.jsonl.gz"
    with gzip.open(corpus,"rt",encoding="utf-8") as f: records=[json.loads(x) for x in f if x.strip()]
    if len(records)!=10000: errors.append(f"corpus count {len(records)}")
    if len({r['record_id'] for r in records})!=10000: errors.append("record IDs not unique")
    if [r['sequence'] for r in records]!=list(range(1,10001)): errors.append("sequence not continuous")
    for r in records:
        if sha(r['source'])!=r['ast']['origin_hash']: errors.append(f"source hash {r['record_id']}")
        if not r.get('_suite_publication',{}).get('source_sha256_verified'): errors.append(f"publication hash {r['record_id']}")
    scripts=list((root/'scripts').rglob('*.jaops'))
    if len(scripts)!=1000: errors.append(f"script count {len(scripts)}")
    with (root/'catalogs/SCRIPT_CATALOG.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
    if len(rows)!=1000: errors.append(f"catalog count {len(rows)}")
    if Counter(r['validation_class'] for r in rows)!=Counter(EXPECTED): errors.append('class distribution')
    if Counter(r['level'] for r in rows)!=Counter({x:100 for x in LEVELS}): errors.append('level distribution')
    if len({r['feature'] for r in rows})!=32: errors.append('feature coverage')
    recmap={r['record_id']:r for r in records}
    for row in rows:
        p=root/row['file']
        if not p.is_file(): errors.append(f"missing {row['file']}"); continue
        src=p.read_text(encoding='utf-8')
        if src!=recmap[row['record_id']]['source']: errors.append(f"source mismatch {row['record_id']}")
        if sha(src)!=row['source_sha256']: errors.append(f"script hash {row['record_id']}")
        for token in ('ja source','module ','use Operations','workspace ','emit '):
            if token not in src: errors.append(f"missing {token} in {row['record_id']}")
        if balance(src)!=0: errors.append(f"brace imbalance {row['record_id']}")
    tb=(root/'textbook/JA21_JA_OPERATIONS_LANGUAGE_TEXTBOOK.md').read_text(encoding='utf-8')
    chapters=len(re.findall(r'^# Chapter \d+:',tb,flags=re.M))
    if chapters!=22: errors.append(f"textbook chapters {chapters}")
    result={'suite':'JA21_JAOPS_1.0.0','records':len(records),'scripts':len(scripts),'catalog_rows':len(rows),
            'features':len({r['feature'] for r in rows}),'textbook_chapters':chapters,
            'max_relative_path':max(len(p.relative_to(root).as_posix()) for p in root.rglob('*')),
            'errors':errors,'status':'pass' if not errors else 'fail'}
    print(json.dumps(result,indent=2)); return 0 if not errors else 1
if __name__=='__main__': raise SystemExit(main())
