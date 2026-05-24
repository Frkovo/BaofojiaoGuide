---
title: 题型分析
sidebar_position: 4
---

# 题型分析 — Complex Numbers

## Type 1：复数方程求根

> **Example 1 (s20/21 Q3a):** Solve $z^3 = -1 - i$, giving your answers in the form $re^{i\theta}$. [5]

<details>
<summary>📝 MS 展开查看</summary>

Modulus: $r = \sqrt{(-1)^2 + (-1)^2} = \sqrt{2}$ **B1**

Argument: $\arg(-1-i) = -\frac{3\pi}{4}$ or $\frac{5\pi}{4}$ **B1**

Formula: $z_k = (\sqrt{2})^{1/3} e^{i(-3\pi/4 + 2k\pi)/3}$, $k = 0, 1, 2$ **M1**

$z_0 = 2^{1/6} e^{-i\pi/4}$ **A1**

$z_1 = 2^{1/6} e^{i5\pi/12}$, $z_2 = 2^{1/6} e^{i13\pi/12}$ **A1**

[Total: 5]
</details>

> **Example 2 (s25/21 Q1):** Solve $z^3 = 27 - 27i$, giving your answers in the form $re^{i\theta}$. [5]

<details>
<summary>📝 MS 展开查看</summary>

Modulus: $r = \sqrt{27^2 + 27^2} = 27\sqrt{2}$ **B1**

Argument: $\arg(27-27i) = -\frac{\pi}{4}$ **B1**

Formula: $z_k = (27\sqrt{2})^{1/3} e^{i(-\pi/4 + 2k\pi)/3}$, $k = 0, 1, 2$ **M1**

$(27\sqrt{2})^{1/3} = 3 \times 2^{1/6}$ **A1**

$z_0 = 3 \times 2^{1/6} e^{-i\pi/12}$, $z_1 = 3 \times 2^{1/6} e^{i7\pi/12}$, $z_2 = 3 \times 2^{1/6} e^{i5\pi/4}$ **A1**

[Total: 5]
</details>

> **Example 3 (w20/22 Q3):** Find the four roots of the equation $(w+1)^6 = 1$, giving your answers in the form $a+ib$. [4]

<details>
<summary>📝 MS 展开查看</summary>

Let $w+1 = e^{2\pi i k/6}$, $k = 0, 1, 2, 3, 4, 5$ **M1**

$w = e^{i\pi k/3} - 1$ **A1**

$k=0$: $w = 0$; $k=1$: $w = e^{i\pi/3} - 1 = -\frac12 + i\frac{\sqrt3}{2}$
$k=2$: $w = e^{i2\pi/3} - 1 = -\frac32 + i\frac{\sqrt3}{2}$
$k=3$: $w = -2$; $k=4$: $w = e^{i4\pi/3} - 1 = -\frac32 - i\frac{\sqrt3}{2}$
$k=5$: $w = e^{i5\pi/3} - 1 = -\frac12 - i\frac{\sqrt3}{2}$ **A1 for any two correct, A1 for rest**

Note: Some roots are repeated — the equation is degree 4 in $w$ so only 4 distinct roots.

[Total: 4]
</details>

> **Example 4 (s21/23 Q1):** Show that $z^8 - iz^5 - z^3 + i = (z^5 - a)(z^3 - b)$, where $a$ and $b$ are constants to be found. Hence solve $z^8 - iz^5 - z^3 + i = 0$, giving your answers in the form $re^{i\theta}$. [1] + [6]

<details>
<summary>📝 MS 展开查看</summary>

Expand: $(z^5 - a)(z^3 - b) = z^8 - bz^5 - az^3 + ab$

Compare: $-b = -i \Rightarrow b = i$, $-a = -1 \Rightarrow a = 1$, $ab = i$ ✓ **B1**

So $a = 1$, $b = i$.

$z^5 = 1$: $z_k = e^{i2k\pi/5}$, $k = 0, 1, 2, 3, 4$ **M1 A1**

$z^3 = i$: $i = e^{i\pi/2}$, so $z_m = e^{i(\pi/2 + 2m\pi)/3}$, $m = 0, 1, 2$ **M1 A1**

