# 📊 A/B Test Analyzer

<div align="center">

**Statistical Significance Testing Made Simple**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat-square)](README.md)

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Learn More](#-understanding-the-results)

</div>

---

## 🎯 Overview

Stop guessing if your changes actually work. **A/B Test Analyzer** is a clean, powerful tool that determines whether the difference between two groups is real or just luck.

Feed it two datasets. Get back science.

```
Control:    [100, 102, 98, 101, 99]
Treatment:  [105, 107, 104, 106, 108]
              ↓
        Statistical Analysis
              ↓
Verdict: ✓ This is a REAL difference (p = 0.0001)
```

---

## ✨ Features

| Feature | Details |
|---------|---------|
| 📈 **Statistical Testing** | Two-sample t-test with comprehensive metrics |
| 📊 **Effect Size Analysis** | Cohen's d coefficient for effect magnitude |
| 🎯 **Confidence Intervals** | 95% CI for the true difference |
| 📝 **Clear Reports** | Human-readable verdicts (no PhD required) |
| ⚡ **Fast & Lightweight** | Pure Python with NumPy/SciPy |

---

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip (package manager)

### Setup

```bash
# Clone or navigate to the project
cd Day_08_AB_Test_Analyzer

# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install numpy scipy
```

---

## 🚀 Quick Start

### Basic Usage

```python
from analysis import run_ab_test, print_report

# Your data
control = [100, 102, 98, 101, 99, 100, 101, 99]
treatment = [105, 107, 104, 106, 108, 106, 105, 107]

# Run analysis
result = run_ab_test(control, treatment, "Button Color Test")

# View results
print_report(result)
```

### Run Built-in Examples

```bash
python analysis.py
```

Executes 3 real-world scenarios:
- ✓ **Clear Difference** — Obvious winner
- ✗ **No Difference** — Inconclusive results
- ✓ **Medium Difference** — Moderate improvement

---

## 📚 Understanding the Results

### The P-Value

| P-Value | Interpretation |
|---------|----------------|
| **< 0.05** | 🎯 Statistically significant (real difference) |
| **≥ 0.05** | ❌ Not significant (probably random variation) |

**What it means:** P-value is the probability of seeing this data if there's actually *no* real difference.

### Effect Size (Cohen's d)

How *big* is the difference, independent of sample size?

| Range | Magnitude | What It Means |
|-------|-----------|--------------|
| d < 0.2 | Negligible | Barely noticeable |
| 0.2 ≤ d < 0.5 | Small | Meaningful but minor |
| 0.5 ≤ d < 0.8 | Medium | Moderate impact |
| d ≥ 0.8 | Large | Substantial difference |

### Confidence Interval (95%)

"We're 95% confident the *true* difference is between X and Y"

**Example:** CI = [2.4, 5.6] means the true difference is somewhere in that range.

---

## 💼 Real-World Example

**Scenario:** Your website's CTA button color changed from blue to red. Did it actually improve conversions?

```
Control Group (Blue):  [42, 45, 41, 43, 44, 42, 45, 43]    → mean: 43.1
Treatment Group (Red): [48, 50, 47, 49, 51, 49, 50, 48]    → mean: 49.0

╔════════════════════════════════════════╗
║ STATISTICAL RESULTS                    ║
╠════════════════════════════════════════╣
║ T-Statistic:       5.82                ║
║ P-Value:           0.0002 ✓            ║
║ Cohen's d:         2.14 (LARGE)        ║
║ 95% CI:            [4.2, 8.6]          ║
╚════════════════════════════════════════╝

VERDICT: ✓ YES — This is a REAL improvement.
Red button significantly outperforms blue.
Not just random luck.
```

---

## 🔧 API Reference

### `run_ab_test(control, treatment, test_name="A/B Test")`

Runs complete statistical analysis on two groups.

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `control` | list/array | Control group measurements |
| `treatment` | list/array | Treatment group measurements |
| `test_name` | str | Optional label for the test |

**Returns:** Dictionary containing:
- `t_stat` — T-test statistic
- `p_value` — Statistical significance
- `cohens_d` — Effect size
- `ci_lower`, `ci_upper` — Confidence interval bounds
- `is_significant` — Boolean verdict
- `effect_interpretation` — Effect magnitude (negligible/small/medium/large)

### `print_report(result)`

Formats and displays analysis results in a professional format.

---

## 🧮 Statistical Methods

### Welch's T-Test
Compares means of two independent groups without assuming equal variances.

### Cohen's d
Standardized effect size: `d = (μ₁ - μ₂) / σ_pooled`

### Confidence Intervals
95% CI using t-distribution with Welch-Satterthwaite degrees of freedom.

---

## 📖 When to Use A/B Testing

✅ **Good use cases:**
- Website UI changes (button color, layout, copy)
- Email subject line variations
- Pricing experiments
- Feature comparisons
- Marketing campaign effectiveness

❌ **Poor use cases:**
- Very small sample sizes (n < 10)
- Highly variable data without sufficient sample
- Predetermined outcomes (not true experimentation)

---

## 🎓 Learn More

- **Statistics Fundamentals** — [StatQuest with Josh Starmer](https://www.youtube.com/c/joshstarmer)
- **A/B Testing Guide** — [Nielsen Norman Group](https://www.nngroup.com/articles/ab-testing-sample-sizes/)
- **SciPy Documentation** — [scipy.stats.ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)

---

<div align="center">

**Day 8 of 50 — Django × Data Science Challenge**

Made with 📊 and ☕

</div>
