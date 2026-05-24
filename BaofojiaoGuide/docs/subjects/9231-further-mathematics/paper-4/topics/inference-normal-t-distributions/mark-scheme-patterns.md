---
title: 评分模式
sidebar_position: 5
---

# Mark Scheme Patterns — Inference Using Normal and t-Distributions

## 标准给分结构

### Single-Sample t-Test（6-7 marks）

| Step | Marks | Typical wording |
|------|-------|----------------|
| $H_0$ / $H_1$ correctly stated | **B1** | "$H_0: \mu = 16$, $H_1: \mu &lt; 16$" |
| Correct test statistic formula | **M1** | "Use of $t = (\bar{x} - \mu)/\sqrt{s^2/n}$" |
| Correct t value (numerical) | **A1** | "$t = -2.771$" |
| Correct critical value / p-value | **B1** | "$t_{0.05}(9) = 1.833$" |
| Valid comparison | **M1** | "Compare $|t|$ with critical value" |
| Correct conclusion in context | **A1** | "Reject $H_0$ — sufficient evidence..." |

### Two-Sample Pooled t-Test（8-9 marks）

| Step | Marks | Typical wording |
|------|-------|----------------|
| $H_0$ / $H_1$ correctly stated | **B1** | "$H_0: \mu_1 = \mu_2$" |
| $s_p^2$ correctly calculated | **M1** | "Pooled variance formula used" |
| $s_p^2$ numerical value correct | **A1** | "$s_p^2 = 7.10$" |
| t statistic (formula + calc) | **M1** | "Substitution into t formula" |
| t value correct | **A1** | "$t = 2.630$" |
| df stated | **B1** | "df = 20" |
| Critical value | **B1** | "$t_{0.025}(20) = 2.086$" |
| Comparison + conclusion | **M1 A1** | "Since $t &gt; t_{\text{crit}}$, reject $H_0$" |

### Paired t-Test（7-8 marks）

| Step | Marks | Typical wording |
|------|-------|----------------|
| Differences $d_i$ calculated | **B1** | "$d = [5, 2, 7, \dots]$" |
| $\bar{d}$ and $s_d^2$ | **M1 A1** | "$\bar{d} = 4.25$, $s_d^2 = 4.50$" |
| t statistic formula + value | **M1 A1** | "$t = 5.667$" |
| df + critical value | **B1** | "$t_{0.05}(7) = 1.895$" |
| Comparison + conclusion | **M1 A1** | "Reject $H_0$ — mean has increased" |

### Confidence Interval（4-6 marks）

| Step | Marks | Typical wording |
|------|-------|----------------|
| Correct formula identified | **B1** | "$\bar{x} \pm t \cdot \sqrt{s^2/n}$" |
| Standard error correctly computed | **M1 A1** | "SE $= \sqrt{9.0/15} = 0.775$" |
| Correct $t$ or $z$ value from tables | **B1** | "$t_{0.025}(14) = 2.145$" |
| Interval endpoints (3 s.f.) | **A1** | "CI: $(40.3, 43.7)$" |

## 常见扣分点

| Mistake | Consequence |
|---------|-------------|
| Wrong degrees of freedom | Lose **B1** (usually method still marked) |
| Using $z$ instead of $t$ | Lose **M1** for wrong formula |
| Confusing one-tail / two-tail critical value | Lose **B1** |
| Not stating normality assumption | Lose **B1** (when explicitly required) |
| Arithmetic error in $s_p^2$ | Lose **A1** (but can still get **M1**) |
| Wrong conclusion despite correct calculation | Lose **A1** |

## 常见 MS 标记模式

- **"Use of $t = (\bar{x} - \mu)/\sqrt{s^2/n}$"** → **M1** (method mark)
- **"Correct substitution"** → **M1** if formula applied correctly
- **"$t = ...$"** → **A1** (accuracy mark, follows a **M1**)
- **"Critical value $t_{0.05}(11) = 1.796$"** → **B1** (independent mark)
- **"$|t| &gt; t_{\text{crit}} \Rightarrow$ reject $H_0$"** → **M1** for comparison, **A1** for conclusion
- **"Assumption: normally distributed"** → **B1**
- **"3 s.f."** → final **A1** requires correct rounding

## 不同 paper 的分数分布参考

| Paper | Q | Type | Marks |
|-------|---|------|-------|
| S20 Q4 | 4 | Paired t-test + One-sample t | 9 |
| S20 Q5 | 5 | CI (difference of means) | 7 |
| W20 Q1 | 1 | One-sample t-test | 6 |
| W20 Q4 | 4 | Paired t-test | 8 |
| S21 Q1 | 1 | z-test | 6 |
| S21 Q4 | 4 | Two-sample pooled t + CI | 9 |
| W21 Q1 | 1 | One-sample t-test | 6 |
| W21 Q4 | 4 | Two-sample pooled t | 8 |
| S22 Q1 | 1 | One-sample t-test | 6 |
| S22 Q5 | 5 | Two-sample z-test | 7 |
| W22 Q1 | 1 | One-sample t-test | 6 |
| W22 Q6 | 6 | CI (difference) | 8 |
| S23 Q1 | 1 | One-sample t-test | 6 |
| S23 Q2 | 2 | CI + two-sample test | 9 |
| W23 Q1 | 1 | Paired t-test | 7 |
| W23 Q3 | 3 | Pooled t + CI | 10 |
| S24 Q1 | 1 | One-sample t-test | 6 |
| S24 Q6 | 6 | Two-sample + CI | 9 |
| W24 Q6 | 6 | CI + hypothesis test | 8 |
| S25 Q1 | 1 | Paired t-test | 7 |
| S25 Q4 | 4 | CI (two-sample) | 7 |
| W25 Q1 | 1 | One-sample t-test | 6 |
| W25 Q3 | 3 | CI + pooled t | 9 |
| W25 Q6 | 6 | Two-sample z-test | 7 |
