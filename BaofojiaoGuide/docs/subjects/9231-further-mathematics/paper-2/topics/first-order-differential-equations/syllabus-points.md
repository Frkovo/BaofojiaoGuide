---
title: 大纲要点
sidebar_position: 2
---

# Syllabus Points — First Order Differential Equations

## 核心知识点

### 1. 一阶线性 ODE 的标准形式

- $\frac{dy}{dx} + P(x)y = Q(x)$
- 注意 $x$ 也可能作为自变量用于 $\frac{dx}{dt}$ 的情形

### 2. 积分因子法

- 定义 $I = e^{\int P(x)\,dx}$
- 乘以 $I$ 后左边化简为 $\frac{d}{dx}(yI)$
- 通解公式：$y = \frac{1}{I}\int IQ\,dx$

### 3. 可分离变量方程

- 形如 $\frac{dy}{dx} = f(x)g(y)$
- 改写为 $\frac{dy}{g(y)} = f(x)\,dx$
- 两边同时积分

### 4. 初值问题（Initial Value Problems）

- 给出 $y(x_0) = y_0$ 的条件
- 用于确定通解中的任意常数
- 有时需要根据物理意义选择正负号

### 5. 特殊形式的积分因子

- 分母含 $\sqrt{x^2 \pm a^2}$ 时，积分因子化为 $x \pm \sqrt{x^2 \pm a^2}$
- 分母为二次式时，积分因子化为 $\sqrt{ax^2+bx+c}$（需配方）
- 三角系数 $P(x) = \cot\theta$ 等时，积分因子简化为 $\sin\theta$ 等

### 6. 常见的 $P(x)$ 积分公式

| $P(x)$ | $\int P\,dx$ | $I = e^{\int P\,dx}$ |
|--------|--------------|----------------------|
| $k$（常数） | $kx$ | $e^{kx}$ |
| $\frac{k}{x}$ | $k\ln x$ | $x^k$ |
| $\tan x$ | $-\ln\cos x$ | $\sec x$ |
| $\cot x$ | $\ln\sin x$ | $\sin x$ |
| $\frac{x}{x^2+a^2}$ | $\frac{1}{2}\ln(x^2+a^2)$ | $\sqrt{x^2+a^2}$ |
| $\frac{x}{\sqrt{x^2+a^2}}$ | $\sqrt{x^2+a^2}$ | $e^{\sqrt{x^2+a^2}}$ |
