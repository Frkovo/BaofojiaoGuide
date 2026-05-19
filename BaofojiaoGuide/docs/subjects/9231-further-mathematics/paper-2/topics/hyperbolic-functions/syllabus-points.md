---
title: 考纲要点
sidebar_position: 3
---

# 考纲要点（Syllabus Points）

以下为 **CAIE 9231 Further Mathematics Paper 2** 中关于 Hyperbolic Functions 的考纲要求。

---

## 1. 双曲函数的定义

- 理解 $\sinh x$、$\cosh x$、$\tanh x$ 及其倒数函数的指数形式定义
- 掌握以下关系：
  $$
  \sinh x = \frac{e^x - e^{-x}}{2}, \quad
  \cosh x = \frac{e^x + e^{-x}}{2}, \quad
  \tanh x = \frac{\sinh x}{\cosh x}
  $$
  $$
  \operatorname{cosech} x = \frac{1}{\sinh x}, \quad
  \operatorname{sech} x = \frac{1}{\cosh x}, \quad
  \coth x = \frac{1}{\tanh x}
  $$

## 2. 双曲恒等式

- 掌握并能够证明核心恒等式：
  - $\cosh^2 x - \sinh^2 x \equiv 1$
  - $1 - \tanh^2 x \equiv \operatorname{sech}^2 x$
  - $\coth^2 x - \operatorname{cosech}^2 x \equiv 1$
- 能够利用上述恒等式推导其他关系
- 注意与三角恒等式的类比关系（Osborne's rule）

## 3. 双曲函数的图像

- 能够画出 $y = \sinh x$、$y = \cosh x$、$y = \tanh x$ 的图像
- 能够画出 $y = \operatorname{sech} x$、$y = \operatorname{cosech} x$、$y = \coth x$ 的图像
- 掌握各函数的关键特征：
  - 定义域和值域
  - 对称性（奇偶性）
  - 渐近线
  - 极值点
  - 与坐标轴的交点

## 4. 反双曲函数

- 理解 $\sinh^{-1} x$、$\cosh^{-1} x$、$\tanh^{-1} x$ 的定义
- 掌握反双曲函数的定义域和值域：
  - $\sinh^{-1} x$：定义域 $\mathbb{R}$，值域 $\mathbb{R}$
  - $\cosh^{-1} x$：定义域 $x \ge 1$，值域 $y \ge 0$
  - $\tanh^{-1} x$：定义域 $|x| &lt; 1$，值域 $\mathbb{R}$
- 掌握反双曲函数的对数形式：
  $$
  \sinh^{-1} x = \ln\left(x + \sqrt{x^2 + 1}\right)
  $$
  $$
  \cosh^{-1} x = \ln\left(x + \sqrt{x^2 - 1}\right) \quad (x \ge 1)
  $$
  $$
  \tanh^{-1} x = \frac{1}{2}\ln\left(\frac{1 + x}{1 - x}\right) \quad (|x| &lt; 1)
  $$

## 5. 双曲函数的求导

- 掌握基本求导公式：
  - $\frac{d}{dx}(\sinh x) = \cosh x$
  - $\frac{d}{dx}(\cosh x) = \sinh x$
  - $\frac{d}{dx}(\tanh x) = \operatorname{sech}^2 x$
  - $\frac{d}{dx}(\operatorname{sech} x) = -\operatorname{sech} x \tanh x$
  - $\frac{d}{dx}(\operatorname{cosech} x) = -\operatorname{cosech} x \coth x$
  - $\frac{d}{dx}(\coth x) = -\operatorname{cosech}^2 x$
- 掌握反双曲函数求导公式：
  - $\frac{d}{dx}(\sinh^{-1} x) = \frac{1}{\sqrt{1 + x^2}}$
  - $\frac{d}{dx}(\cosh^{-1} x) = \frac{1}{\sqrt{x^2 - 1}}$
  - $\frac{d}{dx}(\tanh^{-1} x) = \frac{1}{1 - x^2}$
- 能够使用链式法则、乘积法则、商法则求复合双曲函数
- 能够对隐函数形式的双曲方程求导

## 6. 双曲函数的积分

- 掌握基本积分公式：
  - $\int \sinh x \, dx = \cosh x + C$
  - $\int \cosh x \, dx = \sinh x + C$
  - $\int \operatorname{sech}^2 x \, dx = \tanh x + C$
  - $\int \operatorname{cosech} x \coth x \, dx = -\operatorname{cosech} x + C$
  - $\int \operatorname{sech} x \tanh x \, dx = -\operatorname{sech} x + C$
  - $\int \operatorname{cosech}^2 x \, dx = -\coth x + C$
- 掌握与反双曲函数相关的积分公式：
  - $\int \frac{1}{\sqrt{a^2 + x^2}} \, dx = \sinh^{-1}\left(\frac{x}{a}\right) + C$
  - $\int \frac{1}{\sqrt{x^2 - a^2}} \, dx = \cosh^{-1}\left(\frac{x}{a}\right) + C \quad (x &gt; a)$
  - $\int \frac{1}{a^2 - x^2} \, dx = \frac{1}{a}\tanh^{-1}\left(\frac{x}{a}\right) + C \quad (|x| &lt; a)$

## 7. 双曲代换

- 能够使用双曲代换计算积分：
  - $\sqrt{a^2 + x^2}$ 形式：令 $x = a\sinh t$
  - $\sqrt{x^2 - a^2}$ 形式：令 $x = a\cosh t$
  - $a^2 - x^2$ 形式：令 $x = a\tanh t$

## 8. 弧长

- 能够计算以双曲函数形式给出的曲线的弧长：
  $$
  L = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx
  $$
- 常用恒等式化简：$1 + \sinh^2 x = \cosh^2 x$

## 9. 旋转曲面面积

- 能够计算曲线绕 $x$ 轴旋转所得曲面的面积：
  $$
  S = 2\pi \int_a^b y \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx
  $$
- 熟练使用 $\cosh^2 x = \frac{1}{2}(\cosh 2x + 1)$ 进行积分
