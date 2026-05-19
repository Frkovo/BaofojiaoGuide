---
title: Systems of Linear Equations
sidebar_position: 1
---

# Systems of Linear Equations（线性方程组）

---

## 考纲要求

1. 理解线性方程组的矩阵表示：$A\mathbf{x} = \mathbf{b}$
2. 会用行列式判断方程组是否有唯一解（$\det A \neq 0$）或无唯一解（$\det A = 0$）
3. 理解齐次方程组（$A\mathbf{x} = \mathbf{0}$）和非齐次方程组（$A\mathbf{x} = \mathbf{b}$）的区别
4. 能判断方程组的相容性（consistency）和不相容性（inconsistency）
5. 能给出方程组的几何解释（平面相交、直线、三棱柱等）
6. 掌握参数值变化时方程组解的情况分类讨论

---

## 常见题型

| 题型 | 分值 | 链接 |
|------|------|------|
| 行列式条件（唯一解 / 无唯一解） | 2–5 分 | [题型 1](./question-types.md#question-type-1-行列式条件) |
| 相容性与不相容性 | 3–4 分 | [题型 2](./question-types.md#question-type-2-相容性与不相容性) |
| 几何解释（平面、直线、三棱柱） | 2–3 分 | [题型 3](./question-types.md#question-type-3-几何解释) |

---

## 核心公式

### 矩阵形式

$$
A\mathbf{x} = \mathbf{b}, \quad
A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix},\;
\mathbf{x} = \begin{pmatrix} x \\ y \\ z \end{pmatrix},\;
\mathbf{b} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}
$$

### 唯一解条件

$$
\det A \neq 0 \quad \Rightarrow \quad \text{唯一解（unique solution）}
$$

### 无唯一解条件

$$
\det A = 0 \quad \Rightarrow \quad \text{零个解或无穷多解}
$$

### 齐次方程组 $A\mathbf{x} = \mathbf{0}$

- $\det A \neq 0$：仅有平凡解 $\mathbf{x} = \mathbf{0}$
- $\det A = 0$：有非平凡解（无穷多解）

---

## 常见错误

- 混淆 $\det A = 0$ 意味无解（实际可能是无穷多解或矛盾无解）
- 增广矩阵行变换时忘记处理右侧常数
- 几何解释中混淆"三棱柱"和"两平面平行相交"
- 参数讨论遗漏特殊情况
