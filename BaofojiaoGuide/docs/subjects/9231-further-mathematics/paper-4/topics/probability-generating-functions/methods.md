---
title: 解题方法
sidebar_position: 4
---

# Solution Methods — Probability Generating Functions

## Method 1: Constructing PGF from Word Problem

适用于从文字描述（不放回取球、掷骰子、抛硬币等）构造 PGF。

:::info[Steps]

1. 确定离散随机变量 $X$ 的所有可能取值
   - 如不放回取 $n$ 球中红球个数：$X = 0, 1, \dots, n$
2. 计算每个取值的概率 $P(X = x)$
   - 不放回抽样用组合数：$\frac{C^{\text{成功}}_x \times C^{\text{失败}}_{n-x}}{C^{\text{总数}}_n}$
   - 二项试验用二项概率公式
3. 写出 $G_X(t) = \sum_x P(X = x) \cdot t^x$
4. 若可能，化简为封闭形式（如 $(q+pt)^n$）

:::

## Method 2: Finding Mean and Variance via PGF

适用于已知 $G(t)$（多项式或有理函数），要求 $E(X)$ 和 $\text{Var}(X)$。

:::info[Steps]

1. 求一阶导数 $G'(t)$
   - 多项式：逐项求导
   - $(a+bt)^n$：$n(a+bt)^{n-1} \cdot b$
   - $\frac{pt}{1-qt}$：商法则
   - $e^{\lambda(t-1)}$：链式法则
2. 代入 $t = 1$ 得 $E[X] = G'(1)$
3. 求二阶导数 $G''(t)$
4. 代入 $t = 1$ 得 $E[X(X-1)] = G''(1)$
5. $\text{Var}(X) = G''(1) + G'(1) - [G'(1)]^2$

:::

## Method 3: Sum of Independent Variables (Product of PGFs)

适用于求多个独立随机变量之和的分布或概率。

:::info[Steps]

1. 写出每个变量的 PGF：$G_X(t), G_Y(t), \dots$
   - 若 $X_i$ 独立同分布，$G_{X_i}(t) = G_X(t)$
2. 乘积得和 PGF：$G_{X+Y}(t) = G_X(t) \cdot G_Y(t)$
   - 多个变量：$G_{X_1 + \cdots + X_n}(t) = \prod_{i=1}^{n} G_{X_i}(t)$
3. 若 $X_i$ 独立同分布：$G_{S_n}(t) = [G_X(t)]^n$
4. 展开 PGF，$t^k$ 的系数即为 $P(S = k)$
   - 若展开复杂，利用组合意义求特定系数

:::

## Method 4: Identifying Distribution from PGF

适用于已知 $G(t)$，要求识别分布类型或反推概率分布。

:::info[Steps]

1. 将 $G(t)$ 与标准分布 PGF 比对：
   - $(q+pt)^n$ → $B(n, p)$
   - $\frac{pt}{1-qt}$ → $\text{Geo}(p)$
   - $e^{\lambda(t-1)}$ → $\text{Po}(\lambda)$
   - $\frac{1}{n}(t + t^2 + \cdots + t^n)$ → $\text{DU}(n)$
2. 若 $G(t)$ 是多项式：
   - 展开得 $G(t) = \sum p_k t^k$
   - $p_k = P(X = k)$
3. 若 $G_S(t) = [G_X(t)]^n$ 形式：
   - 开 $n$ 次方得 $G_X(t)$
   - 由 $G_X(t)$ 系数求 $X$ 的分布

:::
