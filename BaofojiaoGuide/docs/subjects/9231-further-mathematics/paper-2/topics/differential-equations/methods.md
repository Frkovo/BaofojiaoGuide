---
title: 解题方法
sidebar_position: 4
---

# Methods — Differential Equations

## 1st order — Integrating factor

$$\frac{dy}{dx} + P(x)y = Q(x) \quad\Rightarrow\quad \mu = e^{\int P\,dx}$$
$$\frac{d}{dx}(\mu y) = \mu Q \quad\Rightarrow\quad \mu y = \int \mu Q\,dx + C$$

**Check the sign of $P$!** E.g. $\frac{dy}{dx} - \frac{2}{x}y = x$ → $P = -\frac{2}{x}$, $\mu = x^{-2}$.

## 2nd order constant coefficients

Auxiliary equation: $am^2 + bm + c = 0$

| Roots | CF form |
|-------|---------|
| Real distinct $m_1,m_2$ | $Ae^{m_1x} + Be^{m_2x}$ |
| Repeated $m$ | $(A+Bx)e^{mx}$ |
| Complex $\alpha \pm i\beta$ | $e^{\alpha x}(A\cos\beta x + B\sin\beta x)$ |

## Particular integral

| RHS $f(x)$ | Try PI |
|------------|--------|
| Constant $k$ | $y = c$ |
| $e^{ax}$ | $y = pe^{ax}$ |
| $\cos\omega x$, $\sin\omega x$ | $y = p\cos\omega x + q\sin\omega x$ |
| Polynomial | Same degree polynomial |

**Overlap:** if PI matches CF, multiply by $x$ (or $x^2$ for double root).

## Substitutions

- $x = e^t$: Euler-type → constant coefficient
- $z = x + y$: some 1st order → separable

**Apply initial conditions after** CF + PI are combined, not before.
