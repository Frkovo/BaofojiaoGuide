---
title: 题型分析
sidebar_position: 2
---

# 题型分析 — Chi-squared Tests

## Question Type 1: GoF for Binomial Distribution

### 如何识别

题目给出频数分布表，要求检验数据是否服从 Binomial 分布。关键词："test whether a Binomial distribution fits"、"Goodness of fit — Binomial"

:::note[标准解题方法]

1. 估计 Binomial 参数 $p$（如果未知）：$\hat{p} = \dfrac{\sum x f_x}{n \sum f_x}$
2. 计算 $P(X = x) = \binom{n}{x} p^x (1-p)^{n-x}$ 对于 $x = 0, 1, \dots, n$
3. 计算期望频数 $E = \text{total} \times P(X = x)$
4. 合并尾部使 $E \geq 5$，通常 $P(X \geq r)$ 合并为一项
5. $\chi^2 = \sum \dfrac{(O - E)^2}{E}$
6. $\mathrm{df} = k - 1 - 1$（估计了 $p$）
7. 查表比较

:::

:::info[评分标准（MS 模式）]

- 估计 $\hat{p}$：**M1** 正确方法，**A1** 数值正确
- 计算 $P(X = x)$：每项各 **M1 A1**（通常前 3 项）
- 合并尾部概率：**B1**
- 计算期望频数：**M1** 方法，**A1** 数值（允许多步误差）
- 计算 $\chi^2$：**M1** 方法，**A1** 数值
- 自由度：**B1**
- 临界值和结论：**M1** 比较，**A1** 正确结论

:::

**Example 1 — 9231/w20/qp/41 Q3 (9 marks):**

The number of defective items, $X$, in a random sample of 8 items is recorded for 200 samples. The results are:

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 |
|-----|---|---|---|---|---|---|
| Frequency | 22 | 79 | 62 | 28 | 7 | 2 |

Test, at the 5% significance level, whether a Binomial distribution with $n = 8$ is a suitable model.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

**Step 1 — Estimate $p$**

Total items checked $= 200 \times 8 = 1600$
Total defectives $= 0 \times 22 + 1 \times 79 + 2 \times 62 + 3 \times 28 + 4 \times 7 + 5 \times 2 = 0 + 79 + 124 + 84 + 28 + 10 = 325$

$\hat{p} = \dfrac{325}{1600} = 0.203125$ **M1 A1**

**Step 2 — Binomial probabilities**

$P(X = x) = \binom{8}{x} (0.203125)^x (0.796875)^{8-x}$

$P(0) = 0.796875^8 = 0.1536$ **M1**
$P(1) = 8 \times 0.203125 \times 0.796875^7 = 0.3131$
$P(2) = \binom{8}{2} \times 0.203125^2 \times 0.796875^6 = 0.2793$
$P(3) = \binom{8}{3} \times 0.203125^3 \times 0.796875^5 = 0.1423$
$P(4) = \binom{8}{4} \times 0.203125^4 \times 0.796875^4 = 0.0454$
$P(5) = \binom{8}{5} \times 0.203125^5 \times 0.796875^3 = 0.0093$ **A1** (all probabilities correct)

$P(6) = 1 - \text{sum}(P(0)\text{ to }P(5)) = 0.0013$ (or compute directly)

**Step 3 — Expected frequencies**

$E = 200 \times P(X = x)$

| $x$ | $O$ | $P$ | $E$ |
|-----|-----|-----|-----|
| 0 | 22 | 0.1536 | 30.72 |
| 1 | 79 | 0.3131 | 62.62 |
| 2 | 62 | 0.2793 | 55.86 |
| 3 | 28 | 0.1423 | 28.46 |
| 4 | 7 | 0.0454 | 9.08 |
| 5 | 2 | 0.0093 | 1.86 |
| $\geq 6$ | 0 | 0.0013 | 0.26 |

**B1** — Combine last three rows: $4+5+6+$ have $E = 9.08 + 1.86 + 0.26 = 11.20$, $O = 7 + 2 + 0 = 9$

**Step 4 — Chi-squared**

| $x$ | $O$ | $E$ | $(O-E)^2/E$ |
|-----|-----|-----|-------------|
| 0 | 22 | 30.72 | 2.476 |
| 1 | 79 | 62.62 | 4.287 |
| 2 | 62 | 55.86 | 0.675 |
| 3 | 28 | 28.46 | 0.007 |
| $\geq 4$ | 9 | 11.20 | 0.432 |

$\chi^2 = 2.476 + 4.287 + 0.675 + 0.007 + 0.432 = 7.877$ **M1 A1**

**Step 5 — Degrees of freedom**

$k = 5$ categories after merging, $m = 1$ parameter ($p$) estimated
$\mathrm{df} = 5 - 1 - 1 = 3$ **B1**