$m=0$: $e^{i\pi/6}$; $m=1$: $e^{i5\pi/6}$; $m=2$: $e^{i3\pi/2} = e^{-i\pi/2}$ **A1**

All 8 roots (no repeats): $e^{i2\pi k/5}$ ($k = 0,\dots,4$) and $e^{i\pi/6}, e^{i5\pi/6}, e^{-i\pi/2}$ **A1**

[Total: 7]
</details>

---

## Type 2：根的和与幂的和

> **Example 1 (s20/21 Q3b):** The three roots of $z^3 = -1 - i$ are $z_1, z_2, z_3$. Given that $k$ is a positive integer, express $w = z_1^{3k} + z_2^{3k} + z_3^{3k}$ in the form $Re^{i\alpha}$. [3]

<details>
<summary>📝 MS 展开查看</summary>

From part (a): $z_j = 2^{1/6} e^{i(-3\pi/4 + 2j\pi)/3}$ for $j = 0, 1, 2$ **B1**

$z_j^3 = \sqrt{2} e^{i(-3\pi/4 + 2j\pi)} = \sqrt{2} e^{-i3\pi/4}$ (same for all $j$) **M1**

$z_j^{3k} = (\sqrt{2})^k e^{-i3k\pi/4}$

$w = 3 \times (\sqrt{2})^k e^{-i3k\pi/4}$ **A1**

[Total: 3]
</details>

> **Example 2 (s21/21 Q5):** The complex numbers $z_1, z_2, \dots, z_n$ are the $n$th roots of unity. State the value of $z_1 + z_2 + \cdots + z_n$. Hence show that $1 + z + z^2 + \cdots + z^{n-1} = 0$ where $z$ is any $n$th root of unity other than $1$. [1] + [2]

<details>
<summary>📝 MS 展开查看</summary>

$z_1 + z_2 + \cdots + z_n = 0$ **B1**

Let $\omega$ be an $n$th root of unity, $\omega \neq 1$.

If $S = 1 + \omega + \omega^2 + \cdots + \omega^{n-1}$, then $\omega S = \omega + \omega^2 + \cdots + \omega^{n-1} + \omega^n = \omega + \omega^2 + \cdots + \omega^{n-1} + 1 = S$ **M1**

So $\omega S = S \Rightarrow S(\omega - 1) = 0$. Since $\omega \neq 1$, $S = 0$. **A1**

[Total: 3]
</details>

> **Example 3:** The complex numbers $u_1, u_2, \dots, u_6$ are the roots of $z^6 = 1$. Find the value of $u_1^{12} + u_2^{12} + \cdots + u_6^{12}$.

<details>
<summary>📝 MS 展开查看</summary>

$u_k = e^{2\pi i k/6} = e^{i\pi k/3}$, $k = 0, 1, \dots, 5$ **B1**

$u_k^{12} = e^{i\pi k/3 \times 12} = e^{i4\pi k} = 1$ (since $4\pi k$ is multiple of $2\pi$ for all $k$) **M1**

$u_1^{12} + u_2^{12} + \cdots + u_6^{12} = 1 + 1 + 1 + 1 + 1 + 1 = 6$ **A1**

[Total: 3]
</details>

---

## Type 3：De Moivre 定理与三角恒等式

> **Example 1 (s20/23 Q8a):** Show that $\sin^6\theta = -\frac{1}{32}(\cos6\theta - 6\cos4\theta + 15\cos2\theta - 10)$. [6]

<details>
<summary>📝 MS 展开查看</summary>

Let $z = \cos\theta + i\sin\theta = e^{i\theta}$.

$2i\sin\theta = z - z^{-1}$ **B1**

$(2i\sin\theta)^6 = (z - z^{-1})^6$ **M1**

Expand: $z^6 - 6z^4 + 15z^2 - 20 + 15z^{-2} - 6z^{-4} + z^{-6}$ **M1 A1**

$= (z^6 + z^{-6}) - 6(z^4 + z^{-4}) + 15(z^2 + z^{-2}) - 20$ **A1**

$= 2\cos6\theta - 12\cos4\theta + 30\cos2\theta - 20$ **A1**

$-64\sin^6\theta = 2\cos6\theta - 12\cos4\theta + 30\cos2\theta - 20$  (since $(2i)^6 = -64$) **M1**

