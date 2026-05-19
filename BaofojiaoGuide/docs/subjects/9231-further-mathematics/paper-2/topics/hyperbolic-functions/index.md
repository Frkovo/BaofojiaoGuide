---
title: Hyperbolic Functions
sidebar_position: 1
---

# Hyperbolic Functions（双曲函数）

---

## 考纲要求

1. 理解双曲函数的定义（指数形式）：$\sinh x = \frac{e^x - e^{-x}}{2}$，$\cosh x = \frac{e^x + e^{-x}}{2}$，$\tanh x = \frac{\sinh x}{\cosh x}$
2. 掌握双曲恒等式：$\cosh^2 x - \sinh^2 x = 1$，$1 - \tanh^2 x = \operatorname{sech}^2 x$，$\coth^2 x - \operatorname{cosech}^2 x = 1$
3. 会画双曲函数图像：$y = \sinh x$，$y = \cosh x$，$y = \tanh x$，$y = \coth x$，$y = \operatorname{sech} x$
4. 理解反双曲函数的定义、定义域和值域
5. 掌握双曲函数及反双曲函数的求导公式
6. 掌握双曲函数及反双曲函数的积分公式
7. 能用双曲代换计算积分
8. 能用双曲函数求弧长（arc length）
9. 能用双曲函数求旋转曲面面积（surface area of revolution）

---

## 常见题型

| 题型 | 分值 | 链接 |
|------|------|------|
| 双曲恒等式证明 | 3 分 | [题型 1](./question-types.md#question-type-1-双曲恒等式证明) |
| 双曲图像与交点 | 2–4 分 | [题型 2](./question-types.md#question-type-2-双曲图像与交点) |
| 双曲函数求导 | 3–5 分 | [题型 3](./question-types.md#question-type-3-双曲函数求导) |
| 弧长问题 | 5–7 分 | [题型 4](./question-types.md#question-type-4-弧长问题) |
| 旋转曲面面积 | 6 分 | [题型 5](./question-types.md#question-type-5-旋转曲面面积) |
| 双曲代换积分 | 4–9 分 | [题型 6](./question-types.md#question-type-6-双曲代换积分) |

---

## 核心公式

### 定义

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

### 恒等式

$$
\cosh^2 x - \sinh^2 x = 1
$$

$$
1 - \tanh^2 x = \operatorname{sech}^2 x
$$

$$
\coth^2 x - \operatorname{cosech}^2 x = 1
$$

### 求导公式

$$
\frac{d}{dx}(\sinh x) = \cosh x, \quad
\frac{d}{dx}(\cosh x) = \sinh x, \quad
\frac{d}{dx}(\tanh x) = \operatorname{sech}^2 x
$$

$$
\frac{d}{dx}(\operatorname{sech} x) = -\operatorname{sech} x \tanh x, \quad
\frac{d}{dx}(\operatorname{cosech} x) = -\operatorname{cosech} x \coth x, \quad
\frac{d}{dx}(\coth x) = -\operatorname{cosech}^2 x
$$

### 反双曲函数求导

$$
\frac{d}{dx}(\sinh^{-1} x) = \frac{1}{\sqrt{1 + x^2}}, \quad
\frac{d}{dx}(\cosh^{-1} x) = \frac{1}{\sqrt{x^2 - 1}}, \quad
\frac{d}{dx}(\tanh^{-1} x) = \frac{1}{1 - x^2}
$$

:::warning[注意定义域]

$\cosh^{-1} x$ 的定义域为 $x \ge 1$，$\tanh^{-1} x$ 的定义域为 $|x| &lt; 1$。

:::

### 积分公式

$$
\int \sinh x \, dx = \cosh x + C, \quad
\int \cosh x \, dx = \sinh x + C, \quad
\int \operatorname{sech}^2 x \, dx = \tanh x + C
$$

$$
\int \frac{1}{\sqrt{a^2 + x^2}} \, dx = \sinh^{-1}\left(\frac{x}{a}\right) + C
$$

$$
\int \frac{1}{\sqrt{x^2 - a^2}} \, dx = \cosh^{-1}\left(\frac{x}{a}\right) + C \quad (x &gt; a)
$$

$$
\int \frac{1}{a^2 - x^2} \, dx = \frac{1}{a} \tanh^{-1}\left(\frac{x}{a}\right) + C \quad (|x| &lt; a)
$$

### 弧长公式

$$
L = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx
$$

### 旋转曲面面积公式

$$
S = 2\pi \int_a^b y \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx
$$

---

## 常见错误

- 混淆 $\sinh x$ 与 $\sin x$ 的导数：$\frac{d}{dx}(\sinh x) = \cosh x$（正号），而非 $\cosh x$ 的负号
- 忘记 $1 - \tanh^2 x = \operatorname{sech}^2 x$ 中的正负号
- 弧长公式中遗漏平方根号内的 $1$
- 反双曲函数求导时忽略定义域限制
- 旋转曲面面积中忘记乘以 $2\pi$
