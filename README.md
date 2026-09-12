# Classification Metrics Workbench

Calculate transparent per-class precision, recall, F1, support, and accuracy from local label pairs.

```bash
cat labels.json | python tool.py
python -m unittest -v
```

This calculates metrics from supplied labels only; it does not train or evaluate a model by itself.
