---
title: 常见错误
sidebar_position: 6
---

# Common Mistakes — Matrices (FP2)

1. **$\det A = 0$ does NOT mean inconsistent.** It means no *unique* solution. The system could still be consistent (infinitely many solutions) or inconsistent (no solutions). Always check by elimination.

2. **Mixing up eigenvector order.** The eigenvector for $\lambda_1$ must be the same column of $P$ as where $\lambda_1$ appears in $D$. If they're swapped, $A \neq PDP^{-1}$.

3. **Sign errors in $\det(A - \lambda I)$.** Remember: subtract $\lambda$ from the diagonal entries only, not from every entry.

4. **Writing $\det(\lambda I - A) = 0$ without adjusting signs.** If you use $\det(\lambda I - A)$, the polynomial differs by a factor of $(-1)^n$. Stick to $\det(A - \lambda I) = 0$.

5. **Forgetting the geometric interpretation.** Questions explicitly ask for it. Three possibilities: planes meet at a point, along a line, or have no common intersection.