$\sin^6\theta = -\frac{1}{32}(\cos6\theta - 6\cos4\theta + 15\cos2\theta - 10)$ **A1 FT**

[Total: 6]

Note: 6 marks for show that — **M1** for correct approach, **A1** for each correct step.
</details>

> **Example 2 (w20/21 Q6a):** Show that $\sin^4\theta = \frac{1}{8}(\cos4\theta - 4\cos2\theta + 3)$. [5]

<details>
<summary>📝 MS 展开查看</summary>

$z = \cos\theta + i\sin\theta$. Then $z^n + z^{-n} = 2\cos n\theta$, $z^n - z^{-n} = 2i\sin n\theta$ **B1**

$(2i\sin\theta)^4 = (z - z^{-1})^4$ **M1**

$= z^4 - 4z^2 + 6 - 4z^{-2} + z^{-4}$ **M1**

$= (z^4 + z^{-4}) - 4(z^2 + z^{-2}) + 6$ **A1**

$= 2\cos4\theta - 8\cos2\theta + 6$ **A1**

$16\sin^4\theta = 2\cos4\theta - 8\cos2\theta + 6$  (since $(2i)^4 = 16$) **A1**

$\sin^4\theta = \frac{1}{8}(\cos4\theta - 4\cos2\theta + 3)$

[Total: 5]
</details>

> **Example 3 (s20/23 Q8c):** Show that the equation $16c^6 + 16(1 - c^2)^3 = 13$ can be reduced to $\cos6\theta = \frac{5}{8}$, where $c = \cos\theta$. Hence express the roots in the form $\cos(k\pi)$. [5]

<details>
<summary>📝 MS 展开查看</summary>

$c = \cos\theta$.

Note from part (a): $\sin^6\theta = -\frac{1}{32}(\cos6\theta - 6\cos4\theta + 15\cos2\theta - 10)$

Also $\sin^2\theta = 1 - c^2$ **B1**

$\sin^6\theta = (1-c^2)^3$ **M1**

So $(1-c^2)^3 = -\frac{1}{32}(\cos6\theta - 6\cos4\theta + 15\cos2\theta - 10)$

The given equation: $16c^6 + 16(1-c^2)^3 = 13$

Using $\cos^2\theta = c^2$ relations: this reduces to $\cos6\theta = \frac{5}{8}$ **M1 A1**

$\cos6\theta = \frac{5}{8} \Rightarrow 6\theta = \pm\cos^{-1}(\frac{5}{8}) + 2k\pi$

$\theta = \pm\frac{1}{6}\cos^{-1}(\frac{5}{8}) + \frac{k\pi}{3}$

Roots in form $\cos(k\pi)$: ... **A1**

[Total: 5]
</details>

> **Example 4 (s22/21 Q6):** Express $\sum_{r=1}^{5} \cos^5(r\pi/11)$ in the form $\operatorname{cosec}(q\pi)$. [5]

<details>
<summary>📝 MS 展开查看</summary>

Let $z = e^{i\theta}$. Then $2\cos\theta = z + z^{-1}$ **B1**

$(2\cos\theta)^5 = (z + z^{-1})^5 = z^5 + 5z^3 + 10z + 10z^{-1} + 5z^{-3} + z^{-5}$ **M1**

$= (z^5 + z^{-5}) + 5(z^3 + z^{-3}) + 10(z + z^{-1})$ **A1**

$= 2\cos5\theta + 10\cos3\theta + 20\cos\theta$ **A1**

$\cos^5\theta = \frac{1}{16}(\cos5\theta + 5\cos3\theta + 10\cos\theta)$

Now sum: $\sum_{r=1}^{5} \cos^5(r\pi/11) = \frac{1}{16}\sum_{r=1}^{5}[\cos(5r\pi/11) + 5\cos(3r\pi/11) + 10\cos(r\pi/11)]$

Using $\sum_{r=1}^{n} \cos(r\theta) = \frac{\sin(n\theta/2)}{\sin(\theta/2)}\cos((n+1)\theta/2)$ with appropriate values... **M1**

After simplification: $= \frac{1}{32}\csc(\pi/22)$ or $\frac{1}{32}\operatorname{cosec}(\pi/22)$ **A1**

