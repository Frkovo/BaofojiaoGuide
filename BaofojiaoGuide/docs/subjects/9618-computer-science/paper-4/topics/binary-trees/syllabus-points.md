---
title: 考纲要点
sidebar_position: 6
---

# 考纲要点

## Syllabus 19.1.8 — Binary Tree ADT

### 核心知识点

1. **Binary Tree 定义**: 一种层次化的数据结构, 每个节点最多有两个子节点
   - 左子节点 (left child): 值小于父节点的元素
   - 右子节点 (right child): 值大于或等于父节点的元素
   - 类比: 文件系统目录结构, 组织结构图

2. **Binary Search Tree (BST) 特性**:
   - 左子树所有节点的值 < 根节点的值
   - 右子树所有节点的值 >= 根节点的值
   - 左右子树本身也是 BST (递归定义)
   - **中序遍历 (in-order) 得到升序序列**

3. **TreeNode 结构**:
   | 属性 | 类型 | 说明 |
   |------|------|------|
   | `Data` | INTEGER / STRING | 节点存储的数据 |
   | `LeftPointer` | INTEGER | 左子节点数组下标, -1 表示无 |
   | `RightPointer` | INTEGER | 右子节点数组下标, -1 表示无 |

4. **TreeClass 结构**:
   | 属性 | 类型 | 说明 |
   |------|------|------|
   | `RootPointer` | INTEGER | 根节点下标, -1 表示空树 |
   | `Tree` / `Nodes` | ARRAY OF TreeNode | 节点数组 |
   | `FreePointer` | INTEGER | 下一个空闲位置 |

5. **核心操作**:
   - **InsertNode**: 按 BST 规则插入新节点
   - **OutputTree / InOrder**: 递归中序遍历输出
   - **PreOrder / PostOrder**: 其他遍历方式 (较少考)

6. **三种遍历顺序**:
   | 遍历方式 | 顺序 | 输出结果特性 |
   |----------|------|-------------|
   | Pre-order | root → left → right | 根节点最先输出 |
   | In-order | left → root → right | 升序输出 (BST) |
   | Post-order | left → right → root | 根节点最后输出 |

### Array-based 实现核心机制

- 节点存储在数组中, 使用数组下标代替指针
- `$-1$` 表示空指针 (null)
- `$FreePointer$` 管理空闲位置, 从 `$0$` 递增
- 新节点放入 `$Tree[FreePointer]$`, 然后 `$FreePointer$` 递增
- 查找插入位置: 从 `$RootPointer$` 开始, 根据值大小向左/右移动

### 典型考题要求

- 声明 TreeNode class (Data + LeftPointer + RightPointer + constructor)
- 声明 TreeClass (RootPointer + 节点数组 + constructor)
- 实现 InsertNode 过程
- 实现 OutputTree 过程 (中序递归)
- 编写主程序提供菜单交互
- 追踪树的状态 (trace)

### 与其他主题的联系

- **Recursion**: OutputTree 通常用递归实现
- **Arrays**: 二叉树底层使用数组存储
- **OOP**: 使用 class 封装 TreeNode 和 TreeClass
- **Sorting**: BST 中序遍历得到有序序列
- **Searching**: BST 提供 O(log n) 的平均查找效率
