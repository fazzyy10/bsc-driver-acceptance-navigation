"""Fabricated factor examples, not the 2022 survey or a real-data replay."""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from bsc_public.factor_validity import pca_kmo_bartlett

def main():
    rng=np.random.default_rng(2026)
    latent=rng.normal(size=(400,1))
    items=.75*latent+rng.normal(scale=.5,size=(400,4))
    x=pca_kmo_bartlett(items)
    print("SYNTHETIC DATA ONLY: 400 fabricated questionnaire rows, not 2022 responses")
    print("KMO:",round(x["kmo"],3))
    print("First principal component variance:",round(x["first_component_variance_pct"],3))
    print("Bartlett p:",format(x["bartlett_p_approx"],".3g"))
    assert x["kmo"]>.7 and x["n"]==400

if __name__=="__main__":
    main()
