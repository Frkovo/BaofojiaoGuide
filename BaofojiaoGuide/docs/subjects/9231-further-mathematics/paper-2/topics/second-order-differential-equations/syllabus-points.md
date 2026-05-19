---
title: 大纲要点
sidebar_position: 2
---

# Syllabus Points — Second Order Differential Equations

## 核心知识点

### 1. 常系数齐次线性 ODE

- $a\frac{d^2y}{dx^2} + b\frac{dy}{dx} + cy = 0$
- 辅助方程 $am^2 + bm + c = 0$
- 三种解的形式依赖判别式 $b^2 - 4ac$

### 2. 非齐次线性 ODE

- 通解 = CF + PI
- 待定系数法求 PI 时，试设形式需与 CF 不冲突
- 若冲突则乘以 $x$（或 $x^2$）

### 3. 待定系数法速查

| $f(x)$ | PI 试设 | 条件 |
|--------|--------|------|
| $k$（常数） | $C$ | 除非 $c = 0$ |
| $kx$ | $Cx + D$ | |
| $kx^2$ | $Cx^2 + Dx + E$ | |
| $ke^{\lambda x}$ | $Ce^{\lambda x}$ | $\lambda$ 非特征根 |
| $k\cos\omega x$ | $C\cos\omega x + D\sin\omega x$ | |
| $k\sin\omega x$ | $C\cos\omega x + D\sin\omega x$ | |

### 4. Euler-Cauchy 方程

- 形式：$at^2\frac{d^2y}{dt^2} + bt\frac{dy}{dt} + cy = f(t)$
- 解法一：设 $y = t^m$ 代入齐次部分
- 解法二：变量代换 $t = e^u$ 化为常系数

### 5. Euler-Cauchy 的三种 CF 形式

| 根的情况 | CF |
|---------|-----|
| 两实根 $m_1 \neq m_2$ | $At^{m_1} + Bt^{m_2}$ |
| 重根 $m$ | $(A + B\ln t)t^m$ |
| 复根 $m = \alpha \pm i\beta$ | $t^\alpha(A\cos(\beta\ln t) + B\sin(\beta\ln t))$ |

### 6. 耦合方程组与矩阵

- $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$ 形式
- 特征值和特征向量确定解的形式
- $\mathbf{x} = \sum c_i \mathbf{v}_i e^{\lambda_i t}$
