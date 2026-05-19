---
title: 详细策略
sidebar_position: 9
---

# 详细策略

## 前 5 分钟策略

1. **快速浏览所有 8 题**，标记：
   - 每题考察的 topic
   - 各小问的分值
   - 是否包含"show that"（通常是送分）
   - 是否有复杂的代数和矩阵计算
2. **制定答题顺序**：
   - 先做熟悉的 topic
   - 先做分值/时间比高的题
   - 先做"show that"题

## 各 Topic 答题策略

### Hyperbolic Functions

- 恒等式证明：从指数形式出发
- 弧长/表面积：代入公式，利用恒等式化简
- 反双曲函数：记住对数形式

### Complex Numbers

- 求根：先求模和辐角，再套公式
- De Moivre：$z^n + z^{-n} = 2\cos n\theta$ 常用
- 级数求和：等比数列求和 + De Moivre

### Maclaurin Series

- 用对数微分法处理 $a^x$ 或 $f(x)^{g(x)}$
- 逐项求导到所需阶数
- 验证 $f(0)$ 是否有定义

### Matrices

- 3$\times$3 行列式用 Sarrus 规则或展开
- 特征向量：解 $(A - \lambda I)v = 0$，行化简
- 对角化：$P$ 的列是特征向量，$D$ 对角元是特征值

### Systems of Linear Equations

- 计算系数矩阵的行列式
- 行列式为 0 时无唯一解
- 对增广矩阵行化简判断一致性

### First Order ODE

- 分类：线性（积分因子）vs 可分离
- 积分因子算出后不要忘记乘右边
- 初值条件代入求常数

### Second Order ODE

- 先求 CF，再求 PI
- CF 形式取决于辅助方程的根
- PI 用待定系数法，注意与 CF 重叠

### Implicit Differentiation

- 一阶导：逐项微分，每项乘 $dy/dx$
- 二阶导：对一阶导结果再微分，代入原方程

### Parametric Equations

- 一阶导：$dy/dx = (dy/dt)/(dx/dt)$
- 二阶导：$d^2y/dx^2 = d/dt(dy/dx) / (dx/dt)$
- 弧长：$L = \int \sqrt{(dx/dt)^2 + (dy/dt)^2}\,dt$

### Integration Techniques

- 递推公式：分部积分 $n$ 次
- 代入法：注意换积分限

### Riemann Sums

- 画图确定矩形高度
- 求和公式记牢
- 上下界要找对方向

## 最后 10 分钟检查清单

- [ ] 是否有未答的题
- [ ] 检查符号错误
- [ ] 检查积分常数是否已求
- [ ] 检查矩阵乘法是否正确
- [ ] 检查数值精度是否符合要求
- [ ] 检查"show that"题是否逻辑闭环
- [ ] 检查每题是否按要求留下了必要步骤
