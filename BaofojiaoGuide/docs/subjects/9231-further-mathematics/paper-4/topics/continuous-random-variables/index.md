---
title: Continuous Random Variables
sidebar_position: 1
---

# Continuous Random Variables（连续随机变量）

## 考纲要求

1. 理解连续随机变量与离散随机变量的区别，理解概率密度函数（PDF）的概念
2. 已知 PDF $f(x)$，求常数 $k$：利用 $\int_{-\infty}^{\infty} f(x)\,dx = 1$
3. 由 PDF 求累积分布函数（CDF）：$F(x) = \int_{-\infty}^{x} f(t)\,dt$
4. 由 CDF 求 PDF：$f(x) = F'(x)$
5. 计算期望：$\displaystyle E[g(X)] = \int_{-\infty}^{\infty} g(x)f(x)\,dx$
6. 计算方差：$\text{Var}(X) = E[X^2] - (E[X])^2$
7. 求中位数（Median）：$F(m) = 0.5$
8. 求四分位数（Quartiles）：$F(Q_1) = 0.25$，$F(Q_3) = 0.75$
9. 求百分位数（Percentiles）：$F(p) = \alpha$，其中 $\alpha$ 为对应比例
10. 变换 $Y = g(X)$ 的分布：CDF 法 $F_Y(y) = P(Y \le y) = P(g(X) \le y)$，然后求导得 PDF

## 常见题型

| 题型 | 频次 | 典型分值 |
|------|------|----------|
| 求 PDF 中的常数 | 几乎每年 | 2-3 分 |
| 求 CDF 并计算概率 | 每年必考 | 4-6 分 |
| 求 $E(X)$ 和 $\text{Var}(X)$ | 每年必考 | 4-7 分 |
| 求中位数 / 四分位数 | 高频 | 3-5 分 |
| 变换 $Y = g(X)$ 的分布 | 高频 | 5-9 分 |
| 分段 PDF 综合题 | 高频 | 8-12 分 |

## 核心公式

### PDF 与 CDF 关系

$$
f(x) \ge 0, \quad \int_{-\infty}^{\infty} f(x)\,dx = 1
$$

$$
F(x) = \int_{-\infty}^{x} f(t)\,dt, \quad f(x) = F'(x)
$$

### 概率计算

$$
P(a \le X \le b) = \int_{a}^{b} f(x)\,dx = F(b) - F(a)
$$

注意连续随机变量中 $P(X = a) = 0$，因此 $P(a \le X \le b) = P(a &lt; X &lt; b)$

### 期望与方差

$$
E[g(X)] = \int_{-\infty}^{\infty} g(x) f(x)\,dx
$$

$$
E[X] = \int_{-\infty}^{\infty} x f(x)\,dx
$$

$$
\text{Var}(X) = E[X^2] - (E[X])^2 = \int_{-\infty}^{\infty} x^2 f(x)\,dx - \left(\int_{-\infty}^{\infty} x f(x)\,dx\right)^2
$$

### 中位数与四分位数

$$
F(m) = 0.5 \quad \text{(Median)}
$$

$$
F(Q_1) = 0.25, \quad F(Q_3) = 0.75
$$

$$
\text{IQR} = Q_3 - Q_1
$$

### 变换（CDF 法）

对 $Y = g(X)$：

1. 写出 $F_Y(y) = P(Y \le y) = P(g(X) \le y)$
2. 解不等式得 $X$ 的范围
3. 用 $F_X$ 或积分表示概率
4. $f_Y(y) = F_Y'(y)$

### 线性变换

若 $Y = aX + b$，则：

$$
E[Y] = aE[X] + b, \quad \text{Var}(Y) = a^2\text{Var}(X)
$$

## 常见错误

1. **忘记 PDF 非负性**：求常数后未检查 $f(x) \ge 0$ 对所有 $x$ 成立
2. **积分上下限错误**：分段 PDF 使用错误的分段区间
3. **CDF 忘记常数**：不定积分后忘记使用 $F(-\infty) = 0$ 确定常数
4. **方差公式混淆**：$\text{Var}(X) = E[X^2] - (E[X])^2$ 而非 $E[X^2] - E[X]$
5. **变换时方向反**：$Y = X^2$ 变换时忘记考虑 $y \ge 0$ 和正负号
6. **连续随机变量的概率点**：误以为 $P(X = a) \ne 0$
