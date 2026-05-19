---
title: Matrices - Common Mistakes
sidebar_position: 6
---

# Matrices 常见错误

---

## 1. 特征方程符号错误

**错误**：写为 $\det(\lambda I - A) = 0$ 并展开时符号搞混。

**正确**：$\det(A - \lambda I) = 0$。虽然 $\det(\lambda I - A) = 0$ 在数学上等价，但展开后多项式可能差一个因子 $(-1)^n$，易出错。

**建议**：统一使用 $\det(A - \lambda I) = 0$。

---

## 2. 特征向量为零向量

**错误**：解 $(A - \lambda I)\mathbf{v} = \mathbf{0}$ 时取 $\mathbf{v} = \mathbf{0}$。

**正确**：特征向量必须为非零向量。若所有变量都被确定为零，说明该 $\lambda$ 不是特征值，或计算有误。

---

## 3. Cayley-Hamilton 代入混淆

**错误**：将特征方程 $p(\lambda) = 0$ 中的 $\lambda$ 替换为 $A$ 时忘记将常数项乘以 $I$。

**错误示例**：
$$
\lambda^2 - 5\lambda + 6 = 0 \Rightarrow A^2 - 5A + 6 = 0 \quad (\times)
$$

**正确**：
$$
\lambda^2 - 5\lambda + 6 = 0 \Rightarrow A^2 - 5A + 6I = 0 \quad (\checkmark)
$$

---

## 4. 对角化 $P$ 和 $D$ 顺序不匹配

**错误**：$P$ 的第一列是 $\lambda_1$ 的特征向量，但 $D$ 的 $(1,1)$ 位置却写了 $\lambda_2$。

**正确**：$P$ 第 $i$ 列的特征向量必须对应 $D$ 的第 $i$ 个对角元。

---

## 5. 高次幂计算中 $D^n$ 错误

**错误**：$D^n$ 写成 $\begin{pmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{pmatrix}^n = \begin{pmatrix} \lambda_1^n & 0 \\ 0 & \lambda_2^n \end{pmatrix}$ 计算正确，但代入时忘记取 $n$ 次方。

**检查**：$D^2 = \begin{pmatrix} \lambda_1^2 & 0 \\ 0 & \lambda_2^2 \end{pmatrix}$，不是 $\begin{pmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{pmatrix}^2 = \begin{pmatrix} \lambda_1^2 & 0 \\ 0 & \lambda_2^2 \end{pmatrix}$（结果虽对，但过程要理解）。

---

## 6. $P^{-1}$ 计算错误

**错误**：$2 \times 2$ 矩阵的逆公式记错。

**正确**：
$$
P = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \quad P^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
$$

**常见错误**：忘记除以 $\det(P)$，或主副对角线元素位置记反。

---

## 7. 多项化简时未反复代入

**错误**：对于 $A^4$，直接计算 $A^4 = (5A - 6I)^2$，但忘记展开时 $A$ 和 $I$ 不交换（其实交换没问题，但需确认）。

**正确方法**：反复利用 $A^2 = 5A - 6I$ 降次。

---

## 8. 3 × 3 行列式展开符号错误

**错误**：展开 $\det(A - \lambda I)$ 时符号规律 $+ - +$ 记错。

**正确**：按第一行展开：
$$
\begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix} = a_{11}\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix} - a_{12}\begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix} + a_{13}\begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix}
$$
