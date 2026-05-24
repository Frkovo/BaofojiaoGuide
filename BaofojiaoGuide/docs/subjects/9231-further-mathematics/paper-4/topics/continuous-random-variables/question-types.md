---
title: 题型分析
sidebar_position: 2
---

# 题型分析 — Continuous Random Variables

## Question Type 1: Finding Constant from PDF

求 PDF 中的未知常数。

### 如何识别

PDF 表达式含未知参数（如 $k$, $c$, $a$），需利用 $\int_{-\infty}^{\infty} f(x)\,dx = 1$ 求解。

### :::note[标准解题方法]

1. 写出 $\displaystyle \int_{-\infty}^{\infty} f(x)\,dx = 1$
2. 对 PDF 在定义域上积分
3. 分段 PDF 则在各段分别积分后求和
4. 解方程得常数
5. 验证 $f(x) \ge 0$（若常数使 PDF 出现负值则舍去）

:::

### :::info[评分标准（MS 模式）]

- **B1** 写出 $\int f(x)\,dx = 1$
- **M1** 正确积分
- **A1** 常数正确（允许 exact form 如 $\frac{3}{8}$ 或 $\frac{1}{12}$）

:::

### 典型例题

**Example 1 — 9231/s20/qp/41 Q3 (2 marks):**

> A continuous random variable $X$ has probability density function
> $$f(x) = \begin{cases} k(2x - x^2), & 0 \le x \le 2, \\ 0, & \text{otherwise.} \end{cases}$$
> Find $k$.

<details>
<summary>📝 MS 展开查看</summary>

$\int_0^2 k(2x - x^2)\,dx = 1$ **B1**

$\int_0^2 (2x - x^2)\,dx = \left[x^2 - \frac{x^3}{3}\right]_0^2 = 4 - \frac{8}{3} = \frac{4}{3}$

$k \times \frac{4}{3} = 1 \Rightarrow k = \frac{3}{4}$ **A1**

[Total: 2]
</details>

---

**Example 2 — 9231/w20/qp/41 Q6 (3 marks):**

> The continuous random variable $X$ has PDF
> $$f(x) = \begin{cases} a(1 - x), & 0 \le x \le 1, \\ a(x - 1), & 1 &lt; x \le 2, \\ 0, & \text{otherwise.} \end{cases}$$
> Find $a$.

<details>
<summary>📝 MS 展开查看</summary>

$\int_0^1 a(1 - x)\,dx + \int_1^2 a(x - 1)\,dx = 1$ **B1**

$\int_0^1 a(1 - x)\,dx = a\left[x - \frac{x^2}{2}\right]_0^1 = a\left(1 - \frac{1}{2}\right) = \frac{a}{2}$ **M1**

$\int_1^2 a(x - 1)\,dx = a\left[\frac{x^2}{2} - x\right]_1^2 = a\left[(2 - 2) - \left(\frac{1}{2} - 1\right)\right] = a\left(0 + \frac{1}{2}\right) = \frac{a}{2}$

$\frac{a}{2} + \frac{a}{2} = a = 1$ **A1**

[Total: 3]
</details>

---

**Example 3 — 9231/s25/qp/41 Q2 (2 marks):**

> A random variable $X$ has PDF
> $$f(x) = \begin{cases} kx(4 - x), & 0 \le x \le 4, \\ 0, & \text{otherwise.} \end{cases}$$
> Find $k$.

<details>
<summary>📝 MS 展开查看</summary>

$\int_0^4 kx(4 - x)\,dx = 1$ **B1**

$\int_0^4 (4x - x^2)\,dx = \left[2x^2 - \frac{x^3}{3}\right]_0^4 = 32 - \frac{64}{3} = \frac{32}{3}$

$k \times \frac{32}{3} = 1 \Rightarrow k = \frac{3}{32}$ **A1**

[Total: 2]
</details>

---

### :::warning[常见陷阱]

- 分段 PDF 积分时遗漏某一段
- 积分上下限写错（没有覆盖 PDF 非零的所有区域）
- 求出常数后未验证 $f(x) \ge 0$

:::

---

## Question Type 2: Finding CDF from PDF

由概率密度函数求累积分布函数。

### 如何识别

已知 PDF $f(x)$，要求 $F(x)$，或要求 $P(a &lt; X &lt; b)$ 且需先求 CDF。

### :::note[标准解题方法]

1. 确定 PDF 的非零区间
2. 对 $x$ 分类讨论：
   - $x$ 在左端左侧：$F(x) = 0$
   - $x$ 在每段内部：$F(x) = \int_{\text{下限}}^x f(t)\,dt$
   - $x$ 在右端右侧：$F(x) = 1$
3. 验证 $F$ 在分段边界处连续
4. 写出分段 CDF 表达式

:::

### :::info[评分标准（MS 模式）]

- **M1** 写出 $F(x) = \int f(t)\,dt$ 的形式
- **A1** 每段 $F(x)$ 表达式正确
- **B1** $F(-\infty) = 0$ 和 $F(\infty) = 1$ 已体现

