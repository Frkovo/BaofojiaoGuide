# Implicit Differentiation — Common Mistakes

## Mistake 1: 对 $y$ 的函数求导时忘记乘 $\frac{dy}{dx}$

**错误**：
$$\frac{d}{dx}(y^2) = 2y$$

**正确**：
$$\frac{d}{dx}(y^2) = 2y\frac{dy}{dx}$$

:::danger
这是隐函数求导中最常见、最致命的错误。每个含 $y$ 的函数求导后都要乘以 $\frac{dy}{dx}$。
:::

### 更多例子

| 函数 | 错误求导 | 正确求导 |
|------|----------|----------|
| $\sin y$ | $\cos y$ | $\cos y \frac{dy}{dx}$ |
| $e^y$ | $e^y$ | $e^y \frac{dy}{dx}$ |
| $\ln y$ | $\frac{1}{y}$ | $\frac{1}{y}\frac{dy}{dx}$ |
| $y^3$ | $3y^2$ | $3y^2\frac{dy}{dx}$ |

## Mistake 2: 乘积法则处理错误

**错误**：
$$\frac{d}{dx}(xy) = y$$

**正确**：
$$\frac{d}{dx}(xy) = y + x\frac{dy}{dx}$$

**错误**：
$$\frac{d}{dx}(x^2y) = 2xy$$

**正确**：
$$\frac{d}{dx}(x^2y) = 2xy + x^2\frac{dy}{dx}$$

## Mistake 3: $\frac{d^2y}{dx^2}$ 时直接用商法则忘记 $\frac{dy}{dx}$

求二阶导数时，对一阶导数表达式使用商法则后，结果中出现的 $y$ 项仍需要乘以 $\frac{dy}{dx}$。

## Mistake 4: 代入点坐标时顺序错误

求出 $\frac{dy}{dx} = -\frac{2x+y}{x+2y}$ 后，在 $(-1,2)$ 处的值：

**正确**：
$$\frac{dy}{dx} = -\frac{2(-1)+2}{-1+2(2)} = -\frac{0}{3} = 0$$

注意 $x=-1$、$y=2$ 同时代入分子分母。

## Mistake 5: 化简不彻底

求 $\frac{dy}{dx}$ 后，部分表达式可以约分或利用原方程简化，但过于简化有时反而浪费时间。注意：
- 若题目要求 "in terms of $x$ and $y$"，确保表达式中只有 $x$ 和 $y$
- 若要求 simplest form，需全部化简

## Mistake 6: 切线法线方程混淆

切线斜率 $= \frac{dy}{dx}$，法线斜率 $= -\frac{1}{\frac{dy}{dx}}$（当 $\frac{dy}{dx} \neq 0$）。

法线方程：$y - y_0 = -\frac{1}{m}(x - x_0)$

## Mistake 7: 驻点判断

令 $\frac{dy}{dx} = 0$ 时，注意 $\frac{dy}{dx}$ 是分式，分子为 0 即可。

但还需确保分母在此点不为 0，否则该点可能是奇点而非驻点。
