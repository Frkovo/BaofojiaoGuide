---
title: 题型分析
sidebar_position: 2
---

# 题型分析 — Inference Using Normal and t-Distributions

## Question Type 1: One-Sample t-Test

### 如何识别

- 问题涉及 **单个总体** 的均值
- 样本量 **较小**（通常 $n &lt; 30$）
- 总体方差 **未知**（题目给出样本标准差 $s$ 或样本方差 $s^2$）
- 需要检验 $H_0: \mu = \mu_0$ 是否成立

:::note[标准解题方法]

**Step 1：建立假设**

$$H_0: \mu = \mu_0$$
$$H_1: \mu \neq \mu_0 \quad\text{(双尾)} \quad\text{或}\quad \mu &gt; \mu_0 \quad\text{或}\quad \mu &lt; \mu_0 \quad\text{(单尾)}$$

**Step 2：确定显著性水平 $\alpha$**

**Step 3：计算检验统计量**

$$t = \frac{\bar{x} - \mu_0}{\sqrt{s^2/n}}$$

**Step 4：确定临界值**

查 t 分布表：$t_{\alpha/2}(n-1)$（双尾）或 $t_{\alpha}(n-1)$（单尾）

**Step 5：作出结论**

若 $|t| &gt; t_{\alpha/2}(n-1)$，拒绝 $H_0$；否则不拒绝 $H_0$

:::

:::info[评分标准（MS 模式）]

- **B1** — 正确建立 $H_0$ 和 $H_1$
- **M1** — 使用正确的 $t = (\bar{x} - \mu_0)/\sqrt{s^2/n}$
- **A1** — 正确计算 $t$ 值
- **B1** — 正确查找/陈述临界值
- **M1** — 比较检验统计量与临界值
- **A1** — 得出正确结论（拒绝/不拒绝 $H_0$），并在上下文中解释

:::

:::warning[常见陷阱]

- 自由度是 $n-1$，不是 $n$
- 必须说明正态性假设："Assume the population is normally distributed"
- 注意单尾 vs 双尾的临界值不同
- 计算 $s^2/n$ 时不要忘记 $n$ 在分母

:::

**Checklist 模板：**

```
H₀: μ = ___
H₁: μ ___ ___ (___-tailed)
α = ___
t = (x̄ - μ₀)/√(s²/n) = (___ - ___)/√(___/___) = ___
Critical value: t_{α/2}(___) = ___
Since |t| ___ t_{crit}, we ___ H₀.
```

**Exam Reference: S20 Q4, W20 Q1, S21 Q1, W21 Q1, S22 Q1, W22 Q1, S23 Q1, W23 Q1, S24 Q1, W24 Q6, S25 Q1, W25 Q1**

### Example 1（S20 Q4 改编）

A random sample of 10 observations from a normal population gave $\bar{x} = 15.2$ and $s^2 = 4.41$. Test at the 5% significance level whether the population mean is less than 16.

<details>
<summary>📝 解答展开查看</summary>

$H_0: \mu = 16$
$H_1: \mu &lt; 16$ (one-tailed)
$\alpha = 0.05$

$t = \frac{15.2 - 16}{\sqrt{4.41/10}} = \frac{-0.8}{\sqrt{0.441}} = \frac{-0.8}{0.664} = -1.205$

Critical value: $t_{0.05}(9) = 1.833$ (one-tailed, lower tail)

Since $-1.205 &gt; -1.833$ (i.e. $|t| &lt; t_{\text{crit}}$), we do **not** reject $H_0$.

Conclusion: There is insufficient evidence that the population mean is less than 16.

**Marks:** H₀/H₁ **B1**, t formula **M1**, t value **A1**, critical value **B1**, comparison **M1**, conclusion **A1** [Total: 6]
</details>

### Example 2（W21 Q1 改编）

A manufacturer claims that the mean lifetime of a battery is 120 hours. A random sample of 8 batteries gives $\bar{x} = 115$ hours, $s = 6$ hours. Assuming the population is normally distributed, test at the 1% level whether the mean lifetime differs from 120 hours.

<details>
<summary>📝 解答展开查看</summary>

$H_0: \mu = 120$
$H_1: \mu \neq 120$ (two-tailed)
$\alpha = 0.01$

$t = \frac{115 - 120}{\sqrt{36/8}} = \frac{-5}{\sqrt{4.5}} = \frac{-5}{2.121} = -2.357$

Critical value: $t_{0.005}(7) = 3.499$

Since $|-2.357| = 2.357 &lt; 3.499$, we do **not** reject $H_0$.

