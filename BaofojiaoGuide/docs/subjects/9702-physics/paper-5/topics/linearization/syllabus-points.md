---
title: 考纲要点
sidebar_position: 3
---

# 考纲要点

## 线性化在 Q2 中的分值分配

Paper 5 Q2 共 15 分，其中线性化相关约 6-8 分：

### Part 1: Data Analysis（8-10 分）

| 知识点 | 分值 | 说明 |
|-------|------|------|
| 计算 derived quantities | 2 分 | 计算表格中 $x$ 和 $y$ 轴所需的派生量 |
| 正确画图 | 4 分 | 坐标轴标注、刻度、数据点、误差棒、直线 |
| 求 gradient | 1 分 | 选两个 far apart 的线上点计算 |
| 求 y-intercept | 1 分 | 从图中直接读或 extrapolate |

### Part 2: Linearization Theory（5-7 分）

| 知识点 | 分值 | MS 标记 |
|-------|------|---------|
| 将公式重排成 $y = mx + c$ | 1-2 分 | **M1** |
| 识别 $y$-axis 和 $x$-axis 的表达式 | 1 分 | **A1** |
| 写出 gradient 表达式 | 1 分 | **B1** |
| 写出 y-intercept 表达式 | 1 分 | **B1** |
| 从 gradient/intercept 反求题目常数 | 1 分 | **B1** |

## 三种必考线性化形式

### 1. Direct Linearization ($y = mx + c$)

- 题目特征：公式本身是或可以重排为线性
- 考题形式：直接问 "determine expressions for gradient and y-intercept"
- 典型例子：$E = I(R_1 + R_2 + r)$, $V = E - Ir$

### 2. Log-Log Linearization ($\lg y = \lg a + n \lg x$)

- 题目特征：公式为 $y = ax^n$ 形式
- 考题形式："plot $\lg y$ against $\lg x$"
- 注意：$a = 10^{\text{intercept}}$，不是直接读 intercept

### 3. Log-Linear Linearization ($\ln y = \ln a + kx$)

- 题目特征：公式为 $y = ae^{kx}$ 形式
- 考题形式："plot $\ln y$ against $x$"
- 注意：$a = e^{\text{intercept}}$，$k = \text{gradient}$

## 评分总览

| 部分 | 内容 | 分值 |
|------|------|------|
| Data analysis | 表格计算 + 画图 | 8-10 |
| Linearization theory | 变形 + 识别 gradient/intercept | 5-7 |
| **Total** | | **15** |
