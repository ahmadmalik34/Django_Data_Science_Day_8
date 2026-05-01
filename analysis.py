import numpy as np
from scipy import stats

def calculate_cohens_d(group1, group2):
    mean1, mean2 = np.mean(group1), np.mean(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    n1, n2 = len(group1), len(group2)
    
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    
    cohens_d = (mean1 - mean2) / pooled_std
    return cohens_d

def interpret_cohens_d(d):
    d = abs(d)
    if d < 0.2:
        return "negligible"
    elif d < 0.5:
        return "small"
    elif d < 0.8:
        return "medium"
    else:
        return "large"

def calculate_confidence_interval(group1, group2, confidence=0.95):
    mean1, mean2 = np.mean(group1), np.mean(group2)
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    
    se_diff = np.sqrt((var1 / n1) + (var2 / n2))
    
    df = ((var1/n1 + var2/n2)**2) / ((var1/n1)**2/(n1-1) + (var2/n2)**2/(n2-1))
    
    alpha = 1 - confidence
    t_crit = stats.t.ppf(1 - alpha/2, df)
    
    diff = mean1 - mean2
    margin_of_error = t_crit * se_diff
    ci_lower = diff - margin_of_error
    ci_upper = diff + margin_of_error
    
    return ci_lower, ci_upper

def run_ab_test(control, treatment, test_name="A/B Test"):
    control = np.array(control)
    treatment = np.array(treatment)
    
    control_mean = np.mean(control)
    control_std = np.std(control, ddof=1)
    control_n = len(control)
    
    treatment_mean = np.mean(treatment)
    treatment_std = np.std(treatment, ddof=1)
    treatment_n = len(treatment)
    
    t_stat, p_value = stats.ttest_ind(control, treatment)
    
    cohens_d = calculate_cohens_d(control, treatment)
    effect_interpretation = interpret_cohens_d(cohens_d)
    
    ci_lower, ci_upper = calculate_confidence_interval(control, treatment)
    
    is_significant = p_value < 0.05
    verdict = "YES ✓" if is_significant else "NO ✗"
    
    return {
        'test_name': test_name,
        'control_mean': control_mean,
        'control_std': control_std,
        'control_n': control_n,
        'treatment_mean': treatment_mean,
        'treatment_std': treatment_std,
        'treatment_n': treatment_n,
        't_stat': t_stat,
        'p_value': p_value,
        'is_significant': is_significant,
        'cohens_d': cohens_d,
        'effect_interpretation': effect_interpretation,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'verdict': verdict
    }

def print_report(result):
    print("\n" + "=" * 60)
    print(f"A/B TEST ANALYZER — {result['test_name']}")
    print("=" * 60)
    
    print("\n📊 CONTROL GROUP STATS")
    print("-" * 60)
    print(f"  Mean:           {result['control_mean']:.2f}")
    print(f"  Std Dev:        {result['control_std']:.2f}")
    print(f"  Sample Size:    {result['control_n']}")
    
    print("\n📊 TREATMENT GROUP STATS")
    print("-" * 60)
    print(f"  Mean:           {result['treatment_mean']:.2f}")
    print(f"  Std Dev:        {result['treatment_std']:.2f}")
    print(f"  Sample Size:    {result['treatment_n']}")
    
    print("\n" + "=" * 60)
    print("📈 STATISTICAL RESULTS")
    print("=" * 60)
    print(f"  T-Statistic:    {result['t_stat']:.4f}")
    print(f"  P-Value:        {result['p_value']:.4f}")
    print(f"  Significance:   {result['verdict']} (p {'<' if result['is_significant'] else '>'} 0.05)")
    
    print(f"\n  Effect Size (Cohen's d): {result['cohens_d']:.3f}")
    print(f"  Interpretation:          {result['effect_interpretation'].upper()}")
    
    print(f"\n  95% Confidence Interval: [{result['ci_lower']:.2f}, {result['ci_upper']:.2f}]")
    
    # Final Verdict
    print("\n" + "=" * 60)
    print("🎯 VERDICT")
    print("=" * 60)
    if result['is_significant']:
        print(f"\n✓ This is a REAL difference ({result['effect_interpretation']} effect).")
        print(f"  Not just random variation. The treatment made a difference.")
    else:
        print(f"\n✗ This is probably just noise.")
        print(f"  No statistically significant difference detected.")
    print("\n" + "=" * 60 + "\n")

def main():
    print("\n🧪 RUNNING EXAMPLE TESTS...\n")
    
    control_1 = [100, 102, 98, 101, 99, 100, 101, 99]
    treatment_1 = [105, 107, 104, 106, 108, 106, 105, 107]
    
    result_1 = run_ab_test(control_1, treatment_1, "Example 1: Clear Difference")
    print_report(result_1)
    
    control_2 = [100, 101, 102, 99, 100, 101, 99, 100]
    treatment_2 = [100, 102, 101, 100, 99, 101, 100, 102]
    
    result_2 = run_ab_test(control_2, treatment_2, "Example 2: No Clear Difference")
    print_report(result_2)
    
    control_3 = [50, 48, 52, 49, 51, 50, 49, 51]
    treatment_3 = [60, 58, 62, 59, 61, 60, 59, 61]
    
    result_3 = run_ab_test(control_3, treatment_3, "Example 3: Medium Difference")
    print_report(result_3)

if __name__ == "__main__":
    main()
