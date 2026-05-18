---
title: Binary Trees
sidebar_position: 1
---

# Binary Trees（二叉树）

## 考纲要求

- 19.1.8 Binary tree ADT：描述特征、实现插入和查找
- ADT 可以从内置类型或其他 ADT 实现

## 常见题型

| 题型 | 分值 | 示例 |
|------|------|------|
| Node 类定义+构造器 | 4 | s24_qp_42 Q2a |
| getter/setter 方法 | 3+3 | s24_qp_42 Q2a |
| TreeClass 定义+构造器 | 4 | s24_qp_42 Q2b |
| InsertNode 方法 | 6 | s24_qp_42 Q2b |
| OutputTree 方法 | 4 | s24_qp_42 Q2b |
| 主程序插入+输出 | 4 | s24_qp_42 Q2c |

## 核心代码模板

```python
class Node:
    def __init__(self, data):
        self.__LeftPointer = -1
        self.__Data = data
        self.__RightPointer = -1

    def GetLeft(self):
        return self.__LeftPointer

    def GetRight(self):
        return self.__RightPointer

    def GetData(self):
        return self.__Data

    def SetLeft(self, p):
        self.__LeftPointer = p

    def SetRight(self, p):
        self.__RightPointer = p


class TreeClass:
    def __init__(self):
        self.__Tree = [Node(-1) for _ in range(20)]
        self.__FirstNode = -1
        self.__NumberNodes = 0

    def InsertNode(self, newNode):
        if self.__NumberNodes == 0:
            self.__Tree[0] = newNode
            self.__FirstNode = 0
            self.__NumberNodes += 1
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
        self.__NumberNodes += 1

    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No nodes")
            return
        for i in range(self.__NumberNodes):
            print(self.__Tree[i].GetLeft(), self.__Tree[i].GetData(),
                  self.__Tree[i].GetRight())
```

## 常见错误

- 插入时比较方向搞反
- 忘记判断空树情况
- 插入后未递增 NumberNodes
- OutputTree 未用 getter 方法访问属性
