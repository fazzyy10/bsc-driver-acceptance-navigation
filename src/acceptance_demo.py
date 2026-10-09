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
    """Fit least-squares with an intercept and return in-sample R²."""
    X, y = np.asarray(X, dtype=float), np.asarray(y, dtype=float)
    if X.ndim != 2 or y.ndim != 1 or X.shape[0] != y.shape[0]:
        raise ValueError("Mismatched predictor/outcome dimensions")
    if not (np.isfinite(X).all() and np.isfinite(y).all()):
        raise ValueError("Only finite inputs allowed")
    design = np.column_stack([np.ones(len(X)), X])
    coef, *_ = np.linalg.lstsq(design, y, rcond=None)
    fitted = design @ coef
    ss_total = float(np.sum((y - y.mean()) ** 2))
    if ss_total <= 0:
        raise ValueError("R² undefined for a constant outcome")
    return {
        "intercept": float(coef[0]),
        "coefficients": coef[1:],
        "r_squared_in_sample": float(1 - np.sum((y - fitted) ** 2) / ss_total),
    }


def pearson(x, y) -> float:
    """Compute sample Pearson r, without a significance test."""
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    if x.ndim != 1 or y.ndim != 1 or len(x) != len(y) or len(x) < 3:
        raise ValueError("Expected equal-sized 1D arrays with three or more observations")
    if x.std() == 0 or y.std() == 0:
        raise ValueError("Correlation undefined for a constant variable")
    return float(np.corrcoef(x, y)[0, 1])
