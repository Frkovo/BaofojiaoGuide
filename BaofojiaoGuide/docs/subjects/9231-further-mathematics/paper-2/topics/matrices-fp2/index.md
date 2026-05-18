---
title: Matrices (Further Pure 2)
sidebar_position: 2
---

# Matrices (Further Pure 2)

## 考纲要求

1. 将 $3\times3$ 线性方程组写成 $A\mathbf{x}=\mathbf{b}$ 形式
2. 理解一致性与 $\det A$ 的关系：$\det = 0$ 时没有唯一解（可能无限多解或无解）
3. 几何解释：三个平面交于一点/一条直线/无公共交点
4. 特征方程 $\det(A-\lambda I)=0$，特征值 $\lambda$ 和特征向量 $\mathbf{e}$ 满足 $A\mathbf{e}=\lambda\mathbf{e}$
5. 求 $2\times2$ 和 $3\times3$ 矩阵的特征值和特征向量（实特征值）
6. 对角化 $A=QDQ^{-1}$，$A^n = QD^nQ^{-1}$
7. Cayley–Hamilton 定理：矩阵满足自己的特征方程

## 常见题型

1. Solving $3\times3$ linear systems
2. Geometric interpretation of planes
3. Finding eigenvalues and eigenvectors
4. Matrix diagonalisation $A=PDP^{-1}$
5. Matrix powers $A^n$
6. Cayley–Hamilton theorem applications

## 核心公式

$$\det(A-\lambda I)=0,\qquad A\mathbf{e}=\lambda\mathbf{e},\qquad A=PDP^{-1},\qquad A^n=PD^nP^{-1}$$

## 常见错误

- $\det A = 0$ ≠ inconsistent——只是无*唯一*解，可能无限多解
- 特征向量列的顺序必须与 $D$ 中特征值的顺序一致
- 把 $\det(A-\lambda I)=0$ 的符号搞反
