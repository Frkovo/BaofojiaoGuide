---
title: 解题方法
---

# 解题方法

---

## 方法 1：构建 Truth Table

**适用场景**：给定逻辑电路图或布尔表达式，列出所有输入组合对应的输出。

**步骤**：
1. 确定输入变量个数 n → 共 2ⁿ 行
2. 按二进制顺序列出所有输入组合（000... → 111...）
3. 对每一行，按电路门逐级计算中间值
4. 计算最终输出值

**易错提醒**：
- 不要遗漏任何输入组合
- 逐门计算时注意 NOT 的优先级最高，AND 次之，OR 最低

---

## 方法 2：K-map 化简

**适用场景**：从 truth table 或 SOP 表达式出发，化简为最简 SOP。

**步骤**：
1. 画出 K-map 框架（Gray code 顺序：00, 01, 11, 10）
2. 填入 truth table 中的输出值（1 或 0）
3. 找出所有 2ⁿ 个相邻 1 的矩形块（可 wraparound）
4. 优先找最大的块（8 > 4 > 2 > 1）
5. 每个块写一个 product term
6. 合并所有 product term 得到 SOP

**K-map 布局（4 变量）**：
```
        CD
AB      00  01  11  10
00      .   .   .   .
01      .   .   .   .
11      .   .   .   .
10      .   .   .   .
```

**规则**：
- 相邻包括上下相邻、左右相邻、**边界 wraparound**
- 每个圈必须包含 1, 2, 4, 8 或 16 个 1
- 每个 1 至少被圈一次
- Don't care 条件可以作为 1 或 0 来帮助化简

---

## 方法 3：布尔代数化简

**适用场景**：给定布尔表达式，用代数法则化简。

**常用法则**：
| 法则 | 公式 |
|------|------|
| De Morgan's | $$\overline{A \cdot B} = \overline{A} + \overline{B}$$ |
| De Morgan's | $$\overline{A + B} = \overline{A} \cdot \overline{B}$$ |
| Double complement | $$\overline{\overline{A}} = A$$ |
| Distributive | $$A \cdot (B + C) = A \cdot B + A \cdot C$$ |
| Absorption | $$A + A \cdot B = A$$ |
| Annulment | $$A + \overline{A} = 1$$, $$A \cdot \overline{A} = 0$$ |

---

## 方法 4：SOP 从 Truth Table 提取

**适用场景**：给定 truth table，输出 SOP 表达式。

**步骤**：
1. 找出所有输出为 1 的行
2. 对每一行，写出对应的 minterm（变量为 1 写原变量，为 0 写反变量）
3. 所有 minterm 用 OR 连接

**示例**：
| A | B | X |
|---|---|---|
| 0 | 0 | 1 → $$\overline{A} \cdot \overline{B}$$ |
| 0 | 1 | 0 |
| 1 | 0 | 1 → $$A \cdot \overline{B}$$ |
| 1 | 1 | 0 |

SOP = $$\overline{A} \cdot \overline{B} + A \cdot \overline{B} = \overline{B}$$
