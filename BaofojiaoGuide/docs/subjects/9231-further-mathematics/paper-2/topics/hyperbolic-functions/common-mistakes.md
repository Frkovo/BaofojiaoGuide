---
title: 常见错误
sidebar_position: 6
---

# 常见错误（Common Mistakes）

---

## Error 1：混淆 $\sinh$ 与 $\sin$ 的导数

**错误**：认为 $\frac{d}{dx}(\sinh x) = \cosh x$ 与 $\frac{d}{dx}(\sin x) = \cos x$ 类似，但误以为 $\frac{d}{dx}(\cosh x) = -\sinh x$（受 $\frac{d}{dx}(\cos x) = -\sin x$ 影响）。

**修正**：
$$
\frac{d}{dx}(\cosh x) = \sinh x \quad (\text{正号，无负号！})
$$
$$
\frac{d}{dx}(\sinh x) = \cosh x
$$
记忆口诀：双曲函数的导数**没有负号**（除 $\tanh$ 以外的倒数函数有负号）。

---

## Error 2：混淆 $\tanh$ 与 $\tan$ 的导数

**错误**：认为 $\frac{d}{dx}(\tanh x) = \sec^2 x$（三角的公式），或忘记 $\operatorname{sech}^2 x$ 的写法。

**修正**：
$$
\frac{d}{dx}(\tanh x) = \operatorname{sech}^2 x
$$
$$
\frac{d}{dx}(\tan x) = \sec^2 x
$$

---

## Error 3：恒等式中符号错误

**错误**：写出 $\cosh^2 x + \sinh^2 x = 1$ 或 $1 + \tanh^2 x = \operatorname{sech}^2 x$。

**修正**：
$$
\cosh^2 x - \sinh^2 x = 1 \quad (\text{减号！})
$$
$$
1 - \tanh^2 x = \operatorname{sech}^2 x \quad (\text{减号！})
$$

---

## Error 4：弧长计算中 $\sqrt{1 + \sinh^2 x}$ 化简错误

**错误**：认为 $\sqrt{1 + \sinh^2 x} = \sinh x$。

**修正**：$\sqrt{1 + \sinh^2 x} = \sqrt{\cosh^2 x} = \cosh x$（因为 $\cosh x &gt; 0$）。

---

## Error 5：忽略 $\cosh x &gt; 0$ 的性质

**错误**：认为 $\sqrt{\cosh^2 x} = |\cosh x|$ 需要讨论正负。

**修正**：$\cosh x \ge 1$ 对所有 $x$ 成立，因此 $\sqrt{\cosh^2 x} = \cosh x$，无需绝对值。

---

## Error 6：混淆 $1 + \operatorname{cosech}^2 x$ 的化简

**错误**：认为 $1 + \operatorname{cosech}^2 x = \cosh^2 x$。

**修正**：
$$
1 + \operatorname{cosech}^2 x = 1 + \frac{1}{\sinh^2 x} = \frac{\sinh^2 x + 1}{\sinh^2 x} = \frac{\cosh^2 x}{\sinh^2 x} = \coth^2 x
$$

---

## Error 7：旋转曲面面积忘记 $2\pi$

**错误**：写成 $S = \int_a^b y \sqrt{1 + (\frac{dy}{dx})^2} \, dx$，漏掉 $2\pi$。

**修正**：
$$
S = 2\pi \int_a^b y \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx
$$

---

## Error 8：$\cosh^2 x$ 积分时忘记降幂

**错误**：直接积分 $\int \cosh^2 x \, dx = \frac{1}{3}\cosh^3 x$ 或其他错误。

**修正**：使用双角公式降幂：
$$
\cosh^2 x = \frac{1}{2}(\cosh 2x + 1)
$$
$$
\int \cosh^2 x \, dx = \frac{1}{2}\left(\frac{1}{2}\sinh 2x + x\right) + C = \frac{1}{4}\sinh 2x + \frac{x}{2} + C
$$

---

## Error 9：解交点方程时忽略指数函数的正值

**错误**：令 $t = e^x$ 后保留 $t \le 0$ 的解。

**修正**：$t = e^x &gt; 0$，必须舍去所有非正解。

---

## Error 10：双曲代换混淆

**错误**：$\sqrt{a^2 + x^2}$ 用了 $x = a\cosh t$，或 $\sqrt{x^2 - a^2}$ 用了 $x = a\sinh t$。

**修正**：
- $\sqrt{a^2 + x^2}$ → $x = a\sinh t$（因为 $\cosh^2 t - \sinh^2 t = 1$，所以 $1 + \sinh^2 t = \cosh^2 t$）
- $\sqrt{x^2 - a^2}$ → $x = a\cosh t$（因为 $\cosh^2 t - 1 = \sinh^2 t$）

---

## Error 11：隐函数求导忘记 $\frac{dy}{dx}$

**错误**：对 $\tanh y = \cos\left(x + \frac{\pi}{4}\right)$ 两边求导时，左边写成 $\operatorname{sech}^2 y$。

**修正**：左边应为 $\operatorname{sech}^2 y \cdot \frac{dy}{dx}$（链式法则）。

---

## Error 12：画图常见问题

- **$\cosh x$ 画成 $x^2$ 抛物线**：$\cosh x$ 在 $x \to \infty$ 时增长快于多项式，且 $y$ 截距为 $1$（不是 $0$）
- **$\operatorname{sech} x$ 画成 $\sec x$**：$\operatorname{sech} x$ 是偶函数，最大值为 $1$，无渐近线
- **$\coth x$ 漏掉渐近线**：$x = 0$ 和 $y = 1$ 都是渐近线
- **$\tanh x$ 误画为 $\arctan x$**：$\tanh x$ 的渐近线为 $y = \pm 1$，而非 $y = \pm \frac{\pi}{2}$
