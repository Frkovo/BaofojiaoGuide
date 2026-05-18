---
title: 考纲要点
sidebar_position: 2
---

# Matrices (FP2) — 考纲要点

## 1. $3\times3$ 线性方程组
- 写成 $A\mathbf{x} = \mathbf{b}$
- $\det A \neq 0$ → 唯一解（三个平面交于一点）
- $\det A = 0$ → 检查一致性（消元法）
  - 一致：无限多解（三个平面交于一条直线）
  - 不一致：无解（无公共交点）

## 2. 特征值特征向量
- 特征方程：$\det(A - \lambda I) = 0$
- 特征向量：$(A - \lambda I)\mathbf{e} = \mathbf{0}$
- 性质：若 $A\mathbf{e} = \lambda\mathbf{e}$，则 $A^n\mathbf{e} = \lambda^n\mathbf{e}$

## 3. 对角化
- $A = PDP^{-1}$，$D$ 为特征值对角阵，$P$ 以特征向量为列
- $A^n = PD^nP^{-1}$

## 4. Cayley–Hamilton 定理
- $A$ 满足自己的特征方程：$p(A) = 0$
- 可用于求 $A^{-1}$、$A^2$ 等