:::

### 典型例题

**Example 1 — 9231/s21/qp/41 Q3 (5 marks):**

> $X$ has PDF $f(x) = \frac{3}{4}(2x - x^2)$, $0 \le x \le 2$, zero otherwise. Find $F(x)$.

<details>
<summary>📝 MS 展开查看</summary>

For $x &lt; 0$: $F(x) = 0$ **B1**

For $0 \le x \le 2$:
$F(x) = \int_0^x \frac{3}{4}(2t - t^2)\,dt$ **M1**
$= \frac{3}{4}\left[t^2 - \frac{t^3}{3}\right]_0^x$
$= \frac{3}{4}\left(x^2 - \frac{x^3}{3}\right) = \frac{3x^2}{4} - \frac{x^3}{4}$
$= \frac{x^2(3 - x)}{4}$ **A1**

For $x &gt; 2$: $F(x) = 1$ **B1**

$$
F(x) = \begin{cases}
0, & x &lt; 0, \\
\frac{x^2(3 - x)}{4}, & 0 \le x \le 2, \\
1, & x &gt; 2.
\end{cases}
$$

**A1** (for correct final form)

[Total: 5]
</details>

---

**Example 2 — 9231/s23/qp/41 Q6 (4 marks):**

> $X$ has PDF $f(x) = \frac{1}{2}\sin x$, $0 \le x \le \pi$, zero otherwise. Find $F(x)$.

<details>
<summary>📝 MS 展开查看</summary>

For $x &lt; 0$: $F(x) = 0$ **B1**

For $0 \le x \le \pi$:
$F(x) = \int_0^x \frac{1}{2}\sin t\,dt$ **M1**
$= \frac{1}{2}[-\cos t]_0^x$
$= \frac{1}{2}(-\cos x + 1)$
$= \frac{1 - \cos x}{2}$ **A1**

For $x &gt; \pi$: $F(x) = 1$ **B1**

Check: $F(\pi) = \frac{1 - (-1)}{2} = 1$ ✓

[Total: 4]
</details>

---

**Example 3 — 9231/w23/qp/41 Q4 (5 marks):**

> $X$ has PDF $f(x) = \frac{3}{8}(x - 1)^2$, $1 \le x \le 3$, zero otherwise. Find $F(x)$.

<details>
<summary>📝 MS 展开查看</summary>

For $x &lt; 1$: $F(x) = 0$ **B1**

For $1 \le x \le 3$:
$F(x) = \int_1^x \frac{3}{8}(t - 1)^2\,dt$ **M1**
$= \frac{3}{8}\left[\frac{(t-1)^3}{3}\right]_1^x$
$= \frac{(x-1)^3}{8}$ **A1**

For $x &gt; 3$: $F(x) = 1$ **B1**

Check: $F(3) = \frac{2^3}{8} = 1$ ✓

$$
F(x) = \begin{cases}
0, & x &lt; 1, \\
\frac{(x-1)^3}{8}, & 1 \le x \le 3, \\
1, & x &gt; 3.
\end{cases}
$$

**A1** (for correct piecewise)

[Total: 5]
</details>

---

### :::warning[常见陷阱]

- 积分变量混淆：用 $F(x) = \int f(t)\,dt$ 而非 $\int f(x)\,dx$
- 分段 CDF 在边界处不连续
- 遗漏左端左侧或右端右侧情况
- 积分常数未用 $F(\text{lower}) = 0$ 确定

:::

---

## Question Type 3: Finding $E(X)$ and $\text{Var}(X)$

求期望和方差。

### 如何识别

要求计算 $E(X)$ 和/或 $\text{Var}(X)$，通常紧随求常数或求 CDF 之后。

### :::note[标准解题方法]

1. 计算 $E[X] = \int x f(x)\,dx$
2. 计算 $E[X^2] = \int x^2 f(x)\,dx$
3. $\text{Var}(X) = E[X^2] - (E[X])^2$
4. 对于分段 PDF，每段乘以对应变量后积分再求和

:::

### :::info[评分标准（MS 模式）]

- **M1** $E[X] = \int x f(x)\,dx$
- **A1** $E[X]$ 正确
- **M1** $E[X^2] = \int x^2 f(x)\,dx$
- **A1** $E[X^2]$ 正确
- **M1** $\text{Var}(X) = E[X^2] - (E[X])^2$
- **A1** $\text{Var}(X)$ 正确

:::

### 典型例题

**Example 1 — 9231/s20/qp/41 Q3 (6 marks):**

> $X$ has PDF $f(x) = \frac{3}{4}(2x - x^2)$, $0 \le x \le 2$, zero otherwise.
> (i) Find $E(X)$.
> (ii) Find $\text{Var}(X)$.

<details>
<summary>📝 MS 展开查看</summary>

