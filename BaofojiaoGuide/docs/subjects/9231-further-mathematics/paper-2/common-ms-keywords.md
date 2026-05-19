---
title: MS 关键词速查
sidebar_position: 6
---

# MS 关键词速查

## 通用缩写

| MS 缩写 | 含义 |
|---------|------|
| **M1** | 方法分（正确方法，不扣数值错误） |
| **A1** | 精度分（在 M 分已得的基础上给） |
| **B1** | 独立分（不依赖方法的正确结果） |
| **DM1** | 依赖方法分（依赖前一个 M* 分） |
| **DB1** | 依赖独立分 |
| **FT** | Follow-through（允许基于前面错误继续给分） |
| **AG** | Answer Given（题目已给答案，需要验证推导） |
| **CAO** | Correct Answer Only |
| **CWO** | Correct Working Only |
| **ISW** | Ignore Subsequent Working |
| **SOI** | Seen Or Implied |
| **SC** | Special Case |
| **WWW** | Without Wrong Working |
| **AWRT** | Answer Which Rounds To |
| **AEF/OE** | Any Equivalent Form / Or Equivalent |

## 各 Topic 常见关键词

### Hyperbolic Functions

| MS 原句 | 含义 |
|---------|------|
| Use exponential forms | 用指数形式代入 |
| Use $\cosh^2 x - \sinh^2 x = 1$ | 应用双曲恒等式 |
| Solves quadratic in $e^x$ | 解关于 $e^x$ 的二次方程 |
| Integrates to $\sinh x$ | 积分为 $\sinh x$ |
| Uses arc length formula | 使用弧长公式 |

### Complex Numbers

| MS 原句 | 含义 |
|---------|------|
| Writes $z$ in $re^{i\theta}$ form | 写出 $z = re^{i\theta}$ 形式 |
| Uses de Moivre | 应用 De Moivre 定理 |
| States $k = 0,1,2$ | 列出 $k$ 的所有取值 |
| Substitutes $z = e^{i\theta}$ | 代入 $z = e^{i\theta}$ |
| Equates real/imaginary parts | 比较实部/虚部 |

### Maclaurin Series

| MS 原句 | 含义 |
|---------|------|
| Differentiates to find $f'(x)$ | 求一阶导 |
| Evaluates at $x = 0$ | 在 $x = 0$ 处取值 |
| Uses $f(x) = f(0) + f'(0)x + \dots$ | 代入 Maclaurin 公式 |
| Writes series up to $x^n$ | 展开到 $x^n$ 项 |

### Matrices

| MS 原句 | 含义 |
|---------|------|
| Attempts $\det(A - \lambda I) = 0$ | 求特征方程 |
| Solves characteristic equation | 解特征方程 |
| Finds eigenvectors | 求特征向量 |
| Forms $P$ and $D$ | 构造 $P$ 和 $D$ 矩阵 |
| Uses Cayley-Hamilton | 应用 Cayley-Hamilton 定理 |

### Differential Equations

| MS 原句 | 含义 |
|---------|------|
| Finds integrating factor | 求积分因子 |
| Multiplies through by IF | 方程两边乘以 IF |
| Identifies LHS as derivative | 识别左边为 $\frac{d}{dx}(y \cdot \text{IF})$ |
| Auxiliary equation | 写出辅助方程 |
| Complimentary function | 齐次解/通解 |
| Particular integral | 特解（待定系数法） |
| Applies boundary/initial conditions | 代入边界/初值条件 |

### Riemann Sums

| MS 原句 | 含义 |
|---------|------|
| Forms sum of areas | 构造矩形面积和 |
| Uses $\sum r$, $\sum r^2$, $\sum r^3$ | 应用求和公式 |
| Takes limit as $n \to \infty$ | 取 $n \to \infty$ 极限 |

### Integration

| MS 原句 | 含义 |
|---------|------|
| Integration by parts | 分部积分 |
| Reduction formula | 递推公式 |
| Substitutes $x = \sin\theta$ | 代入 $x = \sin\theta$ |
| Valid for $n \geq 2$ | 对 $n \geq 2$ 成立 |

## MS 评分原则

1. **M 分**：方法正确即可得，不因数值/代数错误扣
2. **A 分**：必须在对应 M 分已得的前提下才给
3. **B 分**：独立给分，不依赖其他步骤
4. **DM/DB**：依赖前序标记（标记为 $*$）
5. **FT**：若前面错了但后续方法正确，可以 FT 给 A/B 分
6. **ISW**：如果正确结果后出现多余错误工作，忽略后续内容
