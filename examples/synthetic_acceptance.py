"""All 500 rows are fabricated. Never confuse these outputs with dissertation results."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from acceptance_demo import fabricate, ols_in_sample, pearson


def main():
    X, y = fabricate(n=500, seed=2026)
    r = ols_in_sample(X, y)
    print("SYNTHETIC DATA ONLY — 500 generated examples, not 2022 survey responses")
    print(f"Fictional satisfaction/acceptance Pearson r = {pearson(X[:,6],y):.3f}")
    print(f"Fictional in-sample OLS R² = {r['r_squared_in_sample']:.3f}")
    print("Neither value reproduces an original SPSS result.")


if __name__ == "__main__":
    main()
