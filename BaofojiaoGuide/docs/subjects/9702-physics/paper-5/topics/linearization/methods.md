---
title: 解题方法
sidebar_position: 4
---

# 解题方法

## Method 1: Standard Linearization

### When to use

The equation is already linear or can be rearranged directly to $y = mx + c$ without applying logarithms.

### Steps

1. Identify the target variables in the question — what is being plotted on $y$ and $x$ axes
2. Rearrange the given equation so that the $y$ variable is isolated on the LHS
3. Compare with $y = mx + c$ to identify $m$ (gradient) and $c$ (intercept)

:::note[通用公式]

$$\text{Given: } f(y) = A \cdot g(x) + B$$

$$\Rightarrow \text{gradient} = A,\quad \text{intercept} = B$$

:::

### Formula

- Gradient = coefficient of the $x$-axis quantity
- Y-intercept = constant term after rearrangement

### Mistakes to avoid

- Forgetting negative signs in the coefficient
- Not simplifying compound fractions before reading off coefficients

---

## Method 2: Log-Log Linearization

### When to use

The equation is a power law: $y = ax^n$. The exponent $n$ is unknown and needs to be found from the gradient.

### Steps

1. Take $\lg$ of both sides: $\lg y = \lg a + n \lg x$
2. Plot $\lg y$ on $y$-axis against $\lg x$ on $x$-axis
3. Gradient $= n$, y-intercept $= \lg a$
4. Find $a = 10^{\text{intercept}}$

:::note[何时选 $\lg$ 而非 $\ln$]

- Power laws $y = ax^n$ → use $\lg$ (base 10)
- Exponential $y = ae^{kx}$ → use $\ln$ (base $e$)

:::

### Formula

$$\lg y = \underbrace{n}_{\text{gradient}} \lg x + \underbrace{\lg a}_{\text{intercept}}$$

### Mistakes to avoid

- Using $\ln$ instead of $\lg$ (they give different gradient values for power laws)
- Writing $\lg y$ without dividing by units: write $\lg(y/\text{unit})$
- Forgetting that $a = 10^{\text{intercept}}$, not just the intercept itself

---

## Method 3: Log-Linear Linearization

### When to use

The equation is exponential: $y = ae^{kx}$.

### Steps

1. Take $\ln$ of both sides: $\ln y = \ln a + kx$
2. Plot $\ln y$ on $y$-axis against $x$ on $x$-axis
3. Gradient $= k$, y-intercept $= \ln a$
4. Find $a = e^{\text{intercept}}$

### Formula

$$\ln y = \underbrace{k}_{\text{gradient}} x + \underbrace{\ln a}_{\text{intercept}}$$

### Mistakes to avoid

- Plotting $\ln y$ against $\ln x$ instead of against $x$
- Sign errors: if $y = ae^{-kx}$, then gradient $= -k$
- Forgetting units: $\ln(V/\text{V})$ not $\ln V$

---

## Method 4: Reciprocal Linearization

### When to use

The equation has the form $y = a + \frac{b}{x}$ or can be rearranged to show an inverse relationship.

### Steps

1. Rearrange to $y = a + b \cdot \frac{1}{x}$
2. Plot $y$ on $y$-axis against $\frac{1}{x}$ on $x$-axis
3. Gradient $= b$, y-intercept $= a$

### Formula

$$y = \underbrace{b}_{\text{gradient}} \cdot \frac{1}{x} + \underbrace{a}_{\text{intercept}}$$

### Mistakes to avoid

- Plotting $y$ against $x$ instead of $y$ against $1/x$
- Forgetting that the intercept is $a$, not $b$
- Not checking whether the relationship passes through the origin

---

## 方法选择速查

| 看见... | 用 Method | 作图方式 |
|---------|-----------|---------|
| $y = mx + c$ | Standard | $y$ vs $x$ |
| $y = ax^n$ | Log-log | $\lg y$ vs $\lg x$ |
| $y = ae^{kx}$ | Log-linear | $\ln y$ vs $x$ |
| $y = a + b/x$ | Reciprocal | $y$ vs $1/x$ |
| $x$ and $y$ are both powers | Log-log | $\lg y$ vs $\lg x$ |
| One variable is in exponent | Log-linear | $\ln y$ vs $x$ |