**Step 6 — Conclusion**

$\chi^2_{0.05, 3} = 7.815$ **M1**
Since $7.877 &gt; 7.815$, we reject $H_0$.

There is sufficient evidence at the 5% significance level that the Binomial distribution is **not** a suitable model. **A1**

</details>

:::warning[常见陷阱]

- 合并时注意总和：合并后 $O$ 和 $E$ 都要相加
- 自由度是 $k - 1 - 1$，不是 $k - 1$
- $\hat{p}$ 是用加权平均，不是简单平均

:::

---

**Example 2 — 9231/w21/qp/41 Q3 (9 marks):**

The number of accidents per day, $X$, at a factory over a period of 200 days is recorded:

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 |
|-----|---|---|---|---|---|---|
| Frequency | 78 | 74 | 34 | 11 | 2 | 1 |

Test, at the 5% significance level, whether a Binomial distribution with $n = 5$ is suitable.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

**Step 1 — Estimate $p$**

Total accidents $= 0 \times 78 + 1 \times 74 + 2 \times 34 + 3 \times 11 + 4 \times 2 + 5 \times 1 = 0 + 74 + 68 + 33 + 8 + 5 = 188$
Total trials $= 200 \times 5 = 1000$

$\hat{p} = \dfrac{188}{1000} = 0.188$ **M1 A1**

**Step 2 — Binomial probabilities ($n = 5$, $p = 0.188$)**

$P(0) = (0.812)^5 = 0.3527$
$P(1) = 5 \times 0.188 \times (0.812)^4 = 0.4086$
$P(2) = \binom{5}{2} \times 0.188^2 \times 0.812^3 = 0.1893$
$P(3) = \binom{5}{3} \times 0.188^3 \times 0.812^2 = 0.0438$
$P(4) = \binom{5}{4} \times 0.188^4 \times 0.812 = 0.0051$
$P(5) = 0.188^5 = 0.0002$ **A1**

**Step 3 — Expected frequencies ($E = 200 \times P$)**

| $x$ | $O$ | $E$ |
|-----|-----|-----|
| 0 | 78 | 70.54 |
| 1 | 74 | 81.72 |
| 2 | 34 | 37.86 |
| 3 | 11 | 8.76 |
| 4 | 2 | 1.02 |
| 5 | 1 | 0.04 |

**B1** — Combine $x \geq 3$: $E = 8.76 + 1.02 + 0.04 = 9.82$, $O = 11 + 2 + 1 = 14$

**Step 4 — Chi-squared**

| $x$ | $O$ | $E$ | $(O-E)^2/E$ |
|-----|-----|-----|-------------|
| 0 | 78 | 70.54 | 0.789 |
| 1 | 74 | 81.72 | 0.729 |
| 2 | 34 | 37.86 | 0.393 |
| $\geq 3$ | 14 | 9.82 | 1.779 |

$\chi^2 = 0.789 + 0.729 + 0.393 + 1.779 = 3.690$ **M1 A1**

**Step 5 — df**

$k = 4$, $m = 1$ ⇒ $\mathrm{df} = 4 - 1 - 1 = 2$ **B1**

**Step 6 — Conclusion**

$\chi^2_{0.05, 2} = 5.991$ **M1**
$3.690 &lt; 5.991$ ⇒ do not reject $H_0$.

Insufficient evidence to suggest Binomial is not suitable. **A1**

</details>

:::warning[常见陷阱]

- 合并后确保总频数匹配：4+5 合并后频数是 $2 + 1 = 3$ 和 $1.02 + 0.04 = 1.06$

:::

---

**Example 3 — 9231/s25/qp/41 Q3 (9 marks):**

A biologist records the number of seeds germinating, $X$, in each of 100 trays containing 6 seeds each:

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|-----|---|---|---|---|---|---|---|
| Frequency | 2 | 8 | 22 | 32 | 24 | 9 | 3 |

Test, at the 5% significance level, whether a Binomial distribution with $n = 6$ is a suitable model.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

**Step 1 — Estimate $p$**

Total seeds $= 100 \times 6 = 600$
Total germinated $= 0 \times 2 + 1 \times 8 + 2 \times 22 + 3 \times 32 + 4 \times 24 + 5 \times 9 + 6 \times 3$
$= 0 + 8 + 44 + 96 + 96 + 45 + 18 = 307$

$\hat{p} = \dfrac{307}{600} = 0.5117$ **M1 A1**

**Step 2 — Binomial probabilities**

$P(X = x) = \binom{6}{x} (0.5117)^x (0.4883)^{6-x}$

