from pathlib import Path
import sys
import csv
import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from acceptance_demo import fabricate, ols_in_sample, pearson


def test_generated_shape_and_range():
    X, y = fabricate()
    assert X.shape == (500, 9) and y.shape == (500,)
    assert np.all((X >= 1) & (X <= 5))


def test_deterministic_generated_data():
    X, y = fabricate(100, 2026)
    X2, y2 = fabricate(100, 2026)
    np.testing.assert_array_equal(X, X2)
    np.testing.assert_array_equal(y, y2)


def test_seed_changes_generated_data():
    assert not np.array_equal(fabricate(100, 2026)[0], fabricate(100, 2027)[0])


def test_generated_fit_and_dimensions():
    X, y = fabricate()
    model = ols_in_sample(X, y)
    assert 0 <= model["r_squared_in_sample"] <= 1
    assert len(model["coefficients"]) == 9
    assert model["coefficients"][6] > 0 and model["coefficients"][8] > 0


def test_perfect_fit_is_one():
    x = np.arange(30.0).reshape(-1,1)
    assert ols_in_sample(x, 1 + 2*x[:,0])["r_squared_in_sample"] == pytest.approx(1)


def test_pearson_signs():
    x = np.arange(10.)
    assert pearson(x, x) == pytest.approx(1)
    assert pearson(x, -x) == pytest.approx(-1)


@pytest.mark.parametrize("n",[0,2,19])
def test_no_tiny_fabricated_studies(n):
    with pytest.raises(ValueError): fabricate(n=n)


def test_no_constant_outcome():
    X,_ = fabricate()
    with pytest.raises(ValueError): ols_in_sample(X, np.ones(len(X)))


def test_bad_dimensions_are_rejected():
    X,y = fabricate()
    with pytest.raises(ValueError): ols_in_sample(X,y[:-1])


def test_original_reported_correlations_not_changed():
    with (ROOT / "data/published_2022_correlations.csv").open(newline="",encoding="utf8") as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==9 and {int(r["n"]) for r in rows}=={311}
    d={r["construct"]:float(r["pearson_r"]) for r in rows}
    assert d["Satisfaction"] == .767
    assert d["Trust"] == .731
    assert d["Distraction Perception"] == -.279


def test_private_source_files_never_checked_in():
    restricted={".sav",".spv",".sps",".xlsx",".xls",".docx",".pdf",".zip",".sqlite"}
    forbidden = [str(p) for p in ROOT.rglob("*") if p.is_file() and p.suffix.lower() in restricted and ".git" not in p.parts]
    assert forbidden == []


def test_ols_rejects_rank_deficient_predictors():
    X = np.ones((30, 2))
    with pytest.raises(ValueError, match="rank deficient"):
        ols_in_sample(X, np.arange(30.0))


def test_ols_rejects_nonfinite_inputs():
    X, y = fabricate(40)
    X[2, 0] = np.inf
    with pytest.raises(ValueError, match="finite"):
        ols_in_sample(X, y)


def test_pearson_rejects_nonfinite_inputs():
    a = np.arange(10.0)
    a[1] = np.nan
    with pytest.raises(ValueError, match="finite"):
        pearson(a, np.arange(10.0))


def test_ols_rejects_too_few_observations():
    X = np.arange(20.0).reshape(4, 5)
    with pytest.raises(ValueError):
        ols_in_sample(X, np.arange(4.0))
