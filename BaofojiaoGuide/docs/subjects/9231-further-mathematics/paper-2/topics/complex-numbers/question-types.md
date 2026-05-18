---
title: 题型分析
sidebar_position: 3
---

# 题型分析 — Complex Numbers

---

## Question Type 1: de Moivre proof by induction

### 标准方法

**Base case $n=1$：**
$(\cos\theta + i\sin\theta)^1 = \cos\theta + i\sin\theta = \cos(1\cdot\theta) + i\sin(1\cdot\theta)$ ✓

**Induction hypothesis：** 设 $n=k$ 成立

**Induction step：**
$$
\begin{aligned}
(\cos\theta + i\sin\theta)^{k+1}
&= (\cos\theta + i\sin\theta)^k(\cos\theta + i\sin\theta) \\
&= (\cos k\theta + i\sin k\theta)(\cos\theta + i\sin\theta) \\
&= \cos(k+1)\theta + i\sin(k+1)\theta
\end{aligned}
$$

**结论：** 由数学归纳法，对所有正整数 $n$ 成立

---

## Question Type 2: Multiple angle formulae

### 标准方法

$(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$

1. 左边用二项式定理展开
2. 取实部 $= \cos n\theta$，取虚部 $= \sin n\theta$
3. 用 $\sin^2\theta = 1 - \cos^2\theta$ 化为纯 $\cos\theta$ 表达

### 完整原题

**Example 1 — 9231/s23/qp/22 Q3(a) (5 marks):**

> By considering $(z+z^{-1})^4$ where $z = \cos\theta + i\sin\theta$, use de Moivre to show that $\cos 4\theta = 8\cos^4\theta - 8\cos^2\theta + 1$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: $(z+z^{-1})^4 = z^4 + 4z^2 + 6 + 4z^{-2} + z^{-4}$
- **M1**: $z^n+z^{-n} = 2\cos n\theta$
- **A1**: $= 2\cos 4\theta + 8\cos 2\theta + 6$
- **M1**: $\cos 2\theta = 2\cos^2\theta - 1$
- **A1**: $\cos 4\theta = 8\cos^4\theta - 8\cos^2\theta + 1$

</details>

**Example 2 — 9231/w22/qp/22 Q5(b) (4 marks):**

> Use de Moivre's theorem to show that $\cos 4\theta = 8\cos^4\theta - 8\cos^2\theta + 1$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: $(\cos\theta+i\sin\theta)^4 = \cos4\theta + i\sin4\theta$
- **M1**: expands LHS using binomial theorem
- **A1**: correct expansion
- **M1**: equates real parts, uses $\sin^2\theta = 1-\cos^2\theta$
- **A1**: AG

</details>

**Example 3 — 9231/w23/qp/22 Q3(a) (4 marks):**

> Use de Moivre's theorem to show that $\cos 5\theta = 16\cos^5\theta - 20\cos^3\theta + 5\cos\theta$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: $(\cos\theta+i\sin\theta)^5 = \cos5\theta + i\sin5\theta$
- **M1**: binomial expansion
- **M1**: equates real parts, uses $\sin^2\theta = 1-\cos^2\theta$
- **A1**: AG

</details>

---

## Question Type 3: Power reduction

### 标准方法

设 $z = \cos\theta + i\sin\theta = e^{i\theta}$，$z^{-1} = e^{-i\theta}$

$$
\cos\theta = \frac{z+z^{-1}}{2},\qquad
\sin\theta = \frac{z-z^{-1}}{2i}
$$

$$
\cos n\theta = \frac{z^n+z^{-n}}{2},\qquad
\sin n\theta = \frac{z^n-z^{-n}}{2i}
$$

展开乘方后用 $z^n + z^{-n} = 2\cos n\theta$ 归并。

---

## Question Type 4: $C + iS$ method for series summation

### 标准方法

1. 设 $C = \sum \cos(\ldots)$，$S = \sum \sin(\ldots)$
2. $C + iS = \sum e^{i(\ldots)}$，这是等比数列
3. 求等比数列和
4. 取实部得 $C$，取虚部得 $S$

### 常用结果

$$
\sum_{r=0}^{n-1} \cos(2r+1)\theta = \frac{\sin 2n\theta}{2\sin\theta}
$$
$$
\sum_{r=0}^{n-1} \sin(2r+1)\theta = \frac{1 - \cos 2n\theta}{2\sin\theta}
$$

### 完整原题

**Example 1 — 9231/w20/qp/22 Q7 (7 marks):**

> (a) Show that $\displaystyle\sum_{r=1}^n z^{2r} = \frac{z^{2n+1} - z}{z - 1}$, for $z \neq 0,1,-1$.
>
> (b) By letting $z = \cos\theta + i\sin\theta$, show that
> $$1 + 2\sum_{r=1}^n \cos 2r\theta = \frac{\sin(2n+1)\theta}{\sin\theta}.$$

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):** GP sum formula, **M1A1**
**MS (b):**
- **M1**: $1 + 2\sum \cos 2r\theta = \sum_{r=0}^n z^{2r} + \sum_{r=0}^n z^{-2r} - 1$
- **M1**: sums each GP
- **A1**: expression correct
- **M1**: simplifies using $z = e^{i\theta}$
- **A1**: AG

