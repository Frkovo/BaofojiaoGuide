---
title: Probability Generating Functions
sidebar_position: 1
---

# Probability Generating Functions（概率生成函数）

## 考纲要求

1. 理解概率生成函数（PGF）的概念，掌握离散均匀分布（Discrete Uniform）、二项分布（Binomial）、几何分布（Geometric）、泊松分布（Poisson）的 PGF 构造和使用
2. 会用 PGF 求均值和方差：$\mu = G'(1)$，$\sigma^2 = G''(1) + G'(1) - [G'(1)]^2$
3. 理解独立随机变量和的 PGF 等于各 PGF 的乘积：$G_{X+Y}(t) = G_X(t)G_Y(t)$
4. 会由多个独立同分布随机变量和的 PGF 反推单个变量的 PGF

## 常见题型

| 题型 | 频次 | 典型分值 |
|------|------|----------|
| 从离散分布构造 PGF | 每年必考 | 3-5 分 |
| 由 PGF 求均值和方差 | 每年必考 | 4-6 分 |
| 独立随机变量和的 PGF | 高频 | 5-8 分 |
| 由和的 PGF 反推原分布 | 中频 | 4-7 分 |

## 核心公式

### 概率生成函数定义

$$
G_X(t) = E[t^X] = \sum_{x} P(X = x) t^x
$$

### 常用分布的 PGF

| 分布 | $G(t)$ | 参数条件 |
|------|--------|----------|
| 离散均匀 (Discrete Uniform) | $\displaystyle \frac{1}{n}\sum_{x=1}^{n} t^x$ | $X \sim \text{DU}(n)$ |
| 二项分布 (Binomial) | $(q + pt)^n$ | $X \sim B(n, p)$, $q = 1-p$ |
| 几何分布 (Geometric) | $\displaystyle \frac{pt}{1 - qt}$ | $X \sim \text{Geo}(p)$ |
| 泊松分布 (Poisson) | $e^{\lambda(t-1)}$ | $X \sim \text{Po}(\lambda)$ |

### 均值与方差

$$
G'(t) = \frac{d}{dt}G(t), \quad G''(t) = \frac{d^2}{dt^2}G(t)
$$

$$
E[X] = G'(1), \quad E[X(X-1)] = G''(1)
$$

$$
\text{Var}(X) = G''(1) + G'(1) - [G'(1)]^2
$$

### 独立随机变量和

若 $X$ 与 $Y$ 独立，则：

$$
G_{X+Y}(t) = G_X(t) \cdot G_Y(t)
$$

更一般地，若 $S_n = X_1 + X_2 + \cdots + X_n$ 且 $X_i$ 独立同分布：

$$
G_{S_n}(t) = [G_X(t)]^n
$$

## 常见错误

1. **混淆 $G'(1)$ 与 $E[X^2]$**：$G'(1) = E[X]$，而非 $E[X^2]$
2. **方差公式记忆错误**：$\text{Var}(X) = G''(1) + G'(1) - [G'(1)]^2$，不可遗漏 $G'(1)$
3. **忘记简化多项式系数**：构造 PGF 后未合并同类项，导致后续求导错误
4. **不放回抽样概率计算错误**：涉及组合数 $C$ 或排列数 $P$ 时混淆
5. **和 PGF 忘记乘积**：独立变量和的 PGF 是乘积而非和（$G_X \cdot G_Y$ 而非 $G_X + G_Y$）
