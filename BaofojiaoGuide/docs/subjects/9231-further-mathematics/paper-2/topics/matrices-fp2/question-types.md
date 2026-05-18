---
title: 题型分析
sidebar_position: 3
---

# 题型分析 — Matrices (Further Pure 2)

---

## Question Type 1: Solving $3\times3$ linear systems

### 如何识别

题目给出三个关于 $x,y,z$ 的方程，要求证明唯一解、判断一致性、或求参数范围。

**关键词：** system of equations, unique solution, consistent, inconsistent

:::note[标准解题方法]

1. 写成 $A\mathbf{x} = \mathbf{b}$ 形式
2. 计算 $\det A$（按行展开或 Sarrus 法则）
3. $\det \neq 0$：唯一解，三个平面交于一点
4. $\det = 0$：消元法检查
   - 出现矛盾（如 $0=5$）：**不一致**，无解
   - 出现依赖方程：**无限多解**，三个平面交于一条直线

:::

:::info[评分标准（MS 模式）]

- **M1**: 计算行列式（或消元）
- **A1**: 行列式值正确
- **B1**: 正确结论（唯一解 / 无唯一解）
- **B1**: 正确的几何解释

:::

### 完整原题

**Example 1 — 9231/s21/qp/22 Q1 (4 marks):**

> (a) Given that $a$ is an integer, show that the system of equations
> $$ax + 3y + z = 14$$
> $$2x + y + 3z = 0$$
> $$-x + 2y - 5z = 17$$
> has a unique solution and interpret this situation geometrically.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: determinant $= -2a + 30$
- **A1**: $\det \neq 0$ for integer $a$
- **B1**: unique solution
- **B1**: three planes intersect at a single point

</details>

**Example 2 — 9231/w22/qp/22 Q1 (3 marks):**

> (a) Find the set of values of $k$ for which the system of equations
> $$x + 2y + 3z = 1$$
> $$kx + 4y + 6z = 0$$
> $$7x + 8y + 9z = 3$$
> has a unique solution.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: forms determinant
- **M1**: $\det = 12 - 6k$
- **A1**: $k \neq 2$

</details>

**Example 3 — 9231/s23/qp/22 Q1 (5 marks):**

> (a) Show that the system of equations
> $$x + 2y + 3z = 1$$
> $$4x + 5y + 6z = 1$$
> $$7x + 8y + 9z = 1$$
> does not have a unique solution.
>
> (b) Show that the system of equations in part (a) is consistent. Interpret this situation geometrically.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- (a) **M1**: $\det = 0$，**A1**: shown
- (b) **M1**: eliminates to show consistency
- **A1**: three planes intersect in a line
- **B1**: correct geometric description

</details>

:::warning[常见陷阱]

- $\det = 0$ **不等于** inconsistent！只是无唯一解，可能无限多解
- 行列式展开的符号错误——Sarrus 法则仔细做
- 忘记写几何解释——题目明确要求

:::

---

## Question Type 2: Geometric interpretation of planes

### 三种情况

- $\det \neq 0$：**three planes intersect at a single point**
- $\det = 0$ 且一致：**three planes intersect in a line**
- $\det = 0$ 且不一致：**no common point of intersection**

---

## Question Type 3: Finding eigenvalues and eigenvectors

### 如何识别

"Find the eigenvalues and corresponding eigenvectors of the matrix $A$."

:::note[标准解题方法]

1. 写出 $A - \lambda I$（对角线减 $\lambda$）
2. $\det(A - \lambda I) = 0$ → 特征方程
3. 展开行列式得到 $\lambda$ 的多项式并因式分解
4. 解出特征值 $\lambda_1, \lambda_2, \lambda_3$
5. 对每个 $\lambda_i$，解 $(A - \lambda_i I)\mathbf{e} = \mathbf{0}$ 得特征向量

:::

### 完整原题

**Example 1 — 9231/s20/qp/22 Q8 (14 marks total):**

> The matrix $A$ is given by
> $$A = \begin{pmatrix} 3 & 1 & 1 \\ 0 & 6 & -1 \\ 0 & 0 & -2 \end{pmatrix}$$
>
> (a) Find the values of $a$ for which the system of equations
> $$3x + y + z = 0,\; ax + 6y - z = 0,\; ay - 2z = 0$$
> does not have a unique solution. [3]
>
> (b) Use the characteristic equation of $A$ to find the inverse of $A^2$. [4]
>
> (c) Find a matrix $P$ and a diagonal matrix $D$ such that $A^5 = PD^5P^{-1}$. [7]

<details>
<summary>📝 MS 展开查看</summary>

**MS (c):**
- **B1**: eigenvalues are $3,6,-2$
- **M1**: attempts eigenvectors for each $\lambda$
- **A1**: eigenvectors correct for $\lambda=3$
- **A1**: eigenvectors correct for $\lambda=6,-2$
- **M1**: forms $P$ and $D$
- **A1**: $P$ and $D$ correct

</details>

**Example 2 — 9231/s23/qp/22 Q5 (10 marks):**

