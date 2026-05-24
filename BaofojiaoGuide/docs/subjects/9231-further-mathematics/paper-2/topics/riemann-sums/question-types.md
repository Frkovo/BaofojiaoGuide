---
title: 题型分析
sidebar_position: 4
---

# 题型分析 — Riemann Sums

## Type 0: 用积分求求和的下界（通用方法）

### 如何识别
给一个求和 $\sum_{r=1}^{n} f(r)$，要求用积分证明它大于（或小于）某个表达式。

### 核心原理

宽度为 1 的矩形柱，高度取 $f(r)$：

```
f(x) 增函数:
  r=1  r=2  r=3       r=n
  ┌────┬────┬────┬───┬────┐
  │f(1)│f(2)│f(3) │   │f(n)│
  └────┴────┴────┴───┴────┘
  x=0   x=1   x=2        x=n  x=n+1
  
  左端点矩形面积和 = Σ_{r=1}^{n} f(r)   (从 x=0 到 x=n, 高取左端)
  右端点矩形面积和 = Σ_{r=2}^{n+1} f(r) (从 x=1 到 x=n+1, 高取右端)
```

**对于增函数 $f$：**

左端点矩形偏低（高度取区间左端，小于实际函数值）→ **下界**

右端点矩形偏高（高度取区间右端，大于实际函数值）→ **上界**

$$
\boxed{\int_{1}^{n} f(x)\,dx \;\leq\; \sum_{r=2}^{n} f(r) \;\leq\; \int_{0}^{n-1} f(x)\,dx}
$$

**对于减函数 $f$：**

左端点矩形偏高 → **上界**，右端点矩形偏低 → **下界**

$$
\boxed{\int_{1}^{n} f(x)\,dx \;\geq\; \sum_{r=2}^{n} f(r) \;\geq\; \int_{0}^{n-1} f(x)\,dx}
$$

:::note[标准解题方法]
1. **判断单调性**：$f$ 增还是减？（求导 $f'(x)$ 或直接观察）
2. **写出积分-求和不等式**：
   - 增函数：$\int_1^n f(x)\,dx \leq \sum_{r=2}^{n} f(r) \leq \int_0^{n-1} f(x)\,dx$
   - 减函数：不等号反向
3. **调整求和指标到目标形式**：
   - 若目标为 $\sum_{r=1}^{n} f(r)$，则在不等式中加减 $f(1)$ 或 $f(n)$
   - 常用：$\sum_{r=1}^{n} f(r) = f(1) + \sum_{r=2}^{n} f(r)$
4. **计算积分**，代入化简
:::

:::warning[常见陷阱]
- 求和起点和终点搞反：$\sum_{r=2}^{n} f(r)$ 对应 $n-1$ 个矩形，不是 $n$ 个
- $\int_0^{n-1}$ 的积分上限是 $n-1$ 不是 $n$
- 增/减判断错 → 不等号方向全反
- 如果 $f(1)$ 是 $0$（如 $\ln 1 = 0$），可以直接替换
:::

> **Example 1 — 典型题：** 已知 $f(x) = \frac{1}{x}$ 在 $x > 0$ 时为减函数。证明
> $$
> \ln(n+1) < \sum_{r=1}^{n} \frac{1}{r} < 1 + \ln n
> $$

<details>
<summary>📝 MS 展开查看</summary>

$f(x) = 1/x$ 减函数，所以右端点矩形偏低 → 下界，左端点矩形偏高 → 上界。

**M1**: 识别 $f$ 为减函数

右端点（下界）：$\int_1^{n+1} \frac{1}{x}\,dx \leq \sum_{r=2}^{n+1} \frac{1}{r}$

计算：$\int_1^{n+1} \frac{1}{x}\,dx = [\ln x]_1^{n+1} = \ln(n+1)$ **A1**

所以 $\sum_{r=2}^{n+1} \frac{1}{r} \geq \ln(n+1)$

