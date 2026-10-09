# What another researcher can and cannot reproduce here

This checklist is a disclosure of the scope of **publicly available** evidence, not a score for research quality.

| Question | Status | Evidence |
|---|---|---|
| Can a reader identify the original research question and author? | Yes | [Research methods](MEASURES_AND_METHODS.md), [original findings](RESULTS_2022.md) |
| Are historically reported aggregate values machine-readable? | Yes | [Original 2022 aggregate tables](../data/published_2022_aggregates/) |
| Can the historical SPSS regression be recomputed from this repository alone? | **No** | Respondent-level sources are intentionally withheld |
| Is the post-degree statistical demonstration runnable? | Yes | [Runnable guide](REPRODUCE.md), Python example, tests and notebook |
| Are the demonstration inputs actual survey answers? | **No** | Explicit seeded **synthetic** generation |
| Are research-metric definitions checked? | Yes, for synthetic examples | Automated tests for OLS, Cronbach alpha and PCA/KMO/Bartlett |
| Has the public source been run in live CI? | Yes, for the public package, not the 2022 private study | [Verified main-branch run](https://github.com/fazzyy10/bsc-driver-acceptance-navigation/actions/runs/37916817177) |
| Is the assessed 2022 thesis available unredacted? | **No** | Original private archive; respondent privacy gate |
| Is initial response accounting fully reconciled? | **No** | Historical 325/326 inconsistency remains |
| Does this study demonstrate fewer accidents? | **No** | It measures driver acceptance, not accident outcomes |
| Does this repository establish a peer-reviewed publication? | **No** | BSc dissertation and later unpublished methodological exercises |

## Test it yourself

With Python 3.11 and the versions in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python examples/synthetic_acceptance.py
python examples/synthetic_factor_diagnostics.py
python -c "from pathlib import Path; Path('local_results').mkdir(exist_ok=True)"
python -m jupyter nbconvert --execute --to notebook notebooks/overview.ipynb --output overview-executed.ipynb --output-dir local_results
python scripts/repo_preflight.py
```

The notebook juxtaposes a chart of **transcribed 2022 aggregates** with a separate generated-data example. Running it does not turn public summaries into original participant-level evidence.
