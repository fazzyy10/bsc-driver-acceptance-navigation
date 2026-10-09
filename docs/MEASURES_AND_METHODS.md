# What I measured and how I analysed it

The study began with a practical concern: information about routes and traffic can be available, yet a driver may not trust or accept the system supplying it. The research therefore set out to understand **acceptance**, rather than to claim that installing navigation software had already reduced road accidents.

## Study and questionnaire

This was a cross-sectional survey using self-reported Likert-style responses, carried out for my 2022 BSc dissertation. The final historical SPSS analysis used **311 records**. Nine constructs were entered as explanatory variables for driver acceptance: perceived ease of use, usefulness, locational accuracy, processing speed, service and display quality, distraction perception, satisfaction, social influence and trust. The acceptance score was the dependent variable.

I used **IBM SPSS**, not Python, for the original 2022 assessment. The published statistical workflow comprised:

1. Coding questionnaire answers and forming composite construct scores.
2. Checking internal consistency using Cronbach's alpha.
3. Examining exploratory structure using principal components, KMO and Bartlett's test.
4. Looking at each construct's Pearson correlation with acceptance.
5. Fitting individual regressions and then a **simultaneous nine-predictor linear regression**.

The later Python files illustrate these calculations on invented data. They were not used to obtain the original submitted result.

## How I now interpret those choices

A high alpha is a measure of internal consistency, not evidence that the construct is valid in every population. PCA variance explained is not the same as fitting or validating a confirmatory factor model. A two-item scale's overall KMO is mathematically **0.500** whenever the item correlation matrix is nonsingular. That value should not be advertised as independent evidence of strong sampling adequacy.

A strong individual correlation does not guarantee that a coefficient survives adjustment for overlapping predictors. In the original nine-predictor model, the reported p-values for satisfaction and trust were below **.001**; usefulness was **.011**, which does not meet the study's **.01** criterion.

The reported full-model **R² = .679** applies to data used to fit that model; it is not independently assessed predictive accuracy. The survey did not observe road accidents or establish the causal effect of using navigation.

## Evidence and uncertainty

The original thesis contains conflicting initial-return totals (325 and 326). The archived private source processing has unresolved details. That does not justify inventing a corrected response history in a modern repository. The analysis table's N = 311 is explicitly stated, and the originals remain private.

For a research continuation, I would pre-specify missing-data decisions, examine overlapping constructs and sampling bias, and collect genuinely new behavioural outcomes before making any safety claim.

[Results](RESULTS_2022.md) · [Public statistics tables](../data/published_2022_aggregates/) · [Evidence boundaries](EVIDENCE_AND_LIMITATIONS.md).
