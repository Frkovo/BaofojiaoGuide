---
title: 常见错误
---

# 常见错误

## 错误 1：K-map 行列顺序用错
**问题**：使用二进制顺序（00, 01, 10, 11）代替 Gray code 顺序（00, 01, 11, 10）
**后果**：相邻 1 不能正确圈选，化简结果错误
**正确做法**：每行每列只能变化 1 个 bit（Gray code）

## 错误 2：De Morgan's 应用时忘记翻转运算符
**问题**：$$\overline{A \cdot B} = \overline{A} \cdot \overline{B}$$ ❌
**正确**：$$\overline{A \cdot B} = \overline{A} + \overline{B}$$ ✓（AND 变 OR）
**记忆口诀**：断开横线，符号翻转

## 错误 3：K-map 圈选时遗漏 wraparound
**问题**：认为第一行和最后一行不相邻，第一列和最后一列不相邻
**正确做法**：K-map 是**环形**的，上下左右边界都相邻

## 错误 4：Flip-flop 的 Invalid 状态混淆
**问题**：SR flip-flop 中 S=1,R=1 时认为 Q=1 或 Q=0
**正确**：S=1,R=1 是 **Invalid / Not allowed**（Q 和 NOT Q 同时为 1）

## 错误 5：SOP 形式不符要求
**问题**：最终表达式包含不必要的括号或非标准形式
**正确**：SOP = product term 用 AND 连接，再全部用 OR 连接
**示例**：$$A \cdot B + \overline{A} \cdot C$$ ✓（不是 $$(A \cdot B) + (\overline{A} \cdot C)$$）

## 错误 6：半加器与全加器混淆
**区别**：
- **Half adder**：2 个输入（A, B），2 个输出（S, C_out）
- **Full adder**：3 个输入（A, B, C_in），2 个输出（S, C_out）
- Full adder = 两个 half adder 级联
