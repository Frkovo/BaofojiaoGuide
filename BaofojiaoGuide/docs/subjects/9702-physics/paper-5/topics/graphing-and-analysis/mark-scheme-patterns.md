---
title: 评分规律
sidebar_position: 5
---

# 评分规律

## MS 标记含义

| 标记 | 含义 |
|------|------|
| **M1** | "Method" mark — 方法得分点 |
| **A1** | "Accuracy" mark — 精确度得分点 |
| **B1** | "Basic" mark — 基础得分点 |

## Part (c)(i): Plotting Graph 评分规律

### M1: Points

得分要求：
- 5 或 6 个点全部正确（精确到半小格）
- 使用细 `×` 或 `⊙`
- 坐标轴标注物理量和单位

常见扣分原因：
- 点偏移超过半小格 → 不得分
- 漏掉点或画错点
- 使用过大/过粗的标记

### M1: Error Bars

得分要求：
- 每个点都有对称的 error bar
- error bar 长度 = $2 \times \Delta Y$
- 用直线绘制，两端有 cap

常见扣分原因：
- error bars 不对称
- 漏画某个点的 error bar
- error bar 长度与不确定度不匹配

## Part (c)(ii): Lines 评分规律

### M1: Best Fit Line

得分要求：
- 直线（必须用直尺画）
- 点大致均匀分布在线两侧
- 过原点（如果理论要求）

常见扣分原因：
- 弯曲线或徒手画
- 强行连接第一个和最后一个点
- 过度的异常点

### M1: Worst Acceptable Line

得分要求：
- 通过所有 error bars
- 最陡或最缓（steepest / shallowest）
- 与 best fit 不同

常见扣分原因：
- WAL 与 best fit 重合
- WAL 没穿过所有 error bars
- 没有标记 WAL

## Part (c)(iii): Gradient 评分规律

### M1: Gradient of Best Fit

得分要求：
- 两点在 best fit 线上（**不是**数据点）
- 两点间距 &gt; 直线长度的一半
- 正确的 $\Delta y / \Delta x$ 计算
- 代入正确、单位正确

### M1: Uncertainty

得分要求：
- 正确计算 WAL 的 gradient
- $\text{uncertainty} = |\text{best} - \text{worst}|$
- 结果表示为 $\text{gradient} \pm \text{uncertainty}$

## Part (c)(iv): y-intercept 评分规律

### M1: Correct y-intercept

得分要求：
- 从 $y = mx + c$ 代入计算
- **不能**直接从 y 轴读值
- 给出正确的单位

### M1 (if required): Uncertainty

得分要求：
- 用 WAL 计算 intercept
- $\text{uncertainty} = |c_{\text{best}} - c_{\text{worst}}|$

## 通用 MS 规律

:::note[关键原则]

- 作图题所有 **M1** 分是基于**方法正确**，而不是结果精确
- 即使计算有笔误，如果步骤正确仍可能得 **M1**
- 单位和 significant figures 错误通常扣 **A1**（若题干有 **A1**）
- 标注、标记不清也可能扣分

:::

## 典型分数分布

| 题目部分 | 典型分值 | 关键点 |
|---------|---------|--------|
| (c)(i) plot points | **M1** | 5-6 points accurate |
| (c)(i) error bars | **M1** | symmetrical, all points |
| (c)(ii) best fit | **M1** | straight line, balanced |
| (c)(ii) worst line | **M1** | through all error bars |
| (c)(iii) gradient | **M1** | correct $\Delta y/\Delta x$ |
| (c)(iii) uncertainty | **M1** | $\lvert m_{\text{best}} - m_{\text{worst}}\rvert$ |
| (c)(iv) y-intercept | **M1** | $c = y - mx$ |
