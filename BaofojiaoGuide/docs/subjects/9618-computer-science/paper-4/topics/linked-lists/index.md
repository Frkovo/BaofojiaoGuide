---
title: Linked Lists
sidebar_position: 1
---

# Linked Lists（链表）

## 考纲要求

- 19.1.7 Linked list ADT：查找、插入、删除操作
- 用数组实现链表，每个节点包含 data 和 nextNode

## 常见题型

| 题型 | 分值 | 示例 |
|------|------|------|
| 声明节点类型和数组 | 2-4 | s21_qp_41 Q1a |
| 初始化链表数据 | 4 | s21_qp_41 Q1b |
| 遍历输出链表 | 6 | s21_qp_41 Q1c |
| 插入节点到末尾 | 7 | s21_qp_41 Q1d |
| 查找节点 | 4-5 |  |
| 删除节点 | 6-8 |  |

## 核心代码模板

### 节点记录类型
```python
class node:
    def __init__(self):
        self.data = 0
        self.nextNode = 0
```

### 声明并初始化链表
```python
linkedList = [node() for _ in range(10)]

# 手动初始化数据（根据题目表格）
linkedList[0].data = 1
linkedList[0].nextNode = 1
linkedList[1].data = 5
linkedList[1].nextNode = 4
# ...

startPointer = 0
emptyList = 5
```

### 遍历输出
```python
def outputNodes(linkedList, startPointer):
    current = startPointer
    while current != -1:
        print(linkedList[current].data)
        current = linkedList[current].nextNode
```

### 插入到末尾
```python
def addNode(linkedList, startPointer, emptyList):
    data = int(input("Enter the data: "))
    if emptyList == -1:
        return False, startPointer, emptyList
    newNode = emptyList
    emptyList = linkedList[emptyList].nextNode
    linkedList[newNode].data = data
    linkedList[newNode].nextNode = -1
    if startPointer == -1:
        startPointer = newNode
    else:
        current = startPointer
        while linkedList[current].nextNode != -1:
            current = linkedList[current].nextNode
        linkedList[current].nextNode = newNode
    return True, startPointer, emptyList
```

### 查找节点
```python
def findNode(linkedList, startPointer, target):
    current = startPointer
    while current != -1:
        if linkedList[current].data == target:
            return current
        current = linkedList[current].nextNode
    return -1
```

### 删除节点
```python
def deleteNode(linkedList, startPointer, emptyList, target):
    if startPointer == -1:
        return False, startPointer, emptyList
    if linkedList[startPointer].data == target:
        temp = startPointer
        startPointer = linkedList[startPointer].nextNode
        linkedList[temp].nextNode = emptyList
        emptyList = temp
        return True, startPointer, emptyList
    current = startPointer
    while linkedList[current].nextNode != -1:
        if linkedList[linkedList[current].nextNode].data == target:
            temp = linkedList[current].nextNode
            linkedList[current].nextNode = linkedList[temp].nextNode
            linkedList[temp].nextNode = emptyList
            emptyList = temp
            return True, startPointer, emptyList
        current = linkedList[current].nextNode
    return False, startPointer, emptyList
```

## 常见错误

- 忘记更新 emptyList 指针
- 遍历时忘记更新 current 导致死循环
- 删除时没有把被删节点归还空闲链表
- 插入时没有检查空闲链表是否为空
- 没有处理空链表（startPointer == -1）的特殊情况
