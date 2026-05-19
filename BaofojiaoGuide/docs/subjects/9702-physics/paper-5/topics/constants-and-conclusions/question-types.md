---
title: 题型分析
sidebar_position: 2
---

# 题型分析

## Question Type 1: Calculate One Constant from Gradient

### 如何识别

Part (d)(i) — "Use the gradient to determine constant $X$." 题目给出方程，gradient 对应某个表达式，反解常数。

:::note[标准解题方法]

1. 将实验方程与 $y = mx + c$ 对比
2. 确定 gradient 表达式
3. gradient $=$ expression involving constant
4. 代入数值解出常数
5. 包含单位

:::

#### Example 1 — 9702/s20/qp/51 Q2(d)(i)

> From $V = \frac{Q_0}{C}e^{-t/RC}$, the graph of $\ln V$ against $t$ has gradient $k = -\frac{1}{RC}$. Given $R = 39\ \text{k}\Omega$, determine $C$.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: Gradient $k = -\frac{1}{RC}$
- **A1**: $C = -\frac{1}{Rk}$ substituted correctly
- **A1**: $C$ given with correct unit (F or $\mu$F)

</details>

#### Example 2 — 9702/w20/qp/52 Q2(d)(i)

> From $\eta = He^{E/kT}$, the graph of $\ln \eta$ against $1/T$ has gradient $= E/k$. Given $k = 1.38 \times 10^{-23}\ \text{J K}^{-1}$, determine $E$.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: $E = \text{gradient} \times k$
- **A1**: $E$ calculated correctly
- **A1**: $E$ in J (or eV)

</details>

#### Example 3 — 9702/s22/qp/51 Q2(d)(i)

> From $L = SZM^n$, the graph of $\lg L$ against $\lg M$ has gradient $= n$. Determine $n$.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: $n = \text{gradient}$
- **A1**: $n$ correct to 2 or 3 s.f.
- **A1**: $n$ is dimensionless (no unit needed)

</details>

---

## Question Type 2: Calculate Two Constants from Gradient and Intercept

### 如何识别

Part (d)(i) — 同时用 gradient 和 y-intercept 求两个常数。公式线性化后得到 $y = mx + c$，gradient 和 intercept 分别对应不同的表达式。

:::note[标准解题方法]

1. 线性化: $y = mx + c$
2. gradient $m = f(\text{constant}_1)$
3. y-intercept $c = f(\text{constant}_2)$
4. 分别代入数值解出两个常数

:::

#### Example 1 — 9702/w21/qp/51 Q2(d)(i)

> From $f = \frac{v}{4(L + c)}$, graph of $1/f$ against $L$ has gradient $= 4/v$ and intercept $= 4c/v$. Find $v$ and $c$.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: $v = \frac{4}{\text{gradient}}$
- **A1**: $v$ calculated with unit m s$^{-1}$
- **M1**: $c = \frac{\text{intercept} \times v}{4}$
- **A1**: $c$ calculated with unit m

</details>

#### Example 2 — 9702/s23/qp/51 Q2(d)(i)

> From $y = ae^{bx}$, graph of $\ln y$ against $x$ has gradient $= b$ and intercept $= \ln a$. Find $a$ and $b$.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: $b = \text{gradient}$
- **A1**: $b$ unit from context (s$^{-1}$)
- **M1**: $a = e^{\text{intercept}}$
- **A1**: $a$ calculated with correct unit

</details>

#### Example 3 — 9702/w22/qp/52 Q2(d)(i)

> From $V = V_0 e^{-t/RC}$, graph of $\ln V$ against $t$ has gradient $= -1/RC$ and intercept $= \ln V_0$. Find $RC$ and $V_0$.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: $RC = -1/\text{gradient}$
- **A1**: $RC$ with unit s
- **M1**: $V_0 = e^{\text{intercept}}$
- **A1**: $V_0$ with unit V

</details>

---

## Question Type 3: Extension Calculations

### 如何识别

Part (e) — "Use your value of $X$ to determine $Y$." 利用已求出的常数计算另一个物理量。

:::note[标准解题方法]

1. 找到相关公式
2. 代入已求常数和已知值
3. 包含完整计算过程
4. 给出最终值 + 单位

:::

#### Example 1 — 9702/s20/qp/51 Q2(e)

> Use your value of $C$ to determine the charge $Q_0$, given that $V_0$ (from y-intercept) $= Q_0 / C$.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: $Q_0 = V_0 \times C$
- **A1**: $Q_0$ calculated correctly
- **A1**: $Q_0$ in C

</details>

#### Example 2 — 9702/s22/qp/51 Q2(e)

> Use your value of $n$ and $S$ to calculate $ZM$ when $L = 10.0$ W.

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: $ZM = (L/S)^{1/n}$
- **A1**: Numerical substitution correct
- **A1**: Final value with unit

</details>

---

## Question Type 4: Drawing Conclusions

### 如何识别

Part (f) 或 (e)(iii) — "State whether the results support the suggested relationship" 或 "Comment on the agreement."

:::note[标准解题方法]

1. 比较实验值和理论值的差异
2. 考虑不确定度范围
3. 结论必须结合 uncertainties/error bars
4. 标准句式: "The value lies within/outside the range of the uncertainty"

:::

#### Example 1 — 9702/w20/qp/52 Q2(e)

> The theoretical value of $R$ is $4.7\ \Omega$. Does your result support this?

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: Compare experimental $R \pm \Delta R$ with theoretical $4.7\ \Omega$
- **A1**: If $4.7$ lies within $R \pm \Delta R$, "supports within experimental uncertainty"
- **A1**: If outside, "does not support"

</details>

#### Example 2 — 9702/s23/qp/51 Q2(f)

> The constant $n$ is expected to be $2.0$. Does your value agree?

<details>
<summary>MS 展开查看</summary>

**MS:**
- **M1**: $n \pm \Delta n$ compared with $2.0$
- **A1**: Agreement stated with reference to uncertainty
- **A1**: "The expected value lies within/outside the uncertainty range"

</details>

---

### 常见陷阱

:::warning[Constants 陷阱]

- 忘记在最终答案中写单位
- 从 y-intercept 求常数时忘记取指数（$a = e^{\text{intercept}}$ 不是 $a = \text{intercept}$）
- 比较结论时没提 uncertainty
- 符号错误：gradient 为负时，常数可能为正

:::