Conclusion: There is insufficient evidence at the 1% level that the mean lifetime differs from 120 hours.

**Marks:** H₀/H₁ **B1**, test statistic **M1A1**, critical value **B1**, comparison **M1**, conclusion **A1** [Total: 6]
</details>

### Example 3（S24 Q1 改编）

A random sample of 12 students scored a mean of 68 marks with variance 25 on a test. The national average is 72. Test at the 5% level whether the sample mean is significantly lower than the national average. State any necessary assumptions.

<details>
<summary>📝 解答展开查看</summary>

**Assumption:** The test scores are normally distributed.

$H_0: \mu = 72$
$H_1: \mu &lt; 72$ (one-tailed)
$\alpha = 0.05$

$t = \frac{68 - 72}{\sqrt{25/12}} = \frac{-4}{\sqrt{2.083}} = \frac{-4}{1.443} = -2.771$

Critical value: $t_{0.05}(11) = 1.796$

Since $-2.771 &lt; -1.796$ (i.e. $|t| &gt; t_{\text{crit}}$), we **reject** $H_0$.

Conclusion: There is sufficient evidence that the mean score is significantly lower than the national average.

**Marks:** Assumption **B1**, H₀/H₁ **B1**, t **M1A1**, cv **B1**, comparison **M1**, conclusion **A1** [Total: 7]
</details>

---

## Question Type 2: One-Sample Confidence Interval (t)

### 如何识别

- 要求构造 **总体均值的置信区间**
- 总体方差未知，使用 **t 分布**
- 区间形式为 $\bar{x} \pm \text{margin of error}$

:::note[标准解题方法]

**公式：**

$$\bar{x} \pm t_{\alpha/2}(n-1) \cdot \sqrt{\frac{s^2}{n}}$$

其中 $t_{\alpha/2}(n-1)$ 是 t 分布的上 $\alpha/2$ 分位数。

**步骤：**

1. 确定置信水平 $1-\alpha$（如 95% 对应 $\alpha = 0.05$）
2. 查找/计算 $t_{\alpha/2}(n-1)$
3. 计算标准误 $\sqrt{s^2/n}$
4. 计算边际误差 $t_{\alpha/2}(n-1) \times \sqrt{s^2/n}$
5. 写出区间 $(\bar{x} - \text{ME},\ \bar{x} + \text{ME})$

:::

:::info[评分标准（MS 模式）]

- **B1** — 正确使用置信区间公式
- **M1** — 正确代入数值
- **A1** — 正确计算标准误
- **B1** — 正确使用 t 临界值
- **A1** — 最终区间（通常要求 3 s.f.）

:::

:::warning[常见陷阱]

- 在公式中使用 $z$ 代替 $t$（样本量小时 t 更合适）
- 忘记 $\sqrt{s^2/n}$ 中的平方根
- 置信区间应写成 $(a, b)$ 形式

:::

**Checklist 模板：**

```
Confidence level: ___%
α = ___
x̄ = ___, s² = ___, n = ___
Standard error: √(s²/n) = √(___/___) = ___
t_{α/2}(___) = ___
Margin of error: ___ × ___ = ___
CI: (___ - ___, ___ + ___) = (___, ___)
```

**Exam Reference: S20 Q5, W20 Q4, S21 Q4, W22 Q6, S23 Q2, W23 Q3, S24 Q6, S25 Q4, W25 Q3**

### Example 1（S20 Q5 改编）

A random sample of 15 observations from a normal distribution gives $\bar{x} = 42.0$ and $s^2 = 9.0$. Find a 95% confidence interval for the population mean.

<details>
<summary>📝 解答展开查看</summary>

95% CI $\Rightarrow \alpha = 0.05$, $\alpha/2 = 0.025$

$t_{0.025}(14) = 2.145$

Standard error $= \sqrt{9.0/15} = \sqrt{0.6} = 0.775$

Margin of error $= 2.145 \times 0.775 = 1.662$

CI: $42.0 \pm 1.662 = (40.3,\ 43.7)$ (3 s.f.)

**Marks:** Formula **B1**, SE **M1A1**, t-value **B1**, interval **A1** [Total: 5]
</details>

### Example 2（W22 Q6 改编）

A sample of 10 light bulbs has mean lifetime 800 hours and standard deviation 40 hours. Construct a 99% confidence interval for the population mean lifetime, stating any necessary assumptions.

<details>
<summary>📝 解答展开查看</summary>

**Assumption:** The lifetimes are normally distributed.

99% CI $\Rightarrow \alpha = 0.01$, $\alpha/2 = 0.005$

