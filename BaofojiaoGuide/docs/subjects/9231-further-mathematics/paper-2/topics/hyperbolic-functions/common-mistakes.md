---
title: 常见错误
sidebar_position: 6
---

# Common Mistakes — Hyperbolic Functions

1. **Confusing $\cosh^2 x - \sinh^2 x \equiv 1$ with $\cos^2 x + \sin^2 x \equiv 1$.** The minus sign is the key difference — get it wrong and every identity proof fails.

2. **Domain errors on inverse hyperbolic.** $\cosh^{-1} x$ requires $x \ge 1$. $\tanh^{-1} x$ requires $|x| < 1$. If the input is outside these domains, the answer is not real.

3. **Sign errors in $\frac{d}{dx}\cosh x$.** $\frac{d}{dx}\cosh x = +\sinh x$ (NOT $-\sinh x$ which is the derivative of $\cos x$).

4. **Wrong logarithmic form for $\tanh^{-1} x$.** It's $\frac12\ln\frac{1+x}{1-x}$, NOT $\frac12\ln\frac{1-x}{1+x}$.

5. **Forgetting that $e^x > 0$.** When solving hyperbolic equations, you get a quadratic in $e^x$. One root may be negative — discard it.
