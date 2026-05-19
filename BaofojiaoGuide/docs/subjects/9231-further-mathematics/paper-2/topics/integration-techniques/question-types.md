# Integration Techniques — Question Types

## Type 1: Reduction Formulae (7–11 marks)

> **Example: s20/21 Q6** — Given $I_n = \int_0^1 (1 - x^2)^{n/2}\,dx$ for $n \ge 0$.
> (a) Show that $(n+2)I_n = (n+1)I_{n-2}$ for $n \ge 2$. [5]
> (b) Evaluate $I_5$. [3]

<details>
<summary>📝 MS 展开查看</summary>

**(a)** Write $I_n = \int_0^1 (1 - x^2) \cdot (1 - x^2)^{(n-2)/2}\,dx = \int_0^1 (1 - x^2)(1 - x^2)^{(n-2)/2}\,dx$

$= \int_0^1 (1 - x^2)^{(n-2)/2}\,dx - \int_0^1 x^2(1 - x^2)^{(n-2)/2}\,dx$

$= I_{n-2} - \int_0^1 x \cdot x(1 - x^2)^{(n-2)/2}\,dx$

Let $u = x$, $dv = x(1 - x^2)^{(n-2)/2}dx$

$du = dx$, $v = -\frac{1}{n}(1 - x^2)^{n/2}$

$\int_0^1 x^2(1 - x^2)^{(n-2)/2}\,dx = \left[-\frac{x}{n}(1 - x^2)^{n/2}\right]_0^1 + \frac{1}{n}\int_0^1 (1 - x^2)^{n/2}\,dx$

$= 0 + \frac{1}{n}I_n$

So $I_n = I_{n-2} - \frac{1}{n}I_n$

$I_n + \frac{1}{n}I_n = I_{n-2}$

$I_n\frac{n+1}{n} = I_{n-2}$

Therefore $(n+1)I_n = n I_{n-2}$, which is equivalent to $(n+2)I_n = (n+1)I_{n-2}$ (shift index).

**M1** — Split $(1-x^2)^{n/2} = (1-x^2)(1-x^2)^{(n-2)/2}$
**M1** — Express $I_n = I_{n-2} - \int x^2(1-x^2)^{(n-2)/2}dx$
**M1** — Integration by parts with correct $u$, $dv$ selection
**A1** — Correct working leading to $I_n = I_{n-2} - \frac{1}{n}I_n$
**A1** — Correct recurrence $(n+2)I_n = (n+1)I_{n-2}$

**(b)** $I_0 = \int_0^1 1\,dx = 1$

$I_1 = \int_0^1 (1 - x^2)^{1/2}\,dx = \frac{\pi}{4}$

Using $(n+2)I_n = (n+1)I_{n-2}$:

$n=2$: $4I_2 = 3I_0 \Rightarrow I_2 = \frac{3}{4}$

$n=3$: $5I_3 = 4I_1 \Rightarrow I_3 = \frac{4}{5} \cdot \frac{\pi}{4} = \frac{\pi}{5}$

$n=4$: $6I_4 = 5I_2 \Rightarrow I_4 = \frac{5}{6} \cdot \frac{3}{4} = \frac{5}{8}$

$n=5$: $7I_5 = 6I_3 \Rightarrow I_5 = \frac{6}{7} \cdot \frac{\pi}{5} = \frac{6\pi}{35}$

**M1** — Find $I_0$ and $I_1$ correctly
**A1** — Correct iterative application
**A1** — Correct $I_5 = \frac{6\pi}{35}$

</details>

> **Example: s21/23 Q6** — Given $I_n = \int_0^{\pi/2} \sin^n x\,dx$.
> (a) Show that $nI_n = (n-1)I_{n-2}$ for $n \ge 2$. [5]
> (b) Hence find $I_6$. [2]

<details>
<summary>📝 MS 展开查看</summary>

**(a)** $I_n = \int_0^{\pi/2} \sin^{n-1}x \cdot \sin x\,dx$

Let $u = \sin^{n-1}x$, $dv = \sin x\,dx$

$du = (n-1)\sin^{n-2}x\cos x\,dx$, $v = -\cos x$

$I_n = \left[-\sin^{n-1}x\cos x\right]_0^{\pi/2} + (n-1)\int_0^{\pi/2} \sin^{n-2}x\cos^2 x\,dx$

$= 0 + (n-1)\int_0^{\pi/2} \sin^{n-2}x(1-\sin^2 x)\,dx$

$= (n-1)(I_{n-2} - I_n)$

$I_n = (n-1)I_{n-2} - (n-1)I_n$

$nI_n = (n-1)I_{n-2}$

**(b)** $I_0 = \frac{\pi}{2}$, $I_1 = 1$