$t_{0.005}(9) = 3.250$

Standard error $= \sqrt{1600/10} = \sqrt{160} = 12.65$

Margin of error $= 3.250 \times 12.65 = 41.11$

CI: $800 \pm 41.1 = (759,\ 841)$ (3 s.f.)

**Marks:** Assumption **B1**, formula **B1**, SE **M1A1**, t-value **B1**, interval **A1** [Total: 6]
</details>

### Example 3（S25 Q4 改编）

A random sample of 20 packets of cereal gives mean weight 502 g and variance 6.25 g². Find a 90% confidence interval for the population mean weight.

<details>
<summary>📝 解答展开查看</summary>

90% CI $\Rightarrow \alpha = 0.10$, $\alpha/2 = 0.05$

$t_{0.05}(19) = 1.729$

Standard error $= \sqrt{6.25/20} = \sqrt{0.3125} = 0.559$

Margin of error $= 1.729 \times 0.559 = 0.966$

CI: $502 \pm 0.966 = (501,\ 503)$ (3 s.f.)

**Marks:** Formula **B1**, SE **M1A1**, t-value **B1**, interval **A1** [Total: 5]
</details>

---

## Question Type 3: Two-Sample (Pooled) t-Test

### 如何识别

- 涉及 **两个独立总体** 的均值比较
- $H_0: \mu_1 = \mu_2$
- 两总体方差 **相等**（等方差假设 pooled variance）
- 样本量 **较小**
- 两总体方差 **未知**

:::note[标准解题方法]

**Step 1：计算合并方差**

$$s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}$$

**Step 2：计算 t 统计量**

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_p^2\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$$

**Step 3：自由度**

$$\text{df} = n_1 + n_2 - 2$$

**Step 4：比较临界值并作出结论**

:::

:::info[评分标准（MS 模式）]

- **B1** — 正确建立 $H_0$ 和 $H_1$
- **M1** — 计算合并方差 $s_p^2$
- **A1** — $s_p^2$ 数值正确
- **M1** — 使用合并方差的 t 统计量公式
- **A1** — t 值正确
- **B1** — 正确 df 和临界值
- **M1** — 比较
- **A1** — 结论

:::

:::warning[常见陷阱]

- 合并方差是 **方差的加权平均**，不是标准差的加权平均
- 自由度是 $n_1 + n_2 - 2$，不是 $n_1 + n_2$
- 必须假设 **两总体方差相等**（等方差性）且 **各自正态分布**
- 标准误：$\sqrt{s_p^2(1/n_1 + 1/n_2)}$，注意括号内是倒数之和

:::

**Checklist 模板：**

```
H₀: μ₁ = μ₂
H₁: μ₁ ___ μ₂ (___-tailed)
α = ___
n₁ = ___, x̄₁ = ___, s₁² = ___
n₂ = ___, x̄₂ = ___, s₂² = ___
s_p² = [(n₁-1)s₁² + (n₂-1)s₂²]/(n₁+n₂-2) = (___ + ___)/(___) = ___
t = (x̄₁ - x̄₂)/√(s_p²(1/n₁ + 1/n₂)) = ___/√(___ × ___) = ___
df = n₁ + n₂ - 2 = ___
Critical value: t_{α/2}(___) = ___
Since |t| ___ t_{crit}, we ___ H₀.
```

**Exam Reference: S21 Q4, W21 Q4, S22 Q5, W22 Q6, S23 Q2, W23 Q3, S24 Q6, W25 Q6**

### Example 1（S21 Q4 改编）

Two independent random samples from normal populations give:
- Sample A: $n_1 = 10$, $\bar{x}_1 = 25.0$, $s_1^2 = 6.0$
- Sample B: $n_2 = 12$, $\bar{x}_2 = 22.0$, $s_2^2 = 8.0$

Assuming equal population variances, test at the 5% level whether the population means differ.

<details>
<summary>📝 解答展开查看</summary>

$H_0: \mu_1 = \mu_2$
$H_1: \mu_1 \neq \mu_2$ (two-tailed)
$\alpha = 0.05$

$s_p^2 = \frac{(10-1) \times 6.0 + (12-1) \times 8.0}{10 + 12 - 2} = \frac{54 + 88}{20} = \frac{142}{20} = 7.10$

$t = \frac{25.0 - 22.0}{\sqrt{7.10 \times (1/10 + 1/12)}} = \frac{3.0}{\sqrt{7.10 \times 0.1833}} = \frac{3.0}{\sqrt{1.301}} = \frac{3.0}{1.141} = 2.630$

