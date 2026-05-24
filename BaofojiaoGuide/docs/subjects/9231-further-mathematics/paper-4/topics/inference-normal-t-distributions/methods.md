---
title: 解题方法
sidebar_position: 4
---

# Solution Methods — Inference Using Normal and t-Distributions

## Method 1: One-Sample t-Test Procedure

适用于：单个总体均值检验，方差未知，样本量小。

:::info[Steps]

**Step 1: State hypotheses**
$$H_0: \mu = \mu_0, \quad H_1: \mu \neq \mu_0 \ (\text{or } &gt; \ \text{or } &lt;)$$

**Step 2: Calculate test statistic**
$$t = \frac{\bar{x} - \mu_0}{\sqrt{s^2/n}}$$

**Step 3: Find critical value**
From t-tables: $t_{\alpha/2}(n-1)$ (two-tail) or $t_{\alpha}(n-1)$ (one-tail)

**Step 4: Compare and conclude**
If $|t| &gt; t_{\text{crit}}$, reject $H_0$; otherwise do not reject $H_0$.

:::

## Method 2: Two-Sample Pooled t-Test Procedure

适用于：两个独立总体均值比较，方差相等但未知，样本量小。

:::info[Steps]

**Step 1: State hypotheses**
$$H_0: \mu_1 = \mu_2, \quad H_1: \mu_1 \neq \mu_2 \ (\text{or } &gt; \ \text{or } &lt;)$$

**Step 2: Pool variances**
$$s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}$$

**Step 3: Calculate test statistic**
$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_p^2(1/n_1 + 1/n_2)}}$$

**Step 4: Find critical value**
From t-tables: $t_{\alpha/2}(n_1+n_2-2)$ or $t_{\alpha}(n_1+n_2-2)$

**Step 5: Compare and conclude**

:::

## Method 3: Paired t-Test Procedure

适用于：同一组对象前后两次测量 / 配对设计。

:::info[Steps]

**Step 1: Compute differences**
$$d_i = x_i - y_i \ \text{for each pair}$$

**Step 2: Calculate mean and variance of differences**
$$\bar{d} = \frac{\sum d_i}{n}, \quad s_d^2 = \frac{\sum(d_i - \bar{d})^2}{n-1}$$

**Step 3: State hypotheses**
$$H_0: \mu_d = d_0, \quad H_1: \mu_d \neq d_0 \ (\text{or } &gt; \ \text{or } &lt;)$$

**Step 4: Calculate test statistic**
$$t = \frac{\bar{d} - d_0}{\sqrt{s_d^2/n}}$$

**Step 5: Find critical value**
From t-tables: $t_{\alpha/2}(n-1)$ or $t_{\alpha}(n-1)$

**Step 6: Compare and conclude**

:::

## Method 4: Large-Sample z-Test Procedure

适用于：大样本（$n \ge 30$）情况下的均值检验。

:::info[Steps]

**Step 1: State hypotheses**

**Step 2: Calculate z-statistic**
One-sample: $z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$  or  $z = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$
Two-sample: $z = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}}$

**Step 3: Compare with standard normal critical values**
$z_{0.05} = 1.645$, $z_{0.025} = 1.960$, $z_{0.005} = 2.576$

**Step 4: Conclude**

:::

## Method 5: Confidence Interval Construction

:::info[Steps]

**One-sample (t):**
$$\bar{x} \pm t_{\alpha/2}(n-1) \cdot \sqrt{s^2/n}$$

**Two-sample pooled (t):**
$$(\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2}(n_1+n_2-2) \cdot \sqrt{s_p^2(1/n_1 + 1/n_2)}$$

**Paired (t):**
$$\bar{d} \pm t_{\alpha/2}(n-1) \cdot \sqrt{s_d^2/n}$$

**Two-sample large (z):**
$$(\bar{x}_1 - \bar{x}_2) \pm z_{\alpha/2} \cdot \sqrt{s_1^2/n_1 + s_2^2/n_2}$$

:::

## Quick Decision Tree

```text
Is it one sample or two?
├── One sample
│   ├── Small n (n < 30), σ² unknown → One-sample t-test (Method 1)
│   └── Large n (n ≥ 30) → z-test (Method 4)
└── Two samples
    ├── Paired (same subjects) → Paired t-test (Method 3)
    └── Independent
        ├── Small n, equal σ² → Pooled t-test (Method 2)
        └── Large n → z-test (Method 4)
```
