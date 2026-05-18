---
title: 题型分析
sidebar_position: 3
---

# 题型分析 — Integration

---

## Question Type 1: Standard integrals of inverse functions

### 四个必须背熟的公式

$$
\int\frac{dx}{\sqrt{a^2-x^2}} = \sin^{-1}\frac{x}{a}+C
\quad\textbf{不是}\quad \sinh^{-1}\frac{x}{a}
$$

$$
\int\frac{dx}{a^2+x^2} = \frac{1}{a}\tan^{-1}\frac{x}{a}+C
$$

$$
\int\frac{dx}{\sqrt{x^2+a^2}} = \sinh^{-1}\frac{x}{a}+C
\quad\textbf{不是}\quad \cosh^{-1}\frac{x}{a}
$$

$$
\int\frac{dx}{\sqrt{x^2-a^2}} = \cosh^{-1}\frac{x}{a}+C
$$

### 配方法

若二次式不是标准形式，先配方再用公式。

例如 $\displaystyle \int\frac{dx}{\sqrt{x^2+2x+5}} = \int\frac{dx}{\sqrt{(x+1)^2+4}} = \sinh^{-1}\frac{x+1}{2}+C$

---

## Question Type 2: Trigonometric and hyperbolic substitutions

### 代换选择表

| 被积函数含 | 代换 | $dx$ | 化简用恒等式 |
|-----------|------|------|------------|
| $\sqrt{a^2-x^2}$ | $x = a\sin\theta$ | $a\cos\theta\,d\theta$ | $1-\sin^2\theta = \cos^2\theta$ |
| $\sqrt{x^2+a^2}$ | $x = a\sinh u$ | $a\cosh u\,du$ | $\cosh^2 u - \sinh^2 u = 1$ |
| $\sqrt{x^2-a^2}$ | $x = a\cosh u$ | $a\sinh u\,du$ | $\cosh^2 u - \sinh^2 u = 1$ |

---

## Question Type 3: Reduction formulae

### 标准方法

1. 分部积分：设 $u$ 为可化简的部分，$dv$ 为剩余部分
2. 结果将 $I_n$ 用 $I_{n-1}$ 或 $I_{n-2}$ 表示
3. 对具体 $n$ 反复代入直到基础情形（$I_0$ 或 $I_1$）

### 完整原题

**Example 1 — 9231/s20/qp/22 Q6 (10 marks):**

> $I_n = \displaystyle\int_0^{1/2} (1-x^2)^{n/2}\,dx$。
>
> (a) Find $I_1$. [2]
>
> (b) By considering $\dfrac{d}{dx}\left[x(1-x^2)^{n/2}\right]$, show that
> $$nI_{n+2} = 2^{-\frac n2}\sqrt{3} + (n-1)I_n.$$ [5]
>
> (c) Find $I_5$ in the form $k\sqrt{3}$. [3]

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **M1**: $\int(1-x^2)^{-1/2}dx = \sin^{-1}x$
- **A1**: $I_1 = \pi/6$

**MS (b):**
- **M1**: differentiates $x(1-x^2)^{n/2}$
- **M1**: splits into $(1-x^2)^{n/2} - n(1-x^2)^{n/2-1} + n(1-x^2)^{n/2}$
- **M1**: integrates from 0 to 1/2
- **A1**: $nI_{n+2} = \left(\frac12\right)^{n/2}\sqrt{3} + (n-1)I_n$

**MS (c):**
- **B1**: $I_3 = \frac{\sqrt{3}}{4}$
- **M1**: uses formula with $n=3$
- **A1**: $I_5 = \frac{10\sqrt{3}}{27}$

</details>

**Example 2 — 9231/s23/qp/22 Q4 (9 marks):**

> $I_n = \displaystyle\int_0^1 (1+x^5)^n\,dx$.
>
> (a) By considering $\dfrac{d}{dx}[x(1+x^5)^n]$, show that
> $$(5n+1)I_n = 2^n + 5nI_{n-1}.$$ [5]
>
> (b) Find the exact value of $I_1$. [4]

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **M1**: differentiates $x(1+x^5)^n$
- **M1**: $(1+x^5)^n + 5nx^5(1+x^5)^{n-1}$
- **M1**: writes $x^5 = (1+x^5) - 1$
- **M1**: integrates from 0 to 1
- **A1**: AG

