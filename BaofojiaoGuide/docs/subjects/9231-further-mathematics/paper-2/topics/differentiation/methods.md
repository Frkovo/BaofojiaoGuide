---
title: 解题方法
sidebar_position: 4
---

# Methods — Differentiation

## Standard derivatives

| $f(x)$ | $f'(x)$ |
|--------|---------|
| $\sin^{-1} x$ | $\frac{1}{\sqrt{1-x^2}}$ |
| $\cos^{-1} x$ | $-\frac{1}{\sqrt{1-x^2}}$ |
| $\tan^{-1} x$ | $\frac{1}{1+x^2}$ |
| $\sinh^{-1} x$ | $\frac{1}{\sqrt{1+x^2}}$ |
| $\cosh^{-1} x$ | $\frac{1}{\sqrt{x^2-1}}$ |
| $\tanh^{-1} x$ | $\frac{1}{1-x^2}$ |
| $\sinh x$ | $\cosh x$ |
| $\cosh x$ | $\sinh x$ |
| $\tanh x$ | $\operatorname{sech}^2 x$ |

## Maclaurin series

$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots$$

## Implicit differentiation

$\frac{d}{dx}(y^n) = ny^{n-1}\frac{dy}{dx}$, $\frac{d}{dx}(xy) = y + x\frac{dy}{dx}$

## Parametric differentiation

$\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$, $\frac{d^2y}{dx^2} = \frac{d}{dt}(\frac{dy}{dx}) / \frac{dx}{dt}$

## Common errors

- $\frac{d}{dx}\cos^{-1}x = -\frac{1}{\sqrt{1-x^2}}$ (negative sign!)
- $\frac{d}{dx}\tanh^{-1}x = \frac{1}{1-x^2}$, NOT $\frac{1}{1+x^2}$
- $\frac{d}{dx}\cosh x = +\sinh x$, NOT $-\sinh x$
