---
title: 考前速查
sidebar_position: 7
---

# Last-Minute Summary — Differential Equations

## 1st order
$\\frac{dy}{dx} + Py = Q$ → IF $\\mu = e^{\\int P\\,dx}$
$\\frac{d}{dx}(\\mu y) = \\mu Q$ → $\\mu y = \\int \\mu Q\\,dx + C$

Sign of $P$ is critical! E.g. $\\frac{dy}{dx} - \\frac{2}{x}y = x$ gives $P = -\\frac{2}{x}$, $\\mu = x^{-2}$.

## 2nd order constant coefficients
Auxiliary equation: $am^2 + bm + c = 0$

| Roots | CF form |
|-------|---------|
| Real distinct $m_1,m_2$ | $Ae^{m_1x} + Be^{m_2x}$ |
| Repeated $m$ | $(A + Bx)e^{mx}$ |
| Complex $\\alpha \\pm i\\beta$ | $e^{\\alpha x}(A\\cos\\beta x + B\\sin\\beta x)$ |

PI: try form matching RHS. If overlap with CF → multiply by $x$ or $x^2$.

Apply ICs after combining CF + PI, not before.