(i) $E[X] = \int_0^2 x \cdot \frac{3}{4}(2x - x^2)\,dx$ **M1**
$= \frac{3}{4} \int_0^2 (2x^2 - x^3)\,dx$
$= \frac{3}{4}\left[\frac{2x^3}{3} - \frac{x^4}{4}\right]_0^2$
$= \frac{3}{4}\left(\frac{16}{3} - 4\right) = \frac{3}{4} \times \frac{4}{3} = 1$ **A1**

(ii) $E[X^2] = \int_0^2 x^2 \cdot \frac{3}{4}(2x - x^2)\,dx$ **M1**
$= \frac{3}{4} \int_0^2 (2x^3 - x^4)\,dx$
$= \frac{3}{4}\left[\frac{x^4}{2} - \frac{x^5}{5}\right]_0^2$
$= \frac{3}{4}\left(8 - \frac{32}{5}\right) = \frac{3}{4} \times \frac{8}{5} = \frac{6}{5}$ **A1**

$\text{Var}(X) = \frac{6}{5} - 1^2 = \frac{1}{5}$ **M1 A1**

[Total: 6]
</details>

---

**Example 2 — 9231/s22/qp/41 Q3 (7 marks):**

> $X$ has PDF $f(x) = \frac{3}{32}x(4 - x)$, $0 \le x \le 4$, zero otherwise.
> (i) Find $E(X)$.
> (ii) Find $\text{Var}(X)$.
> (iii) Find $E(2X + 3)$.

<details>
<summary>📝 MS 展开查看</summary>

(i) $E[X] = \int_0^4 x \cdot \frac{3}{32}x(4 - x)\,dx$ **M1**
$= \frac{3}{32} \int_0^4 (4x^2 - x^3)\,dx$
$= \frac{3}{32}\left[\frac{4x^3}{3} - \frac{x^4}{4}\right]_0^4$
$= \frac{3}{32}\left(\frac{256}{3} - 64\right) = \frac{3}{32} \times \frac{64}{3} = 2$ **A1**

(ii) $E[X^2] = \int_0^4 x^2 \cdot \frac{3}{32}x(4 - x)\,dx$ **M1**
$= \frac{3}{32} \int_0^4 (4x^3 - x^4)\,dx$
$= \frac{3}{32}\left[x^4 - \frac{x^5}{5}\right]_0^4$
$= \frac{3}{32}\left(256 - \frac{1024}{5}\right) = \frac{3}{32} \times \frac{256}{5} = \frac{24}{5}$ **A1**

$\text{Var}(X) = \frac{24}{5} - 4 = \frac{4}{5}$ **M1 A1**

(iii) $E[2X + 3] = 2E[X] + 3 = 2 \times 2 + 3 = 7$ **M1 A1**

[Total: 7]
</details>

---

**Example 3 — 9231/w23/qp/41 Q4 (7 marks):**

> $X$ has PDF $f(x) = \frac{3}{8}(x - 1)^2$, $1 \le x \le 3$, zero otherwise.
> Find $E(X)$ and $\text{Var}(X)$. Hence find $E(4X - 1)$.

<details>
<summary>📝 MS 展开查看</summary>

$E[X] = \int_1^3 x \cdot \frac{3}{8}(x-1)^2\,dx$ **M1**
$= \frac{3}{8} \int_1^3 x(x^2 - 2x + 1)\,dx$
$= \frac{3}{8} \int_1^3 (x^3 - 2x^2 + x)\,dx$
$= \frac{3}{8}\left[\frac{x^4}{4} - \frac{2x^3}{3} + \frac{x^2}{2}\right]_1^3$
$= \frac{3}{8}\left[\left(\frac{81}{4} - 18 + \frac{9}{2}\right) - \left(\frac{1}{4} - \frac{2}{3} + \frac{1}{2}\right)\right]$
$= \frac{3}{8}\left(20 - \frac{52}{3} + 4\right) = \frac{3}{8} \times \frac{20}{3} = \frac{5}{2}$ **A1**

$E[X^2] = \int_1^3 x^2 \cdot \frac{3}{8}(x-1)^2\,dx$ **M1**
$= \frac{3}{8} \int_1^3 x^2(x^2 - 2x + 1)\,dx$
$= \frac{3}{8} \int_1^3 (x^4 - 2x^3 + x^2)\,dx$
$= \frac{3}{8}\left[\frac{x^5}{5} - \frac{x^4}{2} + \frac{x^3}{3}\right]_1^3$
$= \frac{3}{8}\left(\frac{242}{5} - 40 + \frac{26}{3}\right)$
$= \frac{3}{8}\left(\frac{726}{15} + \frac{130}{15} - \frac{600}{15}\right)$
$= \frac{3}{8} \times \frac{256}{15} = \frac{32}{5}$ **A1**

$\text{Var}(X) = \frac{32}{5} - \left(\frac{5}{2}\right)^2 = \frac{32}{5} - \frac{25}{4} = \frac{128 - 125}{20} = \frac{3}{20}$ **M1 A1**

$E[4X - 1] = 4E[X] - 1 = 4 \times \frac{5}{2} - 1 = 10 - 1 = 9$ **M1 A1**

