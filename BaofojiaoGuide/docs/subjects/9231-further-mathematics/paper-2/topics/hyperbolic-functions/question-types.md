---
title: 题型分析
sidebar_position: 2
---

# 题型分析

---

## Question Type 1: 双曲恒等式证明

### 如何识别

题目要求证明一个双曲恒等式，如 $\cosh^2 x - \sinh^2 x = 1$ 或 $1 - \tanh^2 x = \operatorname{sech}^2 x$。通常分值为 3 分，使用"Prove"或"Show that"等关键词。

:::note[标准解题方法]

1. 将双曲函数写成指数形式：$\sinh x = \frac{e^x - e^{-x}}{2}$，$\cosh x = \frac{e^x + e^{-x}}{2}$
2. 对表达式进行代数化简
3. 或使用已知恒等式 $\cosh^2 x - \sinh^2 x = 1$ 推导其他恒等式

:::

:::info[评分标准（MS 模式）]

- **B1**：正确写出指数形式
- **B1**：正确展开和化简
- **B1**：得到正确结论

:::

### 例题

> **Example 1 (s20/23 Q6(a))**：Prove that $1 - \tanh^2 \theta = \operatorname{sech}^2 \theta$.

<details>
<summary>📝 MS 展开查看</summary>

$\tanh \theta = \frac{e^\theta - e^{-\theta}}{e^\theta + e^{-\theta}}$ **B1**

$1 - \tanh^2 \theta = \frac{(e^\theta + e^{-\theta})^2 - (e^\theta - e^{-\theta})^2}{(e^\theta + e^{-\theta})^2} = \frac{4}{(e^\theta + e^{-\theta})^2}$ **M1**

$= \frac{1}{\cosh^2 \theta} = \operatorname{sech}^2 \theta$ **A1**

</details>

---

> **Example 2 (w20/21 Q8(b))**：Prove that $\coth^2 x - \operatorname{cosech}^2 x = 1$.

<details>
<summary>📝 MS 展开查看</summary>

$\coth^2 x - \operatorname{cosech}^2 x = \frac{\cosh^2 x}{\sinh^2 x} - \frac{1}{\sinh^2 x}$ **M1**

$= \frac{\cosh^2 x - 1}{\sinh^2 x}$ **M1**

$= \frac{\sinh^2 x}{\sinh^2 x} = 1$ **A1** (using $\cosh^2 x - \sinh^2 x = 1$)

</details>

---

> **Example 3 (w22/21 Q4)**：Prove that $\cosh^2 x - \sinh^2 x \equiv 1$.

<details>
<summary>📝 MS 展开查看</summary>

$\cosh^2 x - \sinh^2 x = \left(\frac{e^x + e^{-x}}{2}\right)^2 - \left(\frac{e^x - e^{-x}}{2}\right)^2$ **B1**

$= \frac{e^{2x} + 2 + e^{-2x}}{4} - \frac{e^{2x} - 2 + e^{-2x}}{4}$ **M1**

$= \frac{4}{4} = 1$ **A1**

</details>

---

> **Example 4 (s25/21 Q6(a))**：Prove that $1 - \tanh^2 u = \operatorname{sech}^2 u$.

<details>
<summary>📝 MS 展开查看</summary>

$\tanh u = \frac{e^u - e^{-u}}{e^u + e^{-u}}$ **B1**

$1 - \tanh^2 u = 1 - \frac{(e^u - e^{-u})^2}{(e^u + e^{-u})^2} = \frac{(e^u + e^{-u})^2 - (e^u - e^{-u})^2}{(e^u + e^{-u})^2}$ **M1**

$= \frac{4}{(e^u + e^{-u})^2} = \frac{1}{\cosh^2 u} = \operatorname{sech}^2 u$ **A1**

</details>

---

:::warning[常见陷阱]

- 注意区分 $\tanh^2 x = (\tanh x)^2$，而非 $\tanh(x^2)$
- 指数形式展开时注意符号：$(e^x - e^{-x})^2 = e^{2x} - 2 + e^{-2x}$，中间是减号
- 不要混淆 $\operatorname{sech}^2 x$ 和 $\sec^2 x$

