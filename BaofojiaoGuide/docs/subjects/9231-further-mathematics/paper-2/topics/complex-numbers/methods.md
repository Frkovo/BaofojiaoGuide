---
title: 解题方法
sidebar_position: 3
---

# Solution Methods — Complex Numbers

## 方法一：复数方程求根（$z^n = a+bi$）

适用于求 $z^n = a+bi$ 的全部 $n$ 个根。

:::info[Steps]

1. 将 $a+bi$ 化为模-辐角形式：$a+bi = re^{i\theta}$
   - $r = \sqrt{a^2 + b^2}$
   - $\theta = \arg(a+bi)$（注意象限）
2. 套用 $n$ 次根公式：
   $z_k = r^{1/n}\, e^{i(\theta + 2k\pi)/n},\quad k = 0, 1, \dots, n-1$
3. 化简每个根为 $re^{i\theta}$ 形式
4. 如需直角坐标形式，计算 $x + iy$

:::

:::note[考场提示]

- 必须有 $2k\pi$，漏掉只给 **M0**
- 相邻根辐角差为 $2\pi/n$，可快速验证
- 特殊角（$\pi/6, \pi/4, \pi/3$ 等）的三角函数值要熟记

:::

### 示例：s20/21 Q3(a) — $z^3 = -1 - i$（5分）

| 步骤 | 内容 | 标记 |
|------|------|------|
| 模 | $r = \sqrt{(-1)^2 + (-1)^2} = \sqrt{2}$ | **B1** |
| 辐角 | $\theta = \arg(-1-i) = -3\pi/4$ | **B1** |
| 公式 | $z_k = (\sqrt{2})^{1/3} e^{i(-3\pi/4 + 2k\pi)/3}$ | **M1** |
| $k=0$ | $z_0 = 2^{1/6} e^{-i\pi/4}$ | **A1** |
| $k=1,2$ | $z_1 = 2^{1/6} e^{i5\pi/12}$, $z_2 = 2^{1/6} e^{i13\pi/12}$ | **A1** |

## 方法二：根的和与幂的和

适用于已知 $z_1, z_2, \dots, z_n$ 是 $z^n = a+bi$ 的根，求 $S = z_1^{mk} + z_2^{mk} + \cdots + z_n^{mk}$。

:::info[Steps]

1. 注意 $z^k = (r^{1/n})^k e^{i(\theta + 2\pi j/n)k}$
2. 若 $k$ 是 $n$ 的倍数，则 $z_j^k$ 的值与 $j$ 无关
3. 利用等比数列求和或对称性化简
4. 关键性质：$1 + \omega + \omega^2 + \cdots + \omega^{n-1} = 0$

:::

### 示例：s20/21 Q3(b) — $\omega = z_1^{3k} + z_2^{3k} + z_3^{3k}$（3分）

| 步骤 | 内容 | 标记 |
|------|------|------|
| 观察 | $z_j^3 = \sqrt{2} e^{i(-3\pi/4 + 2j\pi)} = \sqrt{2} e^{-i3\pi/4}$ 与 $j$ 无关 | **M1** |
| 代入 | $z_j^{3k} = (\sqrt{2})^{k} e^{-i3k\pi/4}$ | **A1** |
| 求和 | $\omega = 3 \times (\sqrt{2})^{k} e^{-i3k\pi/4}$ | **A1** |

## 方法三：De Moivre 定理与三角恒等式

适用于证明 $\sin^n\theta$ 或 $\cos^n\theta$ 的线性展开式。

:::info[Steps]

1. 令 $z = \cos\theta + i\sin\theta = e^{i\theta}$
2. 用 De Moivre：$z^n = \cos n\theta + i\sin n\theta$，$z^{-n} = \cos n\theta - i\sin n\theta$
3. 用 $z + z^{-1} = 2\cos\theta$，$z - z^{-1} = 2i\sin\theta$
4. 对 $(2\cos\theta)^n$ 或 $(2i\sin\theta)^n$ 用二项式定理展开
5. 合并 $z^k + z^{-k} = 2\cos k\theta$ 得最终表达式

:::

### 示例：w20/21 Q6(a) — 证明 $\sin^4\theta = \frac{1}{8}(\cos4\theta - 4\cos2\theta + 3)$（5分）

