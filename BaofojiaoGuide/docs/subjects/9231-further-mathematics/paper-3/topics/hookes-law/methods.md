---
title: 解题方法
sidebar_position: 3
---

# Solution Methods — Hooke's Law

## 方法一：静态平衡法

适用求弹性绳在重力下的伸长量。

:::info[Steps]

1. 画受力图，标出重力 $mg$ 和张力 $T$
2. 平衡条件：$T = mg$（竖直）或分量相等
3. 代入 $T = \frac{\lambda x}{L}$，求 $x$
4. 注意自然长度 $L$ 和总长度 $L + x$

:::

## 方法二：能量法

适用于求速度、最大位移等。

:::info[Steps]

1. 确定初末状态的能量
2. 写出能量守恒：
   $\frac{1}{2}mv_1^2 + mgh_1 + \frac{\lambda x_1^2}{2L} = \frac{1}{2}mv_2^2 + mgh_2 + \frac{\lambda x_2^2}{2L}$
3. 代入已知量，求解未知量
4. 注意弹性绳松弛时 $\text{EPE} = 0$

:::

## 方法三：组合弹性系统

适用于多根弹性绳的系统。

:::info[Steps]

1. 判断串联还是并联
2. 并联：总 $\lambda_{\text{eq}} = \lambda_1 + \lambda_2$，伸长量相同
3. 串联：$\frac{1}{\lambda_{\text{eq}}} = \frac{1}{\lambda_1} + \frac{1}{\lambda_2}$，张力相同
4. 用等效弹性模量代入计算

:::

## 方法四：圆周运动 + 弹性绳

适用于弹性绳连接旋转质点。

:::info[Steps]

1. 弹性绳提供向心力
2. $T = \frac{\lambda x}{L} = m\omega^2 r$
3. 几何关系：$r = L + x$
4. 联立求 $x$ 或 $\omega$

:::