df $= 10 + 12 - 2 = 20$
Critical value: $t_{0.025}(20) = 2.086$

Since $2.630 &gt; 2.086$, we **reject** $H_0$.

Conclusion: There is sufficient evidence that the population means differ.

**Marks:** H₀/H₁ **B1**, s_p² **M1A1**, t **M1A1**, df **B1**, cv **B1**, comparison **M1**, conclusion **A1** [Total: 8]
</details>

### Example 2（W22 Q6 改编）

Two groups of students took the same test. Group A (9 students) had $\bar{x}_A = 72$, $s_A = 5$. Group B (11 students) had $\bar{x}_B = 68$, $s_B = 6$. Assuming equal population variances and normality, test at the 1% level whether the mean of Group A is greater than that of Group B.

<details>
<summary>📝 解答展开查看</summary>

$H_0: \mu_A = \mu_B$
$H_1: \mu_A &gt; \mu_B$ (one-tailed)
$\alpha = 0.01$

$s_p^2 = \frac{8 \times 25 + 10 \times 36}{9 + 11 - 2} = \frac{200 + 360}{18} = \frac{560}{18} = 31.11$

$t = \frac{72 - 68}{\sqrt{31.11 \times (1/9 + 1/11)}} = \frac{4}{\sqrt{31.11 \times 0.2020}} = \frac{4}{\sqrt{6.285}} = \frac{4}{2.507} = 1.595$

df $= 18$
Critical value: $t_{0.01}(18) = 2.552$

Since $1.595 &lt; 2.552$, we do **not** reject $H_0$.

Conclusion: There is insufficient evidence that Group A's mean is greater.

**Marks:** H₀/H₁ **B1**, s_p² **M1A1**, t **M1A1**, cv **B1**, comparison **M1**, conclusion **A1** [Total: 8]
</details>

### Example 3（S24 Q6 改编）

Two machines produce the same component. A random sample from Machine 1 (size 8) gives $\bar{x}_1 = 50.2$ mm, $s_1 = 0.3$ mm. From Machine 2 (size 10) gives $\bar{x}_2 = 49.8$ mm, $s_2 = 0.4$ mm. Test at the 5% level whether the mean sizes differ, assuming equal population variances.

<details>
<summary>📝 解答展开查看</summary>

$H_0: \mu_1 = \mu_2$
$H_1: \mu_1 \neq \mu_2$ (two-tailed)
$\alpha = 0.05$

$s_p^2 = \frac{7 \times 0.09 + 9 \times 0.16}{8 + 10 - 2} = \frac{0.63 + 1.44}{16} = \frac{2.07}{16} = 0.1294$

$t = \frac{50.2 - 49.8}{\sqrt{0.1294 \times (1/8 + 1/10)}} = \frac{0.4}{\sqrt{0.1294 \times 0.225}} = \frac{0.4}{\sqrt{0.02911}} = \frac{0.4}{0.1706} = 2.344$

df $= 16$
Critical value: $t_{0.025}(16) = 2.120$

Since $2.344 &gt; 2.120$, we **reject** $H_0$.

Conclusion: There is sufficient evidence that the mean sizes differ.

**Marks:** H₀/H₁ **B1**, s_p² **M1A1**, t **M1A1**, cv **B1**, comparison **M1**, conclusion **A1** [Total: 8]
</details>

---

## Question Type 4: Paired t-Test

### 如何识别

- **同一组对象** 在两种条件下测量（前后对比、左右对比等）
- 数据成对出现（before/after, treatment/control on same subject）
- 问题会明确说明 "paired"、"matched pairs"、"same subjects"
- $H_0: \mu_d = d_0$（通常 $d_0 = 0$）

:::note[标准解题方法]

**Step 1：计算差异**

$$d_i = x_i - y_i \quad \text{(每对差值)}$$

**Step 2：计算差值的均值和方差**

$$\bar{d} = \frac{\sum d_i}{n}, \quad s_d^2 = \frac{\sum (d_i - \bar{d})^2}{n-1}$$

**Step 3：计算 t 统计量**

$$t = \frac{\bar{d} - d_0}{\sqrt{s_d^2/n}}, \quad \text{df} = n - 1$$

**Step 4：比较临界值并作出结论**

:::

:::info[评分标准（MS 模式）]

- **B1** — 正确计算差值 $d_i$
- **M1** — 计算 $\bar{d}$ 和 $s_d^2$
- **A1** — $\bar{d}$ 和 $s_d^2$ 数值正确
- **M1** — t 统计量公式
- **A1** — t 值正确
- **B1** — df 和临界值
- **M1** — 比较
- **A1** — 结论（含上下文的解释）

