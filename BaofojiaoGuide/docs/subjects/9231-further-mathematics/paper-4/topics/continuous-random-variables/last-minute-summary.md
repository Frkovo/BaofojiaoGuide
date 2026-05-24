---
title: 考前总结
sidebar_position: 7
---

# 考前总结 — Continuous Random Variables

## 必背公式

### PDF 与 CDF
$$
\int_{-\infty}^{\infty} f(x)\,dx = 1, \quad f(x) \ge 0
$$
$$
F(x) = \int_{-\infty}^{x} f(t)\,dt, \quad f(x) = F'(x)
$$

### 概率
$$
P(a \le X \le b) = \int_a^b f(x)\,dx = F(b) - F(a)
$$

### 期望与方差
$$
E[g(X)] = \int g(x) f(x)\,dx
$$
$$
E[X] = \int x f(x)\,dx, \quad E[X^2] = \int x^2 f(x)\,dx
$$
$$
\text{Var}(X) = E[X^2] - (E[X])^2
$$

### 分位数
$$
F(m) = 0.5, \quad F(Q_1) = 0.25, \quad F(Q_3) = 0.75
$$

### 变换 CDF 法
$$
F_Y(y) = P(g(X) \le y), \quad f_Y(y) = F_Y'(y)
$$

## 题型速览

| 题型 | 核心操作 | 常考分值 |
|------|---------|----------|
| 求常数 $k$ | $\int f = 1$ | 2-3 |
| 求 CDF | $\int_{-\infty}^x f$ | 4-6 |
| 求 $E(X)$ | $\int xf$ | 2-3 |
| 求 $\text{Var}(X)$ | $\int x^2f - (E[X])^2$ | 3-5 |
| 中位数/四分位数 | 解 $F = 0.5/0.25/0.75$ | 3-5 |
| 变换 $Y = g(X)$ | CDF 法求导 | 5-9 |
| 分段 PDF 综合 | 各段分别处理 | 8-13 |

## 高频红牌警告

1. **写答案前验证** $\int f = 1$ —— 这是最基本的 sanity check
2. **分位数求解后** 确认落在正确区间
3. **变换注意** 单调性 + 定义域 + 链式法则
4. **方差** 是 $E[X^2] - (E[X])^2$，不是 $E[X^2] - E[X]$
5. **$E[g(X)]$** 是 $\int g(x) f(x)\,dx$，不是 $g(E[X])$

## 考场检查清单

- [ ] 求常数后是否验证 $f(x) \ge 0$？
- [ ] CDF 各段在边界处是否连续？
- [ ] $F(-\infty) = 0$ 和 $F(\infty) = 1$ 是否满足？
- [ ] 中位数是否在两个分位点之间？
- [ ] $E[X^2]$ 是否用正确积分式？
- [ ] 变换后 $f_Y(y)$ 的 $y$ 定义域是否写明？
- [ ] 所有答案是否按要求精度给出（3 s.f. / exact）？

## 近五年试卷考点分布

| 试卷 | 题号 | 考点 |
|------|------|------|
| 9231/s20/qp/41 | Q3 | PDF → CDF，$E(X)$，中位数 |
| 9231/w20/qp/41 | Q6 | 分段 PDF，常数，$E(X)$，$\text{Var}(X)$ |
| 9231/s21/qp/41 | Q3 | PDF 常数，CDF，$E(X)$ |
| 9231/w21/qp/41 | Q2 | 变换 $Y = g(X)$，CDF 法 |
| 9231/s22/qp/41 | Q3 | PDF，$E(X)$，$\text{Var}(X)$，中位数 |
| 9231/w22/qp/41 | Q5 | 分段 PDF，常数，CDF，四分位数 |
| 9231/s23/qp/41 | Q6 | 变换 $Y = g(X)$，CDF 法求导 |
| 9231/w23/qp/41 | Q4 | PDF，$E[g(X)]$，$\text{Var}(X)$ |
| 9231/s24/qp/41 | Q7 | 分段 PDF 综合，CDF，中位数 |
| 9231/w24/qp/41 | Q4 | 变换 $Y = X^2$，CDF 法 |
| 9231/s25/qp/41 | Q2 | PDF 常数，$E(X)$，中位数 |
| 9231/w25/qp/41 | Q5 | 分段 PDF，常数，CDF，$\text{Var}(X)$ |