:::

---

## Question Type 2: 双曲图像与交点

### 如何识别

题目要求在同一坐标系中画出两个双曲函数图像，并求交点（通常要求以对数形式表示）。分值为 2–4 分。

:::note[标准解题方法]

1. 令两函数相等，解方程求交点
2. 将双曲函数写成指数形式，化为关于 $e^x$ 的方程
3. 令 $t = e^x$（$t &gt; 0$），解二次方程
4. 取对数得到 $x = \ln t$
5. 画图时标注关键点、渐近线和交点

:::

:::info[评分标准（MS 模式）]

- **B1**：设等式并正确转化为指数形式
- **M1**：正确解出 $e^x$
- **A1**：以 $\ln$ 形式给出答案
- **B1**：正确画图（形状、渐近线、标注交点）

:::

### 例题

> **Example 1 (s20/21 Q5(a)(b))**：The curve $C_1$ has equation $y = \cosh x$ and the curve $C_2$ has equation $y = \sinh 2x$.
> (a) Find the $x$-coordinate of the point of intersection of $C_1$ and $C_2$, giving your answer in logarithmic form. [4]
> (b) Sketch $C_1$ and $C_2$ on the same diagram. [2]

<details>
<summary>📝 MS 展开查看</summary>

(a)

$\cosh x = \sinh 2x$

$\frac{e^x + e^{-x}}{2} = \frac{e^{2x} - e^{-2x}}{2}$ **M1**

$e^x + e^{-x} = e^{2x} - e^{-2x}$

Multiply by $e^{2x}$: $e^{3x} + e^x = e^{4x} - 1$

$e^{4x} - e^{3x} - e^x - 1 = 0$ **M1**

Let $t = e^x$: $t^4 - t^3 - t - 1 = 0$

$(t^2 + 1)(t^2 - t - 1) = 0$

$t^2 - t - 1 = 0$, so $t = \frac{1 \pm \sqrt{5}}{2}$

Since $t &gt; 0$, $t = \frac{1 + \sqrt{5}}{2}$ **A1**

$x = \ln\left(\frac{1 + \sqrt{5}}{2}\right)$ **A1**

(b)

Correct shape of $y = \cosh x$ (U-shape, minimum at $(0,1)$) **B1**

Correct shape of $y = \sinh 2x$ (passes through origin, steeper than $\sinh x$) and intersection point shown **B1**

</details>

---

> **Example 2 (w20/21 Q8(a))**：Sketch the curve $y = \coth x$ for $x &gt; 0$. State the equations of the asymptotes.

<details>
<summary>📝 MS 展开查看</summary>

Correct shape: decreasing curve from $+\infty$ to $1$ as $x \to \infty$ **B1**

Asymptotes: $x = 0$ (or $y$-axis) and $y = 1$ **B1**

</details>

---

> **Example 3 (w22/21 Q4)**：Sketch the curve $y = \operatorname{sech} x$.

<details>
<summary>📝 MS 展开查看</summary>

Correct shape: bell-shaped curve, maximum at $(0,1)$ **B1**

Asymptotes: $y = 0$ as $x \to \pm\infty$ **B1**

</details>

---

:::warning[常见陷阱]

- 解方程时漏掉 $t &gt; 0$ 的条件，导致多出一个不存在的解
- 忘记 $\cosh x$ 的最小值是 $y=1$ 而非 $y=0$
- $\coth x$ 在 $x \to 0^+$ 时趋于 $+\infty$，而非 $-\infty$
- 画 $\operatorname{sech} x$ 时注意它是偶函数，关于 $y$ 轴对称

:::

---

## Question Type 3: 双曲函数求导

### 如何识别

题目要求对包含双曲函数的表达式求导，通常涉及隐函数微分或链式法则。分值为 3–5 分。

:::note[标准解题方法]

1. 识别函数类型：双曲函数、反双曲函数或复合函数
2. 应用对应的求导公式
3. 若为隐函数，两边同时对 $x$ 求导
4. 化简结果

