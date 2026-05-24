---
title: 考前总结
sidebar_position: 7
---

# 考前总结 — Non-parametric Tests

## 核心公式速记

| 检验 | 统计量 | 正态近似 |
|------|--------|---------|
| Signed-rank | $T = \min(T^+, T^-)$ | $\mu = \frac{n(n+1)}{4}$, $\sigma = \sqrt{\frac{n(n+1)(2n+1)}{24}}$ |
| Rank-sum | $W = R_1$ | $\mu = \frac{n_1(n_1+n_2+1)}{2}$, $\sigma = \sqrt{\frac{n_1 n_2 (n_1+n_2+1)}{12}}$ |
| Sign test | $S \sim B(n, 0.5)$ | — |

## 三种检验速判表

| 数据类型 | 检验方法 | 假设条件 |
|---------|---------|---------|
| 单样本 vs 给定中位数 | Wilcoxon signed-rank | 对称分布 |
| 单样本 vs 给定中位数 | Sign test | 无（仅需随机性） |
| 配对数据（before/after） | Wilcoxon signed-rank | 差异对称 |
| 配对数据（before/after） | Sign test | 无 |
| 两独立样本 | Wilcoxon rank-sum | 形状相似 |
| 两独立样本 | Sign test (配对后) | 无 |

## 解题步骤速记

### Wilcoxon Signed-Rank
1. 差值 → 绝对值 → 排序 → 赋秩 → 加符号
2. 正秩和 $T^+$，负秩和 $T^-$
3. $T = \min(T^+, T^-)$
4. 查表：$n$, $\alpha$, 单/双尾
5. $T \leq$ 临界值 ⇒ 拒绝 $H_0$

### Wilcoxon Rank-Sum
1. 合并 → 排序 → 赋秩
2. 计算第一个样本的秩和 $R_1$
3. 查表：$n_1$, $n_2$, $\alpha$
4. $R_1$ 在临界值区间外 ⇒ 拒绝 $H_0$

### Sign Test
1. 记符号（+, -, 0）
2. 排除 0，$n$ = 非零数
3. $S$ = 较少符号数
4. $P(S \leq s)$ from $B(n, 0.5)$
5. 双尾 p-value $= 2 \times P$

## 正态近似条件

| 检验 | 条件 | 连续性校正 |
|------|------|-----------|
| Signed-rank | $n &gt; 20$ | $z = \frac{T \pm 0.5 - \mu}{\sigma}$ |
| Rank-sum | $n_1, n_2 &gt; 10$ | $z = \frac{W \pm 0.5 - \mu}{\sigma}$ |

## 考试中常见陷阱

- ❌ $T = \max(T^+, T^-)$ 不是 $\min$
- ❌ 忘记排除零差异
- ❌ 秩从大到小排
- ❌ 连续性校正用错方向
- ❌ Wilcoxon 用于不对称数据
- ❌ Sign test 双尾忘记 $\times 2$
- ✅ **先判断数据类型**，再选检验方法