[Total: 7]
</details>

---

### :::warning[常见陷阱]

- $E[X^2]$ 积分时仍用 $x f(x)$ 而非 $x^2 f(x)$
- $\text{Var}(X) = E[X^2] - (E[X])^2$ 记成 $E[X^2] - E[X]$
- 分段 PDF 中 $E[X^2]$ 每段积分都需乘以 $x^2$

:::

---

## Question Type 4: Finding Median and Quartiles

求中位数和四分位数。

### 如何识别

要求 median（中位数）、lower/upper quartile（下/上四分位数）、IQR（四分位距）或 percentiles（百分位数）。

### :::note[标准解题方法]

1. 先由 PDF 求出 CDF $F(x)$（若未直接给出）
2. 确定分位数所在的区间：计算 $F$ 在各段端点的值
3. 对中位数解 $F(m) = 0.5$
4. 对 $Q_1$ 解 $F(Q_1) = 0.25$，对 $Q_3$ 解 $F(Q_3) = 0.75$
5. 对 $\alpha$ 百分位解 $F(p_\alpha) = \alpha/100$
6. 确认解落在所假设的分段区间内

:::

### :::info[评分标准（MS 模式）]

- **M1** 写出 $F(m) = 0.5$（或其他对应值）
- **M1** 正确代入 CDF（使用正确的分段）
- **A1** 数值正确（3 s.f. 或 exact form）
- **B1** IQR 计算：$\text{IQR} = Q_3 - Q_1$

:::

### 典型例题

**Example 1 — 9231/s20/qp/41 Q3 (3 marks):**

> $X$ has PDF $f(x) = \frac{3}{4}(2x - x^2)$, $0 \le x \le 2$, zero otherwise. Find the median of $X$.

<details>
<summary>📝 MS 展开查看</summary>

$F(x) = \frac{3x^2}{4} - \frac{x^3}{4} = \frac{x^2(3 - x)}{4}$, $0 \le x \le 2$

$F(1) = \frac{1(2)}{4} = 0.5$ **M1**

Check: $m = 1$ gives $F(1) = \frac{1^2(3 - 1)}{4} = \frac{2}{4} = 0.5$ **M1**

Median $m = 1$ **A1**

[Total: 3]
</details>

---

**Example 2 — 9231/w23/qp/41 Q4 (4 marks):**

> $X$ has PDF $f(x) = \frac{3}{8}(x-1)^2$, $1 \le x \le 3$, zero otherwise.
> Find the lower quartile $Q_1$ and the upper quartile $Q_3$.

<details>
<summary>📝 MS 展开查看</summary>

$F(x) = \frac{(x-1)^3}{8}$, $1 \le x \le 3$

For $Q_1$: $F(Q_1) = 0.25$ **M1**
$\frac{(Q_1 - 1)^3}{8} = \frac{1}{4}$
$(Q_1 - 1)^3 = 2$
$Q_1 - 1 = \sqrt[3]{2}$
$Q_1 = 1 + \sqrt[3]{2} = 2.26$ (3 s.f.) **A1**

For $Q_3$: $F(Q_3) = 0.75$ **M1**
$\frac{(Q_3 - 1)^3}{8} = \frac{3}{4}$
$(Q_3 - 1)^3 = 6$
$Q_3 - 1 = \sqrt[3]{6}$
$Q_3 = 1 + \sqrt[3]{6} = 2.82$ (3 s.f.) **A1**

$\text{IQR} = Q_3 - Q_1 = \sqrt[3]{6} - \sqrt[3]{2} = 0.560$ (3 s.f.)

[Total: 4]
</details>

---

**Example 3 — 9231/s25/qp/41 Q2 (4 marks):**

> $X$ has PDF $f(x) = \frac{3}{32}x(4 - x)$, $0 \le x \le 4$, zero otherwise.
> (i) Find $E(X)$.
> (ii) Find the median of $X$.

<details>
<summary>📝 MS 展开查看</summary>

(i) $E[X] = \int_0^4 x \cdot \frac{3}{32}x(4 - x)\,dx = \frac{3}{32} \int_0^4 (4x^2 - x^3)\,dx$ **M1**
$= \frac{3}{32}\left[\frac{4x^3}{3} - \frac{x^4}{4}\right]_0^4 = \frac{3}{32} \times \frac{64}{3} = 2$ **A1**

(ii) $F(x) = \int_0^x \frac{3}{32}t(4 - t)\,dt = \frac{3}{32}\left[2t^2 - \frac{t^3}{3}\right]_0^x = \frac{3}{32}\left(2x^2 - \frac{x^3}{3}\right)$ **M1**

$F(m) = 0.5 \Rightarrow \frac{3}{32}\left(2m^2 - \frac{m^3}{3}\right) = \frac{1}{2}$
$2m^2 - \frac{m^3}{3} = \frac{16}{3}$
$6m^2 - m^3 = 16$
$m^3 - 6m^2 + 16 = 0$

