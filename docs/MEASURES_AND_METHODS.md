# What I measured and how I analysed it

My dissertation examined why drivers might accept or reject mobile navigation systems. I was interested in the experience of using the technology: whether the information seemed accurate and useful, whether the system was responsive, and whether drivers trusted it enough to rely on it. The study measured **acceptance**. It did not collect accident outcomes.

## Study and questionnaire

This was a cross-sectional survey using self-reported Likert-style responses, carried out for my 2022 BSc dissertation. The final historical SPSS analysis used **311 records**. Nine constructs were entered as explanatory variables for driver acceptance: perceived ease of use, usefulness, locational accuracy, processing speed, service and display quality, distraction perception, satisfaction, social influence and trust. The acceptance score was the dependent variable.

The original analysis was carried out in **IBM SPSS**. I worked through the following stages:

1. Coding questionnaire answers and forming composite construct scores.
2. Checking internal consistency using Cronbach's alpha.
3. Examining exploratory structure using principal components, KMO and Bartlett's test.
4. Looking at each construct's Pearson correlation with acceptance.
5. Fitting individual regressions and then a **simultaneous nine-predictor linear regression**.

The Python examples in this repository were developed in 2026 on fabricated data. They are separate from these SPSS results.

A detail worth checking in the original tables is the distraction-perception result. The simple regression's **model-summary R is +.279**, because that statistic is non-negative. Its **Pearson correlation is −.279**, retaining the direction of association. Both numbers are preserved in the public tables, under their correct names.

## How I now interpret those choices

A high alpha is a measure of internal consistency, not evidence that the construct is valid in every population. PCA variance explained is not the same as fitting or validating a confirmatory factor model. A two-item scale's overall KMO is mathematically **0.500** whenever the item correlation matrix is nonsingular. It therefore says little about sampling adequacy for that two-item construct.

A strong individual correlation does not guarantee that a coefficient survives adjustment for overlapping predictors. In the original nine-predictor model, the reported p-values for satisfaction and trust were below **.001**; usefulness was **.011**, which does not meet the study's **.01** criterion.

The reported full-model **R² = .679** applies to data used to fit that model; it is not independently assessed predictive accuracy. The survey did not observe road accidents or establish the causal effect of using navigation.

## Evidence and uncertainty

The original thesis contains conflicting initial-return totals (325 and 326). The archived private source processing has unresolved details. That does not justify inventing a corrected response history in a modern repository. The analysis table's N = 311 is explicitly stated, and the originals remain private.

For a research continuation, I would pre-specify missing-data decisions, examine overlapping constructs and sampling bias, and collect genuinely new behavioural outcomes before making any safety claim.

[Results](RESULTS_2022.md) · [Public statistics tables](../data/published_2022_aggregates/) · [Evidence boundaries](EVIDENCE_AND_LIMITATIONS.md).
