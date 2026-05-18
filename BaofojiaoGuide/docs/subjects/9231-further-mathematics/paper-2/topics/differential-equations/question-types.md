---
title: 题型分析
sidebar_position: 3
---

# 题型分析 — Differential Equations

---

## Question Type 1: First order linear — integrating factor method

### 如何识别

可写成 $\dfrac{dy}{dx} + P(x)y = Q(x)$ 形式的一阶微分方程

**关键词：** differential equation, integrating factor, find the solution, $y = f(x)$

:::note[标准解题方法]

1. 化成标准形式 $\dfrac{dy}{dx} + Py = Q$（必要时先除以系数）
2. 积分因子 $\mu = e^{\int P\,dx}$
3. 两边乘 $\mu$：$\mu\dfrac{dy}{dx} + \mu Py = \mu Q$
4. 左边 $= \dfrac{d}{dx}(\mu y)$，所以 $\dfrac{d}{dx}(\mu y) = \mu Q$
5. 积分：$\mu y = \int \mu Q\,dx + C$
6. 解出 $y$：$y = \dfrac{1}{\mu}\left(\int \mu Q\,dx + C\right)$
7. 代入初始条件求 $C$

:::

:::info[评分标准（MS 模式）]

- **B1**: 化成标准形式（除以系数）
- **M1**: 正确计算积分因子
- **A1**: $\mu$ 正确
- **M1**: 乘 $\mu$ 后识别 $\dfrac{d}{dx}(\mu y)$
- **M1**: 积分 RHS 正确
- **A1**: 积分结果正确
- **M1**: 用初始条件
- **A1**: 最终 $y = f(x)$

:::

:::warning[常见陷阱]

- **$P$ 的符号！** 若 $\dfrac{dy}{dx} - \dfrac{2}{x}y = x$，则 $P = -\dfrac{2}{x}$，$\mu = x^{-2}$
- 必须先除以 $x$ 的系数：$x\dfrac{dy}{dx} + 2y = e^x$ → $\dfrac{dy}{dx} + \dfrac{2}{x}y = \dfrac{e^x}{x}$
- 积分 RHS 时别忘了 $\mu$：公式是 $\mu y = \int \mu Q\,dx$，不是 $\int Q\,dx$

:::

### 完整原题

**Example 1 — 9231/s20/qp/22 Q1 (6 marks):**

> Find the solution of the differential equation
> $$\frac{dy}{dx} + 5y = e^{-7x}$$
> for which $y = 0$ when $x = 0$. Give your answer in the form $y = f(x)$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1A1**: IF $= e^{5x}$
- **M1**: $\frac{d}{dx}(ye^{5x}) = e^{-2x}$
- **A1**: $ye^{5x} = -\frac12 e^{-2x} + C$
- **M1**: uses $y(0)=0$ to find $C$
- **A1**: $y = \frac12 e^{-5x} - \frac12 e^{-7x}$

</details>

**Example 2 — 9231/w20/qp/22 Q4 (8 marks):**

> Find the solution of the differential equation
> $$x\frac{dy}{dx} + 2y = e^x$$
> for which $y = 3$ when $x = 1$. Give your answer in the form $y = f(x)$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: $\frac{dy}{dx} + \frac{2}{x}y = \frac{e^x}{x}$
- **M1A1**: IF $= x^2$
- **M1**: $\frac{d}{dx}(x^2y) = xe^x$
- **A1**: $x^2y = (x-1)e^x + C$
- **M1**: $C=3$
- **A1**: $y = \frac{(x-1)e^x + 3}{x^2}$

</details>

**Example 3 — 9231/w23/qp/22 Q4 (9 marks):**

