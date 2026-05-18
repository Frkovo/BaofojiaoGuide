---
title: 考前速查
sidebar_position: 7
---

# Differentiation — 考前速查

## 导数表中需特别注意的符号

| 函数 | 导数 | 易错成 |
|------|------|--------|
| $\cos^{-1} x$ | $-\frac{1}{\sqrt{1-x^2}}$ | $+\frac{1}{\sqrt{1-x^2}}$ |
| $\tanh^{-1} x$ | $\frac{1}{1-x^2}$ | $\frac{1}{1+x^2}$ |
| $\cosh x$ | $+\sinh x$ | $-\sinh x$ |
| $\cos^{-1} x$ 是 **唯一负号** 的那个 | — | — |

## Maclaurin
$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots$$

所有导数在 $x=0$ 取值，别忘了阶乘分母。

## 隐函数
$\frac{d}{dx}(y^2) = 2y\frac{dy}{dx}$，$\frac{d}{dx}(xy) = y + x\frac{dy}{dx}$，$\frac{d}{dx}(y) = \frac{dy}{dx}$

## 参数方程
$\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$，$\frac{d^2y}{dx^2} = \frac{d}{dt}(\frac{dy}{dx}) / \frac{dx}{dt}$（不是 $\frac{d^2y/dt^2}{d^2x/dt^2}$）