[Total: 5]
</details>

---

## Type 4：复数级数求和

> **Example 1 (w20/22 Q7b):** Show that $1 + 2\sum_{r=1}^{n} \cos(2r\theta) = \frac{\sin(2n+1)\theta}{\sin\theta}$. [5]

<details>
<summary>📝 MS 展开查看</summary>

Consider $C = 1 + 2\sum_{r=1}^{n} \cos(2r\theta) = \sum_{r=-n}^{n} e^{i2r\theta}$ **M1**

$= e^{-i2n\theta} + e^{-i2(n-1)\theta} + \cdots + 1 + \cdots + e^{i2n\theta}$

Geometric series with first term $e^{-i2n\theta}$, ratio $e^{i2\theta}$, $2n+1$ terms:

$= e^{-i2n\theta} \cdot \frac{1 - e^{i2(2n+1)\theta}}{1 - e^{i2\theta}}$ **M1**

$= \frac{e^{-i2n\theta} - e^{i2(n+1)\theta}}{1 - e^{i2\theta}}$

Multiply numerator and denominator by $e^{-i\theta}$:

$= \frac{e^{i(2n+1)\theta} - e^{-i(2n+1)\theta}}{e^{i\theta} - e^{-i\theta}}$ **A1**

$= \frac{2i\sin(2n+1)\theta}{2i\sin\theta}$ **A1**

$= \frac{\sin(2n+1)\theta}{\sin\theta}$ **A1**

[Total: 5]
</details>

> **Example 2:** Find $\sum_{r=0}^{n-1} \cos(r\theta)$ and $\sum_{r=0}^{n-1} \sin(r\theta)$. [7]

<details>
<summary>📝 MS 展开查看</summary>

$C = \sum_{r=0}^{n-1} \cos(r\theta)$, $S = \sum_{r=0}^{n-1} \sin(r\theta)$

$C + iS = \sum_{r=0}^{n-1} e^{ir\theta}$ **M1**

Geometric series: $= \frac{1 - e^{in\theta}}{1 - e^{i\theta}}$ **M1**

$= \frac{e^{in\theta/2}(e^{-in\theta/2} - e^{in\theta/2})}{e^{i\theta/2}(e^{-i\theta/2} - e^{i\theta/2})}$ **M1**

$= e^{i(n-1)\theta/2} \cdot \frac{\sin(n\theta/2)}{\sin(\theta/2)}$ **A1**

Take real and imaginary parts:

$C = \frac{\sin(n\theta/2)}{\sin(\theta/2)} \cos\left(\frac{(n-1)\theta}{2}\right)$ **A1**

$S = \frac{\sin(n\theta/2)}{\sin(\theta/2)} \sin\left(\frac{(n-1)\theta}{2}\right)$ **A1**

Note: when $\theta = 2m\pi$, $C = n$, $S = 0$ (must handle separately) **B1**

[Total: 7]
</details>

> **Example 3 (w22/21 Q7):** The complex number $w$ satisfies $w^n = 1$ and $w \neq 1$. Show that $1 + w + w^2 + \cdots + w^{n-1} = 0$. Hence, using De Moivre's theorem with $(1 + i\tan\theta)^k$, evaluate $\sum_{k=0}^{n-1} (1 + i\tan\theta)^k$ in simplified form. [10]

<details>
<summary>📝 MS 展开查看</summary>

**Part 1:** $S = 1 + w + w^2 + \cdots + w^{n-1}$

$wS = w + w^2 + \cdots + w^{n-1} + w^n = w + w^2 + \cdots + w^{n-1} + 1 = S$ **M1**

$wS = S \Rightarrow S(w-1) = 0$. Since $w \neq 1$, $S = 0$. **A1**

**Part 2:** $(1 + i\tan\theta)^k = \left(\frac{\cos\theta + i\sin\theta}{\cos\theta}\right)^k = \frac{(\cos\theta + i\sin\theta)^k}{\cos^k\theta}$ **M1**

By De Moivre: $= \frac{\cos k\theta + i\sin k\theta}{\cos^k\theta}$ **M1**

So $\sum_{k=0}^{n-1} (1 + i\tan\theta)^k = \sum_{k=0}^{n-1} \frac{\cos k\theta + i\sin k\theta}{\cos^k\theta}$ **A1**

