---
title: Differential Equations
sidebar_position: 6
---

# Differential Equations

## 考纲要求

1. 一阶线性微分方程的积分因子法：$\frac{dy}{dx}+Py=Q$ → $\mu=e^{\int P\,dx}$ → $\frac{d}{dx}(\mu y)=\mu Q$
2. 二阶常系数线性微分方程的 CF（Complementary Function）：辅助方程 $am^2+bm+c=0$ 的三种根
3. PI（Particular Integral）的确定：多项式、指数、三角形式
4. CF 与 PI 重叠时的处理（乘 $x$ 或 $x^2$）
5. 代换法化简（$x=e^t$、$z=x+y$ 等）
6. 初值条件求特解

## 常见题型

1. First order — integrating factor method
2. Second order — auxiliary equation
3. Particular integral determination
4. Overlap of PI with CF
5. Reduction using substitution
6. Initial value problems

## 核心公式

$$\frac{dy}{dx}+Py=Q \Rightarrow \mu=e^{\int P\,dx},\; \frac{d}{dx}(\mu y)=\mu Q$$
$$a\frac{d^2y}{dx^2}+b\frac{dy}{dx}+cy=0 \Rightarrow am^2+bm+c=0$$

| 根的類型 | CF 形式 |
|---------|---------|
| Real distinct $m_1,m_2$ | $Ae^{m_1x}+Be^{m_2x}$ |
| Repeated $m$ | $(A+Bx)e^{mx}$ |
| Complex $\alpha\pm i\beta$ | $e^{\alpha x}(A\cos\beta x+B\sin\beta x)$ |

## 常见错误

- 积分因子 $P$ 的符号：$\frac{dy}{dx}-\frac{2}{x}y=x$ 的 $P=-\frac{2}{x}$，$\mu=x^{-2}$
- CF/PI 重叠时特解要乘 $x$，不是还是用原形式
- 初值条件：先合併 CF+PI，再代初值
