#!/usr/bin/env python3
"""
Fill ALL empty/skeleton topic files with complete content.
Every file gets 500+ chars of real exam-focused material.
"""

import sys, os
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

BASE = Path(__file__).resolve().parent.parent
TOPICS = BASE / 'docs' / 'subjects' / '9231-further-mathematics' / 'topics'

CONTENT = {
    'hyperbolic-functions': {
        'methods': """---
title: Methods
sidebar_position: 4
---

# Methods — Hyperbolic Functions

## Method 1: Proving hyperbolic identities

**When to use it:** "Show that" or "Prove that" involving $\\sinh$, $\\cosh$, $\\tanh$.

**Steps:**
1. Write all hyperbolic functions in exponential form: $\\sinh x = \\frac{e^x - e^{-x}}{2}$, $\\cosh x = \\frac{e^x + e^{-x}}{2}$
2. Simplify the algebra (expand brackets, collect terms)
3. Alternatively: use known identities ($\\cosh^2 x - \\sinh^2 x \\equiv 1$, $\\sinh 2x \\equiv 2\\sinh x\\cosh x$)

**Example structure (proving $\\cosh 2x \\equiv 2\\cosh^2 x - 1$):**
$$\\cosh 2x = \\frac{e^{2x} + e^{-2x}}{2} = \\frac{(e^x + e^{-x})^2 - 2}{2} = 2\\left(\\frac{e^x + e^{-x}}{2}\\right)^2 - 1 = 2\\cosh^2 x - 1$$

**Mistakes to avoid:**
- Confusing $\\cosh^2 x - \\sinh^2 x \\equiv 1$ with $\\cos^2 x + \\sin^2 x \\equiv 1$
- Sign errors in $\\cosh 2x$ identity (it's $+1$ for $2\\cosh^2 x - 1$, not $-1$)

## Method 2: Solving hyperbolic equations

**When to use it:** "Solve $\\cosh x - 3\\sinh x = 4$" type questions.

**Steps:**
1. Replace $\\cosh x$ and $\\sinh x$ with exponential forms
2. Result: an equation in $e^x$ — multiply through to clear denominators
3. Solve the resulting quadratic in $e^x$
4. Take natural logs: $x = \\ln(\\ldots)$
5. Check domain: $\\cosh x \\ge 1$ always, $\\sinh x$ can be any real

**Example (from 9231/w22/qp/22):**
Solve $\\cosh x - 3\\sinh x = 4$:
$$\\frac{e^x + e^{-x}}{2} - \\frac{3(e^x - e^{-x})}{2} = 4$$
$$e^x + e^{-x} - 3e^x + 3e^{-x} = 8$$
$$-2e^x + 4e^{-x} = 8 \\Rightarrow -2e^{2x} - 8e^x + 4 = 0$$
$$e^{2x} + 4e^x - 2 = 0 \\Rightarrow e^x = -2 \\pm \\sqrt{6}$$
Since $e^x > 0$, $e^x = -2 + \\sqrt{6}$, so $x = \\ln(\\sqrt{6} - 2)$

## Method 3: Logarithmic forms of inverse hyperbolic functions

**When to use it:** Express $\\sinh^{-1} x$, $\\cosh^{-1} x$, $\\tanh^{-1} x$ in $\\ln$ form.

**Key formulas (memorise):**
$$\\sinh^{-1} x = \\ln(x + \\sqrt{x^2 + 1})$$
$$\\cosh^{-1} x = \\ln(x + \\sqrt{x^2 - 1})\\quad(x \\ge 1)$$
$$\\tanh^{-1} x = \\frac{1}{2}\\ln\\frac{1+x}{1-x}\\quad(|x| < 1)$$
""",
        'last-minute-summary': """---
title: Last-Minute Summary
sidebar_position: 7
---

# Last-Minute Summary — Hyperbolic Functions

## Must-know formulas

$$\\sinh x = \\frac{e^x - e^{-x}}{2},\\quad \\cosh x = \\frac{e^x + e^{-x}}{2}$$

$$\\cosh^2 x - \\sinh^2 x \\equiv 1$$

$$\\sinh^{-1} x = \\ln(x + \\sqrt{x^2+1}),\\quad \\cosh^{-1} x = \\ln(x + \\sqrt{x^2-1}),\\quad \\tanh^{-1} x = \\frac12\\ln\\frac{1+x}{1-x}$$

## Common question patterns

| Pattern | First step |
|---------|------------|
| Prove identity involving $\\sinh,\\cosh$ | Write in exponential form |
| Solve $a\\cosh x + b\\sinh x = c$ | Convert to exponentials, solve quadratic in $e^x$ |
| Find $\\sinh^{-1}(\\ldots)$ in log form | Apply formula directly |
| Integrate $1/\\sqrt{x^2+a^2}$ | Result is $\\sinh^{-1}(x/a) + C$ |

## Red flags

- $\\cosh^{-1} x$ domain: $x \\ge 1$
- $\\tanh^{-1} x$ domain: $|x| < 1$
- $\\frac{d}{dx}\\cosh x = +\\sinh x$ (NOT $-\\sinh x$ like $\\cos x$)
""",
    },
    'matrices-fp2': {
        'methods': """---
title: Methods
sidebar_position: 4
---

# Methods — Matrices (Further Pure 2)

## Method 1: Solving $3\\times3$ linear systems

**When to use it:** "Determine whether the system has a unique solution."

**Steps:**
1. Write the system as $A\\mathbf{x} = \\mathbf{b}$
2. Compute $\\det A$
3. If $\\det A \\neq 0$: unique solution exists. Solve using inverse or elimination.
4. If $\\det A = 0$: no unique solution. Check consistency:
   - Try to solve — if contradictory equations → inconsistent (no solution, 3 planes no common intersection)
   - If equations are dependent → consistent with infinite solutions (planes intersect in a line)

**Example (from 9231/s21/qp/22):**
$$\\begin{pmatrix} a & 3 & 1 \\\\ 1 & 1 & 3 \\\\ 2 & -1 & -5 \\end{pmatrix}\\begin{pmatrix}x\\\\y\\\\z\\end{pmatrix} = \\begin{pmatrix}14\\\\0\\\\17\\end{pmatrix}$$
$\\det = a(1\\cdot(-5)-3\\cdot(-1)) - 3(1\\cdot(-5)-3\\cdot2) + 1(1\\cdot(-1)-1\\cdot2)$
$= a(-5+3) - 3(-5-6) + 1(-1-2) = -2a + 33 - 3 = 30 - 2a$
For integer $a$, $\\det \\neq 0$ → unique solution. Geometrically: 3 planes meet at a single point.

## Method 2: Finding eigenvalues and eigenvectors

**When to use it:** Any question mentioning eigenvalues or eigenvectors.

**Steps:**
1. Characteristic equation: $\\det(A - \\lambda I) = 0$
2. Expand determinant to get polynomial in $\\lambda$
3. Solve polynomial for eigenvalues $\\lambda_1, \\lambda_2, \\lambda_3$
4. For each $\\lambda_i$, solve $(A - \\lambda_i I)\\mathbf{e}_i = \\mathbf{0}$:
   - Write the augmented matrix
   - Row reduce
   - Express solution in parametric form

**Example structure:**
For $A = \\begin{pmatrix}3&1&1\\\\0&6&-1\\\\0&0&-2\\end{pmatrix}$:
$$\\det(A-\\lambda I) = (3-\\lambda)(6-\\lambda)(-2-\\lambda) = 0 \\Rightarrow \\lambda = 3, 6, -2$$

For $\\lambda = 3$: $(A-3I)\\mathbf{e} = \\begin{pmatrix}0&1&1\\\\0&3&-1\\\\0&0&-5\\end{pmatrix}\\begin{pmatrix}e_1\\\\e_2\\\\e_3\\end{pmatrix} = \\mathbf{0}$
From row 3: $-5e_3 = 0 \\Rightarrow e_3 = 0$. From row 2: $3e_2 - e_3 = 0 \\Rightarrow e_2 = 0$. So $\\mathbf{e} = \\begin{pmatrix}1\\\\0\\\\0\\end{pmatrix}$

## Method 3: Diagonalisation $A = PDP^{-1}$

**When to use it:** "Find $P$ and $D$ such that $A^5 = PD^5P^{-1}$"

**Steps:**
1. Find all eigenvalues $\\lambda_i$ and eigenvectors $\\mathbf{e}_i$
2. $D = \\operatorname{diag}(\\lambda_1, \\lambda_2, \\lambda_3)$ (eigenvalues on diagonal)
3. $P = [\\mathbf{e}_1 \\; \\mathbf{e}_2 \\; \\mathbf{e}_3]$ (eigenvectors as columns, same order as D)
4. Then $A^n = PD^nP^{-1}$

## Method 4: Cayley–Hamilton theorem

**When to use it:** "Use the characteristic equation to find $A^{-1}$" or "find $A^2$ in terms of $A$ and $I$"

**Key idea:** A matrix satisfies its own characteristic equation.
If $\\det(A - \\lambda I) = \\lambda^2 - 6\\lambda + 11 = 0$, then $A^2 - 6A + 11I = 0$.
So $A^2 = 6A - 11I$, and $A^{-1} = \\frac{1}{11}(6I - A)$.
""",
    },
    'differentiation': {
        'methods': """---
title: Methods
sidebar_position: 4
---

# Methods — Differentiation

## Method 1: Differentiating inverse trig and hyperbolic functions

**Key derivatives (memorise these):**

| $f(x)$ | $f'(x)$ |
|--------|---------|
| $\\sin^{-1} x$ | $\\frac{1}{\\sqrt{1-x^2}}$ |
| $\\cos^{-1} x$ | $-\\frac{1}{\\sqrt{1-x^2}}$ |
| $\\tan^{-1} x$ | $\\frac{1}{1+x^2}$ |
| $\\sinh^{-1} x$ | $\\frac{1}{\\sqrt{1+x^2}}$ |
| $\\cosh^{-1} x$ | $\\frac{1}{\\sqrt{x^2-1}}$ |
| $\\tanh^{-1} x$ | $\\frac{1}{1-x^2}$ |
| $\\sinh x$ | $\\cosh x$ |
| $\\cosh x$ | $\\sinh x$ |
| $\\tanh x$ | $\\operatorname{sech}^2 x$ |

**Chain rule:** For $f(g(x))$, derivative = $f'(g(x)) \\cdot g'(x)$.
E.g. $\\frac{d}{dx}\\sinh^{-1}(2x) = \\frac{1}{\\sqrt{1+(2x)^2}} \\cdot 2 = \\frac{2}{\\sqrt{1+4x^2}}$

## Method 2: Implicit differentiation

**When to use it:** Equation mixing $x$ and $y$ that can't easily be solved for $y$.

**Steps:**
1. Differentiate both sides with respect to $x$
2. Remember: $\\frac{d}{dx}(y) = \\frac{dy}{dx}$, $\\frac{d}{dx}(y^2) = 2y\\frac{dy}{dx}$, etc.
3. Collect $\\frac{dy}{dx}$ terms on one side
4. Solve for $\\frac{dy}{dx}$
5. For $\\frac{d^2y}{dx^2}$: differentiate $\\frac{dy}{dx}$ implicitly again

**Example (from 9231/w20/qp/22):**
$y^2 + (xy+1)^2 = 5$, find $\\frac{dy}{dx}$ at $(1,1)$:
$$2y\\frac{dy}{dx} + 2(xy+1)(y + x\\frac{dy}{dx}) = 0$$
At $(1,1)$: $2(1)\\frac{dy}{dx} + 2(2)(1 + \\frac{dy}{dx}) = 0$
$2\\frac{dy}{dx} + 4 + 4\\frac{dy}{dx} = 0 \\Rightarrow 6\\frac{dy}{dx} = -4 \\Rightarrow \\frac{dy}{dx} = -\\frac{2}{3}$

## Method 3: Maclaurin series

**When to use it:** "Find the Maclaurin series for $f(x)$ up to the term in $x^n$."

**Steps:**
1. Compute $f(0)$, $f'(0)$, $f''(0)$, $f'''(0)$
2. Apply formula: $f(x) = f(0) + f'(0)x + \\frac{f''(0)}{2!}x^2 + \\frac{f'''(0)}{3!}x^3 + \\cdots$

**Example (from 9231/w20/qp/22):**
$f(x) = \\tan(\\frac{\\pi}{4} + x)$:
$f(0) = \\tan\\frac{\\pi}{4} = 1$
$f'(x) = \\sec^2(\\frac{\\pi}{4} + x)$, $f'(0) = \\sec^2\\frac{\\pi}{4} = 2$
$f''(x) = 2\\sec^2(\\frac{\\pi}{4} + x)\\tan(\\frac{\\pi}{4} + x)$, $f''(0) = 2(2)(1) = 4$
$\\tan(\\frac{\\pi}{4} + x) = 1 + 2x + \\frac{4}{2!}x^2 + \\cdots = 1 + 2x + 2x^2 + \\cdots$
""",
        'last-minute-summary': """---
title: Last-Minute Summary
sidebar_position: 7
---

# Last-Minute Summary — Differentiation

## Must-know derivatives

$$\\frac{d}{dx}\\sin^{-1}x = \\frac{1}{\\sqrt{1-x^2}},\\qquad \\frac{d}{dx}\\cos^{-1}x = -\\frac{1}{\\sqrt{1-x^2}}$$
$$\\frac{d}{dx}\\sinh^{-1}x = \\frac{1}{\\sqrt{1+x^2}},\\qquad \\frac{d}{dx}\\cosh^{-1}x = \\frac{1}{\\sqrt{x^2-1}},\\qquad \\frac{d}{dx}\\tanh^{-1}x = \\frac{1}{1-x^2}$$

## Key sign warnings

- $\\frac{d}{dx}\\cos^{-1}x$ is $-\\frac{1}{\\sqrt{1-x^2}}$ (negative!), $\\frac{d}{dx}\\sin^{-1}x$ is positive
- $\\frac{d}{dx}\\tanh^{-1}x = \\frac{1}{1-x^2}$ NOT $\\frac{1}{1+x^2}$ (that's $\\sinh^{-1}x$)
- $\\frac{d}{dx}\\cosh x = +\\sinh x$ NOT $-\\sinh x$ (different from $\\cos x$)

## Maclaurin quick reference

$$f(x) = f(0) + f'(0)x + \\frac{f''(0)}{2!}x^2 + \\frac{f'''(0)}{3!}x^3 + \\cdots$$

Remember to evaluate derivatives at $x = 0$, not at the original variable.
""",
    },
    'integration': {
        'methods': """---
title: Methods
sidebar_position: 4
---

# Methods — Integration

## Method 1: Standard integrals (inverse forms)

**When to use it:** Integrals of form $\\int\\frac{dx}{\\sqrt{a^2-x^2}}$, $\\int\\frac{dx}{a^2+x^2}$, $\\int\\frac{dx}{\\sqrt{x^2\\pm a^2}}$.

**Key results (from MF19, but must know which is which):**

$$\\int\\frac{dx}{\\sqrt{a^2-x^2}} = \\sin^{-1}\\frac{x}{a} + C \\quad (|x| < a)$$
$$\\int\\frac{dx}{a^2+x^2} = \\frac{1}{a}\\tan^{-1}\\frac{x}{a} + C$$
$$\\int\\frac{dx}{\\sqrt{x^2+a^2}} = \\sinh^{-1}\\frac{x}{a} + C$$
$$\\int\\frac{dx}{\\sqrt{x^2-a^2}} = \\cosh^{-1}\\frac{x}{a} + C \\quad (x > a)$$

**Common mistake:** $\\int\\frac{dx}{\\sqrt{a^2-x^2}}$ gives $\\sin^{-1}$, NOT $\\sinh^{-1}$.
$\\int\\frac{dx}{\\sqrt{x^2+a^2}}$ gives $\\sinh^{-1}$, NOT $\\cosh^{-1}$.

## Method 2: Reduction formulae

**When to use it:** "Show that $\\int_0^{\\pi/2} \\sin^n x\\,dx = \\frac{n-1}{n}I_{n-2}$" or similar.

**Steps:**
1. Write $I_n = \\int f(x,n)\\,dx$
2. Apply integration by parts: let $u = \\sin^{n-1}x$, $dv = \\sin x\\,dx$
3. This gives $I_n$ in terms of $I_{n-2}$
4. For specific $n$, apply the formula recursively until reaching $I_0$ or $I_1$

**Example (from 9231/s20/qp/22):**
$I_n = \\int_0^1 (1-x^2)^{n/2}\\,dx$
$\\frac{d}{dx}[x(1-x^2)^{n/2}] = (1-x^2)^{n/2} - nx^2(1-x^2)^{n/2-1}$
$= (1-x^2)^{n/2} - n(1 - (1-x^2))(1-x^2)^{n/2-1}$
$= (1-x^2)^{n/2} - n(1-x^2)^{n/2-1} + n(1-x^2)^{n/2}$
Integrating from 0 to 1: $0 = I_n - nI_{n-2} + nI_n \\Rightarrow nI_n = \\sqrt{3}(\\frac12)^{n} + (n-1)I_{n-2}$

## Method 3: Arc length

**When to use it:** "Find the length of the arc of the curve from $x=a$ to $x=b$."

**Formulas:**
- Cartesian: $s = \\int_a^b \\sqrt{1 + (\\frac{dy}{dx})^2}\\,dx$
- Parametric: $s = \\int_{t_1}^{t_2} \\sqrt{(\\frac{dx}{dt})^2 + (\\frac{dy}{dt})^2}\\,dt$
- Polar: $s = \\int_{\\theta_1}^{\\theta_2} \\sqrt{r^2 + (\\frac{dr}{d\\theta})^2}\\,d\\theta$

**Example (from 9231/s20/qp/22):**
Arc of $y = \\cosh x$ from $x=0$ to $x=a$ where $\\sinh a = \\frac12$:
$$\\frac{dy}{dx} = \\sinh x,\\; 1 + (\\frac{dy}{dx})^2 = 1 + \\sinh^2 x = \\cosh^2 x$$
$$s = \\int_0^a \\cosh x\\,dx = [\\sinh x]_0^a = \\sinh a = \\frac12$$

## Method 4: Surface area of revolution

**When to use it:** "Find the area of the surface generated when the curve is rotated about the $x$-axis."

**Formula:**
$$S = 2\\pi\\int_a^b y\\sqrt{1+\\left(\\frac{dy}{dx}\\right)^2}\\,dx$$

**Don't forget:** Factor of $2\\pi$ and the $y$ inside the integral!
""",
        'last-minute-summary': """---
title: Last-Minute Summary
sidebar_position: 7
---

# Last-Minute Summary — Integration

## Which inverse goes where

| Integral | Result | Common wrong answer |
|----------|--------|-------------------|
| $\\int dx/\\sqrt{a^2-x^2}$ | $\\sin^{-1}(x/a)+C$ | $\\sinh^{-1}(x/a)$ ✗ |
| $\\int dx/(x^2+a^2)$ | $\\frac1a\\tan^{-1}(x/a)+C$ | — |
| $\\int dx/\\sqrt{x^2+a^2}$ | $\\sinh^{-1}(x/a)+C$ | $\\cosh^{-1}(x/a)$ ✗ |
| $\\int dx/\\sqrt{x^2-a^2}$ | $\\cosh^{-1}(x/a)+C$ | $\\sinh^{-1}(x/a)$ ✗ |

## Arc length vs surface area

| Quantity | Formula | Don't forget |
|----------|---------|--------------|
| Arc length (Cartesian) | $\\int\\sqrt{1+(dy/dx)^2}\\,dx$ | Square root around everything |
| Surface area | $2\\pi\\int y\\sqrt{1+(dy/dx)^2}\\,dx$ | Factor $2\\pi$ **and** factor $y$ |

## Reduction formula checklist

- Integration by parts is almost always the first step
- Choose $u =$ the function that simplifies when differentiated
- Write $I_n$ in terms of $I_{n-1}$ or $I_{n-2}$
- For specific $n$, apply recursively
""",
    },
    'complex-numbers': {
        'methods': """---
title: Methods
sidebar_position: 4
---

# Methods — Complex Numbers

## Method 1: de Moivre's theorem

**When to use it:** Any problem involving powers of complex numbers, multiple angles, or roots of unity.

**Theorem:**
$$(\\cos\\theta + i\\sin\\theta)^n = \\cos n\\theta + i\\sin n\\theta$$

**Proof by induction (for positive integer $n$):**
1. Base case $n=1$: trivially true
2. Assume true for $n=k$: $(\\cos\\theta + i\\sin\\theta)^k = \\cos k\\theta + i\\sin k\\theta$
3. For $n=k+1$: multiply both sides by $(\\cos\\theta + i\\sin\\theta)$:
   $$(\\cos\\theta + i\\sin\\theta)^{k+1} = (\\cos k\\theta + i\\sin k\\theta)(\\cos\\theta + i\\sin\\theta)$$
   $$= \\cos k\\theta\\cos\\theta - \\sin k\\theta\\sin\\theta + i(\\sin k\\theta\\cos\\theta + \\cos k\\theta\\sin\\theta)$$
   $$= \\cos(k+1)\\theta + i\\sin(k+1)\\theta$$

## Method 2: Multiple angle formulae

**When to use it:** "Express $\\cos 5\\theta$ in terms of $\\cos\\theta$" or similar.

**Steps:**
1. Write $(\\cos\\theta + i\\sin\\theta)^5 = \\cos 5\\theta + i\\sin 5\\theta$
2. Expand LHS using binomial theorem
3. Equate real parts to get $\\cos 5\\theta$, imaginary parts for $\\sin 5\\theta$

**Example:**
$(\\cos\\theta + i\\sin\\theta)^5 = \\cos^5\\theta + 5i\\cos^4\\theta\\sin\\theta - 10\\cos^3\\theta\\sin^2\\theta - 10i\\cos^2\\theta\\sin^3\\theta + 5\\cos\\theta\\sin^4\\theta + i\\sin^5\\theta$
Equating real parts: $\\cos 5\\theta = \\cos^5\\theta - 10\\cos^3\\theta\\sin^2\\theta + 5\\cos\\theta\\sin^4\\theta$
Using $\\sin^2\\theta = 1 - \\cos^2\\theta$: $\\cos 5\\theta = 16\\cos^5\\theta - 20\\cos^3\\theta + 5\\cos\\theta$

## Method 3: Power reduction

**When to use it:** "Express $\\sin^6\\theta$ in terms of cosines of multiple angles."

**Key substitution:** Let $z = \\cos\\theta + i\\sin\\theta = e^{i\\theta}$.
Then $z^{-1} = \\cos\\theta - i\\sin\\theta = e^{-i\\theta}$.

$$\\cos\\theta = \\frac{z + z^{-1}}{2},\\qquad \\sin\\theta = \\frac{z - z^{-1}}{2i}$$
$$\\cos n\\theta = \\frac{z^n + z^{-n}}{2},\\qquad \\sin n\\theta = \\frac{z^n - z^{-n}}{2i}$$

**Example:** Express $\\sin^6\\theta$:
$$\\sin^6\\theta = \\left(\\frac{z - z^{-1}}{2i}\\right)^6 = -\\frac{1}{64}(z^6 - 6z^4 + 15z^2 - 20 + 15z^{-2} - 6z^{-4} + z^{-6})$$
$$= -\\frac{1}{64}(2\\cos 6\\theta - 12\\cos 4\\theta + 30\\cos 2\\theta - 20)$$
$$= \\frac{1}{32}(10 - 15\\cos 2\\theta + 6\\cos 4\\theta - \\cos 6\\theta)$$

## Method 4: $C + iS$ method for summing series

**When to use it:** "Sum $\\sum_{r=0}^{n-1} \\cos(2r+1)\\theta$" or similar.

**Steps:**
1. Define $C = \\sum_{r=0}^{n-1} \\cos(2r+1)\\theta$ and $S = \\sum_{r=0}^{n-1} \\sin(2r+1)\\theta$
2. Then $C + iS = \\sum_{r=0}^{n-1} e^{i(2r+1)\\theta} = e^{i\\theta}\\sum_{r=0}^{n-1} e^{2ir\\theta}$
3. Sum the geometric series: $= e^{i\\theta}\\cdot\\frac{e^{2in\\theta} - 1}{e^{2i\\theta} - 1}$
4. Simplify and take real part for $C$, imaginary part for $S$

## Method 5: Roots of unity

**When to use it:** "Find the $n$th roots of $1$" or "Solve $z^n = 1$".

$$z_k = e^{2\\pi i k / n} = \\cos\\frac{2\\pi k}{n} + i\\sin\\frac{2\\pi k}{n},\\quad k = 0, 1, \\ldots, n-1$$

**Key properties:**
- Sum of all $n$th roots of unity = $0$
- Product of all $n$th roots of unity = $(-1)^{n-1}$
- Roots form vertices of regular $n$-gon on unit circle
""",
        'last-minute-summary': """---
title: Last-Minute Summary
sidebar_position: 7
---

# Last-Minute Summary — Complex Numbers

## Quick reference

$$(\\cos\\theta + i\\sin\\theta)^n = \\cos n\\theta + i\\sin n\\theta$$
$$\\cos\\theta = \\frac{z+z^{-1}}{2},\\quad \\sin\\theta = \\frac{z-z^{-1}}{2i}$$
$$z^n + z^{-n} = 2\\cos n\\theta,\\quad z^n - z^{-n} = 2i\\sin n\\theta$$
$$\\text{Roots of unity: } z_k = e^{2\\pi i k/n},\\; k=0,1,\\ldots,n-1$$

## Common $C + iS$ series

$$\\sum_{r=0}^{n-1} \\cos(2r+1)\\theta = \\frac{\\sin 2n\\theta}{2\\sin\\theta}$$
$$\\sum_{r=0}^{n-1} \\sin(2r+1)\\theta = \\frac{1 - \\cos 2n\\theta}{2\\sin\\theta}$$

## Red flags

- Complex roots of real polynomials come in conjugate pairs
- $\\arg(z_1z_2) = \\arg z_1 + \\arg z_2$ (mod $2\\pi$)
- Sum of $n$th roots of unity = $0$
- de Moivre only works in mod-arg form, not $a+ib$ form
""",
    },
    'differential-equations': {
        'methods': """---
title: Methods
sidebar_position: 4
---

# Methods — Differential Equations

## Method 1: Integrating factor (1st order linear)

**When to use it:** $\\frac{dy}{dx} + P(x)y = Q(x)$

**Steps:**
1. Ensure DE is in standard form: $\\frac{dy}{dx} + P(x)y = Q(x)$
2. Compute integrating factor: $\\mu = e^{\\int P\\,dx}$
3. Multiply both sides by $\\mu$: $\\mu\\frac{dy}{dx} + \\mu Py = \\mu Q$
4. Note LHS = $\\frac{d}{dx}(\\mu y)$, so $\\frac{d}{dx}(\\mu y) = \\mu Q$
5. Integrate: $\\mu y = \\int\\mu Q\\,dx + C$
6. Solve for $y$: $y = \\frac{1}{\\mu}\\left(\\int\\mu Q\\,dx + C\\right)$
7. Apply initial condition to find $C$

**Example (from 9231/w20/qp/22):**
$x\\frac{dy}{dx} + 2y = e^x$, $y=3$ when $x=1$
Divide by $x$: $\\frac{dy}{dx} + \\frac{2}{x}y = \\frac{e^x}{x}$
$P = \\frac{2}{x}$, $\\int P\\,dx = 2\\ln x = \\ln(x^2)$, $\\mu = e^{\\ln(x^2)} = x^2$
$\\frac{d}{dx}(x^2 y) = x^2 \\cdot \\frac{e^x}{x} = xe^x$
$x^2 y = \\int xe^x\\,dx = (x-1)e^x + C$
$y = \\frac{(x-1)e^x + C}{x^2}$
$y(1)=3$: $3 = \\frac{0 + C}{1} \\Rightarrow C = 3$, so $y = \\frac{(x-1)e^x + 3}{x^2}$

## Method 2: 2nd order linear — CF + PI

**When to use it:** $a\\frac{d^2y}{dx^2} + b\\frac{dy}{dx} + cy = f(x)$

**Steps:**
1. Write auxiliary equation: $am^2 + bm + c = 0$
2. Solve for $m$:
   - Real distinct $m_1 \\neq m_2$: CF $= Ae^{m_1x} + Be^{m_2x}$
   - Repeated $m$: CF $= (A + Bx)e^{mx}$
   - Complex $\\alpha \\pm i\\beta$: CF $= e^{\\alpha x}(A\\cos\\beta x + B\\sin\\beta x)$
3. Find PI based on $f(x)$:
   - $f(x) = k$ (constant): try $y = c$
   - $f(x) = ke^{ax}$: try $y = pe^{ax}$ (unless $a$ is a root of AE)
   - $f(x) = a\\cos\\omega x + b\\sin\\omega x$: try $y = p\\cos\\omega x + q\\sin\\omega x$
   - $f(x) =$ polynomial: try $y$ of same degree
4. If PI form overlaps with CF, multiply by $x$ (or $x^2$ for double root)
5. General solution: $y = $ CF $+$ PI
6. Apply initial conditions to find constants $A, B$

**Example (from 9231/w20/qp/22):**
$\\frac{d^2x}{dt^2} + 8\\frac{dx}{dt} + 15x = 102\\cos 3t$, $x=1$, $\\frac{dx}{dt}=0$ when $t=0$

AE: $m^2 + 8m + 15 = 0 \\Rightarrow (m+3)(m+5)=0 \\Rightarrow m = -3, -5$
CF: $x = Ae^{-3t} + Be^{-5t}$

PI: try $x = p\\cos 3t + q\\sin 3t$
$\\dot{x} = -3p\\sin 3t + 3q\\cos 3t$
$\\ddot{x} = -9p\\cos 3t - 9q\\sin 3t$
Substitute: $(-9p\\cos 3t - 9q\\sin 3t) + 8(-3p\\sin 3t + 3q\\cos 3t) + 15(p\\cos 3t + q\\sin 3t) = 102\\cos 3t$
$\\cos 3t$: $-9p + 24q + 15p = 6p + 24q = 102$
$\\sin 3t$: $-9q - 24p + 15q = 6q - 24p = 0$
Solving: $p = 1$, $q = 4$
PI: $x = \\cos 3t + 4\\sin 3t$
General solution: $x = Ae^{-3t} + Be^{-5t} + \\cos 3t + 4\\sin 3t$
From ICs: $A+B+1=1$, $-3A-5B+12=0$ → $A=6$, $B=-6$
$x = 6e^{-3t} - 6e^{-5t} + \\cos 3t + 4\\sin 3t$

## Method 3: Substitution to reduce DE

**When to use it:** "Use the substitution $x = e^t$" or similar.

**Key substitutions:**
- $x = e^t$ converts $x^2y'' + axy' + by = f(\\ln x)$ to constant coefficient
- $y = ux$ converts homogeneous 1st order to separable
- $z = x + y$ converts certain 1st order to separable
""",
        'last-minute-summary': """---
title: Last-Minute Summary
sidebar_position: 7
---

# Last-Minute Summary — Differential Equations

## 1st order — integrating factor

$$\\frac{dy}{dx} + Py = Q \\Rightarrow \\mu = e^{\\int P\\,dx},\\; \\frac{d}{dx}(\\mu y) = \\mu Q$$

**Critical:** sign of $P$! If DE is $\\frac{dy}{dx} - \\frac{2}{x}y = x$, $P = -\\frac{2}{x}$, $\\mu = x^{-2}$.

## 2nd order — auxiliary equation

$$a\\frac{d^2y}{dx^2} + b\\frac{dy}{dx} + cy = 0 \\Rightarrow am^2 + bm + c = 0$$

| Roots | CF form |
|-------|---------|
| Real distinct $m_1,m_2$ | $Ae^{m_1x} + Be^{m_2x}$ |
| Repeated $m$ | $(A+Bx)e^{mx}$ |
| $\\alpha \\pm i\\beta$ | $e^{\\alpha x}(A\\cos\\beta x + B\\sin\\beta x)$ |

## PI — what to try

| RHS $f(x)$ | Try PI |
|------------|--------|
| Constant $k$ | $y = c$ |
| $e^{ax}$ | $y = pe^{ax}$ |
| $\\cos\\omega x$ or $\\sin\\omega x$ | $y = p\\cos\\omega x + q\\sin\\omega x$ |
| Polynomial | $y$ of same degree |

**If RHS overlaps with CF:** multiply PI by $x$ (or $x^2$ for double root).

**Apply initial conditions AFTER** combining CF + PI, not before.
""",
    },
}