$P(0) = 0.4883^6 = 0.0136$
$P(1) = 6 \times 0.5117 \times 0.4883^5 = 0.0853$
$P(2) = 15 \times 0.5117^2 \times 0.4883^4 = 0.2228$
$P(3) = 20 \times 0.5117^3 \times 0.4883^3 = 0.3107$
$P(4) = 15 \times 0.5117^4 \times 0.4883^2 = 0.2437$
$P(5) = 6 \times 0.5117^5 \times 0.4883 = 0.1020$
$P(6) = 0.5117^6 = 0.0219$ **A1**

**Step 3 — Expected frequencies ($E = 100 \times P$)**

| $x$ | $O$ | $E$ |
|-----|-----|-----|
| 0 | 2 | 1.36 |
| 1 | 8 | 8.53 |
| 2 | 22 | 22.28 |
| 3 | 32 | 31.07 |
| 4 | 24 | 24.37 |
| 5 | 9 | 10.20 |
| 6 | 3 | 2.19 |

**B1** — Combine $x = 0$ and $x = 1$: $E = 1.36 + 8.53 = 9.89$, $O = 2 + 8 = 10$
Combine $x = 6$ with $x = 5$: $E = 10.20 + 2.19 = 12.39$, $O = 9 + 3 = 12$

**Step 4 — Chi-squared**

| $x$ | $O$ | $E$ | $(O-E)^2/E$ |
|-----|-----|-----|-------------|
| 0–1 | 10 | 9.89 | 0.0012 |
| 2 | 22 | 22.28 | 0.0035 |
| 3 | 32 | 31.07 | 0.0278 |
| 4 | 24 | 24.37 | 0.0056 |
| 5–6 | 12 | 12.39 | 0.0123 |

$\chi^2 = 0.0012 + 0.0035 + 0.0278 + 0.0056 + 0.0123 = 0.0504$ **M1 A1**

**Step 5 — df**

$k = 5$, $m = 1$ ⇒ $\mathrm{df} = 5 - 1 - 1 = 3$ **B1**

**Step 6 — Conclusion**

$\chi^2_{0.05, 3} = 7.815$ **M1**
$0.0504 &lt; 7.815$ ⇒ do not reject $H_0$.

Insufficient evidence to reject Binomial as suitable model. **A1**

</details>

:::warning[常见陷阱]

- $E &lt; 5$ 可能出现在两端，需分别合并
- 对比本题（$p \approx 0.5$，对称）与 Example 1（$p$ 较小，右偏）观察合并方式的不同

:::

---

## Question Type 2: GoF for Poisson Distribution

### 如何识别

关键词："Poisson distribution"、"test for randomness"、"Goodness of fit — Poisson"。数据通常是计数数据（事故数、缺陷数等）。

:::note[标准解题方法]

1. 估计 $\hat{\lambda} = \bar{x}$
2. 计算 $P(X = x) = e^{-\lambda} \lambda^x / x!$
3. 计算期望频数 $E = \text{total} \times P(X = x)$
4. 合并尾部使 $E \geq 5$
5. $\chi^2 = \sum (O-E)^2/E$
6. $\mathrm{df} = k - 1 - 1$（估计了 $\lambda$）
7. 查表比较

:::

:::info[评分标准（MS 模式）]

- 估计 $\overline{x}$：**M1 A1**
- 计算 Poisson 概率：每项 **M1 A1**
- 尾部合并：**B1**
- $\chi^2$：**M1 A1**
- 自由度 **B1**，结论 **M1 A1**

:::

**Example 1 — 9231/s22/qp/41 Q4 (10 marks):**

The number of particles emitted per minute by a radioactive source is recorded for 200 minutes:

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|---|
| Frequency | 10 | 28 | 49 | 52 | 35 | 17 | 7 | 2 |

Test, at the 5% significance level, whether a Poisson distribution is a suitable model.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

**Step 1 — Estimate $\lambda$**

$\bar{x} = \dfrac{0 \times 10 + 1 \times 28 + 2 \times 49 + 3 \times 52 + 4 \times 35 + 5 \times 17 + 6 \times 7 + 7 \times 2}{200}$

$= \dfrac{0 + 28 + 98 + 156 + 140 + 85 + 42 + 14}{200} = \dfrac{563}{200} = 2.815$ **M1 A1**

**Step 2 — Poisson probabilities**

$P(X = x) = e^{-2.815} \times 2.815^x / x!$

$P(0) = e^{-2.815} = 0.0599$
$P(1) = 0.0599 \times 2.815 = 0.1686$
$P(2) = 0.1686 \times 2.815/2 = 0.2373$
$P(3) = 0.2373 \times 2.815/3 = 0.2227$
$P(4) = 0.2227 \times 2.815/4 = 0.1567$
$P(5) = 0.1567 \times 2.815/5 = 0.0882$
$P(6) = 0.0882 \times 2.815/6 = 0.0414$
$P(7) = 0.0414 \times 2.815/7 = 0.0167$ **A1**
$P(\geq 8) = 1 - \text{sum} = 0.0085$

