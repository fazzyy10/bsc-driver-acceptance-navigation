"""Fabricated survey-like numbers: research-method demonstration, not the 2022 study."""
from __future__ import annotations
import numpy as np


def fabricate(n: int = 500, seed: int = 2026):
    """Create nine fictional explanatory scores and one fictional outcome."""
    if n < 20:
        raise ValueError("Demonstration requires at least 20 artificial rows")
    rng = np.random.default_rng(seed)
    latent = rng.normal(size=(n, 9))
    X = np.clip(3 + 0.8 * latent + rng.normal(scale=.35, size=(n, 9)), 1, 5)
    y = 0.6 + .37 * X[:, 6] + .31 * X[:, 8] + .12 * X[:, 1] + rng.normal(scale=.45, size=n)
    return X, y


def ols_in_sample(X, y) -> dict:
    """Expose the shared, checked regression implementation for the teaching example."""
    from bsc_public.stats import ols
    fitted = ols(X, y)
    coefficients = np.asarray(fitted["coefficients"], dtype=float)
    return {
        "intercept": float(coefficients[0]),
        "coefficients": coefficients[1:],
        "r_squared_in_sample": fitted["r_squared_in_sample"],
    }

def pearson(x, y) -> float:
    """Compute sample Pearson r, without a significance test."""
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    if x.ndim != 1 or y.ndim != 1 or len(x) != len(y) or len(x) < 3:
        raise ValueError("Expected equal-sized 1D arrays with three or more observations")
    if not (np.isfinite(x).all() and np.isfinite(y).all()):
        raise ValueError("Correlation requires finite observations")
    if x.std() == 0 or y.std() == 0:
        raise ValueError("Correlation undefined for a constant variable")
    return float(np.corrcoef(x, y)[0, 1])
