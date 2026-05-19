---
title: Second Order Differential Equations
sidebar_position: 4
---

# Second Order Differential Equations（二阶微分方程）

---

## 考纲要求

1. 掌握常系数二阶线性 ODE：$a\frac{d^2y}{dx^2} + b\frac{dy}{dx} + cy = f(x)$
2. 会解齐次方程（辅助方程法），处理实根、重根、复根三种情形
3. 会用待定系数法求特解（PI）
4. 理解通解 = CF + PI 的结构
5. 能用初始条件确定特解中的常数
6. 掌握 Euler-Cauchy 型方程通过变量代换化为常系数方程的方法
7. （拓展）了解耦合方程组与矩阵的联系

---

## 常见题型

| 题型 | 分值 | 链接 |
|------|------|------|
| 常系数 ODE（多项式 RHS） | 6–7 分 | [题型 1](./question-types.md) |
| 常系数 ODE（正/余弦 RHS） | 11 分 | [题型 1](./question-types.md) |
| 常系数 ODE（指数 RHS） | 6–10 分 | [题型 1](./question-types.md) |
| Euler-Cauchy 方程 | 4+7 分 | [题型 2](./question-types.md) |
| 耦合系统（矩阵法） | 10–15 分 | [题型 3](./question-types.md) |

---

## 核心公式

### 辅助方程（Auxiliary Equation）

$$
a\frac{d^2y}{dx^2} + b\frac{dy}{dx} + cy = 0 \;\Rightarrow\; am^2 + bm + c = 0
$$

### 齐次解 CF 的三种形式

| 根的情况 | CF |
|---------|-----|
| 两实根 $m_1 \neq m_2$ | $Ae^{m_1x} + Be^{m_2x}$ |
| 重根 $m_1 = m_2$ | $(A + Bx)e^{m_1x}$ |
| 复根 $m = \alpha \pm i\beta$ | $e^{\alpha x}(A\cos\beta x + B\sin\beta x)$ |

### 特解 PI 的形式（待定系数法）

| $f(x)$ 形式 | PI 试设形式 |
|------------|------------|
| 多项式 $p_n(x)$ | $a_nx^n + \cdots + a_0$ |
| $ke^{\lambda x}$ | $Ce^{\lambda x}$（若 $\lambda$ 非根） |
| $k\cos\omega x$ 或 $k\sin\omega x$ | $C\cos\omega x + D\sin\omega x$ |
| 乘积形式 | 按乘积试设 |

---

## 常见错误

- 辅助方程忘设 $= 0$
- 重根情况的 CF 形式写错（漏 $x$ 因子）
- PI 试设形式与 CF 冲突时未乘 $x$
- 初值条件求解常数时代入出错
- Euler-Cauchy 代换后混淆自变量

---

## 真题分布

| 年份 | 题号 | 分值 | 题型 |
|------|------|------|------|
| w20/21 | Q2 | 6+1 | 常系数（多项式 RHS） |
| s21/21 | Q2 | 6+1 | 常系数（多项式 RHS） |
| s20/21 | Q7 | 4+7 | Euler-Cauchy |
| s20/23 | Q1 | 6 | 常系数（指数 RHS） |
| w20/22 | Q6 | 11 | 常系数（余弦 RHS） |
| s25/21 | Q5 | 10 | 常系数（指数 RHS） |
