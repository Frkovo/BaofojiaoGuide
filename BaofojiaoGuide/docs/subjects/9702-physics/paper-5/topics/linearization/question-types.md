---
title: 题型分析
sidebar_position: 2
---

# 题型分析

## Question Type 1: Standard Linearization ($y = mx + c$)

### 如何识别

Equation can be rearranged directly to $y = mx + c$ without logarithms. Variables are linearly related.

:::note[标准解题方法]

1. Rearrange given equation to $y = mx + c$ form
2. Identify what goes on $y$-axis and $x$-axis
3. Write expression for gradient and y-intercept
4. Check that the expression is dimensionally correct

:::

:::info[评分标准（MS 模式）]

- **M1**: Correct rearrangement to $y = mx + c$
- **A1**: Correct identification of $y$ and $x$ variables
- **B1**: Correct expression for gradient
- **B1**: Correct expression for y-intercept

:::

#### Example 1 — 9702/s20/qp/51 Q2(a)

> $$V = \frac{Q_0}{C} e^{-t/RC}$$
> A graph is plotted of $\ln V$ on the $y$-axis against $t$ on the $x$-axis. Determine expressions for the gradient and $y$-intercept.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **B1**: $\text{gradient} = -\frac{1}{CR}$
- **B1**: $y\text{-intercept} = \ln\left(\frac{Q_0}{C}\right)$

</details>

#### Example 2 — 9702/w20/qp/51 Q2(a)

> $$\frac{h_i}{h_o} = \frac{d}{f} - \frac{t}{2f} - 1$$
> A graph is plotted of $\frac{h_i}{h_o}$ on the $y$-axis against $d$ on the $x$-axis. Determine expressions for gradient and $y$-intercept.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **B1**: $\text{gradient} = \frac{1}{f}$
- **B1**: $y\text{-intercept} = -\frac{t}{2f} - 1$

</details>

#### Example 3 — 9702/s21/qp/52 Q2(a)

> $$E = I(R_1 + R_2 + r)$$
> A graph is plotted of $\frac{1}{I}$ on the $y$-axis against $(R_1 + R_2)$ on the $x$-axis. Determine expressions for gradient and $y$-intercept.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **B1**: $\text{gradient} = \frac{1}{E}$
- **B1**: $y\text{-intercept} = \frac{r}{E}$

</details>

---

## Question Type 2: Log-Log Linearization ($\lg y = \lg a + n \lg x$)

### 如何识别

Equation is a power law: $y = ax^n$

:::note[标准解题方法]

1. Take $\lg$ of both sides: $\lg y = \lg a + n \lg x$
2. Plot $\lg y$ against $\lg x$
3. Gradient $= n$, y-intercept $= \lg a$
4. Hence $a = 10^{\text{intercept}}$

:::

#### Example 1 — 9702/s22/qp/51 Q2(a)

> $$L = SZM^n$$
> A graph is plotted of $\lg L$ on the $y$-axis against $\lg M$ on the $x$-axis. Determine expressions for the gradient and $y$-intercept.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **B1**: $\text{gradient} = n$
- **B1**: $y\text{-intercept} = \lg(SZ)$

</details>

#### Example 2 — 9702/s22/qp/52 Q2(a)

> $$L = SKT^a$$
> A graph is plotted of $\lg L$ against $\lg T$. Determine expressions for gradient and $y$-intercept.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **B1**: $\text{gradient} = a$
- **B1**: $y\text{-intercept} = \lg(SK)$

</details>

#### Example 3 — 9702/s24/qp/52 Q2(a)

> $$T = \frac{2L^n}{C}$$
> A graph is plotted of $\lg T$ against $\lg L$. Determine gradient and $y$-intercept.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **B1**: $\text{gradient} = n$
- **B1**: $y\text{-intercept} = \lg(2/C)$

</details>

---

## Question Type 3: Log-Linear Linearization ($\ln y = \ln a + kx$)

### 如何识别

Equation is exponential: $y = ae^{kx}$

:::note[标准解题方法]

1. Take $\ln$ of both sides: $\ln y = \ln a + kx$
2. Plot $\ln y$ against $x$
3. Gradient $= k$, y-intercept $= \ln a$
4. Hence $a = e^{\text{intercept}}$

:::

#### Example 1 — 9702/s20/qp/52 Q2(a)

> $$\eta = He^{E/kT}$$
> A graph is plotted of $\ln\eta$ against $1/T$. Determine expressions for gradient and $y$-intercept.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **B1**: $\text{gradient} = \frac{E}{k}$
- **B1**: $y\text{-intercept} = \ln H$

</details>

#### Example 2 — 9702/w21/qp/52 Q2(a)

> $$R = R_0 e^{-\mu t}$$
> A graph is plotted of $\ln R$ against $t$. Determine gradient and $y$-intercept.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **B1**: $\text{gradient} = -\mu$
- **B1**: $y\text{-intercept} = \ln R_0$

</details>

:::warning[常见陷阱]

- $\ln$ of a quantity with units: write $\ln(V/\text{V})$, NOT $\ln V$
- For $\eta = He^{E/kT}$, the x-axis is $1/T$, NOT $T$
- Sign errors: check if the exponent is negative

:::

---

## Question Type 4: Reciprocal Linearization ($y = a + b/x$)

### 如何识别

Equation contains an inverse term: $y = a + \frac{b}{x}$

:::note[标准解题方法]

1. Rearrange to $y = a + b \cdot \frac{1}{x}$
2. Plot $y$ against $\frac{1}{x}$
3. Gradient $= b$, y-intercept $= a$

:::

#### Example 1 — 9702/s23/qp/51 Q2(a)

> $$V = E - \frac{I}{k}$$
> A graph is plotted of $V$ on the $y$-axis against $I$ on the $x$-axis. Determine expressions for gradient and $y$-intercept.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **B1**: $\text{gradient} = -\frac{1}{k}$
- **B1**: $y\text{-intercept} = E$

</details>

---

## 题型对比总结

| 题型 | 原始关系 | 作图方式 | Gradient | Y-intercept |
|------|---------|---------|----------|-------------|
| Standard | $y = mx + c$ | $y$ vs $x$ | $m$ | $c$ |
| Log-log | $y = ax^n$ | $\lg y$ vs $\lg x$ | $n$ | $\lg a$ |
| Log-linear | $y = ae^{kx}$ | $\ln y$ vs $x$ | $k$ | $\ln a$ |
| Reciprocal | $y = a + b/x$ | $y$ vs $1/x$ | $b$ | $a$ |
