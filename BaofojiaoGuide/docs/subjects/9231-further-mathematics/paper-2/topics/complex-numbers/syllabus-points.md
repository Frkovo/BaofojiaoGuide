---
title: 大纲要点
sidebar_position: 2
---

# Syllabus Points — Complex Numbers

## 核心知识点

### 1. 复数的模-辐角形式（Modulus-Argument Form）

- $z = x + iy = r(\cos\theta + i\sin\theta) = re^{i\theta}$
- $r = |z| = \sqrt{x^2 + y^2}$
- $\theta = \arg(z)$，主辐角范围 $-\pi &lt; \arg(z) \le \pi$
- 辐角加减 $2\pi$ 不改变复数值

### 2. De Moivre 定理

- $(re^{i\theta})^n = r^n e^{in\theta} = r^n(\cos n\theta + i\sin n\theta)$
- 逆用：$r^{1/n} e^{i\theta/n}$ 是 $re^{i\theta}$ 的一个 $n$ 次根
- 适用于正负整数指数
- $z^n + z^{-n} = 2\cos n\theta$，$z^n - z^{-n} = 2i\sin n\theta$

### 3. 复数的 $n$ 次根

- $z^n = a + bi$ 有 $n$ 个不同的根
- 公式：$z_k = r^{1/n} e^{i(\theta + 2k\pi)/n}$，$k = 0, 1, \dots, n-1$
- 所有根在复平面上位于半径为 $r^{1/n}$ 的圆上，等距分布
- 相邻根的辐角差为 $2\pi/n$

### 4. 单位根（Roots of Unity）

- $z^n = 1$ 的根：$\omega_k = e^{2\pi i k / n}$，$k = 0, 1, \dots, n-1$
- 性质：
  - $\sum_{k=0}^{n-1} \omega_k = 0$
  - $\prod_{k=0}^{n-1} \omega_k = (-1)^{n-1}$
  - $\overline{\omega_k} = \omega_{n-k}$
  - $\omega_j \omega_k = \omega_{j+k}$
- 常用于因式分解：$z^n - 1 = (z-1)(z-\omega)(z-\omega^2)\cdots(z-\omega^{n-1})$

### 5. 三角恒等式（Trigonometric Identities）

- 用 $z = \cos\theta + i\sin\theta$ 表示 $\cos n\theta$、$\sin n\theta$
- 用二项式展开 $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$
- 比较实部和虚部得 $\cos^n\theta$、$\sin^n\theta$ 的展开式
- 常用技巧：
  - $(2\cos\theta)^n = z^n + \binom{n}{1} z^{n-2} + \cdots$
  - $(2i\sin\theta)^n = z^n - \binom{n}{1} z^{n-2} + \cdots$

### 6. 复数级数求和（Summation of Series）

- 等比数列求和应用：$\sum_{r=0}^{n-1} z^r = \frac{1 - z^n}{1 - z}$
- 令 $z = e^{i\theta}$ 分离实部和虚部：
  - $\sum_{r=0}^{n-1} \cos(r\theta) = \frac{\sin(n\theta/2)}{\sin(\theta/2)} \cos((n-1)\theta/2)$
  - $\sum_{r=0}^{n-1} \sin(r\theta) = \frac{\sin(n\theta/2)}{\sin(\theta/2)} \sin((n-1)\theta/2)$
- 含 $C = \sum \cos$ 和 $S = \sum \sin$ 的组合题型
- $z = 1$ 时需单独处理
