---
title: Matrices - Question Types
sidebar_position: 2
---

# Matrices 题型分析

---

## Question Type 1: 特征值与特征向量

**分值范围**：2–5 分

**考点**：求 $2 \times 2$ 或 $3 \times 3$ 矩阵的特征值与特征向量。

**解题步骤**：

1. 写出特征方程 $\det(A - \lambda I) = 0$
2. 展开行列式得到关于 $\lambda$ 的多项式
3. 解多项式得到特征值 $\lambda_1, \lambda_2, \dots$
4. 对每个 $\lambda_i$ 解 $(A - \lambda_i I)\mathbf{v} = \mathbf{0}$ 得到特征向量

---

### Example 1: s20/23 Q3 — 特征值与 $A^{-1}$

> The matrix $A = \begin{pmatrix} 5 & 2 \\ 3 & 4 \end{pmatrix}$.
>
> (a) Find the eigenvalues of $A$. [2]
>
> (b) Show that $A$ satisfies its own characteristic equation, and hence find $A^{-1}$. [4]

**解法**：

(a) 特征方程：
$$
\det(A - \lambda I) = \begin{vmatrix} 5-\lambda & 2 \\ 3 & 4-\lambda \end{vmatrix} = (5-\lambda)(4-\lambda) - 6 = 0
$$
$$
\lambda^2 - 9\lambda + 14 = 0 \Rightarrow (\lambda - 2)(\lambda - 7) = 0
$$
所以 $\lambda = 2, 7$。

(b) Cayley-Hamilton：$A^2 - 9A + 14I = 0$，即
$$
A^2 - 9A = -14I \Rightarrow A^{-1} = -\frac{1}{14}(A - 9I) = \frac{1}{14}\begin{pmatrix} -4 & 2 \\ 3 & -5 \end{pmatrix}
$$

<details>
<summary>📝 MS 展开查看</summary>

- **(a)**
  - **B1** 写出特征方程 $\det(A - \lambda I) = 0$
  - **B1** 得到特征值 $\lambda = 2, 7$
- **(b)**
  - **M1** 写出特征方程并代入 $A$
  - **A1** 正确得到 $A^2 - 9A + 14I = 0$
  - **M1** 等式变形求 $A^{-1}$
  - **A1** 正确得到 $A^{-1}$

</details>

---

### Example 2: w20/22 Q9 — 综合题

> The matrix $A = \begin{pmatrix} a & 3 & 1 \\ -1 & 2 & 1 \\ 1 & 0 & 1 \end{pmatrix}$.
>
> (a) Find the characteristic equation of $A$. [3]
>
> (b) Given that $\lambda_1 = 2$ is an eigenvalue, find the value of $a$, and find the other two eigenvalues. [2]

**解法**：

(a) $\det(A - \lambda I) = \begin{vmatrix} a-\lambda & 3 & 1 \\ -1 & 2-\lambda & 1 \\ 1 & 0 & 1-\lambda \end{vmatrix} = 0$

展开得：$(a-\lambda)[(2-\lambda)(1-\lambda)] - 3[-1(1-\lambda) - 1] + 1[0 - (2-\lambda)] = 0$

(b) 代入 $\lambda = 2$：
$$
\det(A - 2I) = \begin{vmatrix} a-2 & 3 & 1 \\ -1 & 0 & 1 \\ 1 & 0 & -1 \end{vmatrix} = (a-2)(0) - 3(1-1) + 1(0) = 0
$$
对所有 $a$ 成立，故需要重新计算特征方程。

<details>
<summary>📝 MS 展开查看</summary>

- **(a)**
  - **M1** 正确写出 $\det(A - \lambda I)$
  - **M1** 展开行列式
  - **A1** 得到特征方程
- **(b)**
  - **M1** 代入 $\lambda = 2$ 到特征方程
  - **A1** 求出 $a$ 和另两个特征值

</details>

---

### Example 3: s21/21 Q6 — 特征值与高次幂

> The matrix $P$ has eigenvalues $2$ and $3$.
>
> (b) Use the characteristic equation of $P$ to find $P^3$ in terms of $P$ and $I$. [4]

**解法**：

特征方程为 $(\lambda - 2)(\lambda - 3) = \lambda^2 - 5\lambda + 6 = 0$

由 Cayley-Hamilton：$P^2 = 5P - 6I$

则 $P^3 = P \cdot P^2 = P(5P - 6I) = 5P^2 - 6P = 5(5P - 6I) - 6P = 19P - 30I$

<details>
<summary>📝 MS 展开查看</summary>

- **M1** 写出特征方程
- **M1** 代入 $P$ 得 $P^2 = 5P - 6I$
- **M1** 用 $P^2$ 表达式计算 $P^3$
- **A1** 正确得到 $P^3 = 19P - 30I$

</details>

---

## Question Type 2: 特征方程 / Cayley-Hamilton 定理

**分值范围**：3–6 分

**考点**：利用 Cayley-Hamilton 定理求 $A^{-1}$、$(A^{-1})^2$ 或化简矩阵多项式。

**解题思路**：