:::

:::info[评分标准（MS 模式）]

- **B1**：正确应用求导公式（如 $\frac{d}{dx}(\tanh y) = \operatorname{sech}^2 y \cdot \frac{dy}{dx}$）
- **M1**：正确使用链式法则或隐函数求导
- **A1**：化简到指定形式

:::

### 例题

> **Example 1 (s20/23 Q6(b))**：Given that $\tanh y = \cos\left(x + \frac{\pi}{4}\right)$, show that $\frac{dy}{dx} = -\operatorname{cosec}\left(x + \frac{\pi}{4}\right)$.

<details>
<summary>📝 MS 展开查看</summary>

Differentiate both sides:

$\operatorname{sech}^2 y \cdot \frac{dy}{dx} = -\sin\left(x + \frac{\pi}{4}\right)$ **M1**

$\frac{dy}{dx} = -\frac{\sin\left(x + \frac{\pi}{4}\right)}{\operatorname{sech}^2 y} = -\sin\left(x + \frac{\pi}{4}\right) \cosh^2 y$ **M1**

Using $\tanh y = \cos\left(x + \frac{\pi}{4}\right)$ and $1 - \tanh^2 y = \operatorname{sech}^2 y$:

$\cosh^2 y = \frac{1}{\operatorname{sech}^2 y} = \frac{1}{1 - \tanh^2 y} = \frac{1}{1 - \cos^2\left(x + \frac{\pi}{4}\right)} = \frac{1}{\sin^2\left(x + \frac{\pi}{4}\right)}$ **M1**

$\frac{dy}{dx} = -\sin\left(x + \frac{\pi}{4}\right) \cdot \frac{1}{\sin^2\left(x + \frac{\pi}{4}\right)} = -\frac{1}{\sin\left(x + \frac{\pi}{4}\right)} = -\operatorname{cosec}\left(x + \frac{\pi}{4}\right)$ **A1**

</details>

---

> **Example 2 (w20/21 Q8(c))**：Given that $y = \ln\left(\coth\left(\frac{x}{2}\right)\right)$, show that $\frac{dy}{dx} = -\operatorname{cosech} x$.

<details>
<summary>📝 MS 展开查看</summary>

$y = \ln\left(\coth\left(\frac{x}{2}\right)\right)$

$\frac{dy}{dx} = \frac{1}{\coth\left(\frac{x}{2}\right)} \cdot \left(-\frac{1}{2}\operatorname{cosech}^2\left(\frac{x}{2}\right)\right)$ **M1**

$= -\frac{1}{2} \cdot \tanh\left(\frac{x}{2}\right) \cdot \operatorname{cosech}^2\left(\frac{x}{2}\right)$ **M1**

$= -\frac{1}{2} \cdot \frac{\sinh\left(\frac{x}{2}\right)}{\cosh\left(\frac{x}{2}\right)} \cdot \frac{1}{\sinh^2\left(\frac{x}{2}\right)} = -\frac{1}{2\sinh\left(\frac{x}{2}\right)\cosh\left(\frac{x}{2}\right)}$ **M1**

$= -\frac{1}{\sinh x} = -\operatorname{cosech} x$ **A1** (using $\sinh x = 2\sinh\left(\frac{x}{2}\right)\cosh\left(\frac{x}{2}\right)$)

</details>

---

> **Example 3**：Differentiate $y = \sinh^{-1}(2x)$.

<details>
<summary>📝 MS 展开查看</summary>

$\frac{dy}{dx} = \frac{1}{\sqrt{1 + (2x)^2}} \cdot 2$ **M1**

$= \frac{2}{\sqrt{1 + 4x^2}}$ **A1**

</details>

---

:::warning[常见陷阱]

