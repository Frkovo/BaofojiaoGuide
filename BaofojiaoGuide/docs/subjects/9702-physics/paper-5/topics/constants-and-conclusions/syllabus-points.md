---
title: 考纲要点
sidebar_position: 3
---

# 考纲要点

## 1. 从 Gradient 求常数

### 方法

1. 写出线性化后的方程: $y = mx + c$
2. 确定 gradient $m$ 对应的表达式
3. 代入 gradient 的数值
4. 解出要求的常数
5. 检查单位

### 常见对应关系

| 原始关系 | 线性化 | gradient = |
|---------|-------|-----------|
| $y = ae^{bx}$ | $\ln y = \ln a + bx$ | $b$ |
| $y = ax^n$ | $\lg y = \lg a + n \lg x$ | $n$ |
| $y = \frac{a}{x} + b$ | $y = a(1/x) + b$ | $a$ |
| $V = V_0 e^{-t/RC}$ | $\ln V = \ln V_0 - t/RC$ | $-1/RC$ |
| $f = \frac{v}{4(L+c)}$ | $1/f = \frac{4}{v}L + \frac{4c}{v}$ | $4/v$ |

## 2. 从 y-intercept 求常数

### 方法

1. 确定 y-intercept $c$ 对应的表达式
2. 注意 $\ln$ 或 $\lg$ 形式需取指数:
   - y-intercept $= \ln a \Rightarrow a = e^{\text{intercept}}$
   - y-intercept $= \lg a \Rightarrow a = 10^{\text{intercept}}$
3. 代入数值
4. 检查单位

### 常见对应关系

| 线性化方程 | y-intercept = |
|-----------|--------------|
| $\ln y = \ln a + bx$ | $\ln a$ |
| $\lg y = \lg a + n \lg x$ | $\lg a$ |
| $y = mx + c$ | $c$ |
| $1/f = \frac{4}{v}L + \frac{4c}{v}$ | $4c/v$ |

## 3. 扩展计算

### 方法

- 将之前求出的常数作为已知值代入新公式
- 计算另一个物理量
- 确保单位一致

## 4. 结论与比较

### 判断标准

- 比较实验值与理论值/预期值
- 考虑实验不确定度范围
- 如果预期值在 $(\text{value} \pm \text{uncertainty})$ 范围内 → "results support the relationship"
- 如果预期值在范围外 → "results do not support the relationship"

### 标准句式

- "The accepted value of $X = \_\_\_$ lies within the range $X \pm \Delta X$, therefore the results support the relationship."
- "The expected value lies outside the uncertainty range, therefore the results do not support the relationship."

## 5. 单位检查

### 方法

- 从 gradient 单位推导常数的单位
- 例: gradient 单位 = V/s, 常数 $C = -1/(R \times \text{gradient})$, 代入单位: $1/(\Omega \times \text{V/s}) = \text{s}/\Omega = \text{F}$
- 量纲分析验证结果

## 6. 精度与有效数字

- 最终常数与输入数据的有效数字一致
- 不确定度保留 1 位有效数字
- 值的小数位数与不确定度对齐
