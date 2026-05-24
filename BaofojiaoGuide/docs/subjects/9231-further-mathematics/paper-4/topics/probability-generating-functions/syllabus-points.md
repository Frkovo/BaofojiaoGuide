---
title: 考纲要求
sidebar_position: 3
---

# 考纲要求 — Probability Generating Functions

## 4.5 Probability Generating Functions

### 1. 概率生成函数的定义 (Definition of PGF)

离散随机变量 $X$ 的概率生成函数定义为：

$$
G_X(t) = E[t^X] = \sum_{x} P(X = x) t^x
$$

其中求和遍及 $X$ 的所有可能取值。$G_X(t)$ 是 $t$ 的函数，定义域为使级数收敛的 $t$ 值（通常 $|t| \le 1$）。

性质：
- $G_X(1) = \sum P(X = x) = 1$
- $G_X(0) = P(X = 0)$

### 2. 常用分布的 PGF (PGFs of Standard Distributions)

#### 离散均匀分布 (Discrete Uniform)

若 $X \sim \text{DU}(n)$，即 $P(X = x) = \frac{1}{n}$，$x = 1, 2, \dots, n$：

$$
G_X(t) = \frac{1}{n}(t + t^2 + \cdots + t^n) = \frac{t(1 - t^n)}{n(1 - t)}
$$

#### 二项分布 (Binomial)

若 $X \sim B(n, p)$，$P(X = x) = \binom{n}{x}p^x(1-p)^{n-x}$：

$$
G_X(t) = \sum_{x=0}^{n} \binom{n}{x}(pt)^x (1-p)^{n-x} = (1-p + pt)^n
$$

记 $q = 1-p$，则 $G_X(t) = (q + pt)^n$。

#### 几何分布 (Geometric)

若 $X \sim \text{Geo}(p)$，$P(X = x) = p(1-p)^{x-1}$，$x = 1, 2, 3, \dots$：

$$
G_X(t) = \sum_{x=1}^{\infty} p(qt)^{x-1} = \frac{pt}{1 - qt}
$$

其中 $q = 1-p$，$|t| &lt; \frac{1}{q}$。

#### 泊松分布 (Poisson)

若 $X \sim \text{Po}(\lambda)$，$P(X = x) = \frac{e^{-\lambda}\lambda^x}{x!}$：

$$
G_X(t) = \sum_{x=0}^{\infty} e^{-\lambda} \frac{(\lambda t)^x}{x!} = e^{\lambda(t-1)}
$$

### 3. 均值和方差的 PGF 求法 (Mean and Variance via PGF)

对 $G_X(t)$ 在 $t = 1$ 处求导：

$$
G'(t) = \frac{d}{dt}G_X(t), \quad G''(t) = \frac{d^2}{dt^2}G_X(t)
$$

$$
E[X] = G'(1) = \left. \frac{d}{dt} G_X(t) \right|_{t=1}
$$

$$
E[X(X-1)] = G''(1) = \left. \frac{d^2}{dt^2} G_X(t) \right|_{t=1}
$$

方差公式：

$$
\text{Var}(X) = E[X^2] - (E[X])^2 = E[X(X-1)] + E[X] - (E[X])^2
$$

即：

$$
\boxed{\text{Var}(X) = G''(1) + G'(1) - [G'(1)]^2}
$$

### 4. 独立随机变量和的 PGF (PGF of Sum of Independent RVs)

若 $X$ 与 $Y$ 独立，则：

$$
G_{X+Y}(t) = G_X(t) \cdot G_Y(t)
$$

推广到 $n$ 个独立同分布随机变量 $X_1, X_2, \dots, X_n$，令 $S_n = X_1 + X_2 + \cdots + X_n$：

$$
G_{S_n}(t) = [G_X(t)]^n
$$

这一性质常用于：
- 由各变量分布求和的分布
- 反推：已知 $G_{S_n}(t) = [G_X(t)]^n$，开 $n$ 次方求 $G_X(t)$

### 5. PGF 与分布的一一对应

PGF 与概率分布一一对应。若两个随机变量有相同的 PGF，则它们同分布。这一性质用于：
- 识别分布类型（如 PGF 为 $(q+pt)^n$ 形式则 $X \sim B(n, p)$）
- 验证分布假设是否合理
