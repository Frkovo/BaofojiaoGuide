---
title: 考前速记
sidebar_position: 7
---

# 考前速记（Last Minute Summary）

---

## 一、必须背熟的公式

### 定义（指数形式）

$$
\sinh x = \frac{e^x - e^{-x}}{2}, \quad
\cosh x = \frac{e^x + e^{-x}}{2}, \quad
\tanh x = \frac{\sinh x}{\cosh x}
$$

### 三大恒等式

$$
\boxed{\cosh^2 x - \sinh^2 x = 1}
$$

$$
\boxed{1 - \tanh^2 x = \operatorname{sech}^2 x}
$$

$$
\boxed{\coth^2 x - \operatorname{cosech}^2 x = 1}
$$

### 重要推论

$$
1 + \sinh^2 x = \cosh^2 x, \quad
1 + \operatorname{cosech}^2 x = \coth^2 x
$$

### 求导公式

| 函数 | 导数 |
|------|------|
| $\sinh x$ | $\cosh x$ |
| $\cosh x$ | $\sinh x$ |
| $\tanh x$ | $\operatorname{sech}^2 x$ |
| $\operatorname{sech} x$ | $-\operatorname{sech} x \tanh x$ |
| $\operatorname{cosech} x$ | $-\operatorname{cosech} x \coth x$ |
| $\coth x$ | $-\operatorname{cosech}^2 x$ |
| $\sinh^{-1} x$ | $\frac{1}{\sqrt{1 + x^2}}$ |
| $\cosh^{-1} x$ | $\frac{1}{\sqrt{x^2 - 1}}$ |
| $\tanh^{-1} x$ | $\frac{1}{1 - x^2}$ |

### 积分公式

$$
\int \sinh x \, dx = \cosh x + C, \quad
\int \cosh x \, dx = \sinh x + C, \quad
\int \operatorname{sech}^2 x \, dx = \tanh x + C
$$

$$
\int \frac{1}{\sqrt{x^2 + a^2}} \, dx = \sinh^{-1}\left(\frac{x}{a}\right) + C
$$

$$
\int \frac{1}{\sqrt{x^2 - a^2}} \, dx = \cosh^{-1}\left(\frac{x}{a}\right) + C \quad (x &gt; a)
$$

### 弧长

$$
L = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx
$$

### 旋转曲面面积

$$
S = 2\pi \int_a^b y \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx
$$

---

## 二、问题模式速查

| 问题类型 | 关键步骤 | 常用恒等式 |
|----------|----------|------------|
| 恒等式证明 | 写成指数形式 → 展开化简 | $(e^x \pm e^{-x})^2 = e^{2x} \pm 2 + e^{-2x}$ |
| 求交点 | 令等式 → 化为 $t = e^x$ 方程 → 取 $\ln$ | $t &gt; 0$ 条件 |
| 求导 | 识别类型 → 应用公式 → 链式法则 | 隐函数记得 $\frac{dy}{dx}$ |
| 弧长 | $\sqrt{1 + (y')^2}$ → 化为 $\cosh x$ | $1 + \sinh^2 x = \cosh^2 x$ |
| 曲面面积 | $2\pi \int y \sqrt{1 + (y')^2} \, dx$ | $\cosh^2 x = \frac{1}{2}(\cosh 2x + 1)$ |
| 双曲代换 | $\sqrt{a^2 + x^2} \to x = a\sinh t$ | $\cosh^2 t - \sinh^2 t = 1$ |

---

## 三、考试红牌警告

:::danger[考场上绝对不要犯的错误]

1. **忘记 $2\pi$**：旋转曲面面积公式中 $S = 2\pi \int y \sqrt{1 + (y')^2} \, dx$，不是 $\pi$ 也不是无系数
2. **符号弄反**：$\frac{d}{dx}(\cosh x) = +\sinh x$（不是 $-\sinh x$）
3. **$t &gt; 0$ 条件**：令 $t = e^x$ 后必须舍去 $t \le 0$ 的解
4. **$\cosh^2 x$ 降幂**：遇到 $\int \cosh^2 x \, dx$ 必须使用 $\cosh^2 x = \frac{1}{2}(\cosh 2x + 1)$
5. **答案形式**：注意题目要求 "logarithmic form" 还是 "exact value"

:::

---

## 四、考前 5 分钟快速检查清单

- [ ] $\sinh x = \frac{e^x - e^{-x}}{2}$ 指数形式记住了吗？
- [ ] $\cosh^2 - \sinh^2 = 1$ 是减号而不是加号？
- [ ] $1 + \sinh^2 = \cosh^2$ 这个变形会用吗？
- [ ] $\frac{d}{dx}(\cosh x) = \sinh x$ 是正号？
- [ ] 弧长公式里根号内有 $1$？
- [ ] 旋转曲面面积有 $2\pi$？
- [ ] $\cosh^2 x$ 积分要降幂？
- [ ] $\sqrt{x^2 - a^2}$ 代换用 $\cosh$？$\sqrt{a^2 + x^2}$ 代换用 $\sinh$？
- [ ] 隐函数求导记得乘以 $\frac{dy}{dx}$？
- [ ] 答案要写成 $\ln$ 形式？
