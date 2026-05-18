---
title: Boolean Algebra and Logic Circuits
---

# Boolean Algebra and Logic Circuits

## 核心考点
- Truth tables 构建与化简
- Boolean algebra laws（De Morgan's, distributive, commutative, associative）
- Karnaugh maps（K-map）化简
- Flip-flops（SR, JK）
- Half adder / Full adder

## Syllabus 覆盖范围
| Section | 内容 |
|---------|------|
| 15.2.1 | Truth tables and logic circuits |
| 15.2.2 | Boolean algebra simplification |
| 15.2.3 | Karnaugh maps |
| 15.2.4 | Flip-flops (SR, JK) |
| 15.2.5 | Adders (half adder, full adder) |

## 常见题型
| 题型 | 典型分值 | 出现频率 |
|------|---------|---------|
| Truth table from circuit | 4-5 分 | 必考 |
| K-map 化简 | 5-7 分 | 必考 |
| Boolean algebra simplification | 3-4 分 | 高频 |
| Flip-flop 分析 | 4-5 分 | 中频 |

## 核心公式
- De Morgan's：$$\overline{A \cdot B} = \overline{A} + \overline{B}$$, $$\overline{A + B} = \overline{A} \cdot \overline{B}$$
- Distributive：$$A \cdot (B + C) = A \cdot B + A \cdot C$$
- K-map：相邻格子可以合并（1, 2, 4, 8, ...）
- Half adder：$$S = A \oplus B$$, $$C_{out} = A \cdot B$$
