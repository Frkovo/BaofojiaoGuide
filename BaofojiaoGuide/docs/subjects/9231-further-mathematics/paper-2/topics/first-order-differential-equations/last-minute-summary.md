---
title: 考前速记
sidebar_position: 7
---

# 考前速记 — First Order Differential Equations

## 核心公式

| 公式 | 说明 |
|------|------|
| $\frac{dy}{dx} + P(x)y = Q(x)$ | 标准形式 |
| $I = e^{\int P\,dx}$ | 积分因子 |
| $\frac{d}{dx}(yI) = IQ$ | 乘 IF 后化简 |
| $y = \frac{1}{I}\int IQ\,dx$ | 通解公式 |
| $\frac{dy}{dx} = f(x)g(y)$ | 可分离形式 |
| $\int \frac{dy}{g(y)} = \int f(x)\,dx$ | 分离变量 |

## 常见积分因子速查

| 原方程形式 | $P(x)$ | $I$ |
|-----------|--------|-----|
| $\frac{dy}{dx} + ky = Q$ | $k$ | $e^{kx}$ |
| $\frac{dy}{dx} + \frac{k}{x}y = Q$ | $\frac{k}{x}$ | $x^k$ |
| $\frac{dy}{dx} + (\tan x)y = Q$ | $\tan x$ | $\sec x$ |
| $\frac{dy}{dx} + (\cot x)y = Q$ | $\cot x$ | $\sin x$ |
| $\frac{dy}{dx} + \frac{x}{x^2+a^2}y = Q$ | $\frac{x}{x^2+a^2}$ | $\sqrt{x^2+a^2}$ |

## 特殊化简

- $e^{\sinh^{-1}x} = x + \sqrt{x^2+1}$
- $e^{\cosh^{-1}x} = x + \sqrt{x^2-1}$
- $\sqrt{(x+a)^2 + b^2}$ 配方后常见

## 易错点

- 先标准化（$dy/dx$ 系数为 $1$）
- 积分因子可忽略积分常数
- 初值条件必须代入
- 通解中的 $+C$ 不可遗漏

## 解题流程

1. 标准化 → 2. 找 $P$ → 3. 求 $I$ → 4. 乘 $I$ → 5. $\frac{d}{dx}(yI)$ → 6. 积分 → 7. 解出 $y$ → 8. 代入初值
