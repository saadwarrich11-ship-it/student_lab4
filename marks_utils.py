"""Column standardisation using loops and NumPy."""
import numpy as np

def standardise_loop(data):
    values = np.asarray(data, dtype=float).tolist()
    if not values or not values[0]:
        raise ValueError("Expected nonempty 2-D data")
    n, m = len(values), len(values[0])
    means = [sum(row[j] for row in values) / n for j in range(m)]
    stds = [(sum((row[j] - means[j]) ** 2 for row in values) / n) ** 0.5 for j in range(m)]
    return np.array([[(row[j] - means[j]) / stds[j] if stds[j] else 0.0
                      for j in range(m)] for row in values])

def standardise_np(data):
    values = np.asarray(data, dtype=float)
    means = values.mean(axis=0, keepdims=True)
    stds = values.std(axis=0, keepdims=True)
    return np.divide(values - means, stds, out=np.zeros_like(values), where=stds != 0)