:::

:::warning[常见陷阱]

- **关键假设：差值服从正态分布**（必须明确说明）
- 自由度 $= n - 1$，其中 $n$ 是 **对数**（不是测量总数）
- 不要误用独立样本的公式（配对要求计算每对差值）
- 如果题目已给出 $\bar{d}$ 和 $s_d^2$，可以直接代入公式
- 配对检验的 $\bar{d}$ 符号方向很重要（$x-y$ 还是 $y-x$ 需保持一致）

:::

**Checklist 模板：**

```
H₀: μ_d = ___
H₁: μ_d ___ ___ (___-tailed)
α = ___
d̄ = ___, s_d² = ___, n = ___
t = (d̄ - d₀)/√(s_d²/n) = (___ - ___)/√(___/___) = ___
df = n - 1 = ___
Critical value: t_{α/2}(___) = ___
Since |t| ___ t_{crit}, we ___ H₀.
```

**Assumption: The differences are normally distributed.**

**Exam Reference: S20 Q4, W20 Q4, S22 Q1, W23 Q1, S25 Q1**

### Example 1（S20 Q4 改编）

Eight students took a pre-test and post-test. The scores are:

| Student | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---------|---|---|---|---|---|---|---|---|
| Pre | 65 | 72 | 58 | 84 | 70 | 69 | 75 | 62 |
| Post | 70 | 74 | 65 | 85 | 76 | 73 | 78 | 68 |

Test at the 5% level whether the mean score has increased.

<details>
<summary>📝 解答展开查看</summary>

Differences (Post - Pre): $d = [5, 2, 7, 1, 6, 4, 3, 6]$

$n = 8$, $\bar{d} = \frac{5+2+7+1+6+4+3+6}{8} = \frac{34}{8} = 4.25$

$s_d^2 = \frac{(5-4.25)^2 + (2-4.25)^2 + \cdots + (6-4.25)^2}{7}$
$= \frac{0.5625 + 5.0625 + 7.5625 + 10.5625 + 3.0625 + 0.0625 + 1.5625 + 3.0625}{7}$
$= \frac{31.5}{7} = 4.50$

$H_0: \mu_d = 0$
$H_1: \mu_d &gt; 0$ (one-tailed, "increased")
$\alpha = 0.05$

$t = \frac{4.25 - 0}{\sqrt{4.50/8}} = \frac{4.25}{\sqrt{0.5625}} = \frac{4.25}{0.75} = 5.667$

df $= 7$
Critical value: $t_{0.05}(7) = 1.895$

Since $5.667 &gt; 1.895$, we **reject** $H_0$.

Conclusion: There is sufficient evidence that the mean score has increased.

**Marks:** Differences **B1**, d̄/s_d² **M1A1**, t **M1A1**, cv **B1**, comparison **M1**, conclusion **A1** [Total: 8]
</details>

### Example 2（W23 Q1 改编）

A study measures the reaction times (ms) of 10 subjects with and without a certain drug. The differences (without - with) have $\bar{d} = 15$ ms and $s_d^2 = 400$ ms². Test at the 1% level whether the drug affects reaction time.

<details>
<summary>📝 解答展开查看</summary>

**Assumption: The differences are normally distributed.**

$H_0: \mu_d = 0$ (no effect)
$H_1: \mu_d \neq 0$ (two-tailed, "affects")
$\alpha = 0.01$

$t = \frac{15 - 0}{\sqrt{400/10}} = \frac{15}{\sqrt{40}} = \frac{15}{6.325} = 2.372$

df $= 9$
Critical value: $t_{0.005}(9) = 3.250$

Since $2.372 &lt; 3.250$, we do **not** reject $H_0$.

Conclusion: There is insufficient evidence that the drug affects reaction time.

**Marks:** Assumption **B1**, H₀/H₁ **B1**, t **M1A1**, cv **B1**, comparison **M1**, conclusion **A1** [Total: 7]
</details>

### Example 3（S25 Q1 改编）

The heart rates of 6 patients were measured before and after exercise. The differences (after - before) are: 12, 18, -3, 25, 10, 16. Test at the 5% level whether the mean heart rate increases after exercise.

<details>
<summary>📝 解答展开查看</summary>

**Assumption: The differences are normally distributed.**

$d = [12, 18, -3, 25, 10, 16]$
$n = 6$, $\bar{d} = \frac{12+18-3+25+10+16}{6} = \frac{78}{6} = 13.0$

