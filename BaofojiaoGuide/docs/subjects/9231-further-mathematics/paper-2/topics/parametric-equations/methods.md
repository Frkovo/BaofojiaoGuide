# Parametric Equations — Solution Methods

## Method 1: Parametric Differentiation

### 1A: First Derivative $\frac{dy}{dx}$

**公式**：

$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{\dot{y}}{\dot{x}}$$

**步骤**：
1. 分别计算 $\frac{dx}{dt}$ 和 $\frac{dy}{dt}$
2. 相除得到 $\frac{dy}{dx}$
3. 如需化简，尽可能约简

### 1B: Second Derivative $\frac{d^2y}{dx^2}$

**公式**：

$$\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{\frac{dx}{dt}}$$

**步骤**：
1. 先求出 $\frac{dy}{dx}$（用 $t$ 表示）
2. 对 $t$ 求导：$\frac{d}{dt}\left(\frac{dy}{dx}\right)$
3. 除以 $\frac{dx}{dt}$ 得到 $\frac{d^2y}{dx^2}$
4. 化简

:::danger[常见错误]
$$\frac{d^2y}{dx^2} \neq \frac{\ddot{y}}{\ddot{x}}$$

$$\frac{d^2y}{dx^2} \neq \frac{d^2y/dt^2}{d^2x/dt^2}$$

必须按照 $\frac{d}{dt}\left(\frac{dy}{dx}\right) / \frac{dx}{dt}$ 来计算。
:::

## Method 2: Arc Length of Parametric Curves

**公式**：

$$L = \int_{t_1}^{t_2} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt$$

**步骤**：
1. 计算 $\frac{dx}{dt}$ 和 $\frac{dy}{dt}$
2. 分别平方后相加
3. 将根号内的表达式简化（常用恒等式）：
   - 完全平方公式
   - $\sin^2 t + \cos^2 t = 1$
   - $1 - \cos t = 2\sin^2(t/2)$
   - $1 + \cos t = 2\cos^2(t/2)$
4. 开方（注意区间内符号）
5. 在给定参数区间上积分

:::tip[常用化简思路]
当 $\frac{dx}{dt}$ 和 $\frac{dy}{dt}$ 含三角函数时，平方和通常可简化为 $A(1 \pm \cos t)$ 或 $A \sin^2 t$ 等形式。

再利用半角公式将根号打开：

$$\sqrt{1 - \cos t} = \sqrt{2\sin^2(t/2)} = \sqrt{2}\left|\sin\frac{t}{2}\right|$$

注意在给定区间内 $\sin(t/2)$ 的符号，去掉绝对值。
:::

## Method 3: Tangents and Normals

**步骤**：
1. 求 $\frac{dy}{dx}$ 在参数 $t$ 处的值
2. 代入对应点的 $x$、$y$ 坐标
3. 切线：$y - y(t_0) = m(x - x(t_0))$
4. 法线：$y - y(t_0) = -\frac{1}{m}(x - x(t_0))$

## Method 4: Stationary Points

令 $\frac{dy}{dx} = 0$，即 $\frac{dy}{dt} = 0$（当 $\frac{dx}{dt} \neq 0$ 时）。

解 $\frac{dy}{dt} = 0$ 得到 $t$ 值，代入 $x(t)$、$y(t)$ 得到坐标。
