---
title: 常见错误
sidebar_position: 6
---

# 常见错误 — Paper 2

## Hyperbolic 与 Trigonometric 混淆

| 正确的（Hyperbolic） | 错误（按三角习惯） |
|----------------------|-------------------|
| $\cosh^2 x - \sinh^2 x \equiv 1$ | $\cosh^2 x + \sinh^2 x \equiv 1$ ✗ |
| $\frac{d}{dx}\cosh x = \sinh x$ | $\frac{d}{dx}\cosh x = -\sinh x$ ✗ |

## 矩阵常见错误

- **$\det A = 0$ ≠ inconsistent**。$\det = 0$ 只是没有*唯一*解，可能无限多解（一致）也可能无解（不一致），要靠消元判断
- **特征向量顺序要和特征值对应**。$P$ 的第一列必须是 $\lambda_1$ 的特征向量
- **$AB$ 的含义**：先做 $B$ 再做 $A$，顺序不能互换

## 求导雷区

| 函数 | 导数 | 易错答案 |
|------|------|---------|
| $\cos^{-1} x$ | $-\frac{1}{\sqrt{1-x^2}}$ | $+\frac{1}{\sqrt{1-x^2}}$ ✗ |
| $\tanh^{-1} x$ | $\frac{1}{1-x^2}$ | $\frac{1}{1+x^2}$ ✗ |

## 积分雷区

$$\int\frac{dx}{\sqrt{a^2-x^2}} = \sin^{-1}\frac{x}{a} + C\text{，不是 }\sinh^{-1}\frac{x}{a}$$
$$\int\frac{dx}{\sqrt{x^2+a^2}} = \sinh^{-1}\frac{x}{a} + C\text{，不是 }\cosh^{-1}\frac{x}{a}$$

## 复数雷区

- Conjugate root theorem：非实根成共轭对出现
- $\arg(z_1z_2) = \arg z_1 + \arg z_2$，但注意主值范围 $(-\pi,\pi]$
- $n$ 次单位根之和 $= 0$

## 微分方程雷区

**积分因子符号：** 对于 $\frac{dy}{dx} + Py = Q$，IF $= e^{\int P\,dx}$。
如果式子是 $\frac{dy}{dx} - \frac{2}{x}y = x$，则 $P = -\frac{2}{x}$，IF $= x^{-2}$。

**CF/PI 重叠：** 如果右端项已经在 CF 中，特解要乘以 $x$（重根乘 $x^2$）。
例如 $\ddot{x} + 4x = \cos 2t$，应设 $x_{PI} = kt\cos 2t$，不是 $k\cos 2t$。

**初值条件：** 先合并 CF+PI 得到通解，**再**代初值，顺序不能反。
