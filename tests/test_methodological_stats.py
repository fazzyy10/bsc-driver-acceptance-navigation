"""Only fabricated data, textbook properties, and transcribed 2022 public tables."""
from pathlib import Path
import csv
import sys
import numpy as np
import pytest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from bsc_public.stats import cronbach_alpha,ols
from bsc_public.factor_validity import pca_kmo_bartlett

def test_alpha_strong_common_factor():
    rng=np.random.default_rng(1)
    z=rng.normal(size=(200,1))
    a=z+rng.normal(scale=.4,size=(200,4))
    assert .8<cronbach_alpha(a)<1

def test_alpha_bad_inputs_rejected():
    for a in [np.ones((20,3)),np.ones((2,3)),np.array([[1,np.nan],[2,3],[3,4]])]:
        with pytest.raises(ValueError):cronbach_alpha(a)

def test_ols_exact_relation_and_no_out_sample_claim():
    rng=np.random.default_rng(2)
    x=rng.normal(size=(100,3))
    y=1+.5*x[:,0]-2*x[:,1]+.1*x[:,2]
    fit=ols(x,y)
    assert fit["coefficients"]==pytest.approx([1,.5,-2,.1],abs=1e-10)
    assert fit["r_squared_in_sample"]==pytest.approx(1)

def test_ols_singular_rejected():
    with pytest.raises(ValueError):ols(np.ones((25,2)),np.arange(25))

def test_two_item_kmo_is_algebraic_half():
    rng=np.random.default_rng(3)
    x=rng.normal(size=180)
    y=x+rng.normal(scale=.5,size=180)
    stats=pca_kmo_bartlett(np.column_stack([x,y]))
    assert stats["kmo"]==pytest.approx(.5,abs=1e-12)
    assert stats["bartlett_df"]==1

def test_pca_pc1_invariant_to_item_order_or_reversal():
    rng=np.random.default_rng(4)
    z=rng.normal(size=(300,1))
    a=z+rng.normal(scale=.5,size=(300,4))
    b=a[:,[2,0,3,1]].copy()
    b[:,1]=6-b[:,1]
    old,new=pca_kmo_bartlett(a),pca_kmo_bartlett(b)
    assert old["kmo"]==pytest.approx(new["kmo"])
    assert old["first_component_variance_pct"]==pytest.approx(new["first_component_variance_pct"])
    assert old["bartlett_p_approx"]==pytest.approx(new["bartlett_p_approx"])

def test_pca_responds_to_strong_common_factor():
    rng=np.random.default_rng(5)
    z=rng.normal(size=(300,1))
    a=z+rng.normal(scale=.35,size=(300,4))
    stats=pca_kmo_bartlett(a)
    assert stats["kmo"]>.8 and stats["first_component_variance_pct"]>75
    assert stats["bartlett_p_approx"]<.001

@pytest.mark.parametrize("bad",[
    np.ones((30,3)),
    np.array([[1,np.nan],[2,3],[3,4],[4,5],[5,6]]),
    np.ones((2,3)),
])
def test_pca_input_gates(bad):
    with pytest.raises(ValueError):pca_kmo_bartlett(bad)

def test_historical_reliability_table_is_original_not_synthetic():
    with (ROOT/"data/published_2022_aggregates/construct_reliability_2022.csv").open(newline="") as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==10
    assert next(float(z["cronbach_alpha"]) for z in rows if z["construct"]=="Trust")==.920
    assert all(.8<=float(z["cronbach_alpha"])<=.95 for z in rows)

def test_historical_pca_table_is_original_not_synthetic():
    with (ROOT/"data/published_2022_aggregates/construct_validity_2022.csv").open(newline="") as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==10
    assert float(next(z["kmo"] for z in rows if z["construct"]=="Perceived Locational Accuracy"))==.5

def test_historical_threshold_not_rediscovered():
    with (ROOT/"data/published_2022_aggregates/multiple_regression_coefficients_2022.csv").open(newline="") as f:
        rows={z["construct"]:z for z in csv.DictReader(f)}
    assert float(rows["Perceived Usefulness"]["p_reported"])>.01
    assert rows["Satisfaction"]["p_reported"]=="<0.001"
    assert rows["Trust"]["p_reported"]=="<0.001"