$s_d^2 = \frac{(12-13)^2 + (18-13)^2 + (-3-13)^2 + (25-13)^2 + (10-13)^2 + (16-13)^2}{5}$
$= \frac{1 + 25 + 256 + 144 + 9 + 9}{5} = \frac{444}{5} = 88.8$

$H_0: \mu_d = 0$
$H_1: \mu_d &gt; 0$ (one-tailed)
$\alpha = 0.05$

$t = \frac{13.0 - 0}{\sqrt{88.8/6}} = \frac{13.0}{\sqrt{14.8}} = \frac{13.0}{3.847} = 3.379$

df $= 5$
Critical value: $t_{0.05}(5) = 2.015$

Since $3.379 &gt; 2.015$, we **reject** $H_0$.

Conclusion: There is sufficient evidence that the mean heart rate increases after exercise.

**Marks:** Assumption **B1**, d̄/s_d² **M1A1**, t **M1A1**, cv **B1**, comparison **M1**, conclusion **A1** [Total: 8]
</details>

---

## Question Type 5: Two-Sample z-Test (Large Samples)

### 如何识别

- 涉及 **两个独立总体** 的均值比较
- 样本量 **足够大**（通常 $n_1, n_2 \ge 30$）
- 总体方差已知或样本量大可用 $s^2$ 替代
- 使用 **标准正态分布** $N(0,1)$

:::note[标准解题方法]

**Step 1：建立假设**

$$H_0: \mu_1 = \mu_2$$
$$H_1: \mu_1 \neq \mu_2 \quad\text{或}\quad \mu_1 &gt; \mu_2 \quad\text{或}\quad \mu_1 &lt; \mu_2$$

**Step 2：计算 z 统计量**

$$z = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} \approx \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

若 $\sigma_1^2 = \sigma_2^2 = \sigma^2$，则 $z = \frac{\bar{x}_1 - \bar{x}_2}{\sigma\sqrt{1/n_1 + 1/n_2}}$

**Step 3：比较临界值（$z_{\alpha/2}$ 或 $z_{\alpha}$）**

**Step 4：作出结论**

:::

:::info[评分标准（MS 模式）]

- **B1** — 正确建立 $H_0$ 和 $H_1$
- **M1** — 使用正确的 z 公式
- **A1** — z 值正确
- **B1** — 临界值（需使用正态分布表，不是 t 表）
- **M1** — 比较
- **A1** — 结论

:::

:::warning[常见陷阱]

- 大样本下仍有人错误使用 t 分布
- 用 $s^2$ 近似 $\sigma^2$ 时不需要合并方差（即使方差相等，大样本下也直接用）
- 分母是 $\sqrt{s_1^2/n_1 + s_2^2/n_2}$，不是 $\sqrt{(s_1^2 + s_2^2)/(n_1 + n_2)}$
- 注意区分 z 检验和 t 检验的使用条件

:::

**Checklist 模板：**

```
H₀: μ₁ = μ₂
H₁: μ₁ ___ μ₂ (___-tailed)
α = ___
x̄₁ = ___, s₁² = ___, n₁ = ___
x̄₂ = ___, s₂² = ___, n₂ = ___
z = (x̄₁ - x̄₂)/√(s₁²/n₁ + s₂²/n₂) = ___/√(___ + ___) = ___
Critical value: z_{α/2} = ___
Since |z| ___ z_{crit}, we ___ H₀.
```

**Exam Reference: S21 Q1, W21 Q4, S22 Q5, W25 Q6, S25 Q4**

### Example 1（S21 Q1 改编）

Two large independent samples from two populations give:
- Sample 1: $n_1 = 50$, $\bar{x}_1 = 105$, $s_1 = 12$
- Sample 2: $n_2 = 60$, $\bar{x}_2 = 100$, $s_2 = 15$

Test at the 5% level whether $\mu_1 &gt; \mu_2$.

<details>
<summary>📝 解答展开查看</summary>

$H_0: \mu_1 = \mu_2$
$H_1: \mu_1 &gt; \mu_2$ (one-tailed)
$\alpha = 0.05$

$z = \frac{105 - 100}{\sqrt{12^2/50 + 15^2/60}} = \frac{5}{\sqrt{144/50 + 225/60}} = \frac{5}{\sqrt{2.88 + 3.75}} = \frac{5}{\sqrt{6.63}} = \frac{5}{2.575} = 1.942$

Critical value: $z_{0.05} = 1.645$

Since $1.942 &gt; 1.645$, we **reject** $H_0$.

Conclusion: There is sufficient evidence that $\mu_1 &gt; \mu_2$.

