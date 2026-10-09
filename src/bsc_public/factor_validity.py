"""PCA, KMO and Bartlett numerical demonstrations on synthetic questionnaire items.

Post-BSc (2026) explanatory code; no private participant data are loaded.
A PCA-based diagnostic does not establish latent construct validity.
"""
from __future__ import annotations
import numpy as np
from scipy.stats import chi2

def pca_kmo_bartlett(items):
    """One-component PCA variance, KMO, approximate Bartlett p on finite rows."""
    a=np.asarray(items,dtype=float)
    if a.ndim != 2:
        raise ValueError("Expected two-dimensional items")
    n,p=a.shape
    if p<2 or n<max(5,p+2):
        raise ValueError("Too few observations or items")
    if not np.isfinite(a).all():
        raise ValueError("Missing or nonfinite values require explicit handling")
    if np.any(a.var(axis=0,ddof=1)<=0):
        raise ValueError("Constant items cannot be evaluated")
    corr=np.corrcoef(a,rowvar=False)
    sign,logdet=np.linalg.slogdet(corr)
    if sign<=0 or np.linalg.cond(corr)>1e12:
        raise ValueError("Correlation matrix is singular or ill-conditioned")
    inverse=np.linalg.inv(corr)
    partial=-inverse/np.sqrt(np.outer(np.diag(inverse),np.diag(inverse)))
    np.fill_diagonal(partial,0)
    offdiag=corr.copy()
    np.fill_diagonal(offdiag,0)
    numerator=float((offdiag**2).sum())
    denominator=float((partial**2).sum())
    if numerator+denominator<=0:
        raise ValueError("KMO undefined for uncorrelated items")
    eigenvalues=np.linalg.eigvalsh(corr)
    chi=-(n-1-(2*p+5)/6)*logdet
    degrees=p*(p-1)//2
    return {"n":n,"items":p,"kmo":numerator/(numerator+denominator),
            "first_component_variance_pct":float(eigenvalues[-1]*100/p),
            "bartlett_chi_square_approx":float(chi),
            "bartlett_df":degrees,"bartlett_p_approx":float(chi2.sf(chi,degrees))}
