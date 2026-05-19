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

## Part (d)(i): Calculate Constant from Gradient 评分规律

### **M1**: 写出常数与 gradient 的关系式

得分要求：
- 正确写出 gradient $=$ expression with constant
- 正确反解 constant $=$ f(gradient)

### **A1**: 数值代入正确

得分要求：
- gradient 值代入正确
- 其他已知值（如 $R$, $k$ 等）代入正确
- 计算过程无算术错误

### **A1**: 单位正确

得分要求：
- 常数给出正确的单位
- 单位从公式推导得出

### MS 典型句式

| 得分点 | MS 句式 |
|-------|--------|
| **M1** | "$C = -1/(Rk)$" |
| **A1** | "$C = 4.7 \times 10^{-6}\ \text{F}$" |
| **A1** | "Correct unit: F" |

## Part (d)(ii): Uncertainty in Constant 评分规律

### **M1**: 正确写出误差传播公式

得分要求：
- $\frac{\Delta C}{C} = \frac{\Delta R}{R} + \frac{\Delta k}{k}$
- 所有不确定度来源都包含

### **A1**: 数值计算正确

得分要求：
- 代入数值正确
- 百分比 → 绝对 转换正确

### **A1**: 最终答案格式正确

得分要求：
- value $\pm$ uncertainty, 带单位
- uncertainty 1 s.f., value 对齐

### MS 典型句式

| 得分点 | MS 句式 |
|-------|--------|
| **M1** | "$\frac{\Delta C}{C} = \frac{\Delta R}{R} + \frac{\Delta k}{k}$" |
| **A1** | "$C = (4.7 \pm 0.5) \times 10^{-6}$ F" |

## Part (e): Extension Calculation 评分规律

### **M1**: 使用正确的公式

得分要求：
- 使用题目要求的关系式
- 正确代入之前求出的常数

### **A1**: 数值计算正确

### **A1**: 单位正确

## Part (f): Conclusion 评分规律

### **M1**: 比较实验值与理论/预期值

得分要求：
- 明确写出实验值 range（考虑 uncertainty）
- 明确写出理论/预期值

### **A1**: 正确判断是否在范围内

得分要求：
- 理论值在实验值 uncertainty 范围内 → "supports"
- 理论值在范围外 → "does not support"

### **A1**: 表达完整

得分要求：
- 句式完整，包含比较的依据
- 提及 uncertainty / experimental error

### MS 典型句式

| 得分点 | MS 句式 |
|-------|--------|
| **M1** | "Compares $4.7\ \Omega$ with $(4.5 \pm 0.3)\ \Omega$" |
| **A1** | "The value lies within the uncertainty range, therefore supports" |
| **A1** | "Clear conclusion with reference to experimental uncertainty" |

## 常见扣分原因

- ❌ 忘记写单位
- ❌ 从 y-intercept 求常数时忘记取指数
- ❌ 符号错误（gradient 为负时代入出错）
- ❌ 结论中没有提及 uncertainty
- ❌ 有效数字位数过多/过少
- ❌ 扩展计算中使用错误（未新求出的）的常数

:::note

常数与结论部分通常占 Q2 的 **6-8 分**（总分 15 分），其中 (d)(i) 约 3 分，(d)(ii) 约 2-3 分，(e)-(f) 约 2-3 分。

:::