- 隐函数求导时忘记乘以 $\frac{dy}{dx}$
- 混淆 $\frac{d}{dx}(\tanh x) = \operatorname{sech}^2 x$ 与 $\frac{d}{dx}(\tan x) = \sec^2 x$
- 忘记 $\frac{d}{dx}(\cosh x) = \sinh x$ 是正的（与 $\frac{d}{dx}(\cos x) = -\sin x$ 不同）
- 反双曲函数求导时忘记链式法则的內导

:::

---

## Question Type 4: 弧长问题

### 如何识别

题目要求计算曲线在某区间上的弧长，函数通常为 $\cosh x$ 或 $\sinh x$。分值为 5–7 分，为 Paper 2 的常见压轴题。

:::note[标准解题方法]

1. 计算 $\frac{dy}{dx}$
2. 代入弧长公式 $L = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx$
3. 利用双曲恒等式 $\cosh^2 x - \sinh^2 x = 1$ 化简根号内表达式
4. 通常可化简为 $\int \cosh x \, dx$ 或 $\int \operatorname{cosech} x \, dx$ 等形式
5. 积分并代入上下限

:::

:::info[评分标准（MS 模式）]

- **B1**：正确写出弧长公式
- **B1**：正确求出 $\frac{dy}{dx}$
- **M1**：正确化简 $\sqrt{1 + (\frac{dy}{dx})^2}$，通常用到 $\cosh^2 x = 1 + \sinh^2 x$
- **A1**：正确积分
- **A1**：代入上下限得到最终答案

:::

### 例题

> **Example 1 (s20/21 Q5(c))**：Find the arc length of the curve $y = \cosh x$ from $x = 0$ to $x = a$, giving your answer in terms of $a$.

<details>
<summary>📝 MS 展开查看</summary>

$y = \cosh x$, $\frac{dy}{dx} = \sinh x$ **B1**

Arc length $L = \int_0^a \sqrt{1 + \sinh^2 x} \, dx$ **B1**

$= \int_0^a \sqrt{\cosh^2 x} \, dx = \int_0^a \cosh x \, dx$ **M1** (using $1 + \sinh^2 x = \cosh^2 x$)

$= [\sinh x]_0^a = \sinh a$ **A1**

</details>

---

> **Example 2 (w20/21 Q8(d))**：The curve $y = \ln\left(\coth\left(\frac{x}{2}\right)\right)$ has arc length from $x = a$ to $x = 2a$ equal to $\ln 4$. Given $\frac{dy}{dx} = -\operatorname{cosech} x$, find the value of $a$.

<details>
<summary>📝 MS 展开查看</summary>

$\frac{dy}{dx} = -\operatorname{cosech} x$

$L = \int_a^{2a} \sqrt{1 + \operatorname{cosech}^2 x} \, dx$ **B1**

$= \int_a^{2a} \sqrt{\coth^2 x} \, dx$ **M1** (using $1 + \operatorname{cosech}^2 x = \coth^2 x$)

$= \int_a^{2a} \coth x \, dx$ (since $x &gt; 0$, $\coth x &gt; 0$)

$= [\ln(\sinh x)]_a^{2a} = \ln(\sinh 2a) - \ln(\sinh a)$ **M1**

$= \ln\left(\frac{\sinh 2a}{\sinh a}\right) = \ln(2\cosh a)$ **M1**

Set equal to $\ln 4$: $2\cosh a = 4$, $\cosh a = 2$

$a = \cosh^{-1} 2 = \ln(2 + \sqrt{3})$ **A1**

</details>

---

> **Example 3**：Find the arc length of $y = \cosh x$ from $x = 0$ to $x = \ln 2$.

<details>
<summary>📝 MS 展开查看</summary>

$\frac{dy}{dx} = \sinh x$

$L = \int_0^{\ln 2} \sqrt{1 + \sinh^2 x} \, dx = \int_0^{\ln 2} \cosh x \, dx$ **M1**

$= [\sinh x]_0^{\ln 2} = \sinh(\ln 2) - 0$ **M1**

$\sinh(\ln 2) = \frac{e^{\ln 2} - e^{-\ln 2}}{2} = \frac{2 - \frac{1}{2}}{2} = \frac{3}{4}$ **A1**

</details>

---