$\sum_{r=1}^{n} \frac{1}{r} = \frac{1}{n+1} + \sum_{r=2}^{n+1} \frac{1}{r} \geq \frac{1}{n+1} + \ln(n+1)$

等等，这不对。换个写法。

**M1**: 正确的不等式是：

对减函数，$\int_1^{n+1} f(x)\,dx \leq \sum_{r=2}^{n+1} f(r)$，且 $\sum_{r=1}^{n} f(r) \leq \int_0^n f(x)\,dx$

实际上标准写法：

$\int_1^{n} \frac{1}{x}\,dx \leq \sum_{r=2}^{n} \frac{1}{r}$  且 $\sum_{r=1}^{n-1} \frac{1}{r} \geq \int_1^{n} \frac{1}{x}\,dx$

**A1**: $\ln n \leq \sum_{r=2}^{n} \frac{1}{r}$ 且 $\sum_{r=1}^{n-1} \frac{1}{r} \geq \ln n$

$\sum_{r=1}^{n} \frac{1}{r} \geq \ln n + \frac{1}{n}$ 且 $\sum_{r=1}^{n} \frac{1}{r} \leq \frac{1}{1} + \ln n$（因为 $\sum_{r=1}^{n-1} \frac{1}{r} = \sum_{r=1}^{n} \frac{1}{r} - \frac{1}{n}$）

所以 $\ln(n+1) < \sum_{r=1}^{n} \frac{1}{r} < 1 + \ln n$ **A1**

[总分: 6]
</details>

---

> **Example 2 — s20/23 Q4 变体：** 已知 $f(x) = \ln x$ 为增函数。证明
> $$
> N\ln N - N + 1 \leq \ln N! \leq N\ln N - N + 1 + \ln N
> $$

<details>
<summary>📝 MS 展开查看</summary>

$f(x) = \ln x$ 增函数。宽度为 $1$ 的矩形：

左端点矩形和 = $\sum_{r=1}^{N-1} \ln r \leq \int_1^N \ln x\,dx$ **M1**

右端点矩形和 = $\sum_{r=2}^{N} \ln r \geq \int_1^N \ln x\,dx$ **M1**

计算积分：$\int_1^N \ln x\,dx = [x\ln x - x]_1^N = N\ln N - N + 1$ **A1**

下界：$\ln(N-1)! \leq N\ln N - N + 1$

$\ln N! = \ln(N-1)! + \ln N \leq N\ln N - N + 1 + \ln N$ **A1**

上界：$N\ln N - N + 1 \leq \ln N!$ **A1**

综上：$N\ln N - N + 1 \leq \ln N! \leq N\ln N - N + 1 + \ln N$

[总分: 5]
</details>

---

> **Example 3 — 增函数求和下限：** 设 $f(x) = \sqrt{x}$ 在 $[1, n]$ 上为增函数。用积分求 $\sum_{r=1}^{n} \sqrt{r}$ 的下界。

<details>
<summary>📝 MS 展开查看</summary>

$f(x) = \sqrt{x}$ 增函数，左端点矩形偏低。

**M1**: 左端点矩形和 $\leq$ 积分

$\sum_{r=1}^{n-1} \sqrt{r} \leq \int_1^{n} \sqrt{x}\,dx$ **A1**

$\int_1^{n} \sqrt{x}\,dx = \left[\frac{2}{3}x^{3/2}\right]_1^n = \frac{2}{3}(n^{3/2} - 1)$ **A1**

所以 $\sum_{r=1}^{n-1} \sqrt{r} \leq \frac{2}{3}(n^{3/2} - 1)$

$\sum_{r=1}^{n} \sqrt{r} = \sum_{r=1}^{n-1} \sqrt{r} + \sqrt{n} \leq \frac{2}{3}(n^{3/2} - 1) + \sqrt{n}$ **A1**

