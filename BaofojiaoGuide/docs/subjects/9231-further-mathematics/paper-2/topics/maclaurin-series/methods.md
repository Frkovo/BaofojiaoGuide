# Maclaurin Series — Solution Methods

## Method 1: From First Principles (Differentiation)

**适用情况**：题目要求"from first principles"或直接使用定义求展开式。

**步骤**：
1. 写出 $f(x)$ 并逐次求导：
   $$f(x),\; f'(x),\; f''(x),\; f'''(x),\; \ldots$$
2. 代入 $x=0$ 计算各阶导数值：
   $$f(0),\; f'(0),\; f''(0),\; f'''(0),\; \ldots$$
3. 代入 Maclaurin 公式：
   $$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots$$
4. 如需指定项数，截断至所需项。

:::tip[何时使用]
当函数无法通过标准展开直接代入时（如 $2^x$、$\sin^{-1}x$、$\ln(\cosh x)$），必须用此法。
:::

## Method 2: Substitution into Standard Series

**适用情况**：函数可以表示为 $f(g(x))$，其中 $f$ 的标准展开已知。

**步骤**：
1. 确定内层函数 $u = g(x)$ 和外层函数 $f(u)$
2. 写出 $f(u)$ 的标准 Maclaurin 展开
3. 代入 $u = g(x)$，保留所需的 $x$ 的幂次
4. 合并同类项

**常用代入**：

| 原函数 | 代入方式 |
|--------|----------|
| $e^{x^2}$ | $e^u$ 展开，$u=x^2$ |
| $\ln(1+\sin x)$ | $\ln(1+u)$ 展开，$u=\sin x$ |
| $\cos(x^2)$ | $\cos u$ 展开，$u=x^2$ |

## Method 3: Logarithmic Differentiation

**适用情况**：函数形如 $y = [f(x)]^{g(x)}$ 或乘积形式。

**步骤**：
1. 取 $\ln y = g(x)\ln f(x)$
2. 隐函数求导得 $\frac{y'}{y} = g'(x)\ln f(x) + g(x)\frac{f'(x)}{f(x)}$
3. 两边乘 $y$ 得 $y'$
4. 继续求高阶导或直接展开

:::warning[注意]
此法常用于求 $a^x$ 型函数的导数（而非展开本身），但 $a^x$ 也常通过 $a^x = e^{x\ln a}$ 处理。
:::

## Method 4: Series Multiplication/Division

**适用情况**：函数是两个已知展开函数的乘积或商。

**步骤**：
1. 分别展开两个函数至所需项数
2. 相乘（逐项相乘，忽略高于所需阶数的项）
3. 相除（用长除法或待定系数法）
4. 合并同类项

## Method 5: Term-by-Term Integration

**适用情况**：需要利用级数近似定积分。

**步骤**：
1. 将被积函数展开为 Maclaurin 级数
2. 逐项积分（在积分限内）
3. 代入上下限计算
4. 如需误差估计，考察第一项被截断项的大小

:::note[示例]
$$e^{-x^2} = 1 - x^2 + \frac{x^4}{2!} - \frac{x^6}{3!} + \cdots$$

$$\int_0^{0.1} e^{-x^2}\,dx \approx \int_0^{0.1} \left(1 - x^2 + \frac{x^4}{2}\right)dx = \left[x - \frac{x^3}{3} + \frac{x^5}{10}\right]_0^{0.1}$$
:::