:::warning[常见陷阱]

- 化简 $\sqrt{1 + \sinh^2 x}$ 时结果应为 $\cosh x$，而非 $\sinh x$
- 注意 $\sqrt{\cosh^2 x} = \cosh x$（因为 $\cosh x &gt; 0$ for all $x$），无需加绝对值
- 当 $\frac{dy}{dx} = \operatorname{cosech} x$ 时，$1 + \operatorname{cosech}^2 x = \coth^2 x$，而非 $\cosh^2 x$
- 积分 $\int \coth x \, dx = \ln|\sinh x| + C$，容易遗忘

:::

---

## Question Type 5: 旋转曲面面积

### 如何识别

题目要求将曲线绕 $x$ 轴旋转所得曲面的面积，函数通常为 $\cosh x$，分值为 6 分。

:::note[标准解题方法]

1. 计算 $\frac{dy}{dx}$
2. 代入旋转曲面面积公式 $S = 2\pi \int_a^b y \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx$
3. 利用双曲恒等式化简
4. 积分

:::

:::info[评分标准（MS 模式）]

- **B1**：正确写出面积公式
- **B1**：代入 $y$ 和 $\frac{dy}{dx}$
- **M1**：化简被积表达式
- **M1**：正确积分
- **A1**：代入上下限
- **A1**：最终答案（通常涉及 $\cosh^2 x$ 积分）

:::

### 例题

> **Example 1 (w20/22 Q2)**：The curve $y = \cosh x$ from $x = 0$ to $x = a$ is rotated about the $x$-axis. Find the surface area of the solid generated.

<details>
<summary>📝 MS 展开查看</summary>

$y = \cosh x$, $\frac{dy}{dx} = \sinh x$

$S = 2\pi \int_0^a y \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx$ **B1**

$= 2\pi \int_0^a \cosh x \sqrt{1 + \sinh^2 x} \, dx$ **B1**

$= 2\pi \int_0^a \cosh x \cdot \cosh x \, dx$ **M1** (using $1 + \sinh^2 x = \cosh^2 x$)

$= 2\pi \int_0^a \cosh^2 x \, dx$

Using $\cosh^2 x = \frac{1}{2}(\cosh 2x + 1)$: **M1**

$S = 2\pi \int_0^a \frac{1}{2}(\cosh 2x + 1) \, dx = \pi \int_0^a (\cosh 2x + 1) \, dx$

$= \pi \left[\frac{1}{2}\sinh 2x + x\right]_0^a = \pi\left(\frac{1}{2}\sinh 2a + a\right)$ **A1**

</details>

---

> **Example 2**：The curve $y = \cosh x$ from $x = 0$ to $x = \ln 3$ is rotated about the $x$-axis. Find the surface area.

<details>
<summary>📝 MS 展开查看</summary>

$S = 2\pi \int_0^{\ln 3} \cosh^2 x \, dx$ **M1**

$= 2\pi \int_0^{\ln 3} \frac{1}{2}(\cosh 2x + 1) \, dx = \pi \int_0^{\ln 3} (\cosh 2x + 1) \, dx$ **M1**

$= \pi \left[\frac{1}{2}\sinh 2x + x\right]_0^{\ln 3}$ **M1**

$\sinh(2\ln 3) = \sinh(\ln 9) = \frac{9 - \frac{1}{9}}{2} = \frac{40}{9}$

$S = \pi\left(\frac{1}{2} \cdot \frac{40}{9} + \ln 3\right) = \pi\left(\frac{20}{9} + \ln 3\right)$ **A1**

</details>

---

:::warning[常见陷阱]

- 旋转曲面面积公式中忘记乘以 $2\pi$
- 忽略 $\cosh^2 x$ 需要降幂处理：$\cosh^2 x = \frac{1}{2}(\cosh 2x + 1)$
- 计算 $\sinh(2\ln a)$ 时小心指数运算：$\sinh(\ln a^2) = \frac{a^2 - a^{-2}}{2}$
- 混淆表面积公式与体积公式

:::

---