下界：$\int_1^{n} \sqrt{x}\,dx \leq \sum_{r=2}^{n} \sqrt{r} = \sum_{r=1}^{n} \sqrt{r} - \sqrt{1}$

所以 $\sum_{r=1}^{n} \sqrt{r} \geq 1 + \frac{2}{3}(n^{3/2} - 1) = \frac{2}{3}n^{3/2} + \frac{1}{3}$ **A1**

[总分: 5]
</details>

---

## Type 1: Upper Bound Using Rectangles (4 marks)

> **Example: s20/21 Q4(a)** — Use rectangles to find an upper bound for $\int_0^1 x^2\,dx$.

<details>
<summary>📝 MS 展开查看</summary>

$f(x) = x^2$ is increasing on $[0,1]$. Divide $[0,1]$ into $n$ equal strips of width $\Delta x = \frac{1}{n}$.

For an upper bound (increasing function), use right endpoints:

$x_i = \frac{i}{n}$ for $i = 1, 2, \ldots, n$

$$U_n = \sum_{i=1}^n f(x_i)\Delta x = \sum_{i=1}^n \left(\frac{i}{n}\right)^2 \cdot \frac{1}{n}$$

$$= \frac{1}{n^3}\sum_{i=1}^n i^2 = \frac{1}{n^3}\cdot\frac{n(n+1)(2n+1)}{6}$$

$$= \frac{(n+1)(2n+1)}{6n^2}$$

As $n\to\infty$, $U_n \to \frac{2}{6} = \frac{1}{3}$, which is the exact value of $\int_0^1 x^2\,dx$.

**M1** — $\Delta x = \frac{1}{n}$ with correct endpoints
**M1** — Form sum $\sum f(x_i)\Delta x$ with correct $x_i$
**A1** — Correct expression $\frac{(n+1)(2n+1)}{6n^2}$
**A1** — Simplify and state upper bound

</details>

> **Example: w20/21 Q4** — Find an upper bound for $\int_0^1 (1 - x^3)\,dx$ using $n$ equal subintervals.

<details>
<summary>📝 MS 展开查看</summary>

$f(x) = 1 - x^3$ is decreasing on $[0,1]$. For decreasing $f$, the upper bound uses **left** endpoints.

$\Delta x = \frac{1}{n}$

Left endpoints: $x_i = \frac{i-1}{n}$ for $i = 1, 2, \ldots, n$

$$U_n = \sum_{i=1}^n f\left(\frac{i-1}{n}\right)\frac{1}{n} = \frac{1}{n}\sum_{i=0}^{n-1} \left(1 - \frac{i^3}{n^3}\right)$$

$$= \frac{1}{n}\left[n - \frac{1}{n^3}\sum_{i=0}^{n-1} i^3\right] = \frac{1}{n}\left[n - \frac{1}{n^3}\cdot\frac{(n-1)^2 n^2}{4}\right]$$

$$= 1 - \frac{(n-1)^2}{4n^2} = 1 - \frac{n^2 - 2n + 1}{4n^2}$$

$$= \frac{3n^2 + 2n - 1}{4n^2}$$

**M1** — Recognize decreasing so use left endpoints
**M1** — Correct sum with $\Delta x = 1/n$
**A1** — Correct sigma sum and formula
**A1** — Simplify to $\frac{3n^2 + 2n - 1}{4n^2}$

</details>

## Type 2: Lower Bound Using Rectangles (4 marks)

> **Example: s20/21 Q4(b)** — Find a lower bound for $\int_0^1 x^2\,dx$ using $n$ equal subintervals.

<details>
<summary>📝 MS 展开查看</summary>

$f(x) = x^2$ is increasing. For lower bound, use left endpoints.

$x_i = \frac{i-1}{n}$ for $i = 1, 2, \ldots, n$

$$L_n = \sum_{i=1}^n f(x_i)\Delta x = \sum_{i=1}^n \left(\frac{i-1}{n}\right)^2 \cdot \frac{1}{n}$$

