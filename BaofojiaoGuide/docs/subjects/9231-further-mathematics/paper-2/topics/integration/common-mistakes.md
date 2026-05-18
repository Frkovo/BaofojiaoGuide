---
title: 常见错误
sidebar_position: 6
---

# Common Mistakes — Integration

1. **Wrong inverse formula.** $\int\frac{dx}{\sqrt{a^2-x^2}}$ gives $\sin^{-1}$ but students use $\sinh^{-1}$. $\int\frac{dx}{\sqrt{x^2+a^2}}$ gives $\sinh^{-1}$ but students use $\cosh^{-1}$. Memorise the four forms.

2. **Missing $dx$ conversion in substitution.** If $x = \sinh u$, then $dx = \cosh u\,du$. Forgetting this changes the whole integral.

3. **Forgetting to change limits.** When substituting $u = g(x)$ in a definite integral, $x=a$ becomes $u=g(a)$, $x=b$ becomes $u=g(b)$.

4. **Arc length vs surface area.** Arc length: $\int\sqrt{1+(dy/dx)^2}\,dx$ (no extra factor). Surface area: $2\pi\int y\sqrt{1+(dy/dx)^2}\,dx$ (extra $2\pi y$). Don't mix them up.

5. **Reduction formula: sign errors.** Integration by parts: $[uv] - \int v\,du$. Watch the minus sign carefully.

6. **Reduction formula: wrong base case.** $I_0 = \int_0^{\pi/2} 1\,dx = \pi/2$, $I_1 = \int_0^{\pi/2} \sin x\,dx = 1$.
