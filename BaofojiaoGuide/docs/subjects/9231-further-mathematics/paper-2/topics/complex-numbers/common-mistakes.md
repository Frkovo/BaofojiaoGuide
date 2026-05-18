---
title: 常见错误
sidebar_position: 6
---

# Common Mistakes — Complex Numbers

1. **Conjugate root theorem.** Non-real roots of real polynomials come in conjugate pairs. If $a+bi$ is a root, so is $a-bi$.

2. **Sign errors in binomial expansion of $(\cos\theta + i\sin\theta)^n$.** Remember $i^2 = -1$, $i^3 = -i$, $i^4 = 1$. Check the sign of every term.

3. **$z^n + z^{-n}$ vs $z^n - z^{-n}$.** $z^n + z^{-n} = 2\cos n\theta$ (real). $z^n - z^{-n} = 2i\sin n\theta$ (imaginary). Don't swap them.

4. **Roots of unity: wrong range.** $z^n = 1$ gives roots for $k = 0,1,\ldots,n-1$. Using $k = 1,\ldots,n$ is also fine, but $k=0$ is included.

5. **$C + iS$: forgetting to sum the GP.** The whole method depends on recognising $C+iS = \sum e^{i(\ldots)}$ as a geometric series. Don't try to sum cos and sin individually.

6. **Missing the "hence" connection.** If part (c) says "hence", you MUST use the result from part (b). Solving from scratch gets 0 marks.