# Also fix the question-types and mark-scheme-patterns for topics that are too thin
QT_EXTRA = {
    'hyperbolic-functions': """
## Type 1: Proving hyperbolic identities

**How to recognise it:** "Show that $\\cosh 2x = 2\\cosh^2 x - 1$" or similar.

**What the examiner wants:** Correct use of exponential definitions OR algebraic manipulation of known identities. Clear logical flow with each step justified.

**Standard method:**
1. Write $\\cosh 2x = \\frac{e^{2x} + e^{-2x}}{2}$
2. Write RHS as $2(\\frac{e^x + e^{-x}}{2})^2 - 1 = \\frac{2(e^{2x} + 2 + e^{-2x})}{4} - 1 = \\frac{e^{2x} + e^{-2x}}{2}$
3. Both sides equal, identity proved. Alternative: start from RHS and work to LHS.

**Mark scheme pattern:** M1 for correct exponential form or identity used, A1 for completing proof.

**Common traps:** Sign errors (cosh vs cos), forgetting $\\sinh 2x = 2\\sinh x\\cosh x$ has no sign change from trig.

## Type 2: Solving hyperbolic equations

**How to recognise it:** "Solve $\\cosh x - 3\\sinh x = 4$, giving your answer in logarithmic form."

**Standard method:**
1. Replace $\\cosh x = \\frac{e^x + e^{-x}}{2}$, $\\sinh x = \\frac{e^x - e^{-x}}{2}$
2. Multiply through by 2, collect terms in $e^x$ and $e^{-x}$
3. Multiply through by $e^x$ to get quadratic in $e^x$
4. Solve for $e^x$, take $\\ln$

**Mark scheme pattern:** M1 for exponential substitution, M1 for forming quadratic, A1 for correct $x$ in log form.

## Type 3: Inverse hyperbolic — logarithmic forms

**How to recognise it:** Express $\\sinh^{-1}(\\ldots)$ in terms of $\\ln$.

**Standard method:** Direct application of formulas:
$\\sinh^{-1} x = \\ln(x + \\sqrt{x^2+1})$, $\\cosh^{-1} x = \\ln(x + \\sqrt{x^2-1})$, $\\tanh^{-1} x = \\frac12\\ln\\frac{1+x}{1-x}$

## Type 4: Integration using hyperbolic substitution

**How to recognise it:** $\\int\\sqrt{x^2 + a^2}\\,dx$ or $\\int\\frac{dx}{\\sqrt{x^2 + a^2}}$.

**Standard method:** Substitute $x = a\\sinh u$, then $dx = a\\cosh u\\,du$, $\\sqrt{x^2 + a^2} = a\\cosh u$.
""",
    'matrices-fp2': """
## Type 1: $3\\times3$ linear systems

**How to recognise it:** "Show that the system has a unique solution" or "determine values of $k$ for consistency".

**Standard method:**
1. Write as $A\\mathbf{x} = \\mathbf{b}$
2. Compute $\\det A$
3. $\\det \\neq 0$ → unique solution (3 planes meet at a point)
4. $\\det = 0$ → check consistency by elimination

**MS pattern:** M1 for determinant, A1 for correct value, B1 for geometric interpretation.

## Type 2: Eigenvalues and eigenvectors

**How to recognise it:** "Find the eigenvalues and corresponding eigenvectors of $A$."

**Standard method:**
1. $\\det(A - \\lambda I) = 0$
2. For each $\\lambda$, solve $(A - \\lambda I)\\mathbf{e} = \\mathbf{0}$

## Type 3: Diagonalisation

**How to recognise it:** "Find $P$ and $D$ such that $A = PDP^{-1}$."

**Standard method:** $D = \\operatorname{diag}(\\lambda_i)$, $P = [\\mathbf{e}_1\\;\\mathbf{e}_2\\;\\mathbf{e}_3]$.

## Type 4: Cayley-Hamilton

**How to recognise it:** "Use the characteristic equation to find $A^{-1}$."

**Standard method:** If $p(\\lambda) = \\lambda^2 - 6\\lambda + 11$, then $A^2 - 6A + 11I = 0$, so $A^{-1} = \\frac{1}{11}(6I - A)$.
""",
    'differentiation': """
## Type 1: Differentiating inverse functions

**How to recognise it:** "Differentiate $\\sinh^{-1}(2x)$" or "find $\\frac{dy}{dx}$ where $y = \\cos^{-1}(x^2)$".

**Standard method:** Use the standard derivatives + chain rule.

## Type 2: Implicit differentiation

**How to recognise it:** Equation with $x$ and $y$ mixed. "Find $\\frac{dy}{dx}$ at the point $(1,1)$."

**Standard method:** Differentiate each term, use $\\frac{d}{dx}(y^n) = ny^{n-1}\\frac{dy}{dx}$.

## Type 3: Maclaurin series

**How to recognise it:** "Find the Maclaurin series for $f(x)$ up to $x^n$."

**Standard method:** Compute $f(0), f'(0), f''(0), \\ldots$, then $f(x) = \\sum \\frac{f^{(n)}(0)}{n!}x^n$.
""",
    'integration': """
## Type 1: Standard inverse integrals

**How to recognise it:** $\\int\\frac{dx}{\\sqrt{4-x^2}}$, $\\int\\frac{dx}{x^2+9}$, $\\int\\frac{dx}{\\sqrt{x^2+16}}$.

**Standard method:** Identify which inverse form, apply formula directly or after completing square.

## Type 2: Reduction formulae

**How to recognise it:** "Show that $I_n = \\frac{n-1}{n}I_{n-2}$" where $I_n = \\int_0^{\\pi/2}\\sin^n x\\,dx$.

**Standard method:** Integration by parts, relate $I_n$ to $I_{n-2}$.

## Type 3: Arc length

**How to recognise it:** "Find the length of the arc of $y = \\cosh x$ from $x=0$ to $x=a$."

**Standard method:** $s = \\int\\sqrt{1+(dy/dx)^2}\\,dx$, simplify the integrand.

## Type 4: Surface area

**How to recognise it:** "Find the area of the surface generated when the curve is rotated through $2\\pi$ radians about the $x$-axis."

**Standard method:** $S = 2\\pi\\int y\\sqrt{1+(dy/dx)^2}\\,dx$. Don't forget $2\\pi$!

## Type 5: Rectangle bounds for integrals

**How to recognise it:** Diagram with rectangles under/over a curve.

**Standard method:** Sum of rectangle areas → compare to integral → inequality.
""",
    'complex-numbers': """
## Type 1: de Moivre for multiple angles

**How to recognise it:** "Show that $\\cos 5\\theta = 16\\cos^5\\theta - 20\\cos^3\\theta + 5\\cos\\theta$."

**Standard method:** Expand $(\\cos\\theta + i\\sin\\theta)^n$, equate real/imaginary parts.

## Type 2: Power reduction

**How to recognise it:** "Express $\\sin^6\\theta$ in terms of cosines of multiples of $\\theta$."

**Standard method:** $\\sin\\theta = \\frac{z - z^{-1}}{2i}$, expand, write in terms of $\\cos n\\theta$.

## Type 3: $C + iS$ series summation

**How to recognise it:** "Sum $\\sum_{r=0}^{n-1} \\cos(2r+1)\\theta$."

**Standard method:** $C + iS = \\sum e^{i(2r+1)\\theta}$, sum GP, separate real/imaginary.

## Type 4: Roots of unity

**How to recognise it:** "Find the $6$th roots of $1$" or "solve $z^6 = 1$".

**Standard method:** $z_k = e^{2\\pi i k/6}$, $k = 0,1,\\ldots,5$.
""",
    'differential-equations': """
## Type 1: Integrating factor (1st order)

**How to recognise it:** $\\frac{dy}{dx} + P(x)y = Q(x)$.

**Standard method:** $\\mu = e^{\\int P\\,dx}$, $\\frac{d}{dx}(\\mu y) = \\mu Q$, integrate.

## Type 2: 2nd order — CF + PI

**How to recognise it:** $a\\frac{d^2y}{dx^2} + b\\frac{dy}{dx} + cy = f(x)$.

**Standard method:** Auxiliary equation → CF. Try PI based on $f(x)$. General solution = CF + PI.

## Type 3: Substitution

**How to recognise it:** "Use the substitution $x = e^t$" or "$z = x + y$".

**Standard method:** Differentiate the substitution, replace in DE, simplify.
""",
}


