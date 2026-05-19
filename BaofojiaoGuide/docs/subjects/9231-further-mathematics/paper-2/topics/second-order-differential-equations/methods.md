---
title: 解题方法
sidebar_position: 3
---

# Solution Methods — Second Order Differential Equations

## 方法一：常系数 ODE 的完整流程

:::info[Steps]

1. 写出辅助方程 $am^2 + bm + c = 0$
2. 求解 $m$ 得到三种情形之一
3. 写出 CF
4. 根据 RHS 形式试设 PI
5. 代入原方程比较系数确定 PI
6. 通解 = CF + PI
7. 若有初值条件，代入求解常数

:::

:::warning[待定系数冲突处理]

若 PI 的试设形式与 CF 中的某项重复，则乘 $x$（一次重复）或 $x^2$（二次重复）。

例如：$y'' - 2y' + y = e^x$，CF 含 $Ae^x$，PI 需试设 $Cx^2e^x$。

:::

## 方法二：Euler-Cauchy 方程

### 解法 A：直接设 $y = t^m$

:::info[Steps]

1. 设 $y = t^m$，代入齐次部分
2. 得到关于 $m$ 的二次方程
3. 根据根的类型写出 CF
4. 对非齐次项，用待定系数法（设为 $Ct^k$ 等）
5. 通解 = CF + PI

:::

### 解法 B：变量代换 $t = e^u$

:::info[Steps]

1. 令 $t = e^u$，则 $u = \ln t$
2. 改写导数：
   - $\frac{dy}{dt} = \frac{1}{t}\frac{dy}{du}$
   - $\frac{d^2y}{dt^2} = \frac{1}{t^2}\left(\frac{d^2y}{du^2} - \frac{dy}{du}\right)$
3. 代入后化为常系数 ODE（以 $u$ 为自变量）
4. 按常系数方法求解
5. 用 $u = \ln t$ 代回

:::

## 方法三：耦合方程组（矩阵法）

:::info[Steps]

1. 将方程组写作 $\dot{\mathbf{x}} = A\mathbf{x} + \mathbf{b}(t)$
2. 求 $A$ 的特征值 $\lambda_1, \lambda_2$
3. 求对应的特征向量 $\mathbf{v}_1, \mathbf{v}_2$
4. 齐次解：$\mathbf{x}_c = C_1\mathbf{v}_1e^{\lambda_1 t} + C_2\mathbf{v}_2e^{\lambda_2 t}$
5. 求特解（如有非齐次项）
6. 代入初值确定常数

:::

## 方法四：初值条件的应用

:::info[Steps]

1. 先求通解 $y = y_c + y_p$
2. 对 $y$ 求导得 $y'$
3. 代入 $x = x_0$：$y(x_0) = y_0$ 和 $y'(x_0) = y_0'$
4. 解两个方程组成的方程组求 $A$ 和 $B$
5. 回代得到特解

:::
