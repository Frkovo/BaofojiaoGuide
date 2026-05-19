---
title: First Order Differential Equations
sidebar_position: 3
---

# First Order Differential Equations（一阶微分方程）

---

## 考纲要求

1. 掌握一阶线性 ODE 的标准形式：$\frac{dy}{dx} + P(x)y = Q(x)$
2. 会用积分因子法（integrating factor）求解：$I = e^{\int P\,dx}$
3. 能处理可分离变量的一阶方程
4. 能应用初始条件求解特解
5. 理解 $t$ 为自变量的情形（如 $\frac{dx}{dt}$）

---

## 常见题型

| 题型 | 分值 | 链接 |
|------|------|------|
| 积分因子法（标准型） | 6–8 分 | [题型 1](./question-types.md#type-1积分因子法) |
| 可分离变量方程 | 4–6 分 | [题型 2](./question-types.md#type-2可分离变量方程) |
| 初值问题（含 IVP） | 6–10 分 | [题型 3](./question-types.md#type-3初值问题) |

---

## 核心公式

### 积分因子法

$$
\frac{dy}{dx} + P(x)y = Q(x)
$$

$$
I = e^{\int P(x)\,dx}
$$

$$
\frac{d}{dx}(yI) = IQ(x)
$$

$$
y = \frac{1}{I}\int IQ(x)\,dx
$$

### 可分离变量

$$
\frac{dy}{dx} = f(x)g(y) \quad\Rightarrow\quad \int \frac{1}{g(y)} \, dy = \int f(x) \, dx
$$

---

## 常见错误

- 忘记积分因子中的指数负号（当 $P(x)$ 有负号时）
- 积分后漏加常数 $C$
- 化简通解时遗漏绝对值
- 代入初值时代数错误

---

## 真题分布

| 年份 | 题号 | 分值 | 题型 |
|------|------|------|------|
| s20/21 | Q1 | 6 | IF + IVP |
| w20/22 | Q4 | 8 | IF + IVP |
| s20/23 | Q7 | 11 | IF（复杂系数） |
| w21/21 | Q7 | 4+7 | IF（特殊形式） |
| w22/21 | Q8 | 11 | IF（三角系数） |
| s25/21 | Q7 | 10 | IF（二次系数） |
