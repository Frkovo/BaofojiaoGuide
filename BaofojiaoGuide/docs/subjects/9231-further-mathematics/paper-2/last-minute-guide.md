---
title: 考前速通
sidebar_position: 4
---

# 考前速通

## 各 Topic 核心公式

### Hyperbolic Functions

$$
\cosh x = \frac{e^x + e^{-x}}{2}, \quad \sinh x = \frac{e^x - e^{-x}}{2}
$$

$$
\tanh x = \frac{\sinh x}{\cosh x}, \quad \operatorname{coth} x = \frac{\cosh x}{\sinh x}
$$

$$
\cosh^2 x - \sinh^2 x = 1, \quad 1 - \tanh^2 x = \operatorname{sech}^2 x
$$

$$
\sinh^{-1} x = \ln\left(x + \sqrt{x^2 + 1}\right)
$$
$$
\cosh^{-1} x = \ln\left(x + \sqrt{x^2 - 1}\right), \quad x \geq 1
$$
$$
\tanh^{-1} x = \frac{1}{2}\ln\left(\frac{1+x}{1-x}\right), \quad |x| < 1
$$

### Complex Numbers

$$
z = re^{i\theta}, \quad z^n = r^n e^{in\theta}
$$

$$
\text{Roots: } z^{1/n} = r^{1/n} e^{i(\theta + 2k\pi)/n}, \quad k = 0, 1, \dots, n-1
$$

$$
\cos n\theta = \operatorname{Re}(e^{in\theta}), \quad \sin n\theta = \operatorname{Im}(e^{in\theta})
$$

### Maclaurin Series

$$
f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots
$$

### Matrices

$$
\det(A - \lambda I) = 0 \quad \text{(特征方程)}
$$

$$
A^n = PD^nP^{-1} \quad \text{(对角化)}
$$

### First Order ODE

$$
\frac{dy}{dx} + P(x)y = Q(x), \quad \text{IF} = e^{\int P\,dx}
$$

$$
\frac{d}{dx}(y \cdot \text{IF}) = Q \cdot \text{IF}
$$

### Second Order ODE

$$
a\frac{d^2y}{dx^2} + b\frac{dy}{dx} + cy = f(x)
$$

辅助方程：$am^2 + bm + c = 0$

| 根的情况 | CF |
|---------|-----|
| 实根 $m_1 \neq m_2$ | $Ae^{m_1x} + Be^{m_2x}$ |
| 重根 $m_1 = m_2$ | $(Ax + B)e^{m_1x}$ |
| 复根 $m = \alpha \pm i\beta$ | $e^{\alpha x}(A\cos\beta x + B\sin\beta x)$ |

### Riemann Sums

$$
\sum_{r=1}^{n} r = \frac{n(n+1)}{2}, \quad \sum_{r=1}^{n} r^2 = \frac{n(n+1)(2n+1)}{6}, \quad \sum_{r=1}^{n} r^3 = \frac{n^2(n+1)^2}{4}
$$

## 见到什么先做什么

| 见到 | 先做 |
|------|------|
| `dy/dx + P(x)y = Q(x)` | 找积分因子 $e^{\int P dx}$ |
| $a\frac{d^2y}{dx^2}+b\frac{dy}{dx}+cy = f(x)$ | 写辅助方程 $am^2+bm+c=0$ |
| $\cosh x$ 或 $\sinh x$ | 转指数形式 $e^x$ |
| $z^n = a+bi$ | 求 $r$ 和 $\theta$，然后 $z = r^{1/n}e^{i(\theta+2k\pi)/n}$ |
| $(1-x^2)^{n/2}$ 的积分 | 令 $x = \sin\theta$ |
| Maclaurin 展开 | 求 $f(0), f'(0), f''(0), \dots$ |
| 矩形法求积分上下界 | 画图确定矩形的高度取左端点还是右端点 |
| 矩阵 $A^n$ | 对角化 $A = PDP^{-1}$，则 $A^n = PD^nP^{-1}$ |
| 隐式函数求 $\frac{d^2y}{dx^2}$ | 先对一阶导再对 $x$ 求导，代入隐式关系 |
| 参数方程弧长 | $L = \int \sqrt{(dx/dt)^2 + (dy/dt)^2}\,dt$ |

## 时间分配

| 阶段 | 时间 | 任务 |
|------|------|------|
| 浏览 | 前 5 分钟 | 快速看 8 题，标记 topic 和分值 |
| 第一轮 | 0-40 分钟 | 做 Q1-Q3（较简单） |
| 第二轮 | 40-80 分钟 | 做 Q4-Q6（中等） |
| 第三轮 | 80-110 分钟 | 做 Q7-Q8（最难） |
| 检查 | 最后 10 分钟 | 核对关键步骤和答案 |

每分约 1.6 分钟。10 分的题最多花 16 分钟。

## 卡住时的对策

| 情况 | 对策 |
|------|------|
| ODE 算不出积分 | 检查积分因子是否正确 |
| 复数根写不出 | 模-辐角形式，画 Argand 图 |
| 矩阵特征向量找不出 | 解 $(A - \lambda I)v = 0$ |
| 递推公式推不出 | 考虑分部积分或微分 |
| 时间不够 | 写方法步骤（可能得 M 分） |

## 交卷前检查清单

- [ ] 所有答案已写
- [ ] 数值答案已保留 3 位有效数字 / 1 位小数
- [ ] 检查了符号（$+/-$）
- [ ] 检查了初始条件是否代入
- [ ] 检查了矩阵乘法是否正确
- [ ] 检查了积分限是否写反
- [ ] 检查了 $dy/dx$ 的分母不为零
