---
title: 考纲要点
sidebar_position: 6
---

# 考纲要点

## Syllabus 19.2 — Recursion applied to binary trees

### 核心知识点

1. **二叉树的递归定义**
   - 二叉树是递归数据结构: 每个节点是其左右子树的根
   - 遍历自然地适合用递归实现

2. **三种遍历方式**
   | 遍历方式 | 访问顺序 | BST 输出特性 |
   |----------|---------|-------------|
   | In-order (中序) | left → root → right | 升序序列 |
   | Pre-order (前序) | root → left → right | 根最先 |
   | Post-order (后序) | left → right → root | 根最后 |

3. **递归遍历模式**
   - Base case: 空节点 (null / `-1`) → 停止递归
   - Recursive case: 按遍历顺序调用左右子树 + 输出

4. **两种数据表示**
   - **2D Array**: `Tree[Index][0..2]` → `[Data, Left, Right]`, `-1` 表示空
   - **OOP**: `TreeNode` 类, `GetData()`, `GetLeft()`, `GetRight()`, `NULL` 表示空

### 考试要求

- 编写递归过程进行 in-order / pre-order / post-order 遍历
- 在 2D array 和 OOP 两种实现上应用递归遍历
- Trace 遍历过程 (填写遍历输出序列)
- 根据遍历输出结果推断树的结构

### 典型考题

- **9618/w21/qp/41 Q3(e)**: 2D array 二叉树 in-order 递归遍历 (7 marks)
- **9618/s25/qp/41 Q3(d)**: OOP 二叉树 in-order 递归遍历 (5 marks)

### 与其他主题的联系

- **Recursion**: 遍历的核心实现方式
- **Binary Trees**: 遍历是二叉树的基本操作
- **2D Arrays**: 二叉树的一种存储表示
- **OOP**: 二叉树的另一种封装方式
- **Sorting**: BST in-order 遍历 = 排序输出