**Step 3 — Expected frequencies ($E = 200 \times P$)**

| $x$ | $O$ | $E$ |
|-----|-----|-----|
| 0 | 10 | 11.98 |
| 1 | 28 | 33.72 |
| 2 | 49 | 47.46 |
| 3 | 52 | 44.54 |
| 4 | 35 | 31.34 |
| 5 | 17 | 17.64 |
| 6 | 7 | 8.28 |
| 7 | 2 | 3.34 |
| $\geq 8$ | 0 | 1.70 |

**B1** — Combine $7+$: $O = 2 + 0 = 2$, $E = 3.34 + 1.70 = 5.04$

**Step 4 — Chi-squared**

| $x$ | $O$ | $E$ | $(O-E)^2/E$ |
|-----|-----|-----|-------------|
| 0 | 10 | 11.98 | 0.327 |
| 1 | 28 | 33.72 | 0.970 |
| 2 | 49 | 47.46 | 0.050 |
| 3 | 52 | 44.54 | 1.249 |
| 4 | 35 | 31.34 | 0.427 |
| 5 | 17 | 17.64 | 0.023 |
| 6 | 7 | 8.28 | 0.198 |
| $\geq 7$ | 2 | 5.04 | 1.834 |

$\chi^2 = 0.327 + 0.970 + 0.050 + 1.249 + 0.427 + 0.023 + 0.198 + 1.834 = 5.078$ **M1 A1**

**Step 5 — df**

$k = 8$, $m = 1$ ⇒ $\mathrm{df} = 8 - 1 - 1 = 6$ **B1**

**Step 6 — Conclusion**

$\chi^2_{0.05, 6} = 12.592$ **M1**
$5.078 &lt; 12.592$ ⇒ do not reject $H_0$.

Poisson distribution is a suitable model. **A1**

</details>

:::warning[常见陷阱]

- Poisson 概率用递推公式 $P(X = x) = P(X = x-1) \times \lambda / x$ 可减少计算量
- 合并尾部时注意是否还有 $E &lt; 5$

:::

---

**Example 2 — 9231/w24/qp/41 Q3 (9 marks):**

The number of goals scored per match in a tournament is recorded for 150 matches:

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 |
|-----|---|---|---|---|---|---|
| Frequency | 45 | 52 | 30 | 16 | 5 | 2 |

Test, at the 5% significance level, whether a Poisson distribution is a suitable model.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

**Step 1 — Estimate $\lambda$**

$\bar{x} = \dfrac{0 \times 45 + 1 \times 52 + 2 \times 30 + 3 \times 16 + 4 \times 5 + 5 \times 2}{150}$
$= \dfrac{0 + 52 + 60 + 48 + 20 + 10}{150} = \dfrac{190}{150} = 1.267$ **M1 A1**

**Step 2 — Poisson probabilities ($\lambda = 1.267$)**

$P(0) = e^{-1.267} = 0.2816$
$P(1) = 0.2816 \times 1.267 = 0.3568$
$P(2) = 0.3568 \times 1.267/2 = 0.2260$
$P(3) = 0.2260 \times 1.267/3 = 0.0955$
$P(4) = 0.0955 \times 1.267/4 = 0.0302$
$P(5) = 0.0302 \times 1.267/5 = 0.0077$ **A1**
$P(\geq 6) = 1 - \text{sum} = 0.0022$

**Step 3 — Expected frequencies ($E = 150 \times P$)**

| $x$ | $O$ | $E$ |
|-----|-----|-----|
| 0 | 45 | 42.24 |
| 1 | 52 | 53.52 |
| 2 | 30 | 33.90 |
| 3 | 16 | 14.33 |
| 4 | 5 | 4.53 |
| $\geq 5$ | 2 | 1.48 |

**B1** — Combine $4+$: $O = 5 + 2 = 7$, $E = 4.53 + 1.48 = 6.01$

**Step 4 — Chi-squared**

| $x$ | $O$ | $E$ | $(O-E)^2/E$ |
|-----|-----|-----|-------------|
| 0 | 45 | 42.24 | 0.180 |
| 1 | 52 | 53.52 | 0.043 |
| 2 | 30 | 33.90 | 0.448 |
| 3 | 16 | 14.33 | 0.195 |
| $\geq 4$ | 7 | 6.01 | 0.163 |

$\chi^2 = 0.180 + 0.043 + 0.448 + 0.195 + 0.163 = 1.029$ **M1 A1**

**Step 5 — df**