</details>

**Example 2 — 标准题型：求 $\cos\theta + \cos3\theta + \cdots + \cos(2n-1)\theta$**

> 设 $C = \sum_{r=1}^n \cos(2r-1)\theta$，$S = \sum_{r=1}^n \sin(2r-1)\theta$。
>
> (a) 用 $C+iS$ 法证明 $C = \dfrac{\sin 2n\theta}{2\sin\theta}$.
>
> (b) 由此求和 $1 + \cos\theta + \cos2\theta + \cdots + \cos n\theta$.

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **M1**: $C+iS = \sum_{r=1}^n e^{i(2r-1)\theta} = e^{i\theta}\frac{1-e^{2in\theta}}{1-e^{2i\theta}}$
- **M1**: simplifies to $\frac{e^{2in\theta}-1}{2i\sin\theta} \cdot e^{-i\theta} \cdot e^{i\theta}$
- **M1**: takes real part
- **A1**: $C = \frac{\sin2n\theta}{2\sin\theta}$

</details>

---

## Question Type 5: $n$th roots of unity

### 标准方法

$$
z^n = 1 \quad\Rightarrow\quad z_k = e^{2\pi i k/n},\; k = 0,1,\ldots,n-1
$$

### 重要性质

- 所有根之和 $= 0$
- 所有根之积 $= (-1)^{n-1}$
- 根均匀分布在单位圆上

### 完整原题

**Example 1 — 9231/w20/qp/22 Q3 (4 marks):**

> Find all the roots of the equation $(w+1)^6 = 1$, giving your answers in the form $x+iy$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: let $z=w+1$, then $z^6=1$
- **M1**: $z_k = e^{2\pi i k/6}$, $k=0,\ldots,5$
- **A1**: $w_k = e^{2\pi i k/6} - 1$ in Cartesian form
- **A1**: all 6 roots correct in $x+iy$

</details>

**Example 2 — 9231/s20/qp/22 Q3 (8 marks):**

> (a) Find the roots of the equation $z^3 = -1 - i$, giving your answers in the form $re^{i\theta}$, where $r > 0$ and $0 \le \theta < 2\pi$. [5]

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **B1**: $|-1-i| = \sqrt2$, $\arg(-1-i) = -\frac{3\pi}{4}$
- **M1**: $z^3 = \sqrt2 e^{i(-\frac{3\pi}{4}+2k\pi)}$
- **M1**: $z_k = 2^{1/6} e^{i(-\frac{\pi}{4}+\frac{2k\pi}{3})}$
- **A1**: $z_0 = 2^{1/6}e^{-i\pi/4}$, $z_1 = 2^{1/6}e^{i5\pi/12}$, $z_2 = 2^{1/6}e^{i13\pi/12}$
- **A1**: all correct

</details>

---

## Question Type 6: Polynomial equations with complex roots

:::warning[注意]

"Hence" 意味着必须用上一步的结论。自己从头解**不得分**。

:::

**Example 1 — 9231/w23/qp/22 Q3 (8 marks):**

> (a) Show $\cos 5\theta = 16\cos^5\theta - 20\cos^3\theta + 5\cos\theta$. [4]
>
> (b) Hence obtain the roots of $32x^5 - 40x^3 + 10x - 1 = 0$ in the form $\cos(k\pi/10)$.

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):** see Type 2 Example 3
**MS (b):**
- **M1**: recognises $32x^5-40x^3+10x = 2\cos5\theta$ when $x=\cos\theta$
- **M1**: $2\cos5\theta - 1 = 0$
- **M1**: $\cos5\theta = \frac12$, $5\theta = \pm\frac{\pi}{3} + 2k\pi$
- **A1**: $\theta = \frac{\pm\pi/3 + 2k\pi}{5}$
- **A1**: $x = \cos\frac{\pi}{15}, \cos\frac{7\pi}{15}, \cos\frac{13\pi}{15}, \cos\frac{11\pi}{15}, \cos\frac{17\pi}{15}$

</details>

**Example 2 — 9231/w22/qp/22 Q5(c) (5 marks):**

> Hence obtain the real roots of the equation $16(8x^4 - 8x^2 + 1)^4 - 9 = 0$ in the form $\cos(q\pi)$, where $q$ is a rational number.

:::note[解题思路]

比较 $\cos 5\theta$ 公式与方程：
$32\cos^5\theta - 40\cos^3\theta + 10\cos\theta = 2\cos 5\theta$
所以 $2\cos 5\theta - 1 = 0$ → $\cos 5\theta = \frac12$
$5\theta = \pm\frac{\pi}{3} + 2k\pi$ → $\theta = \frac{\pm\pi/3 + 2k\pi}{5}$
$x = \cos\theta$，取 $k$ 使所有根互异

:::
