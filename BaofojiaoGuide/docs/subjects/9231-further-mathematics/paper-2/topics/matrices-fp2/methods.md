---
title: 解题方法
sidebar_position: 4
---

# Methods — Matrices (Further Pure 2)

## Solving $3\times3$ systems

1. Write as $A\mathbf{x} = \mathbf{b}$
2. Compute $\det A$
3. $\det \neq 0$ → unique solution (3 planes meet at a point)
4. $\det = 0$ → check consistency by elimination

## Eigenvalues and eigenvectors

1. Characteristic equation: $\det(A - \lambda I) = 0$
2. Solve for $\lambda$ (eigenvalues)
3. For each $\lambda$, solve $(A - \lambda I)\mathbf{e} = \mathbf{0}$ for eigenvector $\mathbf{e}$

## Diagonalisation

$A = PDP^{-1}$ where $D = \operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)$ and $P = [\mathbf{e}_1\;\mathbf{e}_2\;\mathbf{e}_3]$
Then $A^n = PD^nP^{-1}$

## Cayley–Hamilton theorem

$A$ satisfies its own characteristic equation $p(A) = 0$.
E.g. if $p(\lambda) = \lambda^2 - 6\lambda + 11$, then $A^2 - 6A + 11I = 0$, so $A^{-1} = \frac{1}{11}(6I - A)$.