$k = 5$, $m = 1$ ⇒ $\mathrm{df} = 5 - 1 - 1 = 3$ **B1**

**Step 6 — Conclusion**

$\chi^2_{0.05, 3} = 7.815$ **M1**
$1.029 &lt; 7.815$ ⇒ do not reject $H_0$. **A1**

</details>

:::warning[常见陷阱]

- 当 $\lambda$ 较小（如 1.267），Poisson 分布偏斜，尾部合并更关键

:::

---

**Example 3 — 9231/w25/qp/41 Q2 (9 marks):**

The number of bacteria colonies per square on a slide is recorded for 120 squares:

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|-----|---|---|---|---|---|---|---|
| Frequency | 18 | 32 | 31 | 22 | 11 | 4 | 2 |

Test, at the 5% significance level, whether a Poisson distribution is a suitable model.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

**Step 1 — Estimate $\lambda$**

$\bar{x} = \dfrac{0 \times 18 + 1 \times 32 + 2 \times 31 + 3 \times 22 + 4 \times 11 + 5 \times 4 + 6 \times 2}{120}$
$= \dfrac{0 + 32 + 62 + 66 + 44 + 20 + 12}{120} = \dfrac{236}{120} = 1.967$ **M1 A1**

**Step 2 — Poisson probabilities ($\lambda = 1.967$)**

$P(0) = e^{-1.967} = 0.1398$
$P(1) = 0.1398 \times 1.967 = 0.2750$
$P(2) = 0.2750 \times 1.967/2 = 0.2704$
$P(3) = 0.2704 \times 1.967/3 = 0.1773$
$P(4) = 0.1773 \times 1.967/4 = 0.0872$
$P(5) = 0.0872 \times 1.967/5 = 0.0343$
$P(6) = 0.0343 \times 1.967/6 = 0.0112$ **A1**
$P(\geq 7) = 1 - \text{sum} = 0.0048$

**Step 3 — Expected frequencies ($E = 120 \times P$)**

| $x$ | $O$ | $E$ |
|-----|-----|-----|
| 0 | 18 | 16.78 |
| 1 | 32 | 33.00 |
| 2 | 31 | 32.45 |
| 3 | 22 | 21.28 |
| 4 | 11 | 10.46 |
| 5 | 4 | 4.12 |
| $\geq 6$ | 2 | 1.91 |

**B1** — Combine $5+$: $O = 4 + 2 = 6$, $E = 4.12 + 1.91 = 6.03$

**Step 4 — Chi-squared**

| $x$ | $O$ | $E$ | $(O-E)^2/E$ |
|-----|-----|-----|-------------|
| 0 | 18 | 16.78 | 0.089 |
| 1 | 32 | 33.00 | 0.030 |
| 2 | 31 | 32.45 | 0.065 |
| 3 | 22 | 21.28 | 0.024 |
| 4 | 11 | 10.46 | 0.028 |
| $\geq 5$ | 6 | 6.03 | 0.000 |

$\chi^2 = 0.089 + 0.030 + 0.065 + 0.024 + 0.028 + 0.000 = 0.236$ **M1 A1**

**Step 5 — df**

$k = 6$, $m = 1$ ⇒ $\mathrm{df} = 6 - 1 - 1 = 4$ **B1**

**Step 6 — Conclusion**

$\chi^2_{0.05, 4} = 9.488$ **M1**
$0.236 &lt; 9.488$ ⇒ do not reject $H_0$. **A1**

</details>

:::warning[常见陷阱]

- 当 $\chi^2$ 非常小时（如 0.236），模型拟合非常好，但仍需按步骤完整作答

:::

---

## Question Type 3: Test for Independence (Contingency Tables)

### 如何识别

题目给出行列分类的频数表，要求检验两个变量是否独立。关键词："test for independence"、"test for association"、"contingency table"

:::note[标准解题方法]

1. 计算行和 $R_i$、列和 $C_j$、总和 $T$
2. 每格期望频数 $E_{ij} = \dfrac{R_i \times C_j}{T}$
3. 检查 $E_{ij} \geq 5$，否则合并行或列
4. $\chi^2 = \sum \dfrac{(O_{ij} - E_{ij})^2}{E_{ij}}$
5. $\mathrm{df} = (r - 1)(c - 1)$
6. 查表比较

:::

:::info[评分标准（MS 模式）]

- 行和、列和：**B1**
- $E_{ij}$ 计算：**M1** 方法，**A1** 全部正确
- 合并（若需要）：**B1**
- $\chi^2$ 计算：**M1 A1**
- 自由度 **B1**，结论 **M1 A1**

:::

**Example 1 — 9231/s20/qp/41 Q1 (7 marks):**

A survey records favourite ice cream flavour by age group:

