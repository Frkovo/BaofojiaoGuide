---
title: 考前速记
sidebar_position: 7
---

# 考前速记 — Complex Numbers

## 核心公式

| 公式 | 说明 |
|------|------|
| $z = re^{i\theta} = r(\cos\theta + i\sin\theta)$ | 模-辐角形式 |
| $(re^{i\theta})^n = r^n e^{in\theta}$ | De Moivre 定理 |
| $z^n + z^{-n} = 2\cos n\theta$ | 实部提取 |
| $z^n - z^{-n} = 2i\sin n\theta$ | 虚部提取 |
| $2\cos\theta = z + z^{-1}$ | 常用代换 |
| $2i\sin\theta = z - z^{-1}$ | 常用代换 |

## $n$ 次根

$$
z^n = a + bi \;\Rightarrow\; z_k = r^{1/n}\, e^{i(\theta + 2k\pi)/n},\; k = 0, 1, \dots, n-1
$$

- 必须有 $2k\pi$ — 漏掉则丢分
- 所有根在半径为 $r^{1/n}$ 的圆上等距分布
- 相邻根辐角差 $= 2\pi/n$
- 答案以 $re^{i\theta}$ 形式给出

## 单位根

$z^n = 1$ 的根：$\omega_k = e^{2\pi i k/n}$，$k = 0, 1, \dots, n-1$

| 性质 | 公式 |
|------|------|
| 和 | $\sum_{k=0}^{n-1} \omega_k = 0$ |
| 积 | $\prod_{k=0}^{n-1} \omega_k = (-1)^{n-1}$ |
| 共轭 | $\overline{\omega_k} = \omega_{n-k}$ |

## 三角恒等式 — 标准步骤

1. 令 $z = \cos\theta + i\sin\theta = e^{i\theta}$
2. $(2\cos\theta)^n = (z + z^{-1})^n = \sum \binom{n}{k} z^{n-2k}$
3. $(2i\sin\theta)^n = (z - z^{-1})^n = \sum \binom{n}{k}(-1)^k z^{n-2k}$
4. 合并：$z^k + z^{-k} = 2\cos k\theta$
5. 注意 $(2i)^n$ 的值：$n=2 \rightarrow -4$, $n=4 \rightarrow 16$, $n=6 \rightarrow -64$

## 级数求和 — 标准步骤

1. 构造 $C + iS = \sum_{r=0}^{n-1} e^{ir\theta}$
2. 等比数列：$\frac{1 - e^{in\theta}}{1 - e^{i\theta}}$
3. 化简为 $e^{i(n-1)\theta/2}\frac{\sin(n\theta/2)}{\sin(\theta/2)}$
4. 取实部/虚部得 $C$、$S$
5. $\theta = 2m\pi$ 时单独讨论，此时 $C = n$, $S = 0$

## 易错点

- 求根 $2k\pi$ 不能忘
- 辐角注意象限（$\tan^{-1}$ 后调整）
- $(2i)^n$ 含 $i^n$ 的循环，勿直接写 $2^n$
- 级数中 $e^{i\theta} = 1$ 时分母为 $0$
- 单位根积为 $(-1)^{n-1}$ 而非 $1$
- 展开 $(z - z^{-1})^n$ 注意 $(-1)^k$

## 答题技巧

1. 求根先画图 — 快速验证根的位置
2. 三角恒等式从 $(2\cos\theta)^n$ 或 $(2i\sin\theta)^n$ 入手
3. 级数求和用 $C + iS$ 构造，不要分开求 $C$ 和 $S$
4. Show that 题写清每一步推导
5. 检查 $k$ 的范围是否 $0$ 到 $n-1$
6. 弧度制！弧度制！弧度制！