def fill_empty():
    """Fill all empty files with complete content."""
    filled = 0
    for topic_key, files in CONTENT.items():
        topic_dir = TOPICS / topic_key
        for fname, content in files.items():
            fpath = topic_dir / fname
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content.lstrip('\n'))
            filled += 1
            print(f"  FILLED: {topic_key}/{fname}")

    # Also fill question-types and mark-scheme-patterns if they're too thin
    for topic_key, extra in QT_EXTRA.items():
        fpath = TOPICS / topic_key / 'question-types.md'
        if fpath.exists():
            cur = open(fpath, 'r', encoding='utf-8').read()
            # Append extra content before closing
            if '### How to recognise it' not in cur or cur.count('###') < 3:
                new_content = cur.strip() + '\n\n' + extra.lstrip('\n')
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  ENRICHED: {topic_key}/question-types.md")

        # Fix mark-scheme-patterns
        fpath2 = TOPICS / topic_key / 'mark-scheme-patterns.md'
        if fpath2.exists():
            cur = open(fpath2, 'r', encoding='utf-8').read()
            if len(cur) < 300:
                new = f"""---
title: Mark Scheme Patterns
sidebar_position: 5
---

# Mark Scheme Patterns — {topic_key.replace('-',' ').title()}

## Command words used

- **Show that** — full algebraic derivation required, not just stating the result
- **Find** — obtain the answer with working
- **Solve** — find all solutions (complex included)
- **Sketch** — show key features (asymptotes, intercepts, turning points)
- **Hence** — must use previous part's result

## Common mark allocation

| Part | Marks | What's expected |
|------|-------|-----------------|
| (a) | 3-5 | Usually method (M1-2) + answer (A1) |
| (b) | 4-7 | Builds on (a), more method marks |
| (c) | 2-3 | Often answer only, using previous results |

## Efficiency tips

- Show every algebraic step — MS awards method marks even with arithmetic errors
- Write formulas before substituting numbers — this earns the M mark
- For "show that" questions, work backwards from the given answer if stuck
"""
                with open(fpath2, 'w', encoding='utf-8') as f:
                    f.write(new)
                print(f"  FIXED: {topic_key}/mark-scheme-patterns.md")

    # Fix common-mistakes if too thin
    for topic_key in CONTENT:
        fpath = TOPICS / topic_key / 'common-mistakes.md'
        if fpath.exists():
            cur = open(fpath, 'r', encoding='utf-8').read()
            if len(cur) < 300:
                mistakes_data = CONTENT.get(topic_key, {}).get('common-mistakes', '')
                if mistakes_data:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(mistakes_data)
                    print(f"  FIXED: {topic_key}/common-mistakes.md")

    print(f"\nTotal files filled/fixed: {filled}")


def check_all():
    """Final quality check — no file should be under 200 chars."""
    print("\n=== QUALITY CHECK ===")
    all_ok = True
    for f in TOPICS.rglob('*.md'):
        sz = f.stat().st_size
        if sz < 200:
            print(f"  STILL EMPTY: {f} ({sz} bytes)")
            all_ok = False
    # Check subject-level files too
    subj_dir = BASE / 'docs' / 'subjects' / '9231-further-mathematics'
    for f in subj_dir.rglob('*.md'):
        sz = f.stat().st_size
        if sz < 200:
            print(f"  STILL EMPTY: {f} ({sz} bytes)")
            all_ok = False
    if all_ok:
        print("  ALL FILES HAVE CONTENT ✓")
    return all_ok


if __name__ == '__main__':
    fill_empty()
    check_all()
