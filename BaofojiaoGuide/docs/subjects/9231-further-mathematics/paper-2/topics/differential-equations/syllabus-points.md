---
title: 考纲要点
sidebar_position: 2
---

# Differential Equations — 考纲要点

## 1. 一阶线性 — 积分因子
$\frac{dy}{dx} + P(x)y = Q(x)$ → $\mu = e^{\int P\,dx}$ → $\frac{d}{dx}(\mu y) = \mu Q$ → $\mu y = \int\mu Q\,dx + C$

## 2. 二阶常系数 — CF（Complementary Function）
辅助方程 $am^2 + bm + c = 0$：
- 不等实根 $m_1 \neq m_2$：$y = Ae^{m_1x} + Be^{m_2x}$
- 重根 $m$：$y = (A+Bx)e^{mx}$
- 共轭复根 $\alpha \pm i\beta$：$y = e^{\alpha x}(A\cos\beta x + B\sin\beta x)$

## 3. PI（Particular Integral）
- 常数 → 设 $y = c$
- $e^{ax}$ → 设 $y = pe^{ax}$
- $\cos\omega x / \sin\omega x$ → 设 $y = p\cos\omega x + q\sin\omega x$
- 多项式 → 设同次多项式

## 4. CF/PI 重叠
重叠时 PI 乘 $x$（重根乘 $x^2$）

## 5. 代换法
$x = e^t$：欧拉型方程 → 常系数
$z = x + y$：一阶方程 → 可分离变量

## 6. 初值问题
先合并 CF+PI，再代初值求常数
