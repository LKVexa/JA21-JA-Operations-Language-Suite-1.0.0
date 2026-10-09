#!/usr/bin/env python3
from __future__ import annotations
import argparse, gzip, json
from collections import Counter
p=argparse.ArgumentParser(description="Inspect the JA21 JA Operations technical corpus")
p.add_argument("corpus")
p.add_argument("--feature")
p.add_argument("--level")
p.add_argument("--class-name",dest="class_name")
p.add_argument("--limit",type=int,default=10)
a=p.parse_args()
rows=[]
with gzip.open(a.corpus,"rt",encoding="utf-8") as f:
    for line in f:
        r=json.loads(line)
        if a.feature and r.get("feature")!=a.feature: continue
        if a.level and r.get("level")!=a.level: continue
        if a.class_name and r.get("validation_class")!=a.class_name: continue
        rows.append(r)
print(json.dumps({"matches":len(rows),"features":Counter(r["feature"] for r in rows),"levels":Counter(r["level"] for r in rows),"classes":Counter(r["validation_class"] for r in rows)},indent=2,default=dict))
for r in rows[:a.limit]:
    print(f"\n{r['record_id']} {r['feature']} {r['level']} {r['validation_class']}")
    print(r['source'])
