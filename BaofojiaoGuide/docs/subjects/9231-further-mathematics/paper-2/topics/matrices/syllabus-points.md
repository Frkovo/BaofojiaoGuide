---
title: Matrices - Syllabus Points
sidebar_position: 3
---

# Matrices 考纲知识点

---

## 1. Eigenvalues and Eigenvectors（特征值与特征向量）

- 理解特征值的定义：$A\mathbf{v} = \lambda\mathbf{v}$，$\mathbf{v} \neq \mathbf{0}$
- 会推导特征方程 $\det(A - \lambda I) = 0$
- 能求解 $2 \times 2$ 和 $3 \times 3$ 矩阵的特征值
- 能通过解 $(A - \lambda I)\mathbf{v} = \mathbf{0}$ 求特征向量
- 理解特征向量的非零性质

## 2. Characteristic Equation（特征方程）

- 能展开 $2 \times 2$ 和 $3 \times 3$ 行列式得到特征多项式
- 能因式分解二次和三次特征多项式
- 对于 $2 \times 2$ 矩阵：$\lambda^2 - \operatorname{tr}(A)\lambda + \det(A) = 0$
- 对于 $3 \times 3$ 矩阵：$-\lambda^3 + \operatorname{tr}(A)\lambda^2 - \cdots + \det(A) = 0$（注意符号）

## 3. Cayley-Hamilton Theorem（Cayley-Hamilton 定理）

- 理解定理内容：矩阵 $A$ 满足其自身的特征方程
- 能代入 $A$ 得到矩阵方程
- 能利用该定理求 $A^{-1}$、$A^2$、$A^3$ 等
- 能化简矩阵多项式，如 $(A - kI)^n$

## 4. Diagonalization（对角化）

- 理解 $A = PDP^{-1}$ 的含义
- 能构造 $P$（列向量为特征向量）和 $D$（对角元为特征值）
- 会验证 $P$ 的可逆性（特征向量线性无关）
- 能计算 $P^{-1}$

## 5. Powers of Matrices（矩阵高次幂）

- 掌握 $A^n = PD^nP^{-1}$
- 能计算 $A^n$ 用于 $n$ 较大时的情形
- 理解 $D^n$ 的计算：$D^n = \operatorname{diag}(\lambda_1^n, \lambda_2^n, \dots)$
- 能用此方法求解 $A^5$、$A^{10}$ 等

## 6. Related Transformations（相关变换）

- 能处理形如 $(pA + qI)^n$ 的矩阵表达式
- 理解若 $A$ 的特征值为 $\lambda$，则 $f(A)$ 的特征值为 $f(\lambda)$
- 理解 $f(A) = Pf(D)P^{-1}$，其中 $f(D) = \operatorname{diag}(f(\lambda_1), f(\lambda_2), \dots)$
