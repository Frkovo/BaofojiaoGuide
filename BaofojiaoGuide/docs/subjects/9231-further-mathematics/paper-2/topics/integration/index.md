---
title: Integration
sidebar_position: 4
---

# Integration

## 考纲要求

1. 双曲函数积分：$\int\sinh x\,dx = \cosh x + C$，$\int\cosh x\,dx = \sinh x + C$
2. 标准积分：$\int\frac{dx}{\sqrt{a^2-x^2}}$、$\int\frac{dx}{a^2+x^2}$、$\int\frac{dx}{\sqrt{x^2+a^2}}$、$\int\frac{dx}{\sqrt{x^2-a^2}}$
3. 配方法后积分
4. 递推公式的推导和应用
5. 弧长（直角坐标、参数式、极坐标）
6. 旋转体表面积
7. 矩形估计积分上下界

## 常见题型

1. Standard integrals of inverse functions
2. Trigonometric and hyperbolic substitutions
3. Reduction formulae
4. Arc length and surface area of revolution
5. Rectangle bounds and inequalities for sums

## 核心公式

| 积分 | 结果 |
|------|------|
| $\int dx/\sqrt{a^2-x^2}$ | $\sin^{-1}(x/a)+C$ |
| $\int dx/(a^2+x^2)$ | $\frac1a\tan^{-1}(x/a)+C$ |
| $\int dx/\sqrt{x^2+a^2}$ | $\sinh^{-1}(x/a)+C$ |
| $\int dx/\sqrt{x^2-a^2}$ | $\cosh^{-1}(x/a)+C$ |

弧长：$s = \int\sqrt{1+(dy/dx)^2}\,dx$，表面积：$S = 2\pi\int y\sqrt{1+(dy/dx)^2}\,dx$

## 常见错误

- $\sqrt{a^2-x^2}$ 用 $\sin^{-1}$，不是 $\sinh^{-1}$
- $\sqrt{x^2+a^2}$ 用 $\sinh^{-1}$，不是 $\cosh^{-1}$
- 表面积忘了 $2\pi$ 和 $y$ 因子
