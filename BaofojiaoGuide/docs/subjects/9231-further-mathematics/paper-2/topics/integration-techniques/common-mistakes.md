# Integration Techniques — Common Mistakes

## Mistake 1: 分部积分中 $u$ 和 $dv$ 选择不当

**错误选择**（以 $\int x e^x\,dx$ 为例）：
$$u = e^x,\quad dv = x\,dx$$

会导致积分变得更复杂。

**正确选择**（LIATE 法则）：
$$u = x,\quad dv = e^x\,dx$$

### LIATE 优先级速查

| 优先级 | 选 $u$ | 选 $dv$ |
|--------|--------|---------|
| 高 | $\ln x$ | 其余部分 |
| ↓ | $\sin^{-1}x, \tan^{-1}x$ | 其余部分 |
| ↓ | $x^n$ | 其余部分 |
| ↓ | $\sin x, \cos x$ | 其余部分 |
| 低 | $e^x$ | 其余部分 |

## Mistake 2: 递推公式中 $\frac{d}{dx}$ 与 $\frac{d}{dt}$ 混淆

在处理 $\int \sin^n x\,dx$ 时，分部积分：

$$u = \sin^{n-1}x,\quad dv = \sin x\,dx$$

$$du = (n-1)\sin^{n-2}x\cos x\,dx \quad (\text{正确})$$

**错误**：$du = (n-1)\sin^{n-2}x\,dx$（忘记对 $\sin x$ 内部求导的 $\cos x$）

## Mistake 3: 部分分式系数求解错误

常见误区是不对分母做完整分解。

$$\frac{2x^2+3x+1}{(x-1)(x^2+1)} = \frac{A}{x-1} + \frac{Bx+C}{x^2+1}$$

**错误**：写成 $\frac{A}{x-1} + \frac{B}{x^2+1}$（缺少 $x$ 项系数 $C$）

## Mistake 4: 换元忘记调整积分限

$$\int_0^1 f(x)\,dx \xrightarrow{x = \sin\theta} \int_?^? f(\sin\theta)\cos\theta\,d\theta$$

$dx = \cos\theta\,d\theta$，且当 $x=0$ 时 $\theta=0$，$x=1$ 时 $\theta=\frac{\pi}{2}$

**错误**：忘记改变积分上下限，仍用 $0$ 到 $1$。

## Mistake 5: 递推关系方向弄反

如 $nI_n = (n-1)I_{n-2}$，是降次递推。要从 $I_n$ 推到 $I_{n-2}$ 再推到 $I_0$ 或 $I_1$。

**错误**：试图从 $I_0$ 直接算到 $I_n$ 而不使用递推。

## Mistake 6: 有理函数积分中分子分母次数判断

当分子次数 $\ge$ 分母次数时，必须先做多项式除法。

**示例**：
$$\frac{x^3}{x-1} = x^2 + x + 1 + \frac{1}{x-1}$$

不做除法直接分解部分分式会导致错误。

## Mistake 7: 忘记常数 $C$

不定积分结果必须加 $+ C$。定积分则不需要。