> The matrix $A$ is given by
> $$A = \begin{pmatrix} 18 & 5 & -11 \\ 8 & 6 & -4 \\ 32 & 10 & -20 \end{pmatrix}$$
>
> (a) Show that the characteristic equation of $A$ is $\lambda^3 - 4\lambda^2 - 2\lambda + 20 = 0$. [4]
>
> (b) Find a matrix $P$ and a diagonal matrix $D$ such that $A^5 = PD^5P^{-1}$. [6]

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **M1**: $\det(A-\lambda I)=0$ set up
- **M1**: expands determinant
- **M1**: simplifies to cubic
- **A1**: AG

**MS (b):**
- **B1**: eigenvalues $\lambda = 4,2,-2$
- **M1**: eigenvectors for each $\lambda$
- **A1**: eigenvectors correct
- **M1**: forms $P$ and $D$
- **A1**: $P$ and $D$ correct

</details>

**Example 3 — 9231/w23/qp/22 Q6 (6 marks):**

> The matrix $P$ is given by
> $$P = \begin{pmatrix} 1 & -1 & 1 \\ 0 & 2 & 1 \\ 0 & 0 & -1 \end{pmatrix}$$
>
> (a) State the eigenvalues of $P$. [1]
>
> (b) Use the characteristic equation of $P$ to find $P^{-1}$. [5]

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **B1**: $\lambda = 1,2,-1$

**MS (b):**
- **B1**: $(\lambda-1)(\lambda-2)(\lambda+1)=0 \to \lambda^3-2\lambda^2-\lambda+2=0$
- **M1**: $P^3-2P^2-P+2I=0$
- **M1**: rearrange to $P(P^2-2P-I) = -2I$
- **A1**: $P^{-1} = \frac12(-P^2+2P+I)$
- **A1**: $P^{-1} = \frac12\begin{pmatrix}1&1&-1\\0&0&1\\0&0&2\end{pmatrix}$

</details>

---

## Question Type 4: Matrix diagonalisation $A = PDP^{-1}$

### 如何识别

"Find a matrix $P$ and a diagonal matrix $D$ such that $A^5 = PD^5P^{-1}$."

:::note[标准解题方法]

1. 求出所有特征值和特征向量
2. $D = \operatorname{diag}(\lambda_1, \lambda_2, \lambda_3)$（特征值在对角线）
3. $P = [\mathbf{e}_1\; \mathbf{e}_2\; \mathbf{e}_3]$（特征向量按列排，顺序与 $D$ 一致）
4. $A^n = PD^nP^{-1}$

:::

:::warning[常见陷阱]

特征向量的列序**必须**与特征值在对角阵中的位置一致！

:::

---

## Question Type 5: Matrix powers $A^n$

:::note[标准方法]

$$A^n = (PDP^{-1})^n = PD^nP^{-1}$$

$$D^n = \operatorname{diag}(\lambda_1^n, \lambda_2^n, \lambda_3^n)$$

:::

---

## Question Type 6: Cayley–Hamilton theorem applications

### 如何识别

"Use the characteristic equation of $A$ to find $A^{-1}$"

:::note[标准方法]

若特征方程为 $p(\lambda)=0$，则 $p(A)=0$。

**举例：**
$\det(A-\lambda I) = -\lambda^3 + 7\lambda^2 - 36 = 0$
则 $-A^3 + 7A^2 - 36I = 0$
两边乘 $A^{-1}$：$-A^2 + 7A - 36A^{-1} = 0$
$A^{-1} = \dfrac{1}{36}(7A - A^2)$

:::

### 完整原题

**Example 1 — 9231/s20/qp/22 Q8(b):**

> Use the characteristic equation of $A = \begin{pmatrix}3&1&1\\0&6&-1\\0&0&-2\end{pmatrix}$ to find the inverse of $A^2$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: $(\lambda-3)(\lambda-6)(\lambda+2) = \lambda^3 - 7\lambda^2 + 36 = 0$
- **M1**: $36I = 7A^2 - A^3 \to 36(A^{-1})^2 = 7I - A$
- **M1**: rearranges correctly
- **A1**: $(A^{-1})^2 = \dfrac{1}{36}\begin{pmatrix}4&-1&-1\\0&1&1\\0&0&9\end{pmatrix}$

</details>

**Example 2 — 9231/w23/qp/22 Q6(b) (5 marks):**

> Use the characteristic equation of $P = \begin{pmatrix}1&-1&1\\0&2&1\\0&0&-1\end{pmatrix}$ to find $P^{-1}$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: $(\lambda-1)(\lambda-2)(\lambda+1) = \lambda^3 - 2\lambda^2 - \lambda + 2 = 0$
- **M1**: $P^3 - 2P^2 - P + 2I = 0$
- **M1**: rearranges to $-P^2 + 2P + I = 2P^{-1}$
- **A1**: $P^{-1} = \frac12\begin{pmatrix}1&1&-1\\0&0&1\\0&0&2\end{pmatrix}$

</details>

:::tip[注意]

Types 4（对角化）和 Type 5（矩阵幂）的例题已包含在 Type 3 的 Example 1 和 Example 2 中——它们都要求求出 $P$ 和 $D$ 使得 $A^5 = PD^5P^{-1}$，这同时涵盖了对角化和矩阵幂的考点。

:::