> Find the solution of the differential equation
> $$\frac{dy}{dx} + 3y = \sin x$$
> for which $y = 1$ when $x = 0$. Give your answer in the form $y = f(x)$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: IF $= e^{3x}$
- **M1**: $\frac{d}{dx}(ye^{3x}) = e^{3x}\sin x$
- **M1**: integrates RHS using integration by parts
- **A1**: $ye^{3x} = \frac{1}{10}e^{3x}(3\sin x - \cos x) + C$
- **M1**: $C$ from $y(0)=1$
- **A1**: $y = \frac{1}{10}(3\sin x - \cos x + 11e^{-3x})$

</details>

---

## Question Type 2: Second order — auxiliary equation

### 如何识别

$\dfrac{d^2y}{dx^2} + a\dfrac{dy}{dx} + by = f(x)$

**关键词：** complementary function, auxiliary equation, general solution

:::note[标准解题方法]

1. 辅助方程：$am^2 + bm + c = 0$
2. 解出 $m$：
   - 不等实根 $m_1,m_2$：CF $= Ae^{m_1x} + Be^{m_2x}$
   - 重根 $m$：CF $= (A+Bx)e^{mx}$
   - 共轭复根 $\alpha \pm i\beta$：CF $= e^{\alpha x}(A\cos\beta x + B\sin\beta x)$
3. 若 $f(x) \neq 0$，还需找特解 PI
4. 通解 $= \text{CF} + \text{PI}$

:::

### 完整原题

**Example 1 — 9231/w20/qp/22 Q6 (11 marks):**

> Find the particular solution of
> $$\frac{d^2x}{dt^2} + 8\frac{dx}{dt} + 15x = 102\cos 3t$$
> given that, when $t = 0$, $x = 1$ and $\frac{dx}{dt} = 0$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: AE $m^2+8m+15=0$
- **A1**: $m=-3,-5$
- **A1**: CF $= Ae^{-3t}+Be^{-5t}$
- **M1A1**: PI $= p\cos 3t+q\sin 3t$
- **A1**: $p=1,q=4$
- **A1**: GS $= Ae^{-3t}+Be^{-5t}+\cos 3t+4\sin 3t$
- **M1A1**: $A=6,B=-6$

</details>

**Example 2 — 9231/s22/qp/22 Q3 (8 marks):**

> The variables $t$ and $x$ are related by the differential equation
> $$\frac{d^2x}{dt^2} + \frac{dx}{dt} + x = t^2 + 1.$$
>
> (a) Find the general solution. [6]
>
> (b) Deduce an approximate value of $\frac{d^2x}{dt^2}$ for large positive values of $t$. [2]

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **M1**: AE $m^2+m+1=0$
- **M1**: $m = -\frac12 \pm i\frac{\sqrt3}{2}$
- **A1**: CF $= e^{-t/2}(A\cos\frac{\sqrt3}{2}t + B\sin\frac{\sqrt3}{2}t)$
- **M1**: PI: try $x = pt^2 + qt + r$
- **M1**: substitute and equate coefficients
- **A1**: $p=1,q=-2,r=1$, so $x_{PI}=t^2-2t+1$

**MS (b):**
- **B1**: as $t\to\infty$, CF $\to 0$
- **B1**: $\frac{d^2x}{dt^2} \approx 2$

</details>

**Example 3 — 9231/s21/qp/22 Q2 (6 marks):**

> The variables $x$ and $y$ are related by the differential equation
> $$\frac{d^2y}{dx^2} + 3\frac{dy}{dx} + 2y = 2x + 1.$$
>
> (a) Find the general solution. [6]

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **M1**: AE $m^2+3m+2=0$
- **A1**: $m=-1,-2$
- **A1**: CF $= Ae^{-x} + Be^{-2x}$
- **M1**: PI: try $y = px + q$
- **M1**: $2p + 3p + 2px + 2q = 2x+1$ → $2p=2$, $5p+2q=1$
- **A1**: $p=1,q=-2$, so $y_{PI}=x-2$

</details>

---

## Question Type 3: Particular integral determination

### 猜测表