By inspection: $m = 2$: $8 - 24 + 16 = 0$ ✓
$(m - 2)(m^2 - 4m - 8) = 0$
$m = 2$ or $m = 2 \pm 2\sqrt{3}$ (reject as outside $[0,4]$)
Median $m = 2$ **A1**

[Total: 6]
</details>

---

### :::warning[常见陷阱]

- 求解中位数前未确认所在的区间——$F(\text{left}) &lt; 0.5 &lt; F(\text{right})$ 才在该区间求解
- 求解后未验证解是否落在假设的分段内
- CDF 含平方/立方时忘记开方（如 $m^3$ 解得 $m$ 需取立方根）
- 多个可能解时未根据定义域取舍

:::

---

## Question Type 5: Transformation $Y = g(X)$ — CDF Method

变换 $Y = g(X)$ 的分布（CDF 法）。

### 如何识别

已知 $X$ 的 PDF 或 CDF，求 $Y = g(X)$ 的 PDF 或 CDF，或求 $Y$ 的期望/方差。

### :::note[标准解题方法]

1. 写出 $F_Y(y) = P(Y \le y) = P(g(X) \le y)$
2. 根据 $g$ 的单调性转换不等式：
   - $g$ 单调递增：$g(X) \le y \Rightarrow X \le g^{-1}(y)$
   - $g$ 单调递减：$g(X) \le y \Rightarrow X \ge g^{-1}(y)$
   - $g$ 非单调（如 $X^2$）：需分段处理
3. 用 $F_X$ 或积分表示概率
4. 对 $y$ 求导得 $f_Y(y) = F_Y'(y)$
5. 注明 $Y$ 的取值范围

:::

### :::info[评分标准（MS 模式）]

- **M1** $F_Y(y) = P(g(X) \le y)$
- **M1** 正确转换不等式得 $X$ 的范围
- **M1** 用 $F_X$ 或积分表示概率
- **A1** $F_Y(y)$ 形式正确
- **M1** 对 $y$ 求导（链式法则）
- **A1** $f_Y(y)$ 正确（含定义域）

:::

### 典型例题

**Example 1 — 9231/w21/qp/41 Q2 (7 marks):**

> $X$ has PDF $f(x) = \frac{3}{4}(1 - x^2)$, $-1 \le x \le 1$, zero otherwise.
> Find the PDF of $Y = X^2$.

<details>
<summary>📝 MS 展开查看</summary>

$Y = X^2$, so $y \ge 0$. **B1**

For $0 \le y &lt; 1$:
$F_Y(y) = P(Y \le y) = P(X^2 \le y) = P(-\sqrt{y} \le X \le \sqrt{y})$ **M1**
$= \int_{-\sqrt{y}}^{\sqrt{y}} \frac{3}{4}(1 - x^2)\,dx$ **M1**
$= \frac{3}{4}\left[x - \frac{x^3}{3}\right]_{-\sqrt{y}}^{\sqrt{y}}$
$= \frac{3}{4}\left[\left(\sqrt{y} - \frac{y^{3/2}}{3}\right) - \left(-\sqrt{y} + \frac{y^{3/2}}{3}\right)\right]$
$= \frac{3}{4}\left(2\sqrt{y} - \frac{2y^{3/2}}{3}\right)$
$= \frac{3}{2}\sqrt{y} - \frac{1}{2}y^{3/2}$
$= \frac{\sqrt{y}}{2}(3 - y)$ **A1**

$f_Y(y) = F_Y'(y)$ **M1**
$= \frac{3}{4\sqrt{y}} - \frac{3}{4}\sqrt{y}$
$= \frac{3}{4}\left(\frac{1}{\sqrt{y}} - \sqrt{y}\right)$, $0 \le y &lt; 1$ **A1**

For $y \ge 1$: $F_Y(y) = 1$, $f_Y(y) = 0$
For $y &lt; 0$: $F_Y(y) = 0$, $f_Y(y) = 0$

[Total: 7]
</details>

---

**Example 2 — 9231/s23/qp/41 Q6 (8 marks):**

> $X$ has PDF $f(x) = \frac{1}{2}\sin x$, $0 \le x \le \pi$, zero otherwise.
> Find the PDF of $Y = \cos X$.

<details>
<summary>📝 MS 展开查看</summary>

$Y = \cos X$, $x \in [0, \pi] \Rightarrow \cos$ is decreasing from $1$ to $-1$, so $y \in [-1, 1]$.
$x = \cos^{-1} y$, and $\frac{dx}{dy} = -\frac{1}{\sqrt{1 - y^2}}$ **B1**

For $y \in [-1, 1]$:
Since $\cos$ is decreasing on $[0, \pi]$:
$F_Y(y) = P(Y \le y) = P(\cos X \le y) = P(X \ge \cos^{-1} y)$ **M1**
$= \int_{\cos^{-1} y}^{\pi} \frac{1}{2}\sin t\,dt$ **M1**
$= \frac{1}{2}[-\cos t]_{\cos^{-1} y}^{\pi}$
$= \frac{1}{2}[(-\cos\pi) - (-\cos(\cos^{-1} y))]$
$= \frac{1}{2}[1 + y]$ **A1**

