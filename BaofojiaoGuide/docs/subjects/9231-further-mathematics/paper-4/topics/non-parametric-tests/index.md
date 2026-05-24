---
title: Non-parametric Tests
sidebar_position: 1
---

# Non-parametric Tests（非参数检验）

## 考纲要求

1. 理解非参数检验与参数检验的区别（不假设总体分布形态）
2. **Sign test（符号检验）**：单样本中位数检验、配对数据检验
3. **Wilcoxon signed-rank test（符号秩检验）**：单样本中位数检验、配对数据检验
4. **Wilcoxon rank-sum test（秩和检验 / Mann-Whitney 检验）**：两独立样本比较
5. **正态近似**：当样本量较大时（signed-rank: $n &gt; 20$，rank-sum: $n_1, n_2 &gt; 10$）使用正态近似
6. 何时使用非参数检验 vs 参数检验

## 常见题型

| 题型 | 识别关键词 | 分值占比 |
|------|-----------|---------|
| Wilcoxon Signed-Rank (单样本) | "test whether median = ...", "differences from median" | 8–10 marks |
| Wilcoxon Matched-Pairs | "paired comparison", "before and after", "matched pairs" | 8–10 marks |
| Wilcoxon Rank-Sum (两独立样本) | "two independent samples", "compare two groups" | 8–10 marks |
| Sign Test | "sign test", "ignore magnitude", "count signs" | 6–8 marks |
| Normal Approximation | "large sample", "normal approximation", "n &gt; 20" | 8–10 marks |

## 核心公式

| 公式 | 说明 |
|------|------|
| $T = \min(T^+, T^-)$ | Wilcoxon signed-rank 检验统计量 |
| $T^+ = \sum$ 正秩和，$T^- = \sum$ 负秩和 | 正负秩和 |
| $\mu_T = \dfrac{n(n+1)}{4}$ | 正态近似均值（signed-rank） |
| $\sigma_T = \sqrt{\dfrac{n(n+1)(2n+1)}{24}}$ | 正态近似标准差（signed-rank） |
| $z = \dfrac{T \pm 0.5 - \mu_T}{\sigma_T}$ | 连续性校正后的 $z$ 统计量 |
| $W = \min(R_1, R_2)$ 或直接使用 $R_1$ | Wilcoxon rank-sum 检验统计量 |
| $\mu_W = \dfrac{n_1(n_1 + n_2 + 1)}{2}$ | 正态近似均值（rank-sum） |
| $\sigma_W = \sqrt{\dfrac{n_1 n_2 (n_1 + n_2 + 1)}{12}}$ | 正态近似标准差（rank-sum） |
| $S \sim B(n, 0.5)$ | Sign test 中符号数服从二项分布 |

## 常见错误

- Wilcoxon signed-rank：**假设数据对称**（对称性假设），否则只能用 Sign test
- $T = \min(T^+, T^-)$，记住是比较小的一边
- 正态近似忘记 $+0.5$ 连续性校正
- Rank-sum test 中样本大小记反：$n_1$ 是第一个样本
- 零差异（difference = 0）的处理：排除或按规则分配
- 混淆单尾和双尾的临界值表
