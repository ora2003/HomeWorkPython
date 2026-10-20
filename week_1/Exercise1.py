import numpy as np

a = np.array([[10, 100, 200],
              [50, 150, 250]], dtype=np.uint8)

# Expression, Prediction, Actual result
table = [
    ("a.dtype", "int", str(a.dtype)),
    ("a.shape", "(3*2)", str(a.shape)),
    ("a.ndim", "(2D)", str(a.ndim)),
    ("a.size", "2*3", str(a.size)),
    ("a.nbytes", "8", str(a.nbytes)),
    ("a[1, 2]", "250", str(a[1, 2])),
    ("a + 10", "Add 10 to each value", str(a + 10)),
    ("a - 20", "Subtract 20 from each value", str(a - 20)),
    ("a * 2", "Multiply each value by 2", str(a * 2)),
    ("a[0, 1]", "100", str(a[0, 1])),
    ("a.max()", "250", str(a.max())),
    ("a.max(axis=0)", "50 150 250", str(a.max(axis=0))),
    ("a.max(axis=1)", "[200 250]", str(a.max(axis=1)))
]

print(f"{'Expression':<18} {'Prediction':<30} Result")
print("-" * 80)

for expression, prediction, result in table:
    print(f"{expression:<18} {prediction:<30} {result}")