| | Vanilla | Chocolate | Strawberry | Total |
|---|---------|-----------|------------|-------|
| Children | 25 | 30 | 15 | 70 |
| Adults | 35 | 20 | 25 | 80 |
| Total | 60 | 50 | 40 | 150 |

Test at the 5% significance level whether flavour preference is independent of age group.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

**Step 1 — Expected frequencies**

$E_{11} = \dfrac{70 \times 60}{150} = 28.0$
$E_{12} = \dfrac{70 \times 50}{150} = 23.33$
$E_{13} = \dfrac{70 \times 40}{150} = 18.67$
$E_{21} = \dfrac{80 \times 60}{150} = 32.0$
$E_{22} = \dfrac{80 \times 50}{150} = 26.67$
$E_{23} = \dfrac{80 \times 40}{150} = 21.33$ **M1 A1**

All $E \geq 5$ ✓

**Step 2 — Chi-squared**

| Cell | $O$ | $E$ | $(O-E)^2/E$ |
|------|-----|-----|-------------|
| C–V | 25 | 28.0 | 0.321 |
| C–Ch | 30 | 23.33 | 1.907 |
| C–S | 15 | 18.67 | 0.721 |
| A–V | 35 | 32.0 | 0.281 |
| A–Ch | 20 | 26.67 | 1.668 |
| A–S | 25 | 21.33 | 0.631 |

$\chi^2 = 0.321 + 1.907 + 0.721 + 0.281 + 1.668 + 0.631 = 5.529$ **M1 A1**

**Step 3 — df**

$r = 2$, $c = 3$ ⇒ $\mathrm{df} = (2-1)(3-1) = 2$ **B1**

**Step 4 — Conclusion**

$\chi^2_{0.05, 2} = 5.991$ **M1**
$5.529 &lt; 5.991$ ⇒ do not reject $H_0$.

No evidence of association between age and flavour preference. **A1**

</details>

:::warning[常见陷阱]

- $E$ 用分数或小数，不要四舍五入到整数
- $(r-1)(c-1)$ 不是 $r \times c$

:::

---

**Example 2 — 9231/s21/qp/41 Q2 (8 marks):**

Students are classified by grade (A, B, C) and study method (Self-study, Tutored, Mixed):

| | A | B | C | Total |
|---|----|----|----|-------|
| Self-study | 12 | 20 | 8 | 40 |
| Tutored | 18 | 15 | 17 | 50 |
| Mixed | 15 | 25 | 10 | 50 |
| Total | 45 | 60 | 35 | 140 |

Test at the 5% significance level whether grade is independent of study method.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

**Step 1 — Expected frequencies**

$E_{11} = \dfrac{40 \times 45}{140} = 12.86$
$E_{12} = \dfrac{40 \times 60}{140} = 17.14$
$E_{13} = \dfrac{40 \times 35}{140} = 10.00$
$E_{21} = \dfrac{50 \times 45}{140} = 16.07$
$E_{22} = \dfrac{50 \times 60}{140} = 21.43$
$E_{23} = \dfrac{50 \times 35}{140} = 12.50$
$E_{31} = \dfrac{50 \times 45}{140} = 16.07$
$E_{32} = \dfrac{50 \times 60}{140} = 21.43$
$E_{33} = \dfrac{50 \times 35}{140} = 12.50$ **M1 A1**

All $E \geq 5$ ✓

**Step 2 — Chi-squared**

$\chi^2 = \dfrac{(12-12.86)^2}{12.86} + \dfrac{(20-17.14)^2}{17.14} + \dfrac{(8-10)^2}{10} + \dfrac{(18-16.07)^2}{16.07} + \dfrac{(15-21.43)^2}{21.43} + \dfrac{(17-12.50)^2}{12.50} + \dfrac{(15-16.07)^2}{16.07} + \dfrac{(25-21.43)^2}{21.43} + \dfrac{(10-12.50)^2}{12.50}$

$= 0.057 + 0.477 + 0.400 + 0.232 + 1.929 + 1.620 + 0.071 + 0.595 + 0.500 = 5.881$

$\chi^2 = 5.881$ **M1 A1**

**Step 3 — df**

$r = 3$, $c = 3$ ⇒ $\mathrm{df} = (3-1)(3-1) = 4$ **B1**

**Step 4 — Conclusion**

$\chi^2_{0.05, 4} = 9.488$ **M1**
$5.881 &lt; 9.488$ ⇒ do not reject $H_0$. **A1**

</details>

:::warning[常见陷阱]

- $3 \times 3$ 表自由度是 4，不是 9
- 每个 $E$ 都要分别计算，不要以为对称就一定相等

:::

---

**Example 3 — 9231/w23/qp/41 Q2 (8 marks):**

A survey records preferred mobile OS by gender:

