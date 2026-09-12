"""Dependency-free multiclass classification metrics."""
from __future__ import annotations
from collections import defaultdict

def report(actual: list[str], predicted: list[str]) -> dict:
    if len(actual) != len(predicted): raise ValueError("length mismatch")
    labels=sorted(set(actual)|set(predicted)); per_class={}
    for label in labels:
        tp=sum(a==label and p==label for a,p in zip(actual,predicted)); fp=sum(a!=label and p==label for a,p in zip(actual,predicted)); fn=sum(a==label and p!=label for a,p in zip(actual,predicted))
        precision=tp/(tp+fp) if tp+fp else 0.0; recall=tp/(tp+fn) if tp+fn else 0.0
        per_class[label]={"precision":precision,"recall":recall,"f1":2*precision*recall/(precision+recall) if precision+recall else 0.0,"support":sum(a==label for a in actual)}
    accuracy=sum(a==p for a,p in zip(actual,predicted))/len(actual) if actual else 0.0
    return {"accuracy":accuracy,"per_class":per_class}
if __name__ == "__main__":
 import json,sys; payload=json.load(sys.stdin); print(json.dumps(report(payload['actual'],payload['predicted']),indent=2,sort_keys=True))
