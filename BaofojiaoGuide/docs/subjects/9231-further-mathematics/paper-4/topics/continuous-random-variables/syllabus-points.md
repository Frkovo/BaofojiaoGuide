---
title: 考纲要求
sidebar_position: 3
---

# 考纲要求 — Continuous Random Variables

## 4.1 Continuous Random Variables

### 1. 概率密度函数 (Probability Density Function)

连续随机变量 $X$ 的概率密度函数 $f(x)$ 满足：

- $f(x) \ge 0$ 对所有 $x \in \mathbb{R}$
- $\displaystyle \int_{-\infty}^{\infty} f(x)\,dx = 1$
- $P(a \le X \le b) = \displaystyle \int_a^b f(x)\,dx$

PDF 可以分段定义（piecewise），在非定义域上取值为 0。

### 2. 累积分布函数 (Cumulative Distribution Function)

$$
F(x) = P(X \le x) = \int_{-\infty}^{x} f(t)\,dt
$$

性质：
- $F$ 是非递减函数
- $\displaystyle \lim_{x \to -\infty} F(x) = 0$，$\displaystyle \lim_{x \to \infty} F(x) = 1$
- $F'(x) = f(x)$（在 $f$ 连续点处）

### 3. 期望 (Expectation)

对任意函数 $g$：

$$
E[g(X)] = \int_{-\infty}^{\infty} g(x) f(x)\,dx
$$

特殊情况：
- $E[X] = \int_{-\infty}^{\infty} x f(x)\,dx$（均值）
- $E[X^2] = \int_{-\infty}^{\infty} x^2 f(x)\,dx$

### 4. 方差 (Variance)

$$
\text{Var}(X) = E[(X - \mu)^2] = E[X^2] - (E[X])^2
$$

其中 $\mu = E[X]$。

### 5. 中位数与分位数 (Median and Quantiles)

中位数 $m$：$F(m) = 0.5$，即 $P(X \le m) = P(X \ge m) = 0.5$

下四分位数 $Q_1$：$F(Q_1) = 0.25$

上四分位数 $Q_3$：$F(Q_3) = 0.75$

四分位距 (IQR)：$\text{IQR} = Q_3 - Q_1$

百分位数：$P(X \le p_{\alpha}) = \alpha$，其中 $\alpha \in (0, 1)$

### 6. 变换 (Transformations)

若 $Y = g(X)$，可用 **CDF 法** 求 $Y$ 的分布：

1. $F_Y(y) = P(Y \le y) = P(g(X) \le y)$
2. 将不等式改写为 $X$ 的范围
3. 用 $F_X$ 或积分计算概率
4. $f_Y(y) = F_Y'(y)$

常见变换类型：
- **线性** $Y = aX + b$：直接用 $E[Y] = aE[X] + b$，$\text{Var}(Y) = a^2\text{Var}(X)$
- **平方** $Y = X^2$：注意 $y \ge 0$ 且 $P(- \sqrt{y} \le X \le \sqrt{y})$
- **倒数** $Y = 1/X$：注意定义域和不等号方向
- **指数/对数**：注意定义域限制