| $f(x)$ 形式 | 尝试 $y_{PI}$ |
|------------|--------------|
| 常数 $k$ | $y = c$ |
| $ke^{ax}$ | $y = pe^{ax}$ |
| $a\cos\omega x + b\sin\omega x$ | $y = p\cos\omega x + q\sin\omega x$ |
| 多项式 | 同次多项式 |

代入原方程，比较系数求未知常数。

---

## Question Type 4: Overlap of PI with CF

### 何时发生

尝试的特解形式已经在 CF 中出现。

例如 $\dfrac{d^2y}{dx^2} + 4y = \cos 2x$
CF $= A\cos 2x + B\sin 2x$

### 处理方法

- 简单重叠：特解乘以 $x$
- 重根重叠：特解乘以 $x^2$

例如：设 PI $= x(p\cos 2x + q\sin 2x)$

---

## Question Type 5: Reduction using substitution

### 常见代换

**$x = e^t$（欧拉型方程）：**
- $\displaystyle \frac{dy}{dx} = \frac{1}{x}\frac{dy}{dt}$
- $\displaystyle \frac{d^2y}{dx^2} = \frac{1}{x^2}\left(\frac{d^2y}{dt^2} - \frac{dy}{dt}\right)$
- 原方程化为常系数方程

**$z = x + y$：**
- $\displaystyle \frac{dz}{dx} = 1 + \frac{dy}{dx}$
- $\displaystyle \frac{dy}{dx} = \frac{dz}{dx} - 1$
- 代入后化为可分离变量方程

### 完整原题

**Example 1 — 9231/s23/qp/22 Q2 (7 marks):**

> Use the substitution $z = x + y$ to find the solution of the differential equation
> $$\frac{dy}{dx} = \frac{1 + 3x + 3y}{3x + 3y - 1}$$
> for which $y = 0$ when $x = 0$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: $z = x+y$ → $\frac{dz}{dx} = 1 + \frac{dy}{dx}$
- **M1**: $\frac{dz}{dx} - 1 = \frac{1+3z}{3z-1}$
- **M1**: $\frac{dz}{dx} = \frac{6z}{3z-1}$
- **M1**: separates: $\int\frac{3z-1}{6z}dz = \int dx$
- **A1**: $\frac12 z - \frac16\ln z = x + C$
- **M1**: back-substitute $z = x+y$, use $y(0)=0$
- **A1**: $3(x+y) - \ln(x+y) = 6x$

</details>

**Example 2 — 9231/s20/qp/22 Q7 (11 marks):**

> It is given that $x = t^3y$ and
> $$\frac{d^2y}{dt^2} + (4t^3+6t^2)\frac{dy}{dt} + (13t^3+12t^2+6t)y = 61e^{t/2}.$$
>
> (a) Show that $\frac{d^2x}{dt^2} + 4\frac{dx}{dt} + 13x = 61e^{t/2}$. [4]
>
> (b) Find the general solution for $y$ in terms of $t$. [7]

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **B1**: $\frac{dx}{dt} = t^3\frac{dy}{dt} + 3t^2y$
- **B1**: $\frac{d^2x}{dt^2} = t^3\frac{d^2y}{dt^2} + 6t^2\frac{dy}{dt} + 6ty$
- **M1**: substitute into DE
- **A1**: AG

**MS (b):**
- **M1**: AE $m^2+4m+13=0$, $m=-2\pm3i$
- **A1**: CF $x = e^{-2t}(A\cos3t + B\sin3t)$
- **B1**: PI: try $x = ke^{t/2}$
- **M1**: $(1/4 + 2 + 13)k = 61$
- **A1**: $k=4$
- **M1**: $t^3y = e^{-2t}(A\cos3t+B\sin3t) + 4e^{t/2}$
- **A1**: $y = t^{-3}e^{-2t}(A\cos3t+B\sin3t) + 4t^{-3}e^{t/2}$

</details>

---

## Question Type 6: Initial value problems

:::warning[常见陷阱]

求完通解（CF + PI 合并后）**再**代初始条件，**不要**只代进 CF。

:::
