# Implicit Differentiation — Question Types

## Type 1: First Derivative $\frac{dy}{dx}$ (3 marks)

> **Example: w20/22 Q5(a)** — Find $\frac{dy}{dx}$ in terms of $x$ and $y$, given that $x^3 + y^3 = 3xy$.

<details>
<summary>📝 MS 展开查看</summary>

Differentiate implicitly:

$$3x^2 + 3y^2\frac{dy}{dx} = 3y + 3x\frac{dy}{dx}$$

$$3y^2\frac{dy}{dx} - 3x\frac{dy}{dx} = 3y - 3x^2$$

$$\frac{dy}{dx}(3y^2 - 3x) = 3y - 3x^2$$

$$\frac{dy}{dx} = \frac{y - x^2}{y^2 - x}$$

**Marks scheme:**
- **M1** — Differentiate implicitly, including $\frac{d}{dx}(y^3) = 3y^2\frac{dy}{dx}$ and product rule for $3xy$
- **A1** — Correct differentiated equation
- **A1** — Correct expression for $\frac{dy}{dx}$

</details>

## Type 2: Second Derivative $\frac{d^2y}{dx^2}$ (5 marks)

> **Example: w21/21 Q3** — Given $x^3 + y^3 = 3xy$, find $\frac{d^2y}{dx^2}$ in terms of $x$ and $y$.

<details>
<summary>📝 MS 展开查看</summary>

From part (a): $\frac{dy}{dx} = \frac{y - x^2}{y^2 - x}$

Differentiate again:

$$\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{y - x^2}{y^2 - x}\right)$$

Using quotient rule:

$$\frac{d^2y}{dx^2} = \frac{(\frac{dy}{dx} - 2x)(y^2 - x) - (y - x^2)(2y\frac{dy}{dx} - 1)}{(y^2 - x)^2}$$

Substitute $\frac{dy}{dx} = \frac{y - x^2}{y^2 - x}$ and simplify using $x^3 + y^3 = 3xy$.

After simplification:

$$\frac{d^2y}{dx^2} = \frac{2xy}{(y^2 - x)^3}$$

**Marks scheme:**
- **M1** — Attempt quotient rule on $\frac{dy}{dx}$
- **M1** — Differentiate $y$ terms implicitly (including $\frac{dy}{dx}$)
- **A1** — Correct expression before simplification
- **A1** — Substitute expression for $\frac{dy}{dx}$
- **A1** — Correct simplified $\frac{d^2y}{dx^2}$

</details>

## Type 3: Values at Specific Points (8 marks total)

> **Example: s23/23 Q4** — The curve is defined by $x^2 + xy + y^2 = 7$.
> (a) Find $\frac{dy}{dx}$ in terms of $x$ and $y$. [3]
> (b) Find the equation of the tangent at $(-1, 2)$. [2]
> (c) Find $\frac{d^2y}{dx^2}$ at $(-1, 2)$. [3]

<details>
<summary>📝 MS 展开查看</summary>

**(a)** Differentiate:

$$2x + y + x\frac{dy}{dx} + 2y\frac{dy}{dx} = 0$$

$$\frac{dy}{dx}(x + 2y) = -(2x + y)$$

$$\frac{dy}{dx} = -\frac{2x + y}{x + 2y}$$

**M1** — Implicit differentiation with product rule for $xy$
**A1** — Correct differentiated equation
**A1** — Correct $\frac{dy}{dx}$

**(b)** At $(-1, 2)$:

$$\frac{dy}{dx} = -\frac{2(-1) + 2}{-1 + 2(2)} = -\frac{0}{3} = 0$$

Tangent: $y - 2 = 0(x + 1)$ i.e. $y = 2$

**M1** — Substitute point into $\frac{dy}{dx}$
**A1** — Correct equation $y = 2$

**(c)** Differentiate $\frac{dy}{dx}$ expression:

$$\frac{d^2y}{dx^2} = -\frac{(2 + \frac{dy}{dx})(x + 2y) - (2x + y)(1 + 2\frac{dy}{dx})}{(x + 2y)^2}$$

At $(-1, 2)$ with $\frac{dy}{dx} = 0$:

$$\frac{d^2y}{dx^2} = -\frac{(2)(3) - (0)(1)}{9} = -\frac{6}{9} = -\frac{2}{3}$$

**M1** — Attempt quotient rule
**A1** — Correct substitution of $\frac{dy}{dx}=0$ and values
**A1** — Correct $-\frac{2}{3}$

</details>

> **Example: s24/23 Q3** — Given $x\sin y + ye^x = 0$.
> (a) Find $\frac{dy}{dx}$ at $(0, \pi)$. [4]
> (b) Find $\frac{d^2y}{dx^2}$ at $(0, \pi)$. [4]

<details>
<summary>📝 MS 展开查看</summary>

**(a)** Differentiate:

$$\sin y + x\cos y\frac{dy}{dx} + \frac{dy}{dx}e^x + ye^x = 0$$

$$\frac{dy}{dx}(x\cos y + e^x) = -\sin y - ye^x$$

$$\frac{dy}{dx} = -\frac{\sin y + ye^x}{x\cos y + e^x}$$

At $(0, \pi)$: $\frac{dy}{dx} = -\frac{0 + \pi \cdot 1}{0\cdot(-1) + 1} = -\pi$

**M1** — Product rule on $x\sin y$ and $ye^x$
**A1** — Correct differentiated equation
**M1** — Rearrange for $\frac{dy}{dx}$
**A1** — Correct $-\pi$

**(b)** Differentiate $\frac{dy}{dx}$:

Numerator: $N = -(\sin y + ye^x)$, Denominator: $D = x\cos y + e^x$

At $(0, \pi)$ with $\frac{dy}{dx} = -\pi$:

$N' = -(\cos y\frac{dy}{dx} + \frac{dy}{dx}e^x + ye^x)$, $D' = \cos y - x\sin y\frac{dy}{dx} + e^x$

$\frac{d^2y}{dx^2} = \frac{N'D - ND'}{D^2}$ evaluated at $(0, \pi)$

$N' = -((-1)(-\pi) + (-\pi)(1) + \pi(1)) = -(\pi - \pi + \pi) = -\pi $

$D' = -1 - 0 + 1 = 0$

$\frac{d^2y}{dx^2} = \frac{(-\pi)(1) - (-\pi)(0)}{1} = -\pi$

**M1** — Attempt to differentiate $\frac{dy}{dx}$
**M1** — Correct $N'$, $D'$ with chain rule
**A1** — Correct values at $(0, \pi)$
**A1** — Correct $-\pi$

</details>