This is NOT a standard geometric series (ratio involves $\cos\theta$).

Alternatively: $(1 + i\tan\theta) = \frac{e^{i\theta}}{\cos\theta}$, so $(1 + i\tan\theta)^k = \frac{e^{ik\theta}}{\cos^k\theta}$

Sum: $\sum_{k=0}^{n-1} \frac{e^{ik\theta}}{\cos^k\theta} = \sum_{k=0}^{n-1} \left(\frac{e^{i\theta}}{\cos\theta}\right)^k$ **M1**

Geometric with ratio $r = \frac{e^{i\theta}}{\cos\theta} = \sec\theta \cdot e^{i\theta}$:

$= \frac{1 - (e^{i\theta}/\cos\theta)^n}{1 - e^{i\theta}/\cos\theta}$ **M1 A1**

$= \frac{1 - e^{in\theta}/\cos^n\theta}{1 - e^{i\theta}/\cos\theta}$ **A1**

Simplify by multiplying numerator and denominator by $\cos^n\theta$... **A1**

[Total: 10]
</details>

---

## Type 5：De Moivre 展开与多项式方程求解

### 如何识别
给出 $\cos n\theta$ 或 $\frac{\sin n\theta}{\sin\theta}$ 的展开式（作为 $\cos\theta$ 或 $\sin\theta$ 的多项式），要求利用该结果求解一个高次多项式方程，根通常用 $\cos(k\pi/n)$ 形式表达。

:::note[标准解题方法]
1. 用 De Moivre 定理展开 $(\cos\theta + i\sin\theta)^n$
2. 取实部得 $\cos n\theta$，虚部得 $\sin n\theta$
3. $\cos n\theta$ 可写成 $\cos\theta$ 的 $n$ 次多项式；$\frac{\sin n\theta}{\sin\theta}$ 可写成 $\sin\theta$ 的 $n-1$ 次多项式
4. 令 $x = \cos\theta$（或 $x = \sin\theta$）代入原多项式方程
5. 化简得到 $\cos n\theta = k$ 或 $\frac{\sin n\theta}{\sin\theta} = k$
6. 解出 $\theta = \frac{1}{n}(\pm\cos^{-1}k + 2m\pi)$
7. 代回 $x = \cos\theta$ 得到多项式的根
:::

:::info[常用展开]
$$
\cos 3\theta = 4\cos^3\theta - 3\cos\theta
$$
$$
\cos 4\theta = 8\cos^4\theta - 8\cos^2\theta + 1
$$
$$
\cos 5\theta = 16\cos^5\theta - 20\cos^3\theta + 5\cos\theta
$$
$$
\cos 6\theta = 32\cos^6\theta - 48\cos^4\theta + 18\cos^2\theta - 1
$$
$$
\cos 7\theta = 64\cos^7\theta - 112\cos^5\theta + 56\cos^3\theta - 7\cos\theta
$$
$$
\cos 8\theta = 128\cos^8\theta - 256\cos^6\theta + 160\cos^4\theta - 32\cos^2\theta + 1
$$

$$
\frac{\sin 3\theta}{\sin\theta} = 3 - 4\sin^2\theta
$$
$$
\frac{\sin 5\theta}{\sin\theta} = 5 - 20\sin^2\theta + 16\sin^4\theta
$$
$$
\frac{\sin 7\theta}{\sin\theta} = 7 - 56\sin^2\theta + 112\sin^4\theta - 64\sin^6\theta
$$
:::

> **Example 1 — 典型题：** 已知 $\cos 7\theta = 64\cos^7\theta - 112\cos^5\theta + 56\cos^3\theta - 7\cos\theta$。  
> (a) 由此证明方程 $64x^7 - 112x^5 + 56x^3 - 7x + 1 = 0$ 可化为 $\cos 7\theta = -1$，其中 $x = \cos\theta$。  
> (b) 求解该 $7$ 次方程，将根表示为 $\cos(k\pi/7)$ 的形式。

<details>
<summary>📝 MS 展开查看</summary>

**(a)** 令 $x = \cos\theta$，代入已知的 $\cos 7\theta$ 展开式：

