# Maclaurin Series — Common Mistakes

## Mistake 1: 忘记除以阶乘

**错误**：
$$f(x) \approx f(0) + f'(0)x + f''(0)x^2 + f'''(0)x^3$$

**正确**：
$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots$$

:::warning
这是一个非常容易犯的错误。记住：$x^n$ 项的系数必须除以 $n!$。
:::

## Mistake 2: 复合函数展开时遗漏项

**错误**：展开 $e^{-x^2}$ 时只写到 $1 - x^2$ 就停止了。

**正确**：$e^{-x^2} = 1 - x^2 + \frac{x^4}{2} - \frac{x^6}{6} + \cdots$（需包含足够项）

## Mistake 3: 符号错误

### $\sin x$ 交错符号
$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots$$

### $\cos x$ 交错符号
$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots$$

### $\ln(1+x)$ 交错符号
$$\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots$$

## Mistake 4: $\ln$ 展开定义域混淆

$$\ln(1+x) \text{ 展开有效当 } |x| &lt; 1$$

但题目通常要求展开式而非考虑收敛域。注意 $\ln(1+e^x)$ 展开时先处理 $1+e^x$ 再取 $\ln$。

## Mistake 5: 对 $a^x$ 求导错误

**错误**：认为 $\frac{d}{dx}a^x = xa^{x-1}$

**正确**：$\frac{d}{dx}a^x = a^x \ln a$（通过 $a^x = e^{x\ln a}$）

## Mistake 6: 积分近似时忽略截断误差

用级数近似积分时，截断项的选择要确保精度。如求近似值时，注意题目要求的精度（通常 3 s.f. 或 4 s.f.）。

## Mistake 7: 乘法展开丢项

将两个级数相乘时，容易遗漏交叉项。

**示例**：$(1 + x + \frac{x^2}{2})(x - \frac{x^3}{6})$ 展开到 $x^3$ 项：

- $1 \cdot x = x$
- $1 \cdot (-\frac{x^3}{6}) = -\frac{x^3}{6}$
- $x \cdot x = x^2$
- $\frac{x^2}{2} \cdot x = \frac{x^3}{2}$

结果：$x + x^2 + \frac{x^3}{3}$

注意 $x \cdot (-\frac{x^3}{6})$ 是 $x^4$ 项，$x$ 到 $x^3$ 可忽略。
