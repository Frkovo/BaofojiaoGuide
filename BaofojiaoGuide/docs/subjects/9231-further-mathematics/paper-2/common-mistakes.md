---
title: 常见错误
sidebar_position: 5
---

# 常见错误

## 1. 双曲函数（Hyperbolic Functions）

### 混淆双曲恒等式与三角恒等式

| 错误 | 正确 |
|------|------|
| $\cosh^2 x + \sinh^2 x = 1$ | $\cosh^2 x - \sinh^2 x = 1$ |
| $\cosh^2 x + \sinh^2 x = \cosh 2x$ | $\cosh^2 x + \sinh^2 x = \cosh 2x$ ✔（这个是对的） |
| $\sinh^{-1} x = \frac{1}{\sinh x}$ | $\sinh^{-1} x$ 是反函数，不是倒数 |

### 弧长公式中的符号错误

弧长公式：$\displaystyle L = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx$

常见错误：平方根内写了 $-$

## 2. 复数（Complex Numbers）

### 复根的角度遗漏

解 $z^n = a + bi$ 时，忘记加 $2k\pi$ 导致只得到一个根。

:::danger[致命错误]
$z^n = r e^{i\theta}$ 的根是 $z = r^{1/n} e^{i(\theta + 2k\pi)/n}$，$k = 0, 1, \dots, n-1$

必须加 $2k\pi$！
:::

### De Moivre 定理使用错误

$(re^{i\theta})^n = r^n e^{in\theta}$，不是 $r^n e^{i\theta^n}$

## 3. Maclaurin 级数

### 忘记除以阶乘

$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots$

常见错误：$f(x) = f(0) + f'(0)x + f''(0)x^2 + \cdots$（漏了 $n!$）

## 4. 矩阵（Matrices）

### 特征向量的求解错误

解 $(A - \lambda I)v = 0$ 时，行化简出错导致特征向量不对。

### 对角化顺序不匹配

$A = PDP^{-1}$ 中，$P$ 的列必须与 $D$ 的对角元顺序对应。

## 5. 一阶 ODE

### 积分因子忘记取指数

$e^{\int P\,dx}$ 中的积分结果必须取指数，不是 $e$ 的 $\int P\,dx$ 就直接是 IF。

### 忘记乘整个方程

乘以 IF 后，左边变成 $\frac{d}{dx}(y \cdot \text{IF})$，右边 IF 也要乘 $Q(x)$。

## 6. 二阶 ODE

### 辅助方程的根用错

$m = \alpha \pm i\beta$ 时，CF 是 $e^{\alpha x}(A\cos\beta x + B\sin\beta x)$

### 特解形式选择错误

| $f(x)$ 类型 | 特解试设形式 |
|-------------|-------------|
| $k$（常数） | $C$ |
| $ax + b$ | $Cx + D$ |
| $ax^2 + bx + c$ | $Cx^2 + Dx + E$ |
| $ke^{px}$ | $Ce^{px}$（若 $p$ 不是 CF 的根） |
| $k\cos\omega x$ 或 $k\sin\omega x$ | $C\cos\omega x + D\sin\omega x$ |

## 7. Riemann 求和

### 矩形高度取端点错误

- **上界**：取区间内最大值（右端点对于增函数，左端点对于减函数）
- **下界**：取区间内最小值
- 画图确认！

### 求和公式记错

$$
\sum_{r=1}^{n} r^2 = \frac{n(n+1)(2n+1)}{6}, \quad \text{不是 } \frac{n(n+1)(2n-1)}{6}
$$

## 8. 隐式微分

### 忘记链式法则

对 $y$ 的函数求导时，必须乘以 $\frac{dy}{dx}$

如 $\frac{d}{dx}(y^2) = 2y\frac{dy}{dx}$，不是 $2y$

## 9. 参数方程

### 二阶导数公式用错

$$
\frac{d^2y}{dx^2} = \frac{d}{dt}\left(\frac{dy}{dx}\right) \Big/ \frac{dx}{dt}
$$

不是 $\displaystyle \frac{d^2y/dt^2}{d^2x/dt^2}$

:::danger[最常见的错误]
$\displaystyle \frac{d^2y}{dx^2} \neq \frac{d^2y/dt^2}{d^2x/dt^2}$
:::

## 10. 递推公式

### 分部积分的 $u$ 和 $dv$ 选错

通常令 $u$ 为幂函数或对数函数，$dv$ 为指数或三角/双曲函数。

### 忘记递推公式适用于所有 $n$

验证 $n=1$ 或 $n=0$ 的基础情形后再应用递推。
