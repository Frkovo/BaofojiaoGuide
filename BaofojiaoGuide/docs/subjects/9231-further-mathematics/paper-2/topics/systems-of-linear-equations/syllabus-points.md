---
title: Systems of Linear Equations - Syllabus Points
sidebar_position: 3
---

# Systems of Linear Equations 考纲知识点

---

## 1. Matrix Representation（矩阵表示）

- 将三元一次方程组写为 $A\mathbf{x} = \mathbf{b}$ 形式
- $A$ 为 $3 \times 3$ 系数矩阵，$\mathbf{x}$ 为未知数列向量，$\mathbf{b}$ 为常数列向量
- 齐次：$\mathbf{b} = \mathbf{0}$；非齐次：$\mathbf{b} \neq \mathbf{0}$

## 2. Determinant and Unique Solution（行列式与唯一解）

- $\det A \neq 0$ 时，存在唯一解
- $\det A = 0$ 时，无唯一解（可能无解或无穷多解）
- 掌握三元系数行列式的计算（展开法）
- 能通过 $\det A = 0$ 求出参数值

## 3. Gaussian Elimination（高斯消元）

- 能写出增广矩阵 $(A|\mathbf{b})$
- 掌握基本行变换：
  - 交换两行
  - 一行乘以非零常数
  - 一行加上另一行的倍数
- 能化增广矩阵为行阶梯形
- 能从行阶梯形判断相容性

## 4. Consistency and Inconsistency（相容性与不相容性）

- 相容：至少有一个解（唯一解或无穷多解）
- 不相等（矛盾）：无解
- 判断方法：行变换后出现 $0 = c$（$c \neq 0$）→ 矛盾
- 齐次方程组总是相容（至少有平凡解 $\mathbf{x} = \mathbf{0}$）

## 5. Geometric Interpretation（几何解释）

- 每个方程表示三维空间中的一个平面
- $\det A \neq 0$：三个平面交于一点
- $\det A = 0$，相容：三个平面交于一条直线或一个平面
- $\det A = 0$，矛盾：三棱柱（triangular prism）或两平面平行
- 特殊情形：两个平面重合

## 6. Parametric Families of Solutions（参数化解集）

- 当方程组有无穷多解时，用参数表示解
- 通常设一个变量为参数 $t$ 或 $\lambda$
- 用行阶梯形回代得到参数化解