**Marks:** H₀/H₁ **B1**, z **M1A1**, cv **B1**, comparison **M1**, conclusion **A1** [Total: 6]
</details>

### Example 2（W25 Q6 改编）

Two factories produce bolts. Factory A: $n_A = 40$, $\bar{x}_A = 10.2$ mm, $s_A = 0.5$ mm. Factory B: $n_B = 45$, $\bar{x}_B = 10.0$ mm, $s_B = 0.6$ mm. Test at the 1% level whether the mean diameters differ.

<details>
<summary>📝 解答展开查看</summary>

$H_0: \mu_A = \mu_B$
$H_1: \mu_A \neq \mu_B$ (two-tailed)
$\alpha = 0.01$

$z = \frac{10.2 - 10.0}{\sqrt{0.5^2/40 + 0.6^2/45}} = \frac{0.2}{\sqrt{0.25/40 + 0.36/45}} = \frac{0.2}{\sqrt{0.00625 + 0.008}} = \frac{0.2}{\sqrt{0.01425}} = \frac{0.2}{0.1194} = 1.675$

Critical value: $z_{0.005} = 2.576$

Since $1.675 &lt; 2.576$, we do **not** reject $H_0$.

Conclusion: There is insufficient evidence that the mean diameters differ.

**Marks:** H₀/H₁ **B1**, z **M1A1**, cv **B1**, comparison **M1**, conclusion **A1** [Total: 6]
</details>

### Example 3（S22 Q5 改编）

Exam scores from two schools: School X ($n_X = 80$, $\bar{x}_X = 72$, $s_X = 8$) and School Y ($n_Y = 100$, $\bar{x}_Y = 70$, $s_Y = 10$). Test at the 5% level whether School X has a higher mean than School Y.

<details>
<summary>📝 解答展开查看</summary>

$H_0: \mu_X = \mu_Y$
$H_1: \mu_X &gt; \mu_Y$ (one-tailed)
$\alpha = 0.05$

$z = \frac{72 - 70}{\sqrt{8^2/80 + 10^2/100}} = \frac{2}{\sqrt{64/80 + 100/100}} = \frac{2}{\sqrt{0.8 + 1.0}} = \frac{2}{\sqrt{1.8}} = \frac{2}{1.342} = 1.490$

Critical value: $z_{0.05} = 1.645$

Since $1.490 &lt; 1.645$, we do **not** reject $H_0$.

Conclusion: There is insufficient evidence that School X has a higher mean.

**Marks:** H₀/H₁ **B1**, z **M1A1**, cv **B1**, comparison **M1**, conclusion **A1** [Total: 6]
</details>

---

## Question Type 6: Confidence Interval for Difference of Means

### 如何识别

- 要求构造 **两总体均值之差** 的置信区间
- 可以是独立样本或配对样本
- 使用 **正态分布**（大样本）或 **t 分布**（小样本合并方差）

:::note[标准解题方法]

**大样本（z）：**

$$(\bar{x}_1 - \bar{x}_2) \pm z_{\alpha/2} \cdot \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}$$

**小样本等方差（t 合并）：**

$$(\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2}(n_1 + n_2 - 2) \cdot \sqrt{s_p^2\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}$$

**配对（t）：**

$$\bar{d} \pm t_{\alpha/2}(n-1) \cdot \sqrt{\frac{s_d^2}{n}}$$

:::

:::info[评分标准（MS 模式）]

- **B1** — 选择正确的公式
- **M1** — 计算标准误（或合并方差）
- **A1** — 标准误数值正确
- **B1** — 临界值（z 或 t）
- **A1** — 最终区间（3 s.f.）
- **B1** — 区间意义解释（如适用）

:::

:::warning[常见陷阱]

- 独立样本和配对样本的公式不同，不能混用
- 小样本必须用 t 而不是 z
- 合并方差只适用于等方差假设成立的情况
- 区间包含 0 意味着在对应置信水平下均值差不显著

:::

**Checklist 模板（大样本）：**

```
Confidence level: ___%
x̄₁ = ___, s₁² = ___, n₁ = ___
x̄₂ = ___, s₂² = ___, n₂ = ___
SE = √(s₁²/n₁ + s₂²/n₂) = √(___ + ___) = ___
z_{α/2} = ___
CI: (x̄₁ - x̄₂) ± z_{α/2} × SE = ___ ± ___ × ___ = (___, ___)
```

**Exam Reference: S20 Q5, W20 Q4, S21 Q4, W22 Q6, S23 Q2, W23 Q3, S24 Q6, S25 Q4, W25 Q3**

### Example 1（S20 Q5 改编）

