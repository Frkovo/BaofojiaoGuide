---
title: Tree Traversal
sidebar_position: 1
---

# Tree Traversal（树的遍历）

## 考纲要求

- 19.2 Recursion 应用于二叉树遍历
- 重点：中序遍历（升序输出）

## 遍历方式

| 遍历 | 顺序 | 结果 |
|------|------|------|
| 前序 Pre-order | 根 → 左 → 右 | 10 5 1 7 15 |
| 中序 In-order | 左 → 根 → 右 | 1 5 7 10 15 |
| 后序 Post-order | 左 → 右 → 根 | 1 7 5 15 10 |

Paper 4 重点考**中序遍历**，但有时也考前序/后序。

## 核心代码模板

### 中序遍历（OOP Node 对象版）
```python
def OutputInOrder(node):
    if node is None:
        return
    OutputInOrder(node.GetLeft())
    print(node.GetData())
    OutputInOrder(node.GetRight())
```

### 中序遍历（数组版）
```python
def InOrder(nodeIndex):
    if nodeIndex == -1:
        return
    InOrder(ArrayNodes[nodeIndex][0])
    print(ArrayNodes[nodeIndex][1])
    InOrder(ArrayNodes[nodeIndex][2])
```

### 中序遍历（Free-list 版）
```python
def InOrder(nodeIndex):
    if nodeIndex == -1:
        return
    InOrder(self.myTree[nodeIndex].leftPointer)
    print(self.myTree[nodeIndex].item)
    InOrder(self.myTree[nodeIndex].rightPointer)
```

### 全部三种遍历（Free-list 版）
```python
def PreOrder(nodeIndex):
    if nodeIndex == -1:
        return
    print(self.myTree[nodeIndex].item)
    PreOrder(self.myTree[nodeIndex].leftPointer)
    PreOrder(self.myTree[nodeIndex].rightPointer)

def InOrder(nodeIndex):
    if nodeIndex == -1:
        return
    InOrder(self.myTree[nodeIndex].leftPointer)
    print(self.myTree[nodeIndex].item)
    InOrder(self.myTree[nodeIndex].rightPointer)

def PostOrder(nodeIndex):
    if nodeIndex == -1:
        return
    PostOrder(self.myTree[nodeIndex].leftPointer)
    PostOrder(self.myTree[nodeIndex].rightPointer)
    print(self.myTree[nodeIndex].item)
```

## 调用方式

```python
# OOP 版
OutputInOrder(rootNode)

# 数组版
InOrder(RootPointer)

# Free-list 版
bst.InOrder(bst.rootPointer)
```

## 常见错误

- 递归 base case 条件写错（应该是 null/None/-1）
- 中序顺序记反（输出位置决定遍历顺序）
- 2D 数组版用 data 值递归而不是用索引递归
- 递归函数没写 return（虽然遍历不需要返回值，但要确保调用正确）