$$
\cos 7\theta = 64x^7 - 112x^5 + 56x^3 - 7x
$$

**M1**: 代入 $x = \cos\theta$

原方程为 $64x^7 - 112x^5 + 56x^3 - 7x + 1 = 0$，即

$$
64x^7 - 112x^5 + 56x^3 - 7x = -1
$$

所以 $\cos 7\theta = -1$ **A1**

**(b)** 解 $\cos 7\theta = -1$：

$$
7\theta = \pi + 2m\pi \Rightarrow \theta = \frac{\pi + 2m\pi}{7},\ m = 0, 1, \dots, 6
$$

**M1**: 写出通解

$$
x = \cos\theta = \cos\left(\frac{(2m+1)\pi}{7}\right),\ m = 0, 1, \dots, 6
$$

**A1**: 正确写出根的表达式

注意 $m = 3$ 时 $\cos\pi = -1$，$m = 0$ 和 $m = 6$ 等给出相同的 $\cos$ 值（因为 $\cos$ 为偶函数）。实际上不同的根为：
$$
x = \cos\frac{\pi}{7},\ \cos\frac{3\pi}{7},\ \cos\frac{5\pi}{7},\ \cos\pi = -1
$$

**A1**: 列出不同的根（共 4 个不同的实根）

[总分: 6]
</details>

---

> **Example 2 — 典型题：** 已知 $\sin 5\theta = 16\sin^5\theta - 20\sin^3\theta + 5\sin\theta$。  
> (a) 令 $x = \sin\theta$，将方程 $16x^5 - 20x^3 + 5x - 1 = 0$ 化为 $\sin 5\theta = 1$ 的形式。  
> (b) 求解该方程，将根表示为 $\sin\left(\frac{(4k+1)\pi}{10}\right)$ 的形式。

<details>
<summary>📝 MS 展开查看</summary>

**(a)** 代入 $x = \sin\theta$：

**B1**: 已知 $\sin 5\theta = 16\sin^5\theta - 20\sin^3\theta + 5\sin\theta$

所以 $16x^5 - 20x^3 + 5x = \sin 5\theta$ **M1**

方程 $16x^5 - 20x^3 + 5x - 1 = 0 \Rightarrow \sin 5\theta = 1$ **A1**

**(b)** 解 $\sin 5\theta = 1$：

**M1**: $5\theta = \frac{\pi}{2} + 2k\pi \Rightarrow \theta = \frac{\pi}{10} + \frac{2k\pi}{5},\ k = 0, 1, 2, 3, 4$

**A1**: $x = \sin\left(\frac{\pi}{10} + \frac{2k\pi}{5}\right),\ k = 0, 1, 2, 3, 4$

即 $x = \sin\frac{\pi}{10},\ \sin\frac{\pi}{2}=1,\ \sin\frac{9\pi}{10},\ \sin\frac{13\pi}{10},\ \sin\frac{17\pi}{10}$

**A1 FT**: 正确化简

[总分: 6]
</details>

---

> **Example 3 — 典型题：** 已知 $\frac{\sin 7\theta}{\sin\theta} = 7 - 56\sin^2\theta + 112\sin^4\theta - 64\sin^6\theta$。  
> 令 $x = \sin^2\theta$，证明方程 $64x^3 - 112x^2 + 56x - 7 = 0$ 有一根 $x = \sin^2\frac{\pi}{7}$。  
> 由此求出其他两根。

<details>
<summary>📝 MS 展开查看</summary>

**B1**: $\frac{\sin 7\theta}{\sin\theta} = 7 - 56\sin^2\theta + 112\sin^4\theta - 64\sin^6\theta$

令 $x = \sin^2\theta$，则 $\sin^2\theta = x$，$\sin^4\theta = x^2$，$\sin^6\theta = x^3$ **M1**

$$
\frac{\sin 7\theta}{\sin\theta} = 7 - 56x + 112x^2 - 64x^3
$$

**A1**: 正确代入

当 $\theta = \frac{\pi}{7}$ 时，$\sin 7\theta = \sin\pi = 0$，$\sin\theta \neq 0$，所以 $\frac{\sin 7\theta}{\sin\theta} = 0$ **M1**

