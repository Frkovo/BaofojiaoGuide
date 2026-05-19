---
title: MS 模式
sidebar_position: 5
---

# MS 模式

## MS 常见标记含义

| 标记 | 含义 |
|------|------|
| **M1** | Method mark — 方法得分点 |
| **A1** | Accuracy mark — 精确度得分点 |
| **B1** | Basic mark — 基础得分点 |
| **B1 × 2** | 两个独立的基础得分点 |

## Q2(a) 线性化变形 — MS 常见模式

### 标准结构

每个 Q2(a) 的 MS 通常包含恰好 2 个 **B1** 分：

- **B1**: Correct expression for gradient
- **B1**: Correct expression for y-intercept

### 得分句式

| 得分点 | 标准写法 | 例子 |
|-------|---------|------|
| Gradient | $\text{gradient} = \text{expression}$ | $\text{gradient} = -\frac{1}{CR}$ |
| Y-intercept | $y\text{-intercept} = \text{expression}$ | $y\text{-intercept} = \ln\left(\frac{Q_0}{C}\right)$ |
| 带 |gradient $= n$ | gradient $= n$ |
| 带 $\lg$ 截距 | $y\text{-intercept} = \lg(\text{constant})$ | $y\text{-intercept} = \lg(SZ)$ |

### 常见信号词

MS 中出现 "hence" 意味着前一步的答案需要用于后一步。例如：

- Q2(a) 求出 gradient 和 intercept 表达式
- Q2(b) 用这些表达式计算具体常数

## 不同题型 MS 关键词对比

### Standard Linearization

| MS 字句 | 含义 |
|---------|------|
| "correct rearrangement" | 公式变形成 $y = mx + c$ 正确 |
| "correct identification of $y$ and $x$" | 正确识别 $y$ 轴和 $x$ 轴 |
| "gradient = ..." | 系数正确 |
| "y-intercept = ..." | 常数项正确 |

### Log-Log Linearization

| MS 字句 | 含义 |
|---------|------|
| "takes logs" | 对两边取 $\lg$ |
| "gradient = $n$" | 指数正确 |
| "$y$-intercept = $\lg(constant)$" | 对数截距正确 |
| "$a = 10^{\text{intercept}}$" | 正确反解常数 $a$ |

### Log-Linear Linearization

| MS 字句 | 含义 |
|---------|------|
| "takes natural logs" | 取自然对数 $\ln$ |
| "gradient = $k$" 或 "gradient = $-\mu$" | 指数系数正确，注意符号 |
| "$a = e^{\text{intercept}}$" | 正确反解常数 $a$ |

## 常见扣分点

| 错误 | MS 反应 |
|------|---------|
| 符号错误 | 0 分 — gradient sign wrong |
| 混淆 $\ln$ 和 $\lg$ | 0 分 — wrong log base |
| 截距表达式不完全 | 扣 1 分 — e.g. 只写 $\lg a$ 没写 $a = ...$ |
| 忘记对常数取对数 | 0 分 — $y$-intercept 应为 $\lg(constant)$ 而非 $constant$ |

:::note[评分提醒]

Paper 5 Q2(a) 的两个 **B1** 分是独立的。即使 gradient 写错了，intercept 写对了仍然可得 1 分。

:::
