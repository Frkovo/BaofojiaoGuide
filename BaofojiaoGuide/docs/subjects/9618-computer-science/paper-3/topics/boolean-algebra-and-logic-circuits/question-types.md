---
title: 题型分析
---

# 题型分析：Boolean Algebra and Logic Circuits

---

## 题型 1：根据电路图填写 Truth Table

### 典型例题：9618/s21/qp/31 Q7(a)
**题目**：A logic circuit has three inputs $A$, $B$, $C$ and two outputs $S$ and $C_{out}$. The circuit contains XOR, AND, and OR gates. Complete the truth table.

```
S = A XOR B XOR C_in
C_out = (A AND B) OR (C_in AND (A XOR B))
```

**Truth Table**（Full Adder）：

| $A$ | $B$ | $C_{in}$ | $S$ | $C_{out}$ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

<details>
<summary>📝 MS 展开查看</summary>

- **M1**：正确构造 8 行输入组合
- **A1**：全部 $S$ 值正确
- **A1**：全部 $C_{out}$ 值正确
- Note: This is a **full adder** circuit.

</details>

---

## 题型 2：K-map 化简

### 典型例题：9618/s23/qp/32 Q9
**题目**：Complete the K-map from the truth table and derive the simplest sum-of-products (SOP) expression.

**K-map 填入**（4 variables: $A$, $B$, $C$, $D$）：

```
        CD
AB      00  01  11  10
00       1   0   1   1
01       0   1   0   0
11       1   0   1   0
10       1   0   1   1
```

**化简结果（SOP）**：$$\overline{D} + \overline{B}CD + \overline{A}B\overline{C}D + ABCD$$

<details>
<summary>📝 MS 展开查看</summary>

- **M1**：正确将 truth table 填入 K-map
- **M1**：正确圈出相邻的 1
- **A1**：得到正确的简化表达式
- **A1**：最终 SOP 形式正确

</details>

---

## 题型 3：布尔代数化简（De Morgan's Laws）
### 典型例题：9618/w22/qp/32 Q8(c)
**题目**：Simplify the expression $$\overline{(A + B) \cdot C}$$ using De Morgan's laws.

**解题步骤**：
1. Apply De Morgan's: $\overline{(A + B) \cdot C} = \overline{A + B} + \overline{C}$
2. Apply De Morgan's again: $\overline{A + B} = \overline{A} \cdot \overline{B}$
3. Result: $\overline{A} \cdot \overline{B} + \overline{C}$

<details>
<summary>📝 MS 展开查看</summary>

- **M1**：正确应用 De Morgan's 第一次
- **M1**：正确应用 De Morgan's 第二次
- **A1**：最终简化结果正确

</details>

---

## 题型 4：Flip-flop 电路

### 典型例题：9618/w22/qp/32 Q8(a)
**题目**：Complete the truth table for the SR flip-flop.

**SR Flip-flop 特性表**：

| $S$ | $R$ | $Q(t)$ | $Q(t+1)$ | 状态 |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | Hold |
| 0 | 0 | 1 | 1 | Hold |
| 0 | 1 | 0 | 0 | Reset |
| 0 | 1 | 1 | 0 | Reset |
| 1 | 0 | 0 | 1 | Set |
| 1 | 0 | 1 | 1 | Set |
| 1 | 1 | 0 | - | Invalid |
| 1 | 1 | 1 | - | Invalid |

<details>
<summary>📝 MS 展开查看</summary>

- **B1**：$S=0, R=0$ 时 $Q(t+1)=Q(t)$
- **B1**：$S=0, R=1$ 时 $Q(t+1)=0$
- **B1**：$S=1, R=0$ 时 $Q(t+1)=1$
- **B1**：$S=1, R=1$ 时 Invalid / not allowed

</details>
