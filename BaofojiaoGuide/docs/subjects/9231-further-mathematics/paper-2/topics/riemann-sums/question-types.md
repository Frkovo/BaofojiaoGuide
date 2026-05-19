# Riemann Sums — Question Types

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