| | iOS | Android | Other | Total |
|---|-----|---------|-------|-------|
| Male | 28 | 35 | 7 | 70 |
| Female | 32 | 25 | 13 | 70 |
| Total | 60 | 60 | 20 | 140 |

Test at the 5% significance level whether OS preference is independent of gender.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

**Step 1 — Expected frequencies**

$E_{11} = \dfrac{70 \times 60}{140} = 30.0$
$E_{12} = \dfrac{70 \times 60}{140} = 30.0$
$E_{13} = \dfrac{70 \times 20}{140} = 10.0$
$E_{21} = \dfrac{70 \times 60}{140} = 30.0$
$E_{22} = \dfrac{70 \times 60}{140} = 30.0$
$E_{23} = \dfrac{70 \times 20}{140} = 10.0$ **M1 A1**

All $E \geq 5$ ✓

**Step 2 — Chi-squared**

| Cell | $O$ | $E$ | $(O-E)^2/E$ |
|------|-----|-----|-------------|
| M–iOS | 28 | 30.0 | 0.133 |
| M–And | 35 | 30.0 | 0.833 |
| M–Oth | 7 | 10.0 | 0.900 |
| F–iOS | 32 | 30.0 | 0.133 |
| F–And | 25 | 30.0 | 0.833 |
| F–Oth | 13 | 10.0 | 0.900 |

$\chi^2 = 0.133 + 0.833 + 0.900 + 0.133 + 0.833 + 0.900 = 3.732$ **M1 A1**

**Step 3 — df**

$r = 2$, $c = 3$ ⇒ $\mathrm{df} = (2-1)(3-1) = 2$ **B1**

**Step 4 — Conclusion**

$\chi^2_{0.05, 2} = 5.991$ **M1**
$3.732 &lt; 5.991$ ⇒ do not reject $H_0$. **A1**

</details>

:::warning[常见陷阱]

- 本题行列对称（行等和、列等和），可直接用公式：$E = 70 \times 60 / 140 = 30$ 等，注意 Others 列的期望是 10

:::

---

**Example 4 — 9231/s24/qp/41 Q5 (9 marks):**

Data on smoking habits and exercise frequency:

| | Never smoke | Occasional | Regular | Total |
|---|-------------|------------|---------|-------|
| Exercises | 45 | 20 | 10 | 75 |
| Does not exercise | 25 | 25 | 25 | 75 |
| Total | 70 | 45 | 35 | 150 |

Test at the 5% significance level whether smoking habit is independent of exercise.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

**Step 1 — Expected frequencies**

$E_{11} = \dfrac{75 \times 70}{150} = 35.0$
$E_{12} = \dfrac{75 \times 45}{150} = 22.5$
$E_{13} = \dfrac{75 \times 35}{150} = 17.5$
$E_{21} = \dfrac{75 \times 70}{150} = 35.0$
$E_{22} = \dfrac{75 \times 45}{150} = 22.5$
$E_{23} = \dfrac{75 \times 35}{150} = 17.5$ **M1 A1**

All $E \geq 5$ ✓

**Step 2 — Chi-squared**

| Cell | $O$ | $E$ | $(O-E)^2/E$ |
|------|-----|-----|-------------|
| E–N | 45 | 35.0 | 2.857 |
| E–O | 20 | 22.5 | 0.278 |
| E–R | 10 | 17.5 | 3.214 |
| NE–N | 25 | 35.0 | 2.857 |
| NE–O | 25 | 22.5 | 0.278 |
| NE–R | 25 | 17.5 | 3.214 |

$\chi^2 = 2.857 + 0.278 + 3.214 + 2.857 + 0.278 + 3.214 = 12.698$ **M1 A1**

**Step 3 — df**

$r = 2$, $c = 3$ ⇒ $\mathrm{df} = (2-1)(3-1) = 2$ **B1**

**Step 4 — Conclusion**

$\chi^2_{0.05, 2} = 5.991$ **M1**
$12.698 &gt; 5.991$ ⇒ reject $H_0$.

Evidence of association between smoking and exercise. **A1**

</details>

:::warning[常见陷阱]

- 本题 $\chi^2$ 很大（12.698），明显拒绝 $H_0$，仍需写出完整比较过程

:::

---

## Question Type 4: GoF for a Given Probability Function

### 如何识别

题目给出一个概率质量函数（PMF）或概率密度函数（PDF），要求检验数据是否服从该分布。

:::note[标准解题方法]

1. 使用给定分布公式计算 $P(X = x)$
2. 计算期望频数 $E = n \times P(X = x)$
3. 合并 $E &lt; 5$ 的类别
4. $\chi^2 = \sum (O-E)^2/E$
5. 自由度注意：若分布参数固定（无需估计），则 $m = 0$