**MS (b):**
- **M1**: $I_1 = \int_0^1 (1+x^5)dx$
- **A1**: $= \left[x + \frac{x^6}{6}\right]_0^1 = \frac76$

</details>

**Example 3 — 9231/s24/qp/22 Q4 (8 marks):**

> For $n \ge 0$, $I_n = \displaystyle\int_0^{\ln 3} \operatorname{sech}^n x\,dx$.
>
> (a) Show that, for $n \ge 2$,
> $$(n-1)I_n = \left(\frac35\right)^{n-2} + (n-2)I_{n-2}.$$ [5]
>
> (b) Find the value of $I_2$. [3]

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **M1**: writes $\operatorname{sech}^n x = \operatorname{sech}^{n-2}x \cdot \operatorname{sech}^2 x$
- **M1**: uses $\frac{d}{dx}\tanh x = \operatorname{sech}^2 x$
- **M1**: integration by parts or differentiation trick
- **A1**: recurrence relation derived

**MS (b):**
- **M1**: $I_2 = \int_0^{\ln 3} \operatorname{sech}^2 x\,dx = [\tanh x]_0^{\ln 3}$
- **M1**: $\tanh(\ln 3) = \frac{3-1/3}{3+1/3} = \frac{4}{5}$
- **A1**: $I_2 = \frac45$

</details>

---

## Question Type 4: Arc length and surface area of revolution

### 公式

**弧长（直角坐标）：**
$$s = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx$$

**弧长（参数式）：**
$$s = \int_{t_1}^{t_2} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt$$

**表面积（绕 $x$ 轴）：**
$$S = 2\pi\int_a^b y\,\sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx$$

:::warning[常见陷阱]

- 弧长和表面积公式搞混！弧长是 $\int\sqrt{1+(dy/dx)^2}\,dx$，表面积多了 $2\pi y$
- 表面积忘了 $2\pi$ 因子和 $y$ 因子

:::

### 完整原题

**Example 1 — 9231/s20/qp/22 Q5(c) (5 marks):**

> $C_1: y = \cosh x$ 与 $C_2: y = \sinh^2 x$ 交于 $x = a = \ln(\frac12 + \frac12\sqrt{5})$。求 $C_1$ 从 $x=0$ 到 $x=a$ 的弧长。

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: $s = \int_0^a \sqrt{1+\sinh^2 x}\,dx$
- **M1**: $1+\sinh^2 x = \cosh^2 x$
- **M1**: $s = \int_0^a \cosh x\,dx$
- **M1**: $= \sinh a$
- **A1**: $\sinh a = \frac12$

</details>

**Example 2 — 9231/w22/qp/22 Q3(a) (6 marks):**

> A curve has equation $y = \frac12(e^x + e^{-x})$, for $0 \le x \le 1$. Find, in terms of $\pi$ and $e$, the area of the surface generated when the curve is rotated through $2\pi$ radians about the $x$-axis.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: $S = 2\pi\int_0^1 y\sqrt{1+(dy/dx)^2}dx$
- **M1**: $\frac{dy}{dx} = \frac12(e^x - e^{-x}) = \sinh x$
- **M1**: $\sqrt{1+\sinh^2 x} = \cosh x$
- **A1**: $S = 2\pi\int_0^1 \frac12(e^x+e^{-x})\cosh x\,dx$
- **M1**: $\cosh x = \frac12(e^x+e^{-x})$
- **A1**: $S = \frac{\pi}{2}\int_0^1 (e^x+e^{-x})^2 dx = \frac{\pi}{2}\int_0^1 (e^{2x}+2+e^{-2x})dx$ $= \frac{\pi}{2}\left[\frac12 e^{2x} + 2x - \frac12 e^{-2x}\right]_0^1 = \frac{\pi}{4}(e^2 - e^{-2} + 4)$

</details>

:::note[解题过程]

$\dfrac{dy}{dx} = \sinh x$

$1 + \left(\dfrac{dy}{dx}\right)^2 = 1 + \sinh^2 x = \cosh^2 x$

$s = \displaystyle\int_0^a \sqrt{\cosh^2 x}\,dx = \int_0^a \cosh x\,dx = [\sinh x]_0^a = \sinh a$