| 步骤 | 内容 | 标记 |
|------|------|------|
| 设 | $(2i\sin\theta)^4 = (z - z^{-1})^4$ | **M1** |
| 展开 | $= z^4 - 4z^2 + 6 - 4z^{-2} + z^{-4}$ | **M1** |
| 合并 | $= (z^4 + z^{-4}) - 4(z^2 + z^{-2}) + 6$ | **A1** |
| 代入 | $= 2\cos4\theta - 8\cos2\theta + 6$ | **A1** |
| 除以 | $16\sin^4\theta = 2\cos4\theta - 8\cos2\theta + 6 \Rightarrow \sin^4\theta = \frac{1}{8}(\cos4\theta - 4\cos2\theta + 3)$ | **A1** |

## 方法四：复数级数求和

适用于求 $\sum_{r=0}^{n-1} \cos(r\theta)$ 或 $\sum_{r=0}^{n-1} \sin(r\theta)$。

:::info[Steps]

1. 构造 $C + iS = \sum_{r=0}^{n-1} e^{ir\theta}$
2. 等比数列求和：$C + iS = \frac{1 - e^{in\theta}}{1 - e^{i\theta}}$
3. 分子分母同乘 $e^{-i\theta/2}$：
   $C + iS = \frac{e^{-i\theta/2} - e^{i(n-1/2)\theta}}{e^{-i\theta/2} - e^{i\theta/2}}$
4. 化简为 $\frac{\sin(n\theta/2)}{\sin(\theta/2)} e^{i(n-1)\theta/2}$
5. 取实部得 $C$，取虚部得 $S$

:::

:::note[关键点]

- 验证 $e^{i\theta} \neq 1$，即 $\theta \neq 2m\pi$
- 当 $\theta = 2m\pi$ 时，$C = n$，$S = 0$

:::

### 示例：w20/22 Q7(b) — 证明 $1 + 2\sum_{r=1}^{n} \cos(2r\theta) = \frac{\sin(2n+1)\theta}{\sin\theta}$（5分）

| 步骤 | 内容 | 标记 |
|------|------|------|
| 构造 | $\sum_{r=-n}^{n} e^{i2r\theta}$ | **M1** |
| 等比 | $= e^{-i2n\theta}\frac{1 - e^{i2(2n+1)\theta}}{1 - e^{i2\theta}}$ | **M1** |
| 化简 | $= \frac{e^{i(2n+1)\theta} - e^{-i(2n+1)\theta}}{e^{i\theta} - e^{-i\theta}}$ | **A1** |
| 三角 | $= \frac{2i\sin(2n+1)\theta}{2i\sin\theta}$ | **A1** |
| 实部 | $1 + 2\sum_{r=1}^{n} \cos(2r\theta) = \frac{\sin(2n+1)\theta}{\sin\theta}$ | **A1** |

## 方法五：$n$ 次单位根

适用于与 $z^n = 1$ 相关的证明和计算。

:::info[Steps]

1. 写出全部根：$\omega_k = e^{2\pi i k / n}$，$k = 0, 1, \dots, n-1$
2. 利用 $\sum_{k=0}^{n-1} \omega_k^r = 0$（当 $n \nmid r$）或 $n$（当 $n \mid r$）
3. 利用 $\prod_{k=0}^{n-1} (z - \omega_k) = z^n - 1$
4. 将实系数方程转化为复方程求解

:::

### 示例：w20/22 Q3 — $(w+1)^6 = 1$ 的根（4分）

| 步骤 | 内容 | 标记 |
|------|------|------|
| 设 | $w+1 = e^{2\pi i k / 6}$ | **M1** |
| 解 | $w = e^{i\pi k/3} - 1$ | **A1** |
| 列举 | $k=0$: $0$; $k=1$: $e^{i\pi/3} - 1$; $k=2$: $e^{i2\pi/3} - 1$; 等 | **A1** |
| 可化简 | 如 $k=1$: $\frac{1}{2} + i\frac{\sqrt{3}}{2} - 1 = -\frac{1}{2} + i\frac{\sqrt{3}}{2}$ | **A1** |
