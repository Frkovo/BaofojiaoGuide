---
title: Systems of Linear Equations - Question Types
sidebar_position: 2
---

# Systems of Linear Equations 题型分析

---

## Question Type 1: 行列式条件

**分值范围**：2–5 分

**考点**：求参数使得方程组无唯一解（$\det A = 0$），或唯一解（$\det A \neq 0$）。

---

### Example 1: w20/21 Q3 — 三参数讨论

> The system of equations
> $$
> \begin{cases}
> x - 2y - 4z = 1 \\
> x - 2y + kz = 1 \\
> -x + 2y + 2z = 1
> \end{cases}
> $$
>
> (a) Show that this system does not have a unique solution. [2]

**解法**：

系数矩阵 $A = \begin{pmatrix} 1 & -2 & -4 \\ 1 & -2 & k \\ -1 & 2 & 2 \end{pmatrix}$

计算 $\det A$：
$$
\det A = 1\begin{vmatrix} -2 & k \\ 2 & 2 \end{vmatrix} - (-2)\begin{vmatrix} 1 & k \\ -1 & 2 \end{vmatrix} + (-4)\begin{vmatrix} 1 & -2 \\ -1 & 2 \end{vmatrix}
$$
$$
= 1(-4-2k) + 2(2+k) - 4(2-2) = -4-2k+4+2k-0 = 0
$$

$\det A = 0$，故无唯一解。

<details>
<summary>📝 MS 展开查看</summary>

- **M1** 正确计算 $\det A$
- **A1** 得出 $\det A = 0$ 并说明无唯一解

</details>

---

### Example 2: s20/21 Q8(a) — 参数 $a$

> The system
> $$
> \begin{cases}
> 3x + y + z = 0 \\
> x + y + 2z = 0 \\
> 2x + y + az = 0
> \end{cases}
> $$
> (a) Find the values of $a$ for which the system does not have a unique solution. [3]

**解法**：

系数矩阵 $A = \begin{pmatrix} 3 & 1 & 1 \\ 1 & 1 & 2 \\ 2 & 1 & a \end{pmatrix}$

$$
\det A = 3\begin{vmatrix} 1 & 2 \\ 1 & a \end{vmatrix} - 1\begin{vmatrix} 1 & 2 \\ 2 & a \end{vmatrix} + 1\begin{vmatrix} 1 & 1 \\ 2 & 1 \end{vmatrix}
$$
$$
= 3(a-2) - (a-4) + (1-2) = 3a-6-a+4-1 = 2a-3
$$

$\det A = 0 \Rightarrow 2a-3 = 0 \Rightarrow a = \frac{3}{2}$。

当 $a = \frac{3}{2}$ 时，方程组无唯一解。

<details>
<summary>📝 MS 展开查看</summary>

- **M1** 正确写出行列式
- **M1** 展开并化简
- **A1** $a = \frac{3}{2}$

</details>

---

### Example 3: s21/21 Q1 — 参数 $a$ 的方程组

> The system
> $$
> \begin{cases}
> x + y - z = 1 \\
> 2x + y + az = 1 \\
> x - y + 2z = 0
> \end{cases}
> $$
> (a) Find the set of values of $a$ for which the system has a unique solution. [4]
> (b) For the case where the system does not have a unique solution, find the solution set. [1]

**解法**：

(a) $\det A = \begin{vmatrix} 1 & 1 & -1 \\ 2 & 1 & a \\ 1 & -1 & 2 \end{vmatrix} = 1(2+a) - 1(4-a) + (-1)(-2-1) = 2+a-4+a+3 = 2a+1$

$\det A \neq 0 \Rightarrow 2a+1 \neq 0 \Rightarrow a \neq -\frac{1}{2}$

(b) $a = -\frac{1}{2}$ 时，用行变换求解。

<details>
<summary>📝 MS 展开查看</summary>