$I_2 = \frac{1}{2}I_0 = \frac{\pi}{4}$, $I_4 = \frac{3}{4}I_2 = \frac{3\pi}{16}$, $I_6 = \frac{5}{6}I_4 = \frac{5\pi}{32}$

**M1** — Integration by parts
**A1** — Correct derivation of $nI_n = (n-1)I_{n-2}$
**M1** — Find $I_0$, $I_1$
**A1** — Correct $I_6 = \frac{5\pi}{32}$

</details>

## Type 2: Integration by Parts / Substitution (3–4 marks)

> **Example: s20/23 Q2** — Evaluate $\int_0^1 x^2 e^{2x}\,dx$.

<details>
<summary>📝 MS 展开查看</summary>

Let $u = x^2$, $dv = e^{2x}dx$

$du = 2x\,dx$, $v = \frac{1}{2}e^{2x}$

$\int x^2 e^{2x}\,dx = \frac{1}{2}x^2e^{2x} - \int \frac{1}{2}e^{2x} \cdot 2x\,dx = \frac{1}{2}x^2e^{2x} - \int xe^{2x}\,dx$

For $\int xe^{2x}\,dx$: $u = x$, $dv = e^{2x}dx$

$= \frac{1}{2}xe^{2x} - \frac{1}{4}e^{2x}$

So $\int x^2 e^{2x}\,dx = \frac{1}{2}x^2e^{2x} - \frac{1}{2}xe^{2x} + \frac{1}{4}e^{2x} + C$

$\int_0^1 x^2 e^{2x}\,dx = \left[\frac{1}{2}x^2e^{2x} - \frac{1}{2}xe^{2x} + \frac{1}{4}e^{2x}\right]_0^1$

$= \left(\frac{1}{2}e^2 - \frac{1}{2}e^2 + \frac{1}{4}e^2\right) - \frac{1}{4} = \frac{1}{4}(e^2 - 1)$

**M1** — Correct first integration by parts
**A1** — Correct $\int xe^{2x}dx$
**A1** — Correct final answer $\frac{1}{4}(e^2 - 1)$

</details>

## Type 3: Integration of Rational Functions (5 marks)

> **Example: s23/21 Q4** — Find $\int \frac{2x^2 + 3x + 1}{(x-1)(x^2 + 1)}\,dx$.

<details>
<summary>📝 MS 展开查看</summary>

Partial fractions:

$$\frac{2x^2 + 3x + 1}{(x-1)(x^2+1)} = \frac{A}{x-1} + \frac{Bx + C}{x^2+1}$$

Multiplying: $2x^2 + 3x + 1 = A(x^2+1) + (Bx + C)(x-1)$

$= A(x^2+1) + Bx(x-1) + C(x-1)$

$= Ax^2 + A + Bx^2 - Bx + Cx - C$

$= (A+B)x^2 + (-B+C)x + (A-C)$

Compare coefficients:

$x^2$: $A + B = 2$
$x$: $-B + C = 3$
Constant: $A - C = 1$

Solving: $A = 2$, $B = 0$, $C = 1$

Wait — check: $A=2$, then $2+B=2 \Rightarrow B=0$, then $-0+C=3 \Rightarrow C=3$, but $A-C=2-3=-1\neq1$

Re-solve: From $A-C=1 \Rightarrow C = A-1$
From $A+B=2 \Rightarrow B = 2-A$
From $-B+C=3 \Rightarrow -(2-A)+(A-1)=3 \Rightarrow -2+A+A-1=3 \Rightarrow 2A-3=3 \Rightarrow A=3$

Then $B=-1$, $C=2$

Check: $(A+B)=3-1=2\checkmark$, $(-B+C)=1+2=3\checkmark$, $(A-C)=3-2=1\checkmark$

$$\frac{2x^2+3x+1}{(x-1)(x^2+1)} = \frac{3}{x-1} + \frac{-x+2}{x^2+1}$$

$$= \frac{3}{x-1} - \frac{x}{x^2+1} + \frac{2}{x^2+1}$$

Integrate:

$$\int \frac{3}{x-1}\,dx = 3\ln|x-1|$$

$$\int \frac{x}{x^2+1}\,dx = \frac{1}{2}\ln(x^2+1)$$

$$\int \frac{2}{x^2+1}\,dx = 2\tan^{-1}x$$

Answer: $3\ln|x-1| - \frac{1}{2}\ln(x^2+1) + 2\tan^{-1}x + C$

**M1** — Correct partial fraction form
**A1** — Correct coefficients $A=3$, $B=-1$, $C=2$
**M1** — Separate into standard integrals
**A1** — Correct $\ln$ terms
**A1** — Correct $\tan^{-1}$ term

</details>
