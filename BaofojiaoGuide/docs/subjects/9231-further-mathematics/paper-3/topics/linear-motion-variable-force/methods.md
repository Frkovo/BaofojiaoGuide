---
title: 解题方法
sidebar_position: 3
---

# Solution Methods — Linear Motion Under Variable Force

## 方法一：直接积分法 $a = dv/dt$

适用于力是时间函数或速度函数。

:::info[Steps]

1. 写出 $m\frac{dv}{dt} = F(v)$
2. 分离变量：$\int \frac{m}{F(v)} dv = \int dt$
3. 积分，代入初始条件 $v(0) = v_0$
4. 解得 $v(t)$
5. 再积分得 $x(t) = \int v(t) dt$

:::

## 方法二：位移作为变量 $a = v dv/dx$

适用于求速度与位移的关系。

:::info[Steps]

1. 用 $F = mv\frac{dv}{dx}$
2. 分离变量：$\int mv dv = \int F(x) dx$
3. 积分得 $\frac{1}{2}mv^2$ 的表达式
4. 代入初始条件
5. 解得 $v(x)$

:::

## 方法三：空气阻力 $kv$

适用于阻力正比于速度。

:::info[Steps]

1. $m\frac{dv}{dt} = mg - kv$（下落）
2. 分离变量：$\int \frac{m}{mg - kv} dv = \int dt$
3. 积分得 $v(t) = \frac{mg}{k}(1 - e^{-kt/m})$
4. 极限速度 $v_T = mg/k$
5. 再积分得 $x(t)$

:::

## 方法四：空气阻力 $kv^2$

适用于阻力正比于速度平方。

:::info[Steps]

1. $m\frac{dv}{dt} = mg - kv^2$
2. 分离变量：$\int \frac{m}{mg - kv^2} dv = \int dt$
3. 用部分分式或反双曲正切积分
4. 极限速度 $v_T = \sqrt{mg/k}$
5. 也可用 $v\frac{dv}{dx}$ 形式求 $v(x)$

:::
