---
title: 常见错误
sidebar_position: 6
---

# 常见错误 — Chi-squared Tests

## 错误 1：自由度算错

**错误**：独立性检验使用 $\mathrm{df} = r \times c$ 或 $\mathrm{df} = r \times c - 1$

**正解**：$\mathrm{df} = (r - 1)(c - 1)$。例如 $2 \times 3$ 表的自由度是 $(2-1)(3-1) = 2$，**不是** $6$ 或 $5$

**错误**：GOF 忘记减去估计参数 $m$

**正解**：$\mathrm{df} = k - 1 - m$。例如 Binomial 估计 $p$，则 $m = 1$；Poisson 估计 $\lambda$，则 $m = 1$；若 $n$ 也未知且估计，则 $m = 2$

## 错误 2：期望频数计算错误

**错误**：独立性检验中 $E_{ij} = \dfrac{O_{ij}}{T}$（忘记行和列和）

**正解**：$E_{ij} = \dfrac{R_i \times C_j}{T}$

**错误**：GOF 中 $E = P(X = x)$（忘记乘 $n$）

**正解**：$E = n \times P(X = x)$

**错误**：$E$ 四舍五入到整数

**正解**：保留至少 2 位小数

## 错误 3：忽略 $E &lt; 5$ 合并规则

**错误**：保留 $E &lt; 5$ 的单元格进行计算

**正解**：必须与相邻单元格合并，直到所有 $E \geq 5$。注意合并后自由度对应减少

## 错误 4：Yates 校正

**错误**：对 $2 \times 2$ 表使用 Yates 连续性校正

**正解**：考纲**不要求** Yates 校正，直接使用 $\chi^2 = \sum (O-E)^2/E$。但若使用了也不扣分

## 错误 5：结论表述错误

**错误**：只写 "Reject $H_0$" 不写原因

**正解**：必须包含三要素：(1) 显著性水平 (2) 统计结论 (3) 上下文结论

示例："Since $\chi^2_{\text{calc}} &gt; \chi^2_{\text{crit}}$ at the 5% significance level, we reject $H_0$. There is sufficient evidence to suggest that the variables are not independent."

## 错误 6：合并时搞错类别

**错误**：合并 $E &lt; 5$ 但把不相邻的类合并

**正解**：只能合并相邻的类别（通常是尾部合并）。独立性检验中合并整行或整列

## 错误 7：忘记说明估计的参数

**错误**：Binomial GOF 中估计了 $p$ 但不说明，自由度仍用 $k-1$

**正解**：必须说明估计了 $m$ 个参数，自由度 $= k - 1 - m$

## 错误 8：使用错误的分布计算概率

**错误**：应该用 Binomial 但用了 Poisson

**正解**：仔细读题确认理论分布类型。题目会明确说明 "test using a Binomial model" 或 "test using a Poisson model"
