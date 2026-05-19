---
title: Matrices
sidebar_position: 1
---

# Matrices（矩阵）

---

## 考纲要求

1. 理解特征值（eigenvalues）和特征向量（eigenvectors）的定义与计算
2. 掌握特征方程（characteristic equation）：$\det(A - \lambda I) = 0$
3. 理解 Cayley-Hamilton 定理：$A$ 满足其自身的特征方程
4. 能利用 Cayley-Hamilton 定理求 $A^{-1}$、$A^n$ 以及多项式表达式
5. 掌握对角化（diagonalization）：$A = PDP^{-1}$，其中 $D$ 为特征值对角矩阵，$P$ 为特征向量矩阵
6. 能利用 $A^n = PD^nP^{-1}$ 计算矩阵的高次幂
7. 理解相似矩阵（similar matrices）的概念

---

## 常见题型

| 题型 | 分值 | 链接 |
|------|------|------|
| 特征值与特征向量 | 2–5 分 | [题型 1](./question-types.md#question-type-1-特征值与特征向量) |
| 特征方程 / Cayley-Hamilton 定理 | 3–6 分 | [题型 2](./question-types.md#question-type-2-特征方程--cayley-hamilton-定理) |
| 对角化 / 矩阵高次幂（$A^n = PD^nP^{-1}$） | 5–7 分 | [题型 3](./question-types.md#question-type-3-对角化--矩阵高次幂) |

---

## 核心公式

### 特征值与特征向量

$$
\det(A - \lambda I) = 0
$$

$$
(A - \lambda I)\mathbf{v} = \mathbf{0}
$$

### Cayley-Hamilton 定理

若特征方程为 $\lambda^n + a_{n-1}\lambda^{n-1} + \cdots + a_0 = 0$，则

$$
A^n + a_{n-1}A^{n-1} + \cdots + a_0 I = 0
$$

可用于求 $A^{-1}$：

$$
A^{-1} = -\frac{1}{a_0}(A^{n-1} + a_{n-1}A^{n-2} + \cdots + a_1 I)
$$

### 对角化

$$
A = PDP^{-1}, \quad D = \begin{pmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{pmatrix}, \quad P = (\mathbf{v}_1 \; \mathbf{v}_2)
$$

### 矩阵高次幂

$$
A^n = PD^nP^{-1}, \quad D^n = \begin{pmatrix} \lambda_1^n & 0 \\ 0 & \lambda_2^n \end{pmatrix}
$$

---

## 常见错误

- 特征方程写错符号：应为 $\det(A - \lambda I) = 0$，而非 $\det(\lambda I - A) = 0$（虽结果相同但易错）
- 特征向量忘记非零条件
- Cayley-Hamilton 代入时混淆 $\lambda$ 和 $A$
- 对角化时 $P$ 的列顺序与 $D$ 的对角元顺序不一致
- 计算高次幂时未化简 $P^{-1}$ 的分数导致计算错误
