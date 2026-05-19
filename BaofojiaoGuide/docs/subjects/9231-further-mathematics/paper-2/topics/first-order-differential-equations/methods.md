---
title: 解题方法
sidebar_position: 3
---

# Solution Methods — First Order Differential Equations

## 方法一：积分因子法（标准流程）

适用于 $\frac{dy}{dx} + P(x)y = Q(x)$。

:::info[Steps]

1. 确认方程为标准形式 $\frac{dy}{dx} + P(x)y = Q(x)$，识别 $P(x)$ 和 $Q(x)$
2. 计算积分因子 $I = e^{\int P(x)\,dx}$，化简 $I$
3. 方程两边同乘 $I$，左边化为 $\frac{d}{dx}(yI)$
4. 两边积分：$yI = \int IQ(x)\,dx$
5. 计算右边的积分（可能需分部积分、换元等）
6. 求出 $y = \frac{1}{I}\int IQ\,dx$
7. 如有初值，代入确定常数 $C$

:::

:::warning[注意]

积分因子化简时，常可忽略积分常数——因为最终通解已包含任意常数。

:::

## 方法二：可分离变量法

适用于 $\frac{dy}{dx} = f(x)g(y)$。

:::info[Steps]

1. 将方程改写为 $\frac{dy}{g(y)} = f(x)\,dx$
2. 两边积分：$\int \frac{1}{g(y)}\,dy = \int f(x)\,dx$
3. 尽可能显式地写出 $y$ 的表达式
4. 代入初值条件确定常数

:::

## 方法三：初值问题

适用于所有一阶 ODE 附加初始条件 $y(x_0) = y_0$。

:::info[Steps]

1. 按照通用方法求通解
2. 代入 $x = x_0$，$y = y_0$
3. 解出常数 $C$
4. 回代得到特解
5. 如需化简，整理为最简形式

:::

## 方法四：特殊形式积分因子的化简技巧

:::info[Steps]

当 $P(x)$ 为分式形式时：

1. 对分母配方：$x^2 + bx + c = (x + \frac{b}{2})^2 + (c - \frac{b^2}{4})$
2. 积分 $\int \frac{x + a}{(x+a)^2 + k^2}\,dx = \frac{1}{2}\ln[(x+a)^2 + k^2]$
3. 积分因子化为 $I = \sqrt{(x+a)^2 + k^2}$

当分母为 $x^2 + a^2$ 且分子为常数时：

1. $P(x) = \frac{1}{x^2+a^2}$ 对应 $I = e^{\frac{1}{a}\tan^{-1}\frac{x}{a}}$
2. 这通常不是简单的代数形式，需保留指数形式

:::