- 先求特征方程 $\det(A - \lambda I) = 0$
- 代入 $A$ 得矩阵方程
- 移项求 $A^{-1}$：将常数项移到一边，两边同乘 $A^{-1}$
- 求 $(A^{-1})^2$：先将 $A^{-1}$ 用 $A$ 表示，再平方

---

### Example 1: s20/21 Q8(b) — 用特征方程求 $A^{-1}$

> The matrix $A = \begin{pmatrix} 1 & 2 & a \\ 2 & 1 & 2 \\ 1 & 1 & 1 \end{pmatrix}$.
>
> (b) Given that $a = 3$, find the characteristic equation of $A$. Hence find $A^{-1}$. [4]

<details>
<summary>📝 MS 展开查看</summary>

- **M1** 正确写出 $\det(A - \lambda I)$
- **A1** 得到特征方程
- **M1** 代入 $A$ 并变形
- **A1** 正确得到 $A^{-1}$

</details>

---

### Example 2: s25/21 Q8(d) — 化简 $(A-2I)^3$

> (d) For a $3 \times 3$ matrix $A$ with characteristic equation $\lambda^3 - 6\lambda^2 + 11\lambda - 6 = 0$, express $(A-2I)^3$ in terms of $A^2$, $A$, $I$. [3]

**解法**：

由 Cayley-Hamilton：$A^3 - 6A^2 + 11A - 6I = 0$

展开 $(A-2I)^3 = A^3 - 6A^2 + 12A - 8I$

代入 $A^3 = 6A^2 - 11A + 6I$：
$$
(A-2I)^3 = (6A^2 - 11A + 6I) - 6A^2 + 12A - 8I = A - 2I
$$

<details>
<summary>📝 MS 展开查看</summary>

- **M1** 展开 $(A-2I)^3$
- **M1** 代入 $A^3$ 的 Cayley-Hamilton 表达式
- **A1** 正确化简为 $A - 2I$

</details>

---

## Question Type 3: 对角化 / 矩阵高次幂

**分值范围**：5–7 分

**考点**：构造 $P$ 和 $D$ 使得 $A = PDP^{-1}$，进而求 $A^n$。

**解题步骤**：

1. 求特征值 $\lambda_1, \lambda_2, \dots$
2. 求对应的特征向量 $\mathbf{v}_1, \mathbf{v}_2, \dots$
3. 构造 $P = (\mathbf{v}_1 \; \mathbf{v}_2)$，$D = \operatorname{diag}(\lambda_1, \lambda_2)$
4. 计算 $P^{-1}$（$2 \times 2$ 直接用公式）
5. $A^n = PD^nP^{-1}$

---

### Example 1: s20/21 Q8(c) — $A^5 = PDP^{-1}$

> The matrix $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 2 \\ 1 & 1 & 1 \end{pmatrix}$.
>
> (c) Find matrices $P$ and $D$ such that $A^5 = PDP^{-1}$. [7]

**解法**：

先求 $A$ 的特征值和特征向量，构造 $P$ 和 $D$，则 $A^5 = PD^5P^{-1}$。

$D = \begin{pmatrix} \lambda_1^5 & 0 & 0 \\ 0 & \lambda_2^5 & 0 \\ 0 & 0 & \lambda_3^5 \end{pmatrix}$

<details>
<summary>📝 MS 展开查看</summary>

- **B1** 求出一个特征值
- **B1** 求出全部特征值
- **M1** 求特征向量
- **A1** 正确得到特征向量
- **A1** 正确构造 $P$
- **A1** 正确构造 $D$（含 $5$ 次幂）
- **B1** 指出 $A^5 = PD^5P^{-1}$

</details>

---

### Example 2: s24/21 Q9 — $(14A+24I)^2 = PDP^{-1}$

> (a) Find a matrix $P$ and a diagonal matrix $D$ such that $(14A+24I)^2 = PDP^{-1}$. [7]

**解法**：

1. 先求 $A$ 的特征值 $\lambda$
2. $(14A+24I)^2$ 的特征值为 $(14\lambda+24)^2$
3. 特征向量与 $A$ 相同
4. $D = \operatorname{diag}\big((14\lambda_1+24)^2, (14\lambda_2+24)^2, (14\lambda_3+24)^2\big)$

<details>
<summary>📝 MS 展开查看</summary>

- **B1** 求 $A$ 的特征值
- **M1** 认识到特征向量不变
- **M1** 正确计算新特征值 $(14\lambda+24)^2$
- **A1** 正确得到 $D$
- **A1** 正确得到 $P$
- **A1** 正确得到 $P^{-1}$
- **A1** 完成

</details>

---

### Example 3: w20/22 Q9 — 对角化与 $A^{-1}$

综合题：包含特征方程、对角化、求逆矩阵。

<details>
<summary>📝 MS 展开查看</summary>

- **M1** 求特征值
- **M1** 求特征向量
- **M1** 构造 $P$ 和 $D$
- **A1** 正确得到 $A = PDP^{-1}$
- **M1** 利用 $A^{-1} = PD^{-1}P^{-1}$ 求逆
- **A1** 正确得到 $A^{-1}$

</details>
