---
title: 题型分析
sidebar_position: 2
---

# 题型分析

## Question Type 1: Uncertainty in Derived Quantities (Table)

### 如何识别

Part (b) — "Calculate and record values of $Y$. Include the absolute uncertainties."

:::note[标准解题方法]

1. Calculate the derived quantity for each row
2. Use the uncertainty propagation formula
3. Record uncertainty beside each value
4. Use consistent significant figures

:::

#### Example 1 — 9702/s20/qp/51 Q2(b)

> Values of $t$ and $V$ given. $\Delta V = 0.2$ V for all. Calculate $\ln(V/\text{V})$ with uncertainties.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: $\ln(V/\text{V})$ values calculated correctly
- **A1**: $\Delta(\ln V) = \Delta V / V$ producing uncertainties from $\pm 0.03$ to $\pm 0.14$

</details>

#### Example 2 — 9702/w20/qp/52 Q2(b)

> Values of $d$ given with $\Delta d$. Calculate $1/d$ with uncertainties.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: $1/d$ values correct
- **A1**: $\Delta(1/d) = \Delta d / d^2$ producing decreasing uncertainties

</details>

#### Example 3 — 9702/s22/qp/51 Q2(b)

> Values of $M$ given. Calculate $\lg(M/10^{30}\ \text{kg})$ with uncertainties.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: $\lg(M/10^{30})$ values correct
- **A1**: $\Delta(\lg M) = 0.434 \times \Delta M / M$

</details>

---

## Question Type 2: Gradient Uncertainty

### 如何识别

Part (c)(iii) — "Determine gradient. Include absolute uncertainty."

:::note[标准解题方法]

1. Calculate gradient of best fit line (large triangle)
2. Calculate gradient of worst acceptable line
3. Uncertainty = |best - worst|
4. Answer: $\text{gradient} \pm \text{uncertainty}$

:::

#### Example 1 — 9702/s20/qp/51 Q2(c)(iii)

> From graph of $\ln V$ against $t$, determine gradient $k$ with its absolute uncertainty.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: Best fit gradient from large triangle, $\Delta\ln V / \Delta t$
- **A1**: Worst acceptable gradient through error bars
- **A1**: $\Delta k = |k_{\text{best}} - k_{\text{worst}}|$

</details>

#### Example 2 — 9702/w22/qp/52 Q2(c)(iii)

> From graph of $V$ against $1/d$, determine gradient with uncertainty.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: Best fit line gradient using large triangle method
- **A1**: Worst acceptable line through all error bars
- **A1**: Uncertainty = absolute difference

</details>

#### Example 3 — 9702/s23/qp/51 Q2(c)(iii)

> From graph of $\lg I$ against $\lg V$, determine $n$ (gradient) with uncertainty.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: Best fit gradient = $n$
- **A1**: Worst fit gradient calculated
- **A1**: $\Delta n = |n_{\text{best}} - n_{\text{worst}}|$ given to 1 s.f.

</details>

---

## Question Type 3: Combined Uncertainty in Final Constant

### 如何识别

Part (d)(ii) — "Determine the absolute/percentage uncertainty in constant $X$."

:::note[标准解题方法]

1. If $C = -\frac{1}{R \times \text{gradient}}$, then:
2. $\frac{\Delta C}{C} = \frac{\Delta R}{R} + \frac{\Delta \text{gradient}}{\text{gradient}}$
3. $\Delta C = C \times \left(\frac{\Delta R}{R} + \frac{\Delta \text{gradient}}{\text{gradient}}\right)$

:::

#### Example 1 — 9702/s22/qp/51 Q2(d)(ii)

> Given $C = -\frac{1}{R \times k}$, find percentage uncertainty in $C$ using $\Delta R$ and $\Delta k$.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: $\frac{\Delta C}{C} = \frac{\Delta R}{R} + \frac{\Delta k}{k}$
- **A1**: Percentage uncertainty in $C$ calculated correctly
- **A1**: Final $C$ stated as value $\pm$ absolute uncertainty

</details>

#### Example 2 — 9702/w20/qp/52 Q2(d)(ii)

> Using $R = \frac{\text{gradient}}{T}$ and known $\Delta T$, find uncertainty in $R$.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: $\frac{\Delta R}{R} = \frac{\Delta \text{gradient}}{\text{gradient}} + \frac{\Delta T}{T}$
- **A1**: Correct $\Delta R$ calculated
- **A1**: Answer with consistent units

</details>

#### Example 3 — 9702/s23/qp/51 Q2(d)(ii)

> From $A = \frac{k}{10^{\text{intercept}}}$, find percentage uncertainty in $A$ given $\Delta k$ and $\Delta \text{intercept}$.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: $\frac{\Delta A}{A} = \frac{\Delta k}{k} + \ln 10 \times \Delta(\text{intercept})$
- **A1**: Correct propagation applied
- **A1**: Absolute uncertainty in $A$ to 1 s.f.

</details>

---

## Question Type 4: y-intercept Uncertainty

### 如何识别

Part (c)(iv) — "Determine y-intercept. Include absolute uncertainty."

:::note[标准解题方法]

1. Read y-intercept from best fit line
2. Read y-intercept from worst acceptable line
3. Uncertainty = $|$best intercept $-$ worst intercept$|$

:::

#### Example 1 — 9702/w22/qp/52 Q2(c)(iv)

> Determine y-intercept $\ln V_0$ with its uncertainty.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: Best fit y-intercept read correctly
- **A1**: Worst fit y-intercept read correctly
- **A1**: $\Delta(\text{intercept}) = |\text{best} - \text{worst}|$

</details>

---

### 常见陷阱

:::warning[Uncertainty 陷阱]

- 表格中 uncertainty 的有效数字位数应与原始数据匹配（通常 1-2 s.f.）
- worst line 必须通过所有 error bars，而不是随便画
- 组合误差时误用加法/乘法规则
- 忘记转换 absolute 和 percentage uncertainty

:::
