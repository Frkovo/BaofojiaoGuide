# Maclaurin Series — Question Types

## Type 1: Standard Maclaurin from First Principles (5–7 marks)

Obtain the Maclaurin series for a given function by successive differentiation.

> **Example: s20/21 Q2** — Use the Maclaurin series to find the first three non-zero terms in the expansion of $2^x$.

<details>
<summary>📝 MS 展开查看</summary>

Let $f(x) = 2^x = e^{x\ln 2}$

$f'(x) = 2^x \ln 2$, $f''(x) = 2^x (\ln 2)^2$, $f'''(x) = 2^x (\ln 2)^3$

$f(0) = 1$, $f'(0) = \ln 2$, $f''(0) = (\ln 2)^2$, $f'''(0) = (\ln 2)^3$

$$2^x = 1 + (\ln 2)x + \frac{(\ln 2)^2}{2!}x^2 + \frac{(\ln 2)^3}{3!}x^3 + \cdots$$

**Marks scheme:**
- **M1** — Write $2^x = e^{x\ln 2}$ or attempt to differentiate
- **A1** — Correct derivatives (at least 2)
- **A1** — Correct first term $1$
- **A1** — Correct $(\ln 2)x$ term
- **A1** — Correct $\frac{(\ln 2)^2}{2}x^2$ term
- **A1** — Correct $\frac{(\ln 2)^3}{6}x^3$ term

</details>

> **Example: s23/23 Q1** — Find the Maclaurin series for $\sin^{-1} x$ up to the term in $x^3$.

<details>
<summary>📝 MS 展开查看</summary>

Let $f(x) = \sin^{-1} x$

$f'(x) = (1 - x^2)^{-1/2}$, $f''(x) = x(1 - x^2)^{-3/2}$, $f'''(x) = (1 - x^2)^{-3/2} + 3x^2(1 - x^2)^{-5/2}$

$f(0) = 0$, $f'(0) = 1$, $f''(0) = 0$, $f'''(0) = 1$

$$\sin^{-1} x = x + \frac{x^3}{6} + \cdots$$

**Marks scheme:**
- **M1** — Differentiate to find $f'(x) = (1-x^2)^{-1/2}$
- **A1** — Correct $f'(0) = 1$, $f''(0) = 0$
- **A1** — Correct $f'''(0) = 1$ and final series

</details>

## Type 2: Composite Functions / Log Diff (4–7 marks)

> **Example: w20/21 Q1** — Find the Maclaurin series for $e^{-x^2}$ up to the term in $x^4$.

<details>
<summary>📝 MS 展开查看</summary>

Substitute $u = -x^2$ into $e^u = 1 + u + \frac{u^2}{2!} + \frac{u^3}{3!} + \cdots$

$$e^{-x^2} = 1 + (-x^2) + \frac{(-x^2)^2}{2!} + \frac{(-x^2)^3}{3!} + \cdots$$

$$e^{-x^2} = 1 - x^2 + \frac{x^4}{2} - \frac{x^6}{6} + \cdots$$

**Marks scheme:**
- **M1** — Use substitution $u=-x^2$ in standard $e^u$ series
- **A1** — Correct $1 - x^2$ term
- **A1** — Correct $\frac{x^4}{2}$ term

</details>

> **Example: s21/23 Q2** — Find the Maclaurin series for $\ln(\cosh x)$ up to the term in $x^4$.

<details>
<summary>📝 MS 展开查看</summary>

Method 1: Direct differentiation.

$\cosh x = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \cdots$

$\ln(\cosh x) = \ln\left(1 + \frac{x^2}{2} + \frac{x^4}{24} + \cdots\right)$

Let $u = \frac{x^2}{2} + \frac{x^4}{24} + \cdots$, use $\ln(1+u)=u-\frac{u^2}{2}+\frac{u^3}{3}-\cdots$

$$\ln(\cosh x) = \left(\frac{x^2}{2} + \frac{x^4}{24}\right) - \frac{1}{2}\left(\frac{x^2}{2}\right)^2 + \cdots = \frac{x^2}{2} - \frac{x^4}{12} + \cdots$$

**Marks scheme:**
- **B1** — Correct $\cosh x$ expansion (at least 2 terms)
- **M1** — Use $\ln(1+u)$ expansion with correct substitution
- **A1** — Correct $\frac{x^2}{2}$ term
- **A1** — Correct $-\frac{x^4}{12}$ term

</details>

> **Example: s24/21 Q2** — Find the Maclaurin series for $e^{1+x^2} + e^{1-x}$ up to the term in $x^3$.

<details>
<summary>📝 MS 展开查看</summary>

$e^{1+x^2} = e \cdot e^{x^2} = e\left(1 + x^2 + \frac{x^4}{2!} + \cdots\right)$

$e^{1-x} = e \cdot e^{-x} = e\left(1 - x + \frac{x^2}{2!} - \frac{x^3}{3!} + \cdots\right)$

Sum: $e(2 - x + \frac{3}{2}x^2 - \frac{1}{6}x^3 + \cdots)$

**Marks scheme:**
- **M1** — Factor $e$ from both expressions
- **A1** — Correct expansion of $e^{1+x^2}$ up to $x^3$ terms
- **A1** — Correct expansion of $e^{1-x}$ up to $x^3$ terms
- **A1** — Correct sum: $2e - ex + \frac{3}{2}ex^2 - \frac{1}{6}ex^3$

</details>

## Type 3: Approximation of Integrals (2 marks)

> **Example: w22/21 Q1 (part)** — Use the Maclaurin series for $\ln(1+e^x)$ to approximate $\int_0^{0.1} \ln(1+e^x)\,dx$.

<details>
<summary>📝 MS 展开查看</summary>

First expand $\ln(1+e^x)$.

$e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots$

$1+e^x = 2 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots = 2\left(1 + \frac{x}{2} + \frac{x^2}{4} + \frac{x^3}{12} + \cdots\right)$

$\ln(1+e^x) = \ln 2 + \ln\left(1 + \frac{x}{2} + \frac{x^2}{4} + \frac{x^3}{12} + \cdots\right)$

Use $\ln(1+u)=u-\frac{u^2}{2}+\cdots$ with $u = \frac{x}{2} + \frac{x^2}{4} + \frac{x^3}{12}+\cdots$

$\ln(1+e^x) = \ln 2 + \frac{x}{2} + \frac{x^2}{8} + \cdots$

Integrate term by term:

$$\int_0^{0.1} \ln(1+e^x)\,dx \approx \int_0^{0.1} \left(\ln 2 + \frac{x}{2} + \frac{x^2}{8}\right)dx$$

$$= \left[\ln 2 \cdot x + \frac{x^2}{4} + \frac{x^3}{24}\right]_0^{0.1}$$

$$= 0.1\ln 2 + \frac{0.01}{4} + \frac{0.001}{24} \approx 0.0697$$

**Marks scheme (integral part):**
- **M1** — Integrate series term-by-term
- **A1** — Correct numerical answer

</details>
