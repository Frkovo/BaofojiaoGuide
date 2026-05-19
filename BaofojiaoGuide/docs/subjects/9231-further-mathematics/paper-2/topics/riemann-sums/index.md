# Riemann Sums

## 考纲要求

- 利用矩形法求定积分的上界（Upper Bound）
- 利用矩形法求定积分的下界（Lower Bound）
- 利用 Riemann 和近似估计 $\ln N!$（Stirling 型近似）
- 理解等分分割与不等分分割的区别

## 常见题型

| 题型 | 分值 | 频率 |
|------|------|------|
| 上界矩形估计 | 4 marks | 高频 |
| 下界矩形估计 | 4 marks | 高频 |
| Stirling 型近似（$\ln N!$） | 8 marks | 中频 |

## 核心公式

Riemann 上界（递增函数 $f(x)$，右端点）：

$$\int_a^b f(x)\,dx\approx\sum_{i=1}^n f(x_i)\Delta x\quad\text{(上界)}$$

Riemann 下界（递增函数 $f(x)$，左端点）：

$$\int_a^b f(x)\,dx\approx\sum_{i=0}^{n-1} f(x_i)\Delta x\quad\text{(下界)}$$

递减函数则上下界与递增函数相反。

Stirling 近似：

$$\ln N!=\sum_{r=1}^N\ln r\approx N\ln N-N+\frac{1}{2}\ln(2\pi N)$$

利用积分估计 $\ln N!$：

$$\int_1^N \ln x\,dx &lt; \ln N! &lt; \int_1^N \ln x\,dx+\ln N$$

## 常见错误

1. **上下界方向混淆**：递增函数与递减函数的上下界规则相反
2. **矩形端点选错**：左端点与右端点混淆
3. **$\ln N!$ 与积分关系混淆**：误将求和直接等同积分而非估计
4. **分割数 $n$ 与求和范围不匹配**：分子分母中 $n$ 的对应关系错误
5. **不等式方向错误**：放缩过程中不等号方向弄反