$f_Y(y) = F_Y'(y) = \frac{1}{2}$, $y \in [-1, 1]$ **M1 A1**

Alternatively by CDF formula for monotonic decreasing:
$f_Y(y) = f_X(g^{-1}(y)) \left|\frac{dx}{dy}\right| = \frac{1}{2}\sin(\cos^{-1} y) \cdot \frac{1}{\sqrt{1 - y^2}}$
$= \frac{1}{2} \cdot \sqrt{1 - y^2} \cdot \frac{1}{\sqrt{1 - y^2}} = \frac{1}{2}$ **M1 A1**

[Total: 8]
</details>

---

**Example 3 — 9231/w24/qp/41 Q4 (7 marks):**

> $X$ has PDF $f(x) = e^{-x}$, $x \ge 0$, zero otherwise.
> Find the PDF of $Y = \sqrt{X}$.

<details>
<summary>📝 MS 展开查看</summary>

$Y = \sqrt{X}$, $y \ge 0$. $g$ is strictly increasing. **B1**

$x = y^2$, $\frac{dx}{dy} = 2y$

$F_Y(y) = P(Y \le y) = P(\sqrt{X} \le y) = P(X \le y^2)$ **M1**
$= F_X(y^2)$ **M1**
$= \int_0^{y^2} e^{-t}\,dt$
$= [-e^{-t}]_0^{y^2} = 1 - e^{-y^2}$ **A1**

$f_Y(y) = F_Y'(y) = 2y e^{-y^2}$, $y \ge 0$ **M1 A1**

Or directly: $f_Y(y) = f_X(y^2) \cdot 2y = e^{-y^2} \cdot 2y$, $y \ge 0$ **M1 A1**

[Total: 7]
</details>

---

### :::warning[常见陷阱]

- 忽略 $g$ 的单调性——单调和非单调变换处理方式不同
- 忘记写 $Y$ 的取值范围（$Y = X^2$ 时 $y \ge 0$，$Y = \cos X$ 时 $y$ 有界等）
- 非单调变换（如 $Y = X^2$）未正确处理正负分支
- 求导时链式法则遗漏——$f_Y(y) = f_X(g^{-1}(y)) \cdot \left|\frac{d}{dy} g^{-1}(y)\right|$

:::

---

## Question Type 6: Piecewise PDF Problems

分段 PDF 综合题。

### 如何识别

PDF 在两个或多个区间上有不同表达式，通常综合考察求常数、CDF、期望、方差、中位数等多个知识点。

### :::note[标准解题方法]

1. 分别处理每段 PDF
2. 求常数：各段积分之和等于 1
3. 求 CDF：逐段从下限积分至 $x$，保持 $F$ 在边界连续
4. 求期望/方差：$E[X] = \int x f(x)\,dx$，每段分别积分后求和
5. 求中位数/分位数：先确定所在区间（用 $F$ 在各端点的值判断）
6. 变换 $Y = g(X)$：注意 $g$ 在 $X$ 各段上的单调性

:::

### :::info[评分标准（MS 模式）]

- **B1** 识别并正确写出各段 PDF
- **M1** 每段正确积分
- **A1** 每段结果正确
- **M1** 各段结果汇总
- **A1/F1** 最终答案（可 follow-through 前问错误）

:::

### 典型例题

**Example 1 — 9231/w20/qp/41 Q6 (10 marks):**

> $X$ has PDF $f(x) = \begin{cases} a(1 - x), & 0 \le x \le 1, \\ a(x - 1), & 1 &lt; x \le 2, \\ 0, & \text{otherwise.} \end{cases}$
> (i) Find $a$.
> (ii) Find $F(x)$.
> (iii) Find $E(X)$ and $\text{Var}(X)$.

<details>
<summary>📝 MS 展开查看</summary>

(i) $\int_0^1 a(1 - x)\,dx + \int_1^2 a(x - 1)\,dx = 1$ **B1**
$a\left[x - \frac{x^2}{2}\right]_0^1 + a\left[\frac{x^2}{2} - x\right]_1^2 = 1$
$a(1 - 0.5) + a[(2 - 2) - (0.5 - 1)] = \frac{a}{2} + \frac{a}{2} = a = 1$ **A1**

(ii) For $x &lt; 0$: $F(x) = 0$ **B1**
For $0 \le x \le 1$:
$F(x) = \int_0^x (1 - t)\,dt = \left[t - \frac{t^2}{2}\right]_0^x = x - \frac{x^2}{2}$ **M1 A1**
For $1 &lt; x \le 2$:
$F(x) = \int_0^1 (1 - t)\,dt + \int_1^x (t - 1)\,dt = \frac{1}{2} + \left[\frac{t^2}{2} - t\right]_1^x$ **M1**
$= \frac{1}{2} + \left[\left(\frac{x^2}{2} - x\right) - \left(\frac{1}{2} - 1\right)\right]$
$= \frac{1}{2} + \frac{x^2}{2} - x + \frac{1}{2}$
$= 1 + \frac{x^2}{2} - x = \frac{x^2 - 2x + 2}{2}$ **A1**
For $x &gt; 2$: $F(x) = 1$ **B1**

