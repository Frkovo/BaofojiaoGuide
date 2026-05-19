# Implicit Differentiation — Solution Methods

## Method 1: Finding $\frac{dy}{dx}$

**步骤**：
1. 对等式两边同时对 $x$ 求导
2. 对每个 $y$ 的函数项，使用链式法则乘 $\frac{dy}{dx}$
3. 对 $x$ 与 $y$ 的乘积项，使用乘积法则
4. 将所有含 $\frac{dy}{dx}$ 的项移到等式一边
5. 提出 $\frac{dy}{dx}$ 并求解

**示例流程**：

$$x^2 + y^2 = 25$$

$$2x + 2y\frac{dy}{dx} = 0$$

$$\frac{dy}{dx} = -\frac{x}{y}$$

:::tip[链式法则]
$$\frac{d}{dx}f(y) = f'(y)\frac{dy}{dx}$$

$$\frac{d}{dx}\sin y = \cos y\frac{dy}{dx}$$

$$\frac{d}{dx}e^y = e^y\frac{dy}{dx}$$
:::

## Method 2: Finding $\frac{d^2y}{dx^2}$

### Sub-method 2A: Direct Differentiation

**步骤**：
1. 对 $\frac{dy}{dx}$ 的表达式再次对 $x$ 求导
2. 右侧使用商法则（如果是分式形式）
3. 遇到 $\frac{dy}{dx}$ 时，代入第一步的表达式
4. 利用原方程化简

### Sub-method 2B: Implicit Second Derivative

有时先对原方程再求导一次更简单：

1. 对第一步得到的方程再对 $x$ 求导
2. 直接得到含 $\frac{d^2y}{dx^2}$ 的方程
3. 代入 $\frac{dy}{dx}$ 的表达式

:::warning[注意]
$$\frac{d^2y}{dx^2} \neq \frac{d^2y/dt^2}{d^2x/dt^2}$$

正确的做法是：

$$\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right)$$
:::

## Method 3: Values at Specific Points

**步骤**：
1. 先求出 $\frac{dy}{dx}$ 的一般表达式
2. 代入给定点的坐标 $(x_0, y_0)$
3. 计算数值（注意 $x$、$y$ 都代入）

**切线方程**：$y - y_0 = m(x - x_0)$，其中 $m = \frac{dy}{dx}\big|_{(x_0,y_0)}$

**法线方程**：$y - y_0 = -\frac{1}{m}(x - x_0)$（$m \neq 0$ 时）

## Method 4: Stationary Points on Implicit Curves

**步骤**：
1. 令 $\frac{dy}{dx} = 0$
2. 代入原方程（通常得到一个关于 $x$、$y$ 的简化方程）
3. 与原方程联立求解驻点坐标
4. 用二阶导数判断极值性质

:::note[关键思想]
$\frac{dy}{dx}=0$ 等价于分子为 0（当 $\frac{dy}{dx}$ 是分式时）。
:::
