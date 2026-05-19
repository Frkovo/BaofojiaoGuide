---
title: Complex Numbers
sidebar_position: 1
---

# Complex Numbers（复数）

---

## 考纲要求

1. 掌握复数的模-辐角形式 $z = re^{i\theta} = r(\cos\theta + i\sin\theta)$
2. 掌握 De Moivre 定理：$(re^{i\theta})^n = r^n e^{in\theta}$ 及其逆用
3. 能求 $z^n = a + bi$ 的全部 $n$ 个根，并以 $re^{i\theta}$ 形式作答
4. 理解单位根 $z^n = 1$ 的性质：根在单位圆上等距分布，和为 $0$，积为 $(-1)^{n-1}$
5. 能用复数方法推导三角恒等式：$\sin n\theta$、$\cos n\theta$ 的高次幂展开
6. 能用复数对三角函数级数求和：$\sum_{r=0}^{n-1} \cos(r\theta)$、$\sum_{r=0}^{n-1} \sin(r\theta)$
7. 能将三角方程转化为复数方程求解

---

## 常见题型

| 题型 | 分值 | 链接 |
|------|------|------|
| 复数方程求根（$z^n = a+bi$） | 4–6 分 | [题型 1](./question-types.md) |
| 根的和与幂的和 | 3–4 分 | [题型 2](./question-types.md) |
| De Moivre / 三角恒等式 | 5–6 分 | [题型 3](./question-types.md) |
| 复数级数求和 | 5–7 分 | [题型 4](./question-types.md) |
| $n$ 次单位根 | 1–4 分 | [题型 5](./question-types.md) |

---

## 核心公式

### 模-辐角形式

$$
z = x + iy = r(\cos\theta + i\sin\theta) = re^{i\theta}
$$

$$
r = |z| = \sqrt{x^2 + y^2}, \quad \theta = \arg(z) = \tan^{-1}\left(\frac{y}{x}\right)
$$

### De Moivre 定理

$$
(re^{i\theta})^n = r^n e^{in\theta} = r^n(\cos n\theta + i\sin n\theta)
$$

$$
(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta
$$

### 共轭与倒数

$$
z^{-1} = \frac{1}{r}e^{-i\theta}, \quad z^{-n} = r^{-n}e^{-in\theta}
$$

$$
z^n + z^{-n} = 2\cos n\theta, \quad z^n - z^{-n} = 2i\sin n\theta
$$

### $n$ 次根公式

$$
z^n = a + bi \quad\Rightarrow\quad z = r^{1/n}\, e^{i(\theta + 2k\pi)/n},\; k = 0, 1, \dots, n-1
$$

其中 $r = |a+bi|$，$\theta = \arg(a+bi)$

### $n$ 次单位根

$$
z^n = 1 \quad\Rightarrow\quad z = e^{2\pi i k / n} = \cos\frac{2k\pi}{n} + i\sin\frac{2k\pi}{n},\; k = 0, 1, \dots, n-1
$$

#### 单位根性质

设 $\omega = e^{2\pi i / n}$，则：

- $1 + \omega + \omega^2 + \cdots + \omega^{n-1} = 0$
- $\omega^n = 1$，$\omega^k = \overline{\omega^{n-k}}$
- 全部根为 $\{1, \omega, \omega^2, \dots, \omega^{n-1}\}$

### 等比数列求和（复数）

$$
1 + z + z^2 + \cdots + z^{n-1} = \frac{1 - z^n}{1 - z}
$$

当 $z = e^{i\theta}$ 时：

$$
\sum_{r=0}^{n-1} e^{ir\theta} = \frac{1 - e^{in\theta}}{1 - e^{i\theta}} = e^{i(n-1)\theta/2}\,\frac{\sin(n\theta/2)}{\sin(\theta/2)}
$$

### 三角恒等式（复数法）

$$
\cos n\theta = \frac{z^n + z^{-n}}{2}, \quad \sin n\theta = \frac{z^n - z^{-n}}{2i}
$$

$$
\cos^n\theta = \frac{1}{2^n} \sum_{k=0}^n \binom{n}{k} \cos((n-2k)\theta)
$$

---

## 常见错误

- 求 $z^n = a+bi$ 的根时忘记加 $2k\pi$（只得到一个根）
- 辐角范围理解错误：主辐角 $\arg(z) \in (-\pi, \pi]$
- De Moivre 定理中 $(\cos\theta + i\sin\theta)^n \neq \cos(n\theta) + i\sin(n\theta)$ 的逆用混淆
- 级数求和时忘记端点（$z=1$ 的情况需单独讨论）
- 单位根的和为零，但积为 $(-1)^{n-1}$ 而非 $1$
- 三角恒等式证明中二项式展开时符号错误
