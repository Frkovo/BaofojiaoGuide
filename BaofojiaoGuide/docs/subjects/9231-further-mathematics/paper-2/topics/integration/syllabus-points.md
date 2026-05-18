---
title: 考纲要点
sidebar_position: 2
---

# Integration — 考纲要点

## 1. 双曲函数积分
$\int\sinh x\,dx = \cosh x + C$
$\int\cosh x\,dx = \sinh x + C$
$\int\operatorname{sech}^2 x\,dx = \tanh x + C$

## 2. 标准反函数积分
$\int\frac{dx}{\sqrt{a^2-x^2}} = \sin^{-1}\frac{x}{a} + C$
$\int\frac{dx}{a^2+x^2} = \frac1a\tan^{-1}\frac{x}{a} + C$
$\int\frac{dx}{\sqrt{x^2+a^2}} = \sinh^{-1}\frac{x}{a} + C$
$\int\frac{dx}{\sqrt{x^2-a^2}} = \cosh^{-1}\frac{x}{a} + C$

## 3. 三角/双曲代换
$\sqrt{a^2-x^2}$ → $x = a\sin\theta$；$\sqrt{x^2+a^2}$ → $x = a\sinh u$

## 4. 递推公式
分部积分 → $I_n$ 用 $I_{n-1}$ 或 $I_{n-2}$ 表示

## 5. 弧长
直角坐标：$s = \int_a^b \sqrt{1+(dy/dx)^2}\,dx$
参数式：$s = \int_{t_1}^{t_2} \sqrt{(dx/dt)^2+(dy/dt)^2}\,dt$

## 6. 表面积
$S = 2\pi\int_a^b y\sqrt{1+(dy/dx)^2}\,dx$（绕 $x$ 轴）

## 7. 矩形估计
上界用右端点 $f(r/n)$，下界用左端点 $f((r-1)/n)$