From two independent normal populations with equal variance:
- Sample 1: $n_1 = 8$, $\bar{x}_1 = 45$, $s_1^2 = 12$
- Sample 2: $n_2 = 10$, $\bar{x}_2 = 40$, $s_2^2 = 15$

Construct a 95% confidence interval for $\mu_1 - \mu_2$.

<details>
<summary>📝 解答展开查看</summary>

95% CI $\Rightarrow \alpha = 0.05$, $\alpha/2 = 0.025$

$s_p^2 = \frac{7 \times 12 + 9 \times 15}{8 + 10 - 2} = \frac{84 + 135}{16} = \frac{219}{16} = 13.69$

$t_{0.025}(16) = 2.120$

SE $= \sqrt{13.69 \times (1/8 + 1/10)} = \sqrt{13.69 \times 0.225} = \sqrt{3.080} = 1.755$

$(\bar{x}_1 - \bar{x}_2) \pm t \times \text{SE} = 5 \pm 2.120 \times 1.755 = 5 \pm 3.721$

CI: $(1.28,\ 8.72)$ (3 s.f.)

**Marks:** s_p² **M1A1**, t-value **B1**, SE **M1A1**, interval **A1** [Total: 6]
</details>

### Example 2（W22 Q6 改编）

Two large samples:
- Sample A: $n_A = 50$, $\bar{x}_A = 100$, $s_A = 10$
- Sample B: $n_B = 60$, $\bar{x}_B = 96$, $s_B = 12$

Construct a 99% confidence interval for $\mu_A - \mu_B$.

<details>
<summary>📝 解答展开查看</summary>

99% CI $\Rightarrow \alpha = 0.01$, $\alpha/2 = 0.005$, $z_{0.005} = 2.576$

SE $= \sqrt{10^2/50 + 12^2/60} = \sqrt{100/50 + 144/60} = \sqrt{2 + 2.4} = \sqrt{4.4} = 2.098$

$(\bar{x}_A - \bar{x}_B) \pm z \times \text{SE} = 4 \pm 2.576 \times 2.098 = 4 \pm 5.404$

CI: $(-1.40,\ 9.40)$ (3 s.f.)

Since the interval contains 0, the difference is not significant at the 1% level.

**Marks:** z-value **B1**, SE **M1A1**, interval **A1**, interpretation **B1** [Total: 5]
</details>

### Example 3（S23 Q2 改编）

A paired experiment on 12 subjects gives differences with $\bar{d} = 3.5$ and $s_d^2 = 8.0$. Construct a 90% confidence interval for the mean difference.

<details>
<summary>📝 解答展开查看</summary>

90% CI $\Rightarrow \alpha = 0.10$, $\alpha/2 = 0.05$
$t_{0.05}(11) = 1.796$

SE $= \sqrt{8.0/12} = \sqrt{0.6667} = 0.8165$

$\bar{d} \pm t \times \text{SE} = 3.5 \pm 1.796 \times 0.8165 = 3.5 \pm 1.466$

CI: $(2.03,\ 4.97)$ (3 s.f.)

**Marks:** t-value **B1**, SE **M1A1**, interval **A1** [Total: 4]
</details>

---

## Quick Reference: Choosing the Correct Test

| Situation | Test | Statistic | df |
|-----------|------|-----------|----|
| One sample, $\sigma^2$ unknown, small $n$ | One-sample t | $t = \frac{\bar{x} - \mu_0}{\sqrt{s^2/n}}$ | $n-1$ |
| One sample, $\sigma^2$ known or large $n$ | z-test | $z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$ | $\infty$ |
| Two independent samples, equal $\sigma^2$, small | Pooled t | $t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_p^2(1/n_1 + 1/n_2)}}$ | $n_1+n_2-2$ |
| Two independent samples, large $n$ | z-test | $z = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}}$ | $\infty$ |
| Paired data | Paired t | $t = \frac{\bar{d} - d_0}{\sqrt{s_d^2/n}}$ | $n-1$ |

## Degrees of Freedom Summary

| Test | df Formula | Notes |
|------|------------|-------|
| One-sample t | $n-1$ | $n$ = sample size |
| Two-sample pooled t | $n_1 + n_2 - 2$ | Equal variances assumed |
| Paired t | $n-1$ | $n$ = number of pairs |
| z-test | $\infty$ | Use standard normal table |
| CI (t, one-sample) | $n-1$ | Same as one-sample t |
| CI (t, pooled) | $n_1 + n_2 - 2$ | Same as pooled t |
| CI (paired) | $n-1$ | Same as paired t |
