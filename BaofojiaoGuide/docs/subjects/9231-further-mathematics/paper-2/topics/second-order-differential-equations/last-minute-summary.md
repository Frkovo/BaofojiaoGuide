---
title: 考前速记
sidebar_position: 7
---

# 考前速记 — Second Order Differential Equations

## 核心公式

| 情形 | CF 形式 |
|------|---------|
| 实根 $m_1 \neq m_2$ | $Ae^{m_1x} + Be^{m_2x}$ |
| 重根 $m$ | $(A + Bx)e^{mx}$ |
| 复根 $\alpha \pm i\beta$ | $e^{\alpha x}(A\cos\beta x + B\sin\beta x)$ |

## PI 试设速查

| $f(x)$ | 试设 $y_p$ |
|--------|-----------|
| $k$ | $C$ |
| $ax + b$ | $Cx + D$ |
| $ax^2 + bx + c$ | $Cx^2 + Dx + E$ |
| $ke^{\lambda x}$ | $Ce^{\lambda x}$ |
| $k\cos\omega x$ | $C\cos\omega x + D\sin\omega x$ |
| $k\sin\omega x$ | $C\cos\omega x + D\sin\omega x$ |

## Euler-Cauchy 方程

标准形式：$at^2y'' + bty' + cy = f(t)$

| 根的情况 | CF |
|---------|-----|
| 实根 $m_1 \neq m_2$ | $At^{m_1} + Bt^{m_2}$ |
| 重根 $m$ | $(A + B\ln t)t^m$ |
| 复根 $\alpha \pm i\beta$ | $t^\alpha(A\cos(\beta\ln t) + B\sin(\beta\ln t))$ |

变量代换：$t = e^u$，则 $t\frac{d}{dt} = \frac{d}{du}$，$t^2\frac{d^2}{dt^2} = \frac{d^2}{du^2} - \frac{d}{du}$

## 易错点

- 重根 CF 必须乘 $x$（或 $\ln t$）
- PI 冲突时乘 $x$（或 $x^2$）
- 三角 RHS 的 PI 必须含 $\cos + \sin$
- 初值代入时需要两个条件：$y$ 和 $y'$

## 解题流程

1. 写 AE → 2. 求根 → 3. 写 CF → 4. 试设 PI → 5. 代入比较系数 → 6. 通解 = CF + PI → 7. 代入初值