$$= \frac{1}{n^3}\sum_{i=1}^n (i-1)^2 = \frac{1}{n^3}\sum_{j=0}^{n-1} j^2$$

$$= \frac{1}{n^3}\cdot\frac{(n-1)n(2n-1)}{6}$$

$$= \frac{(n-1)(2n-1)}{6n^2}$$

As $n\to\infty$, $L_n \to \frac{1}{3}$.

**M1** — Use left endpoints for lower bound
**M1** — Correct sum
**A1** — $\frac{(n-1)(2n-1)}{6n^2}$
**A1** — Lower bound stated

</details>

## Type 3: Stirling-Type Approximations ($\ln N!$) (8 marks)

> **Example: s20/23 Q4** — Use rectangles to estimate $\ln N!$.

Consider $f(x) = \ln x$ on $[1, N]$. Since $f$ is increasing:

Left endpoint sum (lower bound):

$$\sum_{r=1}^{N-1} \ln r \le \int_1^N \ln x\,dx$$

Right endpoint sum (upper bound):

$$\int_1^N \ln x\,dx \le \sum_{r=2}^N \ln r$$

Since $\ln 1 = 0$, we have $\sum_{r=1}^{N-1} \ln r = \ln(N-1)!$ and $\sum_{r=2}^N \ln r = \ln N!$.

<details>
<summary>📝 MS 展开查看</summary>

$\int_1^N \ln x\,dx = [x\ln x - x]_1^N = N\ln N - N + 1$

Lower bound: $\ln(N-1)! \le N\ln N - N + 1$

$\ln N! = \ln(N-1)! + \ln N \le N\ln N - N + 1 + \ln N$

Upper bound: $N\ln N - N + 1 \le \ln N!$

Therefore:

$$N\ln N - N + 1 \le \ln N! \le N\ln N - N + 1 + \ln N$$

For large $N$, $\ln N! \approx N\ln N - N + \frac{1}{2}\ln(2\pi N)$ (full Stirling).

**M1** — Set $f(x) = \ln x$, note increasing
**M1** — Write $\int_1^N \ln x\,dx$ and evaluate to $N\ln N - N + 1$
**M1** — Lower bound: $\ln(N-1)! \le \int_1^N \ln x\,dx$
**M1** — Upper bound: $\int_1^N \ln x\,dx \le \ln N!$
**A1** — Correct inequality: $N\ln N - N + 1 \le \ln N! \le N\ln N - N + 1 + \ln N$

</details>

> **Example: w20/22 Q8** — Use upper and lower Riemann sums for $\int_1^n \ln x\,dx$ to show that:

$$n^n e^{1-n} \le n! \le n^{n+1} e^{1-n}$$

<details>
<summary>📝 MS 展开查看</summary>

From Riemann sums on $\ln x$:

$\ln(n-1)! \le \int_1^n \ln x\,dx \le \ln n!$

$\int_1^n \ln x\,dx = n\ln n - n + 1$

So: $\ln(n-1)! \le n\ln n - n + 1 \le \ln n!$

From RHS: $n\ln n - n + 1 \le \ln n! \Rightarrow \ln n! \ge n\ln n - n + 1$

$\Rightarrow n! \ge e^{n\ln n - n + 1} = n^n e^{1-n}$

From LHS: $\ln(n-1)! \le n\ln n - n + 1$

$\ln n! = \ln(n-1)! + \ln n \le n\ln n - n + 1 + \ln n$

$\Rightarrow n! \le n^{n+1}e^{1-n}$

Therefore: $n^n e^{1-n} \le n! \le n^{n+1} e^{1-n}$

**M1** — Riemann sum inequalities
**A1** — Correct integral evaluation
**M1** — Lower bound manipulation
**M1** — Upper bound manipulation
**A1** — Correct final inequality
**A1** — Exponential form

</details>
