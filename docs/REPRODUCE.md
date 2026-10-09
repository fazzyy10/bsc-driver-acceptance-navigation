# Run the public example

The dissertation was analysed in IBM SPSS on real questionnaire responses. Those private records are **not provided here**. This is a separate Python demonstration built entirely on **fabricated data**. It helps explain model fitting without using a single original respondent record.

With Python 3.11:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python examples/synthetic_acceptance.py
python examples/synthetic_factor_diagnostics.py
python -c "from pathlib import Path; Path('local_results').mkdir(exist_ok=True)"
python -m jupyter nbconvert --execute --to notebook notebooks/overview.ipynb --output overview-executed.ipynb --output-dir local_results
python scripts/repo_preflight.py
```

The script prints **SYNTHETIC DATA** and an in-sample regression result generated from a fixed random seed. The tests verify the output's dimensions, reproducibility and mathematical identities. Neither the regression result nor the example's correlation is an independent reproduction of the 2022 thesis statistics.

The public CI workflow repeats the test and example. Passing CI establishes that **this public example runs**, not that the original SPSS study has been replicated.

[Back to the homepage](../README.md).


The notebook reads historical **aggregate-only** tables for its first charts, then produces synthetic data for the code demonstration. Its generated coefficients, reliability, PCA and R² are **not** new findings about the 2022 respondents.
