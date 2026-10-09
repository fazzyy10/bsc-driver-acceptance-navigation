"""Statistical methods for synthetic illustrations, not the original SPSS analysis."""
from __future__ import annotations
import numpy as np

def cronbach_alpha(items):
    """Alpha for a complete-case item matrix (observations x questions)."""
    a = np.asarray(items, dtype=float)
    if a.ndim != 2 or a.shape[1] < 2 or a.shape[0] < 3:
        raise ValueError("Require at least 3 rows and 2 items")
    if not np.isfinite(a).all():
        raise ValueError("Non-finite answers require an explicit missing-data rule")
    total = a.sum(axis=1).var(ddof=1)
    if total <= 0:
        raise ValueError("No variation in the total scale score")
    n = a.shape[1]
    return float(n / (n - 1) * (1 - a.var(axis=0, ddof=1).sum() / total))

def ols(X, y):
    """Fit OLS with intercept; return *in-sample* statistics."""
    X, y = np.asarray(X, float), np.asarray(y, float).reshape(-1)
    if X.ndim != 2 or X.shape[0] != y.size or X.shape[0] <= X.shape[1] + 1:
        raise ValueError("Invalid regression dimensions")
    if not np.isfinite(X).all() or not np.isfinite(y).all():
        raise ValueError("Non-finite data")
    D = np.column_stack([np.ones(len(X)), X])
    if np.linalg.matrix_rank(D) < D.shape[1]:
        raise ValueError("The predictor design is rank deficient")
    beta = np.linalg.lstsq(D, y, rcond=None)[0]
    yhat = D @ beta
    tss = float(np.square(y - y.mean()).sum())
    if tss == 0:
        raise ValueError("R squared undefined for a constant outcome")
    return {"coefficients": beta.tolist(), "r_squared_in_sample":
            float(1 - np.square(y-yhat).sum()/tss)}