(iii) $E[X] = \int_0^1 x(1 - x)\,dx + \int_1^2 x(x - 1)\,dx$ **M1**
$= \int_0^1 (x - x^2)\,dx + \int_1^2 (x^2 - x)\,dx$
$= \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 + \left[\frac{x^3}{3} - \frac{x^2}{2}\right]_1^2$
$= \left(\frac{1}{2} - \frac{1}{3}\right) + \left[\left(\frac{8}{3} - 2\right) - \left(\frac{1}{3} - \frac{1}{2}\right)\right]$
$= \frac{1}{6} + \left(\frac{2}{3} + \frac{1}{6}\right) = 1$ **A1**

$E[X^2] = \int_0^1 x^2(1 - x)\,dx + \int_1^2 x^2(x - 1)\,dx$ **M1**
$= \int_0^1 (x^2 - x^3)\,dx + \int_1^2 (x^3 - x^2)\,dx$
$= \left[\frac{x^3}{3} - \frac{x^4}{4}\right]_0^1 + \left[\frac{x^4}{4} - \frac{x^3}{3}\right]_1^2$
$= \left(\frac{1}{3} - \frac{1}{4}\right) + \left[\left(4 - \frac{8}{3}\right) - \left(\frac{1}{4} - \frac{1}{3}\right)\right]$
$= \frac{1}{12} + \left(\frac{4}{3} + \frac{1}{12}\right) = \frac{1}{12} + \frac{17}{12} = \frac{3}{2}$ **A1**

$\text{Var}(X) = \frac{3}{2} - 1^2 = \frac{1}{2}$ **M1 A1**

[Total: 10]
</details>

---

**Example 2 — 9231/w22/qp/41 Q5 (11 marks):**

> $X$ has PDF
> $$f(x) = \begin{cases} \frac{1}{3}, & 0 \le x &lt; 1, \\ \frac{2}{3}(2 - x), & 1 \le x \le 2, \\ 0, & \text{otherwise.} \end{cases}$$
> (i) Verify this is a valid PDF.
> (ii) Find $F(x)$.
> (iii) Find the median of $X$.
> (iv) Find $P(X &gt; 1.5)$.

<details>
<summary>📝 MS 展开查看</summary>

(i) $f(x) \ge 0$ for all $x$. **B1**
$\int_0^1 \frac{1}{3}\,dx + \int_1^2 \frac{2}{3}(2 - x)\,dx = \frac{1}{3} + \frac{2}{3}\left[2x - \frac{x^2}{2}\right]_1^2$ **M1**
$= \frac{1}{3} + \frac{2}{3}\left[(4 - 2) - \left(2 - \frac{1}{2}\right)\right]$
$= \frac{1}{3} + \frac{2}{3}\left(2 - \frac{3}{2}\right) = \frac{1}{3} + \frac{2}{3} \times \frac{1}{2} = \frac{1}{3} + \frac{1}{3} = 1$ **A1**

(ii) For $x &lt; 0$: $F(x) = 0$ **B1**
For $0 \le x &lt; 1$:
$F(x) = \int_0^x \frac{1}{3}\,dt = \frac{x}{3}$ **A1**
For $1 \le x \le 2$:
$F(x) = \int_0^1 \frac{1}{3}\,dt + \int_1^x \frac{2}{3}(2 - t)\,dt$ **M1**
$= \frac{1}{3} + \frac{2}{3}\left[2t - \frac{t^2}{2}\right]_1^x$
$= \frac{1}{3} + \frac{2}{3}\left[\left(2x - \frac{x^2}{2}\right) - \left(2 - \frac{1}{2}\right)\right]$
$= \frac{1}{3} + \frac{2}{3}\left(2x - \frac{x^2}{2} - \frac{3}{2}\right)$
$= \frac{1}{3} + \frac{4x}{3} - \frac{x^2}{3} - 1$
$= \frac{4x}{3} - \frac{x^2}{3} - \frac{2}{3}$
$= \frac{4x - x^2 - 2}{3}$ **A1**
For $x &gt; 2$: $F(x) = 1$ **A1**

(iii) $F(1) = \frac{1}{3} &lt; 0.5$ and $F(2) = 1$, so median in $[1, 2]$. **M1**
$\frac{4m - m^2 - 2}{3} = \frac{1}{2}$
$4m - m^2 - 2 = \frac{3}{2}$
$8m - 2m^2 - 4 = 3$
$2m^2 - 8m + 7 = 0$
$m = \frac{8 \pm \sqrt{64 - 56}}{4} = \frac{8 \pm \sqrt{8}}{4} = 2 \pm \frac{\sqrt{2}}{2}$
$m = 2 - \frac{\sqrt{2}}{2}$ (since $m \le 2$) **A1**
$m = 1.29$ (3 s.f.)