$$
7 - 56x + 112x^2 - 64x^3 = 0 \text{ 即 } 64x^3 - 112x^2 + 56x - 7 = 0
$$

所以 $x = \sin^2\frac{\pi}{7}$ 是方程的一根 **A1**

因式分解：$64x^3 - 112x^2 + 56x - 7 = (4x - 1)^2(4x - 7)$ **M1 A1**

另两根为 $x = \frac{1}{4}$ 和 $x = \frac{7}{4}$（但 $\sin^2\theta \leq 1$，所以只取 $x = \frac{1}{4}$）

**A1**: $\sin^2\frac{\pi}{7},\ \frac{1}{4}$ 为两根

[总分: 8]
</details>

:::warning[常见陷阱]
- $\cos n\theta$ 展开成 $\cos\theta$ 的多项式时，注意次数和符号
- 代入后注意 $\cos\theta$ 的取值范围 $[-1, 1]$，超出范围的根需舍去
- $\cos$ 为偶函数，$\cos(k\pi/7)$ 中 $k$ 和 $7-k$ 给出相同值
- $\sin$ 为奇函数，注意正负号
- 注意方程的次数：若原方程是 $n$ 次，应有 $n$ 个根（含重根和复数根）
- $\theta$ 的通解要写完整：$\theta = \frac{1}{n}(\pm\cos^{-1}k + 2m\pi)$
:::

---

## Type 6：$n$ 次单位根

> **Example 1 (s21/21 Q5):** The complex numbers $z_1, z_2, \dots, z_n$ are the $n$th roots of unity. State the value of $z_1 + z_2 + \cdots + z_n$. Hence show that $1 + z + z^2 + \cdots + z^{n-1} = 0$ where $z$ is any $n$th root of unity other than $1$. [1] + [2]

<details>
<summary>📝 MS 展开查看</summary>

Sum = 0 **B1**

Let $\omega \neq 1$ be an $n$th root of unity. $S = 1 + \omega + \omega^2 + \cdots + \omega^{n-1}$.

$\omega S = \omega + \omega^2 + \cdots + \omega^{n-1} + \omega^n = \omega + \omega^2 + \cdots + \omega^{n-1} + 1 = S$ **M1**

$S(\omega - 1) = 0 \Rightarrow S = 0$ (since $\omega \neq 1$) **A1**

[Total: 3]
</details>

> **Example 2:** If $\omega = e^{2\pi i/7}$, find the value of $(1 + \omega)(1 + \omega^2)(1 + \omega^4)$.

<details>
<summary>📝 MS 展开查看</summary>

Note $1 + \omega + \omega^2 + \cdots + \omega^6 = 0$ **B1**

$x^7 - 1 = (x-1)(x-\omega)(x-\omega^2)\cdots(x-\omega^6)$ **M1**

Put $x = -1$: $(-1)^7 - 1 = -2 = (-1-1)(-1-\omega)(-1-\omega^2)\cdots(-1-\omega^6)$

$-2 = -2(-1-\omega)(-1-\omega^2)\cdots(-1-\omega^6)$

$1 = (-1-\omega)(-1-\omega^2)\cdots(-1-\omega^6)$ **A1**

$= (-1)^6 (1+\omega)(1+\omega^2)\cdots(1+\omega^6) = (1+\omega)(1+\omega^2)\cdots(1+\omega^6)$ **A1**

Now $(1+\omega)(1+\omega^2)(1+\omega^4)$ is half of the product (the other half is conjugates), so:

$(1+\omega)(1+\omega^2)(1+\omega^4) = 1$ **A1**

[Total: 5]
</details>

> **Example 3:** Let $\omega = e^{2\pi i/3}$. Find the value of $\omega^2 + \omega + 1$ and deduce the value of $(1 + \omega + \omega^2)^n$ for any integer $n$.

<details>
<summary>📝 MS 展开查看</summary>

$\omega$ is a cube root of unity: $\omega^3 = 1$, $\omega \neq 1$.

$1 + \omega + \omega^2 = 0$ **B1**

Therefore $(1 + \omega + \omega^2)^n = 0$ for any positive integer $n$. **A1**

For $n = 0$: $0^0$ undefined; for negative $n$: undefined.

[Total: 2]
</details>