- **(a)**
  - **M1** 正确写出 $\det A$
  - **M1** 展开行列式
  - **A1** 化简到 $2a+1$
  - **A1** $a \neq -\frac{1}{2}$
- **(b)**
  - **M1** 代入 $a$ 并求解
  - **A1** 解集正确

</details>

---

## Question Type 2: 相容性与不相容性

**分值范围**：3–4 分

**考点**：当 $\det A = 0$ 时，判断方程组是矛盾（无解）还是相容（无穷多解）。

**方法**：用增广矩阵行变换（Gaussian elimination）检查是否有矛盾方程 $0 = c$（$c \neq 0$）。

---

### Example 1: w20/21 Q3(b)(c) — $k = -4$ 相容，$k = -2$ 矛盾

> (b) When $k = -4$, the equations are consistent. Interpret this situation geometrically. [3]
> (c) When $k = -2$, the equations are inconsistent. Interpret this situation geometrically. [2]

**解法**：

(b) $k = -4$ 时方程组相容，有无穷多解。三个平面交于一条直线。

(c) $k = -2$ 时方程组矛盾（无解）。三个平面没有公共交点，形成三棱柱形态。

<details>
<summary>📝 MS 展开查看</summary>

- **(b)**
  - **B1** 指出相容/无穷多解
  - **B1** 三个平面交于一条直线
  - **B1** 正确描述几何关系
- **(c)**
  - **B1** 指出矛盾/无解
  - **B1** 三个平面形成三棱柱

</details>

---

### Example 2: w23/21 Q1 — 参数 $k$

> The system
> $$
> \begin{cases}
> x + y + z = 2 \\
> 2x + y - z = 3 \\
> 2x + 3y + kz = 4
> \end{cases}
> $$
> (a) Find the value of $k$ for which the system is inconsistent. [4]

**解法**：

增广矩阵行变换：
$$
\left(\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 2 & 1 & -1 & 3 \\ 2 & 3 & k & 4 \end{array}\right)
$$

得 $k = 5$ 时出现矛盾方程。

<details>
<summary>📝 MS 展开查看</summary>

- **M1** 写出增广矩阵
- **M1** 正确行变换
- **M1** 得到参数条件
- **A1** $k = 5$

</details>

---

## Question Type 3: 几何解释

**分值范围**：2–3 分

**考点**：将方程组的代数结果用几何语言描述。

**常见情形**：

| 代数结果 | 几何解释 |
|----------|----------|
| $\det A \neq 0$，唯一解 | 三个平面交于一点 |
| $\det A = 0$，相容（无穷多解） | 三个平面交于一条直线（或一个平面） |
| $\det A = 0$，矛盾（无解） | 三个平面没有公共交点（三棱柱或两平面平行） |

---

### Example 1: w20/21 Q3(d) — 三棱柱（triangular prism）

> (d) When $k \neq -2$ and $k \neq -4$, the equations are inconsistent and the planes form a triangular prism. Explain what is meant by a triangular prism. [2]

**解答**：三个平面两两相交，交线互相平行。三条交线形成一个三棱柱状的形状，但没有三个平面共同的交点。

<details>
<summary>📝 MS 展开查看</summary>

- **B1** 三个平面两两相交
- **B1** 交线互相平行，形成三棱柱

</details>

---

### Example 2: w22/22 Q1 — 三个方程

> The system
> $$
> \begin{cases}
> x + 2y - z = 3 \\
> 2x - y + 2z = 1 \\
> 3x + y + kz = 2
> \end{cases}
> $$
> (a) Find the value of $k$ for which the system has no unique solution. [3]
> (b) For this value of $k$, determine whether the system is consistent or inconsistent. [2]

**解法**：

(a) $\det A = 0 \Rightarrow k = -3$

(b) 代入 $k = -3$ 行变换，检查是否矛盾。

<details>
<summary>📝 MS 展开查看</summary>

- **M1** 计算 $\det A$
- **A1** $k = -3$
- **M1** 增广矩阵行变换
- **A1** 判断相容/矛盾

</details>
