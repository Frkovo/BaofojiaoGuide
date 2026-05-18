---
title: 考前速记
---

# 考前速记

## 必须记住的公式

### De Morgan's Laws
$$\overline{A \cdot B} = \overline{A} + \overline{B}$$
$$\overline{A + B} = \overline{A} \cdot \overline{B}$$

### K-map 化简规则
- 圈选 2ⁿ 个相邻 1（1, 2, 4, 8, 16）
- Gray code 顺序：00, 01, 11, 10
- Wraparound 相邻包括边界

### Half Adder
$$S = A \oplus B$$
$$C_{out} = A \cdot B$$

### Full Adder
$$S = A \oplus B \oplus C_{in}$$
$$C_{out} = A \cdot B + C_{in} \cdot (A \oplus B)$$

## 必考题型与套路
| 题型 | 关键步骤 | 验证 |
|------|---------|------|
| Truth table | 2ⁿ 行，逐门计算 | 用 SOP 回算检查 |
| K-map | Gray code 布局，圈最大 | 检查每个 1 都被圈 |
| Boolean simplify | 先 De Morgan's，再 distributive | 展开验证 |
| Flip-flop | SR：11 为 invalid；JK：11 为 toggle | 对照特性表 |

## Red Flags 🚩
| 情况 | 处理 |
|------|------|
| K-map 中两行/列跳变 2 bits | **顺序错了**，应该用 Gray code |
| 表达式上方横线覆盖多个项 | 需要 De Morgan's |
| SR flip-flop 出现 11 | 标记为 **Invalid** |
| SOP 表达式有括号嵌套 | 需要展开 |

## 考试快速检查清单
- [ ] K-map 行列顺序是 Gray code？
- [ ] SOP 表达式中没有多余括号？
- [ ] De Morgan's 应用后 AND/OR 对换了？
- [ ] Flip-flop 的 11 状态标为 Invalid？
- [ ] Half adder 只有 2 个输入？
- [ ] Full adder 有 3 个输入？
