---
title: 知识点总结
---

# 布尔代数与逻辑电路 (Boolean Algebra and Logic Circuits)

## 逻辑门 (Logic Gates)

### 基本逻辑门

| 门 | 符号 | 布尔表达式 | 真值表 (A, B → Q) |
|---|---|---|---|
| **NOT** | 三角形 + 小圆 | $Q = \overline{A}$ | $0 \to 1,\; 1 \to 0$ |
| **AND** | D 形 | $Q = A \cdot B$ | $00 \to 0,\; 01 \to 0,\; 10 \to 0,\; 11 \to 1$ |
| **OR** | 弧形 | $Q = A + B$ | $00 \to 0,\; 01 \to 1,\; 10 \to 1,\; 11 \to 1$ |
| **NAND** | AND + 小圆 | $Q = \overline{A \cdot B}$ | $00 \to 1,\; 01 \to 1,\; 10 \to 1,\; 11 \to 0$ |
| **NOR** | OR + 小圆 | $Q = \overline{A + B}$ | $00 \to 1,\; 01 \to 0,\; 10 \to 0,\; 11 \to 0$ |
| **XOR** | OR 加弧线 | $Q = A \oplus B$ | $00 \to 0,\; 01 \to 1,\; 10 \to 1,\; 11 \to 0$ |

:::tip[记忆口诀]
- AND: 全1出1
- OR: 有1出1
- NAND: AND取反，全1出0
- NOR: OR取反，全0出1
- XOR: 不同出1
:::

## 真值表 (Truth Tables)

### 构建方法

- **从逻辑电路**: 列出所有输入组合，逐门计算中间值，得到最终输出
- **从布尔表达式**: 逐项计算表达式的值，覆盖 $2^n$ 种输入组合
- **从问题描述**: 翻译文字条件为逻辑条件，确定每个输入组合的输出

### 步骤

1. 确定输入变量个数 $n$，共有 $2^n$ 行
2. 按二进制顺序列出所有输入组合
3. 逐行计算中间信号值
4. 计算最终输出值

:::warning[注意]
输入组合应按二进制顺序（000, 001, 010, ...）排列，不要乱序
:::

## 布尔代数 (Boolean Algebra)

### 基本定律

- **交换律 (Commutative)**: $A + B = B + A$, $A \cdot B = B \cdot A$
- **结合律 (Associative)**: $(A + B) + C = A + (B + C)$, $(A \cdot B) \cdot C = A \cdot (B \cdot C)$
- **分配律 (Distributive)**: $A \cdot (B + C) = A \cdot B + A \cdot C$, $A + (B \cdot C) = (A + B) \cdot (A + C)$

### 基本规则

- $A + 0 = A$, $A + 1 = 1$
- $A \cdot 0 = 0$, $A \cdot 1 = A$
- $A + A = A$, $A \cdot A = A$
- $A + \overline{A} = 1$, $A \cdot \overline{A} = 0$
- $\overline{\overline{A}} = A$ (双重否定律)

### 吸收律 (Absorption)

- $A + A \cdot B = A$
- $A \cdot (A + B) = A$

### 德·摩根定律 (De Morgan's Laws)

$$ \overline{A + B} = \overline{A} \cdot \overline{B} $$

$$ \overline{A \cdot B} = \overline{A} + \overline{B} $$

- 推广: $\overline{A + B + C + ...} = \overline{A} \cdot \overline{B} \cdot \overline{C} \cdot ...$
- 推广: $\overline{A \cdot B \cdot C \cdot ...} = \overline{A} + \overline{B} + \overline{C} + ...$

:::tip[德·摩根定律应用]
- "断开"长非号: 与变或，或变与，每个变量取反
- 常用于将 AND-OR 电路转为 NAND-NAND 或 NOR-NOR 实现
:::

## 卡诺图 (Karnaugh Maps / K-maps)

### 基本结构

- **2 变量 K-map**: $2 \times 2$ 网格（4 个格子）
- **3 变量 K-map**: $2 \times 4$ 网格（8 个格子）
- **4 变量 K-map**: $4 \times 4$ 网格（16 个格子）

### 标注规则

- 行和列的标签按 **格雷码 (Gray code)** 顺序排列
  - 每次只改变一个变量
  - 2 变量: 00, 01, 11, 10
  - 相邻格子之间仅一个变量不同

### 分组规则 (Grouping Rules)

- 每个组必须是 **矩形**，大小为 $2^n$（1, 2, 4, 8, 16）
- 每个组尽可能大（覆盖更多 1）
- **环绕 (Wrap-around)**: 网格边缘的格子可以跨边界分组
- **重叠 (Overlap)**: 格子可以被多个组共享
- 所有值为 1 的格子必须至少被一个组覆盖
- 不能包含值为 0 的格子
- 可用无关项 (don't care / X) 来扩大分组

### 简化 SOP 表达式

1. 在 K-map 中标出所有输出为 1 的格子
2. 按规则找出所有质蕴含项(prime implicants)
3. 选择最少的组覆盖所有 1
4. 每个组对应一个乘积项，相加即得最简 SOP

:::warning[注意]
- 4 变量 K-map 的角落 (0,0) 和 (3,3) 可以环绕分组
- 每组的项数 = 去掉的变量数；组越大，表达式越简
:::

## 触发器 (Flip-flops)

### SR 触发器 (SR Flip-flop)

| S | R | Q(next) | 说明 |
|---|---|---|---|
| 0 | 0 | Q | 保持状态 |
| 0 | 1 | 0 | 复位 (Reset) |
| 1 | 0 | 1 | 置位 (Set) |
| 1 | 1 | - | 禁止状态 (Invalid) |

- 使用两个交叉耦合的 NAND 或 NOR 门构成
- **作为数据存储**: 能存储 1 位二进制数据
- 电平触发或边沿触发

### JK 触发器 (JK Flip-flop)

| J | K | Q(next) | 说明 |
|---|---|---|---|
| 0 | 0 | Q | 保持状态 |
| 0 | 1 | 0 | 复位 (Reset) |
| 1 | 0 | 1 | 置位 (Set) |
| 1 | 1 | $\overline{Q}$ | 翻转 (Toggle) |

- 解决了 SR 触发器的禁止状态问题
- J = S, K = R, 但 J=K=1 时触发翻转
- 常用于计数器、分频器

### 触发器应用

- **寄存器**: 多个触发器并行存储多位数据
- **计数器**: JK 触发器级联实现二进制计数
- **状态机**: 存储有限状态机的当前状态

## 加法器 (Adders)

### 半加器 (Half Adder)

- 输入: A, B（两个 1 位二进制数）
- 输出: S (Sum), C (Carry out)

| A | B | S | C |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

- **表达式**: $S = A \oplus B$, $C = A \cdot B$
- **电路**: 1 个 XOR 门 + 1 个 AND 门
- 不能处理进位输入

### 全加器 (Full Adder)

- 输入: A, B, $C_{in}$（进位输入）
- 输出: S (Sum), $C_{out}$ (Carry out)

| A | B | $C_{in}$ | S | $C_{out}$ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

- **表达式**:
  - $S = A \oplus B \oplus C_{in}$
  - $C_{out} = (A \cdot B) + (C_{in} \cdot (A \oplus B))$
- **电路**: 由两个半加器 + 1 个 OR 门构成
- $n$ 位加法器: 将 $n$ 个全加器级联（串行进位加法器，Ripple-carry adder）

:::tip[考点提示]
- 半加器 vs 全加器: 半加器无进位输入，全加器有进位输入
- 全加器是构建多位加法器的基本单元
- 串行进位加法器速度受限，因进位需要逐级传播
:::
