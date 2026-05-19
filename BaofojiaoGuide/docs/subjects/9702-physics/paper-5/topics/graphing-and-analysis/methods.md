---
title: 方法框架
sidebar_position: 4
---

# 方法框架

## Overview

Q2 作图题的四步法，每一步对应 MS 中特定的得分点。

---

## Step 1: Choosing Scales

:::note[关键规则]

- 图至少占网格一半（水平和垂直方向）
- 刻度取 1, 2 或 5 个单位对应 2 cm 方格
- 避开 3, 6, 7, 9 等不便读数的刻度
- 原点不需要包含在图中（允许 false origin）

:::

---

## Step 2: Plotting Points and Error Bars

### 2.1 描点

:::note[描点要求]

- 用细小的 `×` 或 `⊙`（直径 &lt; 1 mm）
- 精度到半小格（half a small square）
- 如果点偏离预期位置，检查计算

:::

### 2.2 误差线（Error Bars）

:::note[Error Bars 要求]

- 在 DV 方向画 error bars（通常是 y 方向）
- 对称：中心 = 数据点，长度 = 2 $\times$ 绝对不确定度
- 如果题目要求双向 error bars：x 和 y 方向都要画
- 用细直线绘制，两端有横线（cap）

:::

---

## Step 3: Drawing Lines

### 3.1 Best Fit Line

:::note[最佳拟合线]

- 直尺画直线，作为 line of best fit
- 点大致均匀分布在直线两侧（上下的数量接近）
- 不应强行通过所有点（忽略异常值）

:::

### 3.2 Worst Acceptable Line（WAL）

:::note[WAL 要求]

- 过所有 error bars 的最陡（steepest）或最缓（shallowest）直线
- 标记为 WAL 或用虚线/不同颜色
- 如果 error bars 只有垂直方向，WAL 可在 error bars 内旋转

:::

:::warning[常见错误]

- **不要**连接第一个点和最后一个点
- WAL **必须**穿过所有 error bars
- WAL 和 best fit 不能是同一条线

:::

---

## Step 4: Gradient and y-intercept

### 4.1 计算 Gradient

:::note[梯度计算步骤]

1. 在 best fit 线上选择两个点（**不是**数据点）
2. 两点间距 &gt; 所画直线长度的一半
3. 在点旁标注坐标 $(x_1, y_1)$ 和 $(x_2, y_2)$
4. $\text{gradient} = \frac{y_2 - y_1}{x_2 - x_1}$
5. 保留与数据精度一致的 significant figures

:::

### 4.2 计算 Gradients 的不确定度

:::note[不确定度计算]

- 用相同方法计算 WAL 的 gradient
- $\text{uncertainty} = |\text{gradient}_{\text{best}} - \text{gradient}_{\text{worst}}|$

:::

### 4.3 计算 y-intercept

:::note[y-intercept 方法]

- 使用 $y = mx + c$
- 代入 best fit 线上一点和 gradient
- $c = y - mx$
- 从不直接读纵坐标（false origin 时读数错误）

:::

### 4.4 y-intercept 的不确定度

:::note[不确定度方法]

- 用 WAL 重复同样的计算
- $\text{uncertainty} = |c_{\text{best}} - c_{\text{worst}}|$

:::
