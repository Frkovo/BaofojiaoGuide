---
title: Linked Lists
sidebar_position: 1
---

# Linked Lists（链表）

## 考纲要求

- 19.1.7 Linked list ADT：find, insert, delete

## 常见题型

| 题型 | 分值 | 示例 |
|------|------|------|
| 声明节点类型和链表数组 | 2-4 | s21_qp_41 Q1a |
| 初始化链表数据 | 4 | s21_qp_41 Q1b |
| 遍历输出链表 | 6 | s21_qp_41 Q1c |
| 插入节点 | 7 | s21_qp_41 Q1d |
| 删除节点 | 6-8 |  |
| 查找节点 | 4-5 |  |

## 核心代码模板

### 方式一：Node class（Class 模拟 record）

```python
class node:
    def __init__(self):
        self.data = 0
        self.nextNode = 0
```

声明并初始化：
```python
linkedList = [node() for _ in range(10)]
linkedList[0].data = 1
linkedList[0].nextNode = 1
# ...
startPointer = 0
emptyList = 5
```

### 方式二：两个数组（data_array + pointer_array）

```python
data_array = [None] * 10
pointer_array = list(range(1, 10)) + [-1]
startPointer = -1
heapPointer = 0
```

### 遍历
```python
def OutputNodes(linkedList, startPointer):
    current = startPointer
    while current != -1:
        print(linkedList[current].data)
        current = linkedList[current].nextNode
```

### 插入到末尾
```python
def AddNode(linkedList, startPointer, emptyList):
    data = int(input("Enter data: "))
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

### 插入到头部
```python
def InsertAtHead(linkedList, startPointer, heapPointer, value):
    if heapPointer == -1:
        print("Linked list is full")
        return startPointer, heapPointer
    insertIndex = heapPointer
    heapPointer = pointer_array[heapPointer]
    linkedList[insertIndex].data = value
    linkedList[insertIndex].nextNode = startPointer
    startPointer = insertIndex
    return startPointer, heapPointer
```

### 查找节点
```python
def FindNode(linkedList, startPointer, target):
    current = startPointer
    while current != -1:
        if linkedList[current].data == target:
            return current
        current = linkedList[current].nextNode
    return -1
```

### 删除节点
```python
def DeleteNode(linkedList, startPointer, heapPointer, value):
    if startPointer == -1:
        return False, startPointer, heapPointer
    if linkedList[startPointer].data == value:
        temp = startPointer
        startPointer = linkedList[startPointer].nextNode
        linkedList[temp].nextNode = heapPointer
        heapPointer = temp
        return True, startPointer, heapPointer
    current = startPointer
    while linkedList[current].nextNode != -1:
        if linkedList[linkedList[current].nextNode].data == value:
            temp = linkedList[current].nextNode
            linkedList[current].nextNode = linkedList[temp].nextNode
            linkedList[temp].nextNode = heapPointer
            heapPointer = temp
            return True, startPointer, heapPointer
        current = linkedList[current].nextNode
    return False, startPointer, heapPointer
```

## 常见错误

- 忘记更新 heapPointer/emptyList
- 遍历时忘记更新 current（死循环）
- 删除时未将被删节点归还空闲链
- 插入时未检查空闲链是否为空
- 未处理空链表（startPointer == -1）
