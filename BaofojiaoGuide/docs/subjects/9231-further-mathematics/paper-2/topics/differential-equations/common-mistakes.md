---
title: 常见错误
sidebar_position: 6
---

# Common Mistakes — Differential Equations

1. **Wrong sign of $P$ in integrating factor.** For $\frac{dy}{dx} + Py = Q$, the IF is $\mu = e^{\int P\,dx}$. If the DE is $\frac{dy}{dx} - \frac{2}{x}y = x$, then $P = -\frac{2}{x}$, NOT $+\frac{2}{x}$.

2. **Applying initial conditions too early.** You must find the general solution (CF + PI) FIRST, then substitute $x$ and $y$ to find the constants. Don't apply ICs to CF alone.

3. **PI overlap with CF.** If the RHS matches a term in CF, the standard PI won't work. Multiply by $x$ (or $x^2$ for double roots).

4. **Complex roots: wrong CF form.** For $m = \alpha \pm i\beta$, CF is $e^{\alpha x}(A\cos\beta x + B\sin\beta x)$, NOT $e^{\alpha x}(\cos\beta x + \sin\beta x)$. You need the arbitrary constants $A$ and $B$.

5. **Repeated root: wrong CF form.** For repeated root $m$, CF is $(A+Bx)e^{mx}$, NOT $Ae^{mx} + Be^{mx}$ (these are not independent).

6. **Forgetting to divide through first.** If the DE is $x\frac{dy}{dx} + 2y = e^x$, divide by $x$ before finding the IF.
