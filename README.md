# A/B Test Analyzer

A command-line tool for running statistical A/B tests and determining if differences between two groups are statistically significant.

## What It Does

Given two datasets (control group vs treatment group), this tool:
- Calculates descriptive statistics (mean, std dev, sample size)
- Runs a two-sample t-test
- Computes effect size (Cohen's d)
- Calculates 95% confidence intervals
- Provides a plain-English verdict: "Real difference" or "Probably noise"

## Key Functions

### `run_ab_test(control, treatment, test_name)`
Main function that runs the complete analysis.

**Parameters:**
- `control` (list/array): Control group data
- `treatment` (list/array): Treatment group data
- `test_name` (str): Label for the test

**Returns:** Dictionary with all statistical results

### `print_report(result)`
Formats and prints a clean report of the test results.

## Example Usage

```python
control = [100, 102, 98, 101, 99]
treatment = [105, 107, 104, 106, 108]

result = run_ab_test(control, treatment, "My Test")
print_report(result)
```

## Understanding the Output

**P-Value:** If < 0.05, the difference is statistically significant (not just random luck)

**Cohen's d (Effect Size):**
- < 0.2 = negligible
- 0.2–0.5 = small
- 0.5–0.8 = medium
- > 0.8 = large

**Confidence Interval:** We're 95% confident the real difference is within this range

## Running the Code

```bash
python analysis.py
```

This runs 3 example tests showing clear difference, no difference, and medium difference scenarios.

## Statistical Concepts Used

- **T-Test (Independent samples):** Compares two unrelated groups
- **Cohen's d:** Standardized effect size
- **Confidence Intervals:** Range of plausible values for the true difference
- **P-Value:** Probability of observing this difference if there's actually no real effect
