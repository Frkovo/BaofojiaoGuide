---
title: 常见错误
sidebar_position: 6
---

# Common Mistakes — Differentiation

1. **Sign of $\frac{d}{dx}\cos^{-1}x$.** It's $-\frac{1}{\sqrt{1-x^2}}$, NOT $+\frac{1}{\sqrt{1-x^2}}$ (that's $\sin^{-1}x$). This is the most common sign error.

2. **$\frac{d}{dx}\tanh^{-1}x$ vs $\frac{d}{dx}\sinh^{-1}x$.** $\frac{d}{dx}\tanh^{-1}x = \frac{1}{1-x^2}$ (no square root!), while $\frac{d}{dx}\sinh^{-1}x = \frac{1}{\sqrt{1+x^2}}$.

3. **Implicit: forgetting the chain rule.** $\frac{d}{dx}(y^2) = 2y\frac{dy}{dx}$, NOT $2y$. Every $y$ term gets multiplied by $\frac{dy}{dx}$.

4. **Implicit: product rule on $xy$.** $\frac{d}{dx}(xy) = y + x\frac{dy}{dx}$ (derivative of $x$ times $y$, plus $x$ times derivative of $y$).

5. **Maclaurin: evaluating at $x$ instead of $0$.** You need $f(0)$, $f'(0)$, $f''(0)$, etc., not $f(x)$, $f'(x)$, $f''(x)$.

6. **Maclaurin: forgetting factorial denominators.** The $n$th term is $\frac{f^{(n)}(0)}{n!}x^n$.
