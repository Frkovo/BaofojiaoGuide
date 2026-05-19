---
title: 题型总览
sidebar_position: 8
---

# 题型总览

## 六种核心题型概览

| # | 题型 | 典型分值 | 出现频率 | 所属 Topic |
|---|------|---------|---------|-----------|
| 1 | 一阶线性 ODE（积分因子） | 6-10 | ~80% | First Order Differential Equations |
| 2 | 二阶常系数 ODE（含初值） | 6-11 | ~90% | Second Order Differential Equations |
| 3 | Maclaurin 级数展开 | 5-7 | ~90% | Maclaurin Series |
| 4 | 复数求根 / De Moivre | 4-6 | ~80% | Complex Numbers |
| 5 | 矩阵特征值 / 对角化 | 10-15 | ~90% | Matrices |
| 6 | Riemann 求和上下界 | 8-10 | ~85% | Riemann Sums |

## 各题型详细分析

### 题型 1：一阶线性 ODE（积分因子）

- **如何识别**：形如 $dy/dx + P(x)y = Q(x)$ 且不能用分离变量法
- **标准解法**：
  1. 求积分因子 $I = e^{\int P\,dx}$
  2. 两边乘以 $I$
  3. 左边化为 $\frac{d}{dx}(yI)$
  4. 两边积分
  5. 代入初始条件
- **详见**：[First Order Differential Equations](topics/first-order-differential-equations/question-types)

### 题型 2：二阶常系数 ODE

- **如何识别**：形如 $a\frac{d^2y}{dx^2} + b\frac{dy}{dx} + cy = f(x)$
- **标准解法**：
  1. 辅助方程 $am^2 + bm + c = 0$
  2. CF（实根/复根/重根）
  3. PI（待定系数法）
  4. 通解 = CF + PI
  5. 代入初始条件
- **详见**：[Second Order Differential Equations](topics/second-order-differential-equations/question-types)

### 题型 3：Maclaurin 级数

- **如何识别**：要求展开到 $x^n$ 或用级数近似积分
- **标准解法**：
  1. 求导 $f'(x), f''(x), \dots$
  2. 代入 $x=0$
  3. 代入公式 $f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots$
- **详见**：[Maclaurin Series](topics/maclaurin-series/question-types)

### 题型 4：复数求根 / De Moivre

- **如何识别**：求 $z^n = a+bi$ 的根，或证明三角恒等式
- **标准解法**：
  1. 写为 $re^{i\theta}$ 形式
  2. $z^{1/n} = r^{1/n}e^{i(\theta + 2k\pi)/n}$
  3. 代 $k = 0, 1, \dots, n-1$
- **详见**：[Complex Numbers](topics/complex-numbers/question-types)

### 题型 5：矩阵特征值 / 对角化

- **如何识别**：求特征值、用 Cayley-Hamilton 求逆、对角化
- **标准解法**：
  1. $\det(A - \lambda I) = 0$ 求特征值
  2. 解 $(A - \lambda I)v = 0$ 求特征向量
  3. 构造 $P$（特征向量为列）和 $D$（特征值为对角元）
- **详见**：[Matrices](topics/matrices/question-types)

### 题型 6：Riemann 求和

- **如何识别**：用 $n$ 个矩形求积分上下界
- **标准解法**：
  1. 画图确定矩形高度
  2. 求和 $\sum f(x_r) \cdot \frac{1}{n}$
  3. 用 $\sum r$、$\sum r^2$、$\sum r^3$ 化简
  4. 必要时取 $n \to \infty$
- **详见**：[Riemann Sums](topics/riemann-sums/question-types)

## 其他重要题型

| 题型 | 分值 | 出现频率 | 详见 |
|------|------|---------|------|
| 双曲函数恒等式和图像 | 3-5 | ~70% | [Hyperbolic Functions](topics/hyperbolic-functions/question-types) |
| 线性方程组一致性 | 4-9 | ~60% | [Systems of Linear Equations](topics/systems-of-linear-equations/question-types) |
| 隐式微分 | 8 | ~50% | [Implicit Differentiation](topics/implicit-differentiation/question-types) |
| 递推公式 | 7-11 | ~50% | [Integration Techniques](topics/integration-techniques/question-types) |
| 参数方程弧长 | 5-6 | ~30% | [Parametric Equations](topics/parametric-equations/question-types) |