由 $\cosh a = \dfrac{1+\sqrt{5}}{2}$，$\sinh a = \sqrt{\cosh^2 a - 1} = \dfrac12$

所以 $s = \dfrac12$

:::

---

## Question Type 5: Rectangle bounds and inequalities for sums

### 标准方法

1. 确定矩形高：
   - 上界用右端点 $f(r/n)$
   - 下界用左端点 $f((r-1)/n)$
2. 求和：$\displaystyle\sum_{r=1}^n \frac{1}{n}f\left(\frac{r}{n}\right)$
3. 用求和公式：
   $\displaystyle\sum r = \frac{n(n+1)}{2}$
   $\displaystyle\sum r^2 = \frac{n(n+1)(2n+1)}{6}$
4. 化简代数式，与积分比较得出不等式

### 完整原题

**Example 1 — 9231/s20/qp/22 Q4 (8 marks):**

> 曲线 $y = x^2$ 在 $0 \le x \le 1$ 上有 $n$ 个等宽 $\frac{1}{n}$ 的矩形。
> (a) 考虑矩形面积之和，证明 $\displaystyle\int_0^1 x^2\,dx \le \frac{2n^2+3n+1}{6n^2}$.
> (b) 用类似方法找出下界。

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **M1**: sum $= \frac1n\sum_{r=1}^n (\frac{r}{n})^2 = \frac{1}{n^3}\sum r^2$
- **A1**: $= \frac{1}{n^3}\cdot\frac{n(n+1)(2n+1)}{6}$
- **M1**: simplifies
- **A1**: $\frac{2n^2+3n+1}{6n^2}$

**MS (b):**
- **M1**: lower bound uses left endpoints
- **A1**: $= \frac{(n-1)n(2n-1)}{6n^3}$
- **A1**: $= \frac{2n^2-3n+1}{6n^2}$

</details>

**Example 2 — 9231/s21/qp/22 Q3 (8 marks):**

> 曲线 $y = x^3$ 在 $0 \le x \le 1$ 上有 $n$ 个等宽 $\frac{1}{n}$ 的矩形。
>
> (a) 证明 $\displaystyle\int_0^1 x^3\,dx \le U_n$，其中 $U_n = \left(\frac{n+1}{2n}\right)^2$. [4]
>
> (b) 用类似方法找出下界 $L_n$. [4]

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **M1**: $\frac1n\sum_{r=1}^n (\frac{r}{n})^3 = \frac1{n^4}\sum r^3$
- **A1**: $= \frac1{n^4} \cdot \frac{n^2(n+1)^2}{4}$
- **M1**: simplifies to $\frac{(n+1)^2}{4n^2}$
- **A1**: AG

**MS (b):**
- **M1**: left endpoints: $\frac1n\sum_{r=0}^{n-1} (\frac{r}{n})^3 = \frac1{n^4}\sum_{r=1}^{n-1} r^3$
- **A1**: $= \frac1{n^4} \cdot \frac{(n-1)^2 n^2}{4}$
- **A1**: $L_n = \frac{(n-1)^2}{4n^2}$

</details>

**Example 3 — 9231/w21/qp/22 Q3 (8 marks):**

> 曲线 $y = 1-x^2$ 在 $0 \le x \le 1$ 上有 $n$ 个等宽 $\frac{1}{n}$ 的矩形。
>
> (a) 证明 $\displaystyle\int_0^1 (1-x^2)\,dx \le \frac{4n^2+3n-1}{6n^2}$. [4]
>
> (b) 求下界。 [4]

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **M1**: $\frac1n\sum_{r=1}^n (1-(\frac{r}{n})^2) = 1 - \frac1{n^3}\sum r^2$
- **A1**: $= 1 - \frac{(n+1)(2n+1)}{6n^2}$
- **M1**: simplifies
- **A1**: $\frac{4n^2+3n-1}{6n^2}$

**MS (b):**
- **M1**: left endpoints: $\frac1n\sum_{r=0}^{n-1} (1-(\frac{r}{n})^2)$
- **A1**: $= 1 - \frac{(n-1)n(2n-1)}{6n^3}$
- **A1**: $= \frac{4n^2-3n+1}{6n^2}$

</details>
