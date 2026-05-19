# Parametric Equations — Common Mistakes

## Mistake 1: $\frac{d^2y}{dx^2}$ 直接用 $\frac{\ddot{y}}{\ddot{x}}$

**最严重、最常见的错误！**

**错误**：
$$\frac{d^2y}{dx^2} = \frac{\ddot{y}}{\ddot{x}}$$

**正确**：
$$\frac{d^2y}{dx^2} = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{\frac{dx}{dt}}$$

### 正确与错误对比

| 表达式 | 正确？ |
|--------|--------|
| $\frac{dy}{dx} = \frac{\dot{y}}{\dot{x}}$ | ✅ |
| $\frac{d^2y}{dx^2} = \frac{\ddot{y}}{\ddot{x}}$ | ❌ |
| $\frac{d^2y}{dx^2} = \frac{d}{dt}\left(\frac{\dot{y}}{\dot{x}}\right) / \dot{x}$ | ✅ |

## Mistake 2: 弧长公式漏平方

**错误**：
$$L = \int \sqrt{\frac{dx}{dt} + \frac{dy}{dt}}\,dt$$

**正确**：
$$L = \int \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt$$

## Mistake 3: 平方和展开错误

计算 $\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2$ 时，容易漏项或符号错误。

**建议**：列出每项的平方，合并同类项。使用 $x = a(t)$, $y = b(t)$ 的记号辅助。

## Mistake 4: 根号化简时忽略绝对值

$$\sqrt{\sin^2\frac{t}{2}} = \left|\sin\frac{t}{2}\right|$$

在 $t \in [0, 2\pi]$ 时，$\sin\frac{t}{2} \ge 0$ 当 $t/2 \in [0,\pi]$ 即 $t \in [0,2\pi]$，但若区间不同需注意符号。

## Mistake 5: 弧长积分上下限用错

弧长积分是对参数 $t$ 积分，不是对 $x$ 或 $y$。

**错误**：
$$L = \int_{x_1}^{x_2} \sqrt{\dot{x}^2 + \dot{y}^2}\,dt$$

**正确**：
$$L = \int_{t_1}^{t_2} \sqrt{\dot{x}^2 + \dot{y}^2}\,dt$$

## Mistake 6: 求 $\frac{dy}{dx}$ 时未化简

如 $\frac{dy}{dx} = \frac{t^2/(1+t^2)}{2t/(1+t^2)} = \frac{t^2}{2t} = \frac{t}{2}$，需约分至最简。

## Mistake 7: 对参数求导时链式法则应用错误

求 $\frac{d}{dt}\left(\frac{dy}{dx}\right)$ 时：
- 如果 $\frac{dy}{dx}$ 是 $t$ 的函数，直接求导
- 如果 $\frac{dy}{dx}$ 还是 $x$ 和 $y$ 的函数，需用链式法则
