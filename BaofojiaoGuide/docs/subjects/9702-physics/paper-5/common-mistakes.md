---
title: 常见错误
sidebar_position: 5
---

# 常见错误

## Q1 实验设计常见错误

### 1. 变量定义错误

- **错误**: 混淆独立变量和因变量
- **正确**: Independent variable: what you change; Dependent variable: what you measure
- **例子**: 如果题目说"investigate how $k$ varies with $A$"，则 $A$ 是 IV，$k$ 是 DV

### 2. 控制变量表述不完整

- **错误**: 只说"keep all other variables constant"
- **正确**: 具体列出 2-3 个可识别的变量并说明如何控制

### 3. 缺少实验范围

- **错误**: 没有说明测量多少组数据
- **正确**: "take measurements for at least 6 different values of $X$ covering a suitable range"

### 4. 重复测量缺失

- **错误**: "measure $Y$ for each value of $X$"
- **正确**: "repeat the measurement of $Y$ at each value of $X$ and calculate the mean"

### 5. 分析方法错误

- **错误**: "plot a graph of $k$ against $A$" 但关系是非线性的
- **正确**: 线性化后作图，如 $k$ against $A^{-3/2}$ 或 $\lg k$ against $\lg A$

### 6. 安全措施太笼统

- **错误**: "be careful" 或 "wear safety goggles" 没有上下文
- **正确**: 针对具体风险的安全措施，如"wear safety goggles to protect eyes from snapping springs"

### 7. 仪器选择不当

- **错误**: 用 ruler 测量小直径 (应使用 micrometer)
- **正确**: 根据被测量的精度要求选择仪器 (micrometer for $d&lt;1$ cm, ruler for $d&gt;10$ cm)

## Q2 数据分析常见错误

### 8. 梯度表达式错误

- **错误**: 忘记负号或符号错误
- **正确**: 仔细代入，检查表达式在物理上是否合理

### 9. 对数不确定度计算错误

- **错误**: $\Delta(\ln x) = \ln(\Delta x)$
- **正确**: $\Delta(\ln x) = \frac{\Delta x}{x}$

### 10. 有效数字问题

- **错误**: $\ln$ 值保留的有效数字与原始数据不一致
- **正确**: $\ln$ 值的小数位数 = 原始数据有效位数

### 11. 错误线的画法

- **错误**: 最差直线连接第一个和最后一个数据点
- **正确**: 最差直线是通过所有 error bar 的最陡/最缓直线

### 12. 用假原点求 y-intercept

- **错误**: 直接从 y 轴读 intercept
- **正确**: 代入 $y = mx + c$ 计算

### 13. 梯度计算点间隔不够

- **错误**: 选的两个点太近
- **正确**: 选的两个点间隔 &gt; 所画直线长度的一半

### 14. 缺少单位

- **错误**: 最后答案只有数值
- **正确**: 常数 + 单位 (dimensionally correct)

### 15. 忘记 error bars

- **错误**: 只画了 best fit line 没有 error bars
- **正确**: 所有点必须画 error bars，WAL 要通过所有 error bars
