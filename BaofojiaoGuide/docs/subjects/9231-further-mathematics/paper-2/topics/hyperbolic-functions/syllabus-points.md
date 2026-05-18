---
title: 考纲要点
sidebar_position: 2
---

# Hyperbolic Functions — 考纲要点

## 1. 指数定义
$\sinh x = \frac{e^x - e^{-x}}{2}$，$\cosh x = \frac{e^x + e^{-x}}{2}$，$\tanh x = \frac{\sinh x}{\cosh x}$
$\operatorname{sech} x = \frac{1}{\cosh x}$，$\operatorname{cosech} x = \frac{1}{\sinh x}$，$\coth x = \frac{\cosh x}{\sinh x}$

## 2. 图像
- $y = \cosh x$：U 形，最小点 $(0,1)$，偶函数
- $y = \sinh x$：过 $(0,0)$，奇函数
- $y = \tanh x$：渐近线 $y = \pm 1$，过 $(0,0)$

## 3. 恒等式
$\cosh^2 x - \sinh^2 x \equiv 1$
$\sinh 2x \equiv 2\sinh x\cosh x$
$\cosh 2x \equiv \cosh^2 x + \sinh^2 x \equiv 2\cosh^2 x - 1 \equiv 2\sinh^2 x + 1$

## 4. 反双曲函数的对数形式
$\sinh^{-1} x = \ln(x + \sqrt{x^2+1})$
$\cosh^{-1} x = \ln(x + \sqrt{x^2-1})$，$x \ge 1$
$\tanh^{-1} x = \frac12\ln\frac{1+x}{1-x}$，$|x| < 1$

## 5. 积分中的应用
$\int\frac{dx}{\sqrt{x^2+a^2}} = \sinh^{-1}\frac{x}{a} + C$
$\int\frac{dx}{\sqrt{x^2-a^2}} = \cosh^{-1}\frac{x}{a} + C$