(iv) $P(X &gt; 1.5) = 1 - F(1.5) = 1 - \frac{4(1.5) - (1.5)^2 - 2}{3}$ **M1**
$= 1 - \frac{6 - 2.25 - 2}{3} = 1 - \frac{1.75}{3} = \frac{1.25}{3} = \frac{5}{12}$ **A1**

[Total: 11]
</details>

---

**Example 3 — 9231/s24/qp/41 Q7 (12 marks):**

> $X$ has PDF
> $$f(x) = \begin{cases} kx, & 0 \le x \le 2, \\ k(4 - x), & 2 &lt; x \le 4, \\ 0, & \text{otherwise.} \end{cases}$$
> (i) Find $k$.
> (ii) Find $F(x)$.
> (iii) Find $E(X)$.
> (iv) Find the interquartile range.

<details>
<summary>📝 MS 展开查看</summary>

(i) $\int_0^2 kx\,dx + \int_2^4 k(4 - x)\,dx = 1$ **B1**
$k\left[\frac{x^2}{2}\right]_0^2 + k\left[4x - \frac{x^2}{2}\right]_2^4 = 1$
$k(2) + k\left[(16 - 8) - (8 - 2)\right] = 2k + 2k = 4k = 1$ **M1**
$k = \frac{1}{4}$ **A1**

(ii) For $x &lt; 0$: $F(x) = 0$ **B1**
For $0 \le x \le 2$:
$F(x) = \int_0^x \frac{1}{4}t\,dt = \frac{x^2}{8}$ **A1**
For $2 &lt; x \le 4$:
$F(x) = \int_0^2 \frac{1}{4}t\,dt + \int_2^x \frac{1}{4}(4 - t)\,dt$ **M1**
$= \frac{1}{2} + \frac{1}{4}\left[4t - \frac{t^2}{2}\right]_2^x$
$= \frac{1}{2} + \frac{1}{4}\left[\left(4x - \frac{x^2}{2}\right) - \left(8 - 2\right)\right]$
$= \frac{1}{2} + \frac{1}{4}\left(4x - \frac{x^2}{2} - 6\right)$
$= \frac{1}{2} + x - \frac{x^2}{8} - \frac{3}{2}$
$= x - \frac{x^2}{8} - 1$ **A1**
For $x &gt; 4$: $F(x) = 1$ **B1**

(iii) $E[X] = \int_0^2 x \cdot \frac{1}{4}x\,dx + \int_2^4 x \cdot \frac{1}{4}(4 - x)\,dx$ **M1**
$= \frac{1}{4}\int_0^2 x^2\,dx + \frac{1}{4}\int_2^4 (4x - x^2)\,dx$
$= \frac{1}{4}\left[\frac{x^3}{3}\right]_0^2 + \frac{1}{4}\left[2x^2 - \frac{x^3}{3}\right]_2^4$
$= \frac{1}{4}\left(\frac{8}{3}\right) + \frac{1}{4}\left[\left(32 - \frac{64}{3}\right) - \left(8 - \frac{8}{3}\right)\right]$
$= \frac{2}{3} + \frac{1}{4}\left(\frac{32}{3} - \frac{16}{3}\right) = \frac{2}{3} + \frac{1}{4} \times \frac{16}{3} = \frac{2}{3} + \frac{4}{3} = 2$ **A1**

(iv) $F(2) = \frac{4}{8} = 0.5$

For $Q_1$: Since $F(2) = 0.5 &gt; 0.25$, $Q_1$ is in $[0, 2]$.
$\frac{Q_1^2}{8} = \frac{1}{4} \Rightarrow Q_1^2 = 2 \Rightarrow Q_1 = \sqrt{2}$ **M1 A1**

For $Q_3$: Since $F(2) = 0.5 &lt; 0.75$, $Q_3$ is in $[2, 4]$.
$Q_3 - \frac{Q_3^2}{8} - 1 = \frac{3}{4}$ **M1**
Multiply by 8: $8Q_3 - Q_3^2 - 8 = 6$
$Q_3^2 - 8Q_3 + 14 = 0$
$Q_3 = \frac{8 \pm \sqrt{64 - 56}}{2} = \frac{8 \pm \sqrt{8}}{2} = 4 \pm \sqrt{2}$
$Q_3 = 4 - \sqrt{2}$ (since $Q_3 \le 4$) **A1**

$\text{IQR} = (4 - \sqrt{2}) - \sqrt{2} = 4 - 2\sqrt{2} = 1.17$ (3 s.f.) **B1**

[Total: 12]
</details>

---

### :::warning[常见陷阱]

- 求 CDF 时分段边界处未保持连续性
- 求 $E[X]$ 或 $E[X^2]$ 时各段使用相同的函数形式（忘记每段 PDF 不同）
- 求中位数时未先判断所在区间，直接使用错误段表达式
- 分段 PDF 变换 $Y = g(X)$ 时，忽略 $g$ 在各段上的不同单调性

:::
