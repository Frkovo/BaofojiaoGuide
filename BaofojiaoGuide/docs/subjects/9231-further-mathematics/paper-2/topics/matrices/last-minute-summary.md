---
title: Matrices - Last Minute Summary
sidebar_position: 7
---

# Matrices 考前速览

---

## 核心公式

| 公式 | 说明 |
|------|------|
| $\det(A - \lambda I) = 0$ | 特征方程 |
| $(A - \lambda I)\mathbf{v} = \mathbf{0}$ | 特征向量定义 |
| $A^2 - \operatorname{tr}(A)A + \det(A)I = 0$ | $2 \times 2$ 特征方程特例 |
| $A^n + a_{n-1}A^{n-1} + \cdots + a_0 I = 0$ | Cayley-Hamilton |
| $A = PDP^{-1}$ | 对角化 |
| $A^n = PD^nP^{-1}$ | 高次幂 |
| $D^n = \operatorname{diag}(\lambda_1^n, \lambda_2^n, \dots)$ | 对角矩阵幂 |

---

## 解题流程图

```
求特征值 → 求特征向量 → Cayley-Hamilton / 对角化
        ↘            ↘
      $A^{-1}$    $A^n = PD^nP^{-1}$
     化简多项式
```

---

## 常见套路

### 求 $A^{-1}$ 的两种方法

1. **Cayley-Hamilton**：写出特征方程 → 代入 $A$ → 移项
2. **对角化**：$A^{-1} = PD^{-1}P^{-1}$

### 化简 $(A - kI)^n$

展开后利用 Cayley-Hamilton 消去高次项。

### 处理 $f(A)$ 的对角化

若 $A = PDP^{-1}$，则 $f(A) = Pf(D)P^{-1}$，其中 $f(D) = \operatorname{diag}(f(\lambda_1), f(\lambda_2), \dots)$。

---

## 检查清单

- [ ] 特征值计算是否检查了 $\det(A - \lambda I) = 0$？
- [ ] 特征向量是否非零？
- [ ] Cayley-Hamilton 中常数项是否加了 $I$？
- [ ] 对角化中 $P$ 和 $D$ 的顺序是否匹配？
- [ ] $P^{-1}$ 的公式是否正确（除以 $\det P$）？
- [ ] $A^n$ 中的 $n$ 是幂次，$D$ 的对角元也需取 $n$ 次幂？
- [ ] $3 \times 3$ 行列式展开符号是否用对（$+ - +$）？

---

## 必须记住

> **Cayley-Hamilton**: $A$ 满足特征方程，常数变 $I$。
>
> **对角化**: 特征向量排成 $P$，特征值排成 $D$，顺序要一致。
>
> **高次幂**: $A^n = PD^nP^{-1}$，$D$ 的对角元取 $n$ 次方。
