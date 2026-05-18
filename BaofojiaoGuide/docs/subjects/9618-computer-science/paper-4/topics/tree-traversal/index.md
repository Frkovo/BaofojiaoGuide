---
title: Tree Traversal
sidebar_position: 1
---

# Tree Traversal（树遍历）

## 考纲要求

- 19.2 Recursion 扩展到二叉树遍历

## 核心代码模板

### 中序遍历（2D 数组版本）
```python
def InOrder(nodeIndex):
    global ArrayNodes
    if nodeIndex == -1:
        return
    InOrder(ArrayNodes[nodeIndex][0])
    print(ArrayNodes[nodeIndex][1])
    InOrder(ArrayNodes[nodeIndex][2])
```

### 中序遍历（OOP 版本）
```python
def OutputInOrder(node):
    if node is None:
        return
    OutputInOrder(node.GetLeft())
    print(node.GetData())
    OutputInOrder(node.GetRight())
```

### 调用方式
```python
# 2D 数组版
InOrder(RootPointer)

# OOP 版
OutputInOrder(tree.GetRootNode())
```

## 三种遍历顺序

| 遍历方式 | 顺序 | 输出结果（示例树 10,5,15） |
|---------|------|--------------------------|
| 中序 InOrder | 左→根→右 | 5, 10, 15（升序！） |
| 前序 PreOrder | 根→左→右 | 10, 5, 15 |
| 后序 PostOrder | 左→右→根 | 5, 15, 10 |

Paper 4 只考中序遍历。

## 常见错误

- 递归 base case 写错
- 2D 数组版：用数据值而不是索引递归
- 忘记 return（递归 base case 不 return 导致继续执行）
