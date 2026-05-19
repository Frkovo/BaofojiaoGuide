# Parametric Equations

## 考纲要求

- 对参数方程求一阶导数 $\frac{dy}{dx}$
- 对参数方程求二阶导数 $\frac{d^2y}{dx^2}$
- 计算参数曲线的弧长
- 处理涉及参数 $t$ 或 $\theta$ 的曲线问题

## 常见题型

| 题型 | 分值 | 频率 |
|------|------|------|
| 参数方程求导（$\frac{dy}{dx}$、$\frac{d^2y}{dx^2}$） | 3–5 marks | 必考 |
| 参数曲线的弧长计算 | 5–6 marks | 高频 |

## 核心公式

一阶导数：

$$\frac{dy}{dx}=\frac{dy/dt}{dx/dt}=\frac{\dot{y}}{\dot{x}}$$

二阶导数：

$$\frac{d^2y}{dx^2}=\frac{d}{dx}\left(\frac{dy}{dx}\right)=\frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{dx/dt}$$

弧长公式（参数形式）：

$$L=\int_a^b\sqrt{\left(\frac{dx}{dt}\right)^2+\left(\frac{dy}{dt}\right)^2}\,dt$$

或简写为：

$$L=\int_a^b\sqrt{\dot{x}^2+\dot{y}^2}\,dt$$

## 常见错误

1. **忘记除以 $\dot{x}$**：$\frac{d}{dx}\left(\frac{dy}{dx}\right)$ 需先对 $t$ 求导再除以 $\dot{x}$
2. **弧长公式遗漏平方**：根号内漏掉平方符号
3. **积分限混淆**：参数 $t$ 的范围与 $x$、$y$ 的范围混淆
4. **$\frac{d^2y}{dx^2}$ 直接对 $t$ 求二阶导**：误以为 $\frac{d^2y}{dx^2}=\frac{\ddot{y}}{\ddot{x}}$
5. **化简不彻底**：根号内表达式未完全平方化简
