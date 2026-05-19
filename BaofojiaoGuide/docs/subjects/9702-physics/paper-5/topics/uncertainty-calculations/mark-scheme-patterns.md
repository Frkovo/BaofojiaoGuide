---
title: 评分规律
sidebar_position: 5
---

# 评分规律

## MS 标记含义

| 标记 | 含义 |
|------|------|
| **M1** | "Method" mark — 方法得分点（计算正确） |
| **A1** | "Accuracy" mark — 精确度得分点（不确定度正确） |
| **B1** | "Basic" mark — 基础得分点 |
| **D1** | "Detail" mark — 细节得分点 |

## Uncertainty in Derived Quantities 评分规律

### **M1**: Derived quantity 计算正确

得分要求：
- 对每一行的 derived quantity 进行正确计算
- 常用计算：$\ln(V/\text{V})$, $\lg(M/10^{30})$, $1/d$, $1/\sqrt{h}$
- 保留足够的小数位数

扣分原因：
- 计算错误
- 有效数字位数不一致
- 没有计入常数（如除以 $\text{V}$ 或 $10^{30}$）

### **A1**: Uncertainty 计算正确

得分要求：
- 使用正确的 propagation formula
- 在表格中为每个 derived quantity 列出对应的 uncertainty
- uncertainty 的有效数字位数合理（通常 1-2 s.f.）

扣分原因：
- 公式错误
- uncertainty 位数不一致
- 忘记列出

### MS 典型句式

| 得分点 | MS 句式 |
|-------|--------|
| **M1** | "All values of $\ln(V/\text{V})$ correct" |
| **A1** | "$\Delta(\ln V) = \Delta V / V$ stated and values correct" |
| **M1** | "Values of $1/d$ correct to 3 s.f." |
| **A1** | "$\Delta(1/d) = \Delta d / d^2$ and values correct to 1 or 2 s.f." |

## Gradient Uncertainty 评分规律

### **M1**: Best fit gradient

得分要求：
- 用 large triangle 计算 gradient
- 在图上标注 triangle 的坐标
- 计算过程清晰

### **A1**: Worst acceptable gradient

得分要求：
- worst line 通过所有 error bars
- 明确标注是哪条 worst line
- 用同样方法计算 gradient

### **A1**: Uncertainty 结果

得分要求：
- $\Delta m = \lvert m_{\text{best}} - m_{\text{worst}}\rvert$
- 最终值表达为 $m \pm \Delta m$
- $\Delta m$ 给 1 位有效数字

### MS 典型句式

| 得分点 | MS 句式 |
|-------|--------|
| **M1** | "Best fit gradient $= \Delta y / \Delta x$ using large triangle" |
| **A1** | "Worst acceptable line drawn through all error bars" |
| **A1** | "$\Delta m = \lvert m_{\text{best}} - m_{\text{worst}}\rvert = 0.04$" |

## Combined Uncertainty 评分规律

### **M1**: Error propagation setup

得分要求：
- 正确写出分数不确定度的组合公式
- $\frac{\Delta C}{C} = \frac{\Delta R}{R} + \frac{\Delta m}{m}$

### **A1**: 数值计算

得分要求：
- 数值代入正确
- 百分比或绝对不确定度正确

### **A1**: 最终答案

得分要求：
- 格式正确: value $\pm$ uncertainty, 带单位
- uncertainty 与 value 的小数位数对齐

## y-intercept Uncertainty 评分规律

### **M1**: Best fit intercept correct

### **A1**: Worst fit intercept correct

### **A1**: $\Delta$ intercept 正确

## 常见 MS 关键词

| 关键短语 | 分值 |
|---------|------|
| "values of ... correct" | **M1** |
| "uncertainty in ... correct" | **A1** |
| "triangle method used" | **M1** |
| "worst acceptable line" | **A1** |
| "error bars considered" | **A1** |
| "final answer with uncertainty" | **A1** |

:::note

Paper 5 Q2 的不确定度部分通常占总分的 **6-8 分**（总分 15 分）。其中约 3-4 分来自表格的 derived quantities，2-3 分来自 gradient/intercept 不确定度，1-2 分来自组合误差。

:::