## Question Type 6: 双曲代换积分

### 如何识别

被积函数含有 $\sqrt{a^2 + x^2}$、$\sqrt{x^2 - a^2}$ 或 $a^2 - x^2$ 的形式，使用双曲代换比三角代换更简洁。分值为 4–9 分。

:::note[标准解题方法]

1. 识别形式并选择合适的代换：
   - $\sqrt{a^2 + x^2}$：令 $x = a\sinh t$，则 $dx = a\cosh t \, dt$，$\sqrt{a^2 + x^2} = a\cosh t$
   - $\sqrt{x^2 - a^2}$：令 $x = a\cosh t$，则 $dx = a\sinh t \, dt$，$\sqrt{x^2 - a^2} = a\sinh t$
   - $a^2 - x^2$：令 $x = a\tanh t$，则 $dx = a\operatorname{sech}^2 t \, dt$，$a^2 - x^2 = a^2\operatorname{sech}^2 t$
2. 代入并化简积分
3. 使用双曲恒等式进一步化简
4. 积分后用反双曲函数代回

:::

:::info[评分标准（MS 模式）]

- **B1**：选择正确的代换
- **M1**：正确代换 $dx$ 和表达式
- **M1**：化简被积函数
- **A1**：积分结果
- **A1**：代回原变量（如需要）

:::

### 例题

> **Example 1**：Evaluate $\int \frac{1}{\sqrt{4 + x^2}} \, dx$.

<details>
<summary>📝 MS 展开查看</summary>

Let $x = 2\sinh t$, $dx = 2\cosh t \, dt$ **B1**

$\sqrt{4 + x^2} = \sqrt{4 + 4\sinh^2 t} = 2\sqrt{1 + \sinh^2 t} = 2\cosh t$ **M1**

$\int \frac{1}{\sqrt{4 + x^2}} \, dx = \int \frac{2\cosh t}{2\cosh t} \, dt = \int 1 \, dt = t + C$ **M1**

$= \sinh^{-1}\left(\frac{x}{2}\right) + C$ **A1**

</details>

---

> **Example 2**：Evaluate $\int \frac{1}{\sqrt{x^2 - 9}} \, dx$ for $x &gt; 3$.

<details>
<summary>📝 MS 展开查看</summary>

Let $x = 3\cosh t$, $dx = 3\sinh t \, dt$ **B1**

$\sqrt{x^2 - 9} = \sqrt{9\cosh^2 t - 9} = 3\sqrt{\cosh^2 t - 1} = 3\sinh t$ **M1**

$\int \frac{1}{\sqrt{x^2 - 9}} \, dx = \int \frac{3\sinh t}{3\sinh t} \, dt = \int 1 \, dt = t + C$ **M1**

$= \cosh^{-1}\left(\frac{x}{3}\right) + C$ **A1**

</details>

---

> **Example 3**：Evaluate $\int_0^1 \frac{1}{\sqrt{1 + x^2}} \, dx$, giving your answer in logarithmic form.

<details>
<summary>📝 MS 展开查看</summary>

Let $x = \sinh t$, $dx = \cosh t \, dt$ **B1**

When $x = 0$, $t = 0$; when $x = 1$, $t = \sinh^{-1} 1$ **M1**

$\int_0^1 \frac{1}{\sqrt{1 + x^2}} \, dx = \int_0^{\sinh^{-1} 1} \frac{\cosh t}{\cosh t} \, dt = \int_0^{\sinh^{-1} 1} 1 \, dt$ **M1**

$= [t]_0^{\sinh^{-1} 1} = \sinh^{-1} 1$ **A1**

$\sinh^{-1} 1 = \ln(1 + \sqrt{2})$ **A1**

</details>

---

:::warning[常见陷阱]

- 代换后忘记乘以 $dx$ 对应的微分
- 混淆 $\sqrt{a^2 + x^2}$ 和 $\sqrt{x^2 - a^2}$ 的对应代换
- 定积分代换后忘记更新上下限
- 反双曲函数与对数形式的转换不熟练

:::