:::

:::info[评分标准（MS 模式）]

- 使用给定分布计算概率：**M1 A1**
- 期望频数：**M1 A1**
- 合并：**B1**
- $\chi^2$：**M1 A1**
- 自由度：**B1**
- 结论：**M1 A1**

:::

**Example 1 — 9231/s23/qp/41 Q3 (10 marks):**

A discrete random variable $X$ has probability function $P(X = x) = \dfrac{k}{x + 1}$ for $x = 0, 1, 2, 3, 4$. The following observed frequencies are obtained from 200 trials:

| $x$ | 0 | 1 | 2 | 3 | 4 |
|-----|---|---|---|---|---|
| Frequency | 68 | 56 | 38 | 24 | 14 |

Test at the 5% significance level whether the data fit the given distribution.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

**Step 1 — Find $k$**

$\sum_{x=0}^4 \dfrac{k}{x+1} = k\left(1 + \dfrac12 + \dfrac13 + \dfrac14 + \dfrac15\right) = k\left(\dfrac{60 + 30 + 20 + 15 + 12}{60}\right) = k \times \dfrac{137}{60} = 1$

$k = \dfrac{60}{137}$ **M1 A1**

**Step 2 — Theoretical probabilities**

$P(0) = \dfrac{60}{137} \times 1 = 0.4380$
$P(1) = \dfrac{60}{137} \times \dfrac12 = 0.2190$
$P(2) = \dfrac{60}{137} \times \dfrac13 = 0.1460$
$P(3) = \dfrac{60}{137} \times \dfrac14 = 0.1095$
$P(4) = \dfrac{60}{137} \times \dfrac15 = 0.0876$ **A1**

**Step 3 — Expected frequencies ($E = 200 \times P$)**

| $x$ | $O$ | $E$ |
|-----|-----|-----|
| 0 | 68 | 87.60 |
| 1 | 56 | 43.80 |
| 2 | 38 | 29.20 |
| 3 | 24 | 21.90 |
| 4 | 14 | 17.52 |

All $E \geq 5$ ✓ **B1**

**Step 4 — Chi-squared**

$\chi^2 = \dfrac{(68-87.60)^2}{87.60} + \dfrac{(56-43.80)^2}{43.80} + \dfrac{(38-29.20)^2}{29.20} + \dfrac{(24-21.90)^2}{21.90} + \dfrac{(14-17.52)^2}{17.52}$

$= 4.388 + 3.397 + 2.652 + 0.201 + 0.707 = 11.345$ **M1 A1**

**Step 5 — df**

$k = 5$ categories, $m = 0$ (no parameters estimated — $k$ was derived from the distribution, not estimated from data)
$\mathrm{df} = 5 - 1 - 0 = 4$ **B1**

**Step 6 — Conclusion**

$\chi^2_{0.05, 4} = 9.488$ **M1**
$11.345 &gt; 9.488$ ⇒ reject $H_0$.

Data does not fit the given distribution. **A1**

</details>

:::warning[常见陷阱]

- 注意 $m = 0$ 还是 $m = 1$：本题中分布参数 $k$ 由概率总和为 1 确定，**不是**从数据估计的，所以 $m = 0$
- 如果分布有未知参数（如 Binomial 的 $p$）且从数据估计，则 $m = 1$

:::

---

**Example 2 — 9231/s20/qp/41 Q1 variation (6 marks):**

Given $P(X = x) = \dfrac{1}{5}$ for $x = 1, 2, 3, 4, 5$ (uniform distribution), observed frequencies from 100 trials:

| $x$ | 1 | 2 | 3 | 4 | 5 |
|-----|---|---|---|---|---|
| Frequency | 15 | 25 | 22 | 18 | 20 |

Test at the 5% level.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

**Step 1 — Expected frequencies**

$P(X = x) = 0.2$ for all $x$
$E = 100 \times 0.2 = 20$ for all $x$ **B1**

**Step 2 — Chi-squared**

$\chi^2 = \dfrac{(15-20)^2}{20} + \dfrac{(25-20)^2}{20} + \dfrac{(22-20)^2}{20} + \dfrac{(18-20)^2}{20} + \dfrac{(20-20)^2}{20}$

$= 1.25 + 1.25 + 0.20 + 0.20 + 0.00 = 2.90$ **M1 A1**

**Step 3 — df**

$k = 5$, $m = 0$ ⇒ $\mathrm{df} = 5 - 1 = 4$ **B1**

**Step 4 — Conclusion**

$\chi^2_{0.05, 4} = 9.488$ **M1**
$2.90 &lt; 9.488$ ⇒ do not reject $H_0$. **A1**

</details>

:::warning[常见陷阱]

- 均匀分布没有估计参数，$m = 0$

:::
