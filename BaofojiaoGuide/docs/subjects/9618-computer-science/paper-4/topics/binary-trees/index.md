---
title: Binary Trees
sidebar_position: 1
---

# Binary Trees（二叉树）

## 考纲要求

- 19.1.8 Binary tree ADT：insert, find, traverse
- ADT 可以从数组或链表实现

## 常见题型

| 题型 | 分值 | 示例 |
|------|------|------|
| Node 类定义 + 构造器 | 4 | s24_qp_42 Q2a |
| TreeClass + 构造器 | 4 | s24_qp_42 Q2b |
| InsertNode | 6 | s24_qp_42 Q2b |
| OutputTree | 4 | s24_qp_42 Q2b |
| 中序遍历 | 5-7 | w21_qp_41 Q3e |

## 核心代码模板

### 方式一：OOP 方式（array of Node objects）

```python
class Node:
    def __init__(self, data):
        self.__LeftPointer = -1
        self.__Data = data
        self.__RightPointer = -1

class TreeClass:
    def __init__(self):
        self.__Tree = [Node(-1) for _ in range(20)]
        self.__FirstNode = -1
        self.__NumberNodes = 0

    def InsertNode(self, newNode):
        if self.__NumberNodes == 0:
            self.__Tree[0] = newNode
            self.__FirstNode = 0
            self.__NumberNodes = self.__NumberNodes + 1
            return
        self.__Tree[self.__NumberNodes] = newNode
        current = self.__FirstNode
        direction = ""
        while current != -1:
            previous = current
            if newNode.GetData() < self.__Tree[current].GetData():
                current = self.__Tree[current].GetLeft()
                direction = "left"
            else:
                current = self.__Tree[current].GetRight()
                direction = "right"
        if direction == "left":
            self.__Tree[previous].SetLeft(self.__NumberNodes)
        else:
            self.__Tree[previous].SetRight(self.__NumberNodes)
        self.__NumberNodes = self.__NumberNodes + 1

    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No nodes")
            return
        for i in range(self.__NumberNodes):
            print(self.__Tree[i].GetLeft(), self.__Tree[i].GetData(),
                  self.__Tree[i].GetRight())
```

### 方式二：Free-list 方式（leftPointer 做空闲链）

```python
class Node:
    def __init__(self):
        self.item = None
        self.leftPointer = -1
        self.rightPointer = -1

class BST:
    def __init__(self, capacity):
        self.myTree = [Node() for _ in range(capacity)]
        self.rootPointer = -1
        self.nextFreePointer = 0
        # 初始化空闲链表
        for i in range(capacity - 1):
            self.myTree[i].leftPointer = i + 1
        self.myTree[capacity - 1].leftPointer = -1

    def InsertNode(self, item):
        if self.nextFreePointer == -1:
            print("No nodes free")
            return
        newNode = self.nextFreePointer
        self.nextFreePointer = self.myTree[self.nextFreePointer].leftPointer
        self.myTree[newNode].item = item
        self.myTree[newNode].leftPointer = -1
        self.myTree[newNode].rightPointer = -1
        if self.rootPointer == -1:
            self.rootPointer = newNode
            return
        current = self.rootPointer
        while True:
            if item < self.myTree[current].item:
                if self.myTree[current].leftPointer == -1:
                    self.myTree[current].leftPointer = newNode
                    break
                else:
                    current = self.myTree[current].leftPointer
            else:
                if self.myTree[current].rightPointer == -1:
                    self.myTree[current].rightPointer = newNode
                    break
                else:
                    current = self.myTree[current].rightPointer

    def InOrder(self, nodeIndex):
        if nodeIndex == -1:
            return
        self.InOrder(self.myTree[nodeIndex].leftPointer)
        print(self.myTree[nodeIndex].item, end=" ")
        self.InOrder(self.myTree[nodeIndex].rightPointer)
```

## 常见错误

- 插入时比较方向搞反（小左大右）
- 忘记处理空树
- 未更新空闲链表指针
- 递归遍历没有 base case
