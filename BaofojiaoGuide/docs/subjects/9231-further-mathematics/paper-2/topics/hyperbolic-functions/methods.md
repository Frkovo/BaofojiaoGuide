---
title: 解题方法
sidebar_position: 4
---

# Methods — Hyperbolic Functions

## Proving identities

Write $\sinh x = \frac{e^x - e^{-x}}{2}$, $\cosh x = \frac{e^x + e^{-x}}{2}$
Key identity: $\cosh^2 x - \sinh^2 x \equiv 1$
Double angle: $\sinh 2x \equiv 2\sinh x\cosh x$, $\cosh 2x \equiv 2\cosh^2 x - 1 \equiv 2\sinh^2 x + 1$

## Solving hyperbolic equations

1. Replace $\cosh x$, $\sinh x$ with exponential forms
2. Multiply through to clear denominators
3. Solve quadratic in $e^x$
4. $x = \ln(\text{positive root})$

## Inverse hyperbolic logarithmic forms

$\sinh^{-1} x = \ln(x + \sqrt{x^2+1})$
$\cosh^{-1} x = \ln(x + \sqrt{x^2-1})$ ($x \ge 1$)
$\tanh^{-1} x = \frac12\ln\frac{1+x}{1-x}$ ($|x| < 1$)

## Hyperbolic substitution for integrals

$\sqrt{x^2 + a^2}$: try $x = a\sinh u$
$\sqrt{x^2 - a^2}$: try $x = a\cosh u$
Then $dx = a\cosh u\,du$, simplify using $\cosh^2 u - \sinh^2 u = 1$
