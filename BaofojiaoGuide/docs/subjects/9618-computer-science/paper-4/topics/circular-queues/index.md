---
title: Circular Queues
sidebar_position: 1
---

# Circular Queues（循环队列）

## 考纲要求

- 19.1.6 Queue ADT 扩展：循环队列实现

## 核心代码模板

### 方式一：用 NumberItems 计数

```python
Queue = [-1] * 20
HeadPointer = -1
TailPointer = -1
NumberItems = 0

def Enqueue(item):
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems == 20:
        return False
    if HeadPointer == -1:
        HeadPointer = 0
    TailPointer = (TailPointer + 1) % 20
    Queue[TailPointer] = item
    NumberItems = NumberItems + 1
    return True

def Dequeue():
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems == 0:
        return -1
    item = Queue[HeadPointer]
    HeadPointer = (HeadPointer + 1) % 20
    NumberItems = NumberItems - 1
    return item
```

### 方式二：牺牲一个槽位检测满

```python
class MyQueue:
    def __init__(self, capacity):
        self.list = [None] * capacity
        self.front = 0
        self.rear = 0

    def Enqueue(self, element):
        if (self.rear + 1) % len(self.list) == self.front:
            print("Queue is full")
            return False
        self.list[self.rear] = element
        self.rear = (self.rear + 1) % len(self.list)
        return True

    def Dequeue(self):
        if self.rear == self.front:
            print("Queue is empty")
            return None
        element = self.list[self.front]
        self.front = (self.front + 1) % len(self.list)
        return element

    def Output(self):
        i = self.front
        while i != self.rear:
            print(self.list[i])
            i = (i + 1) % len(self.list)
```

### 循环队列 + 记录类型
```python
class SaleRecord:
    def __init__(self):
        self.ID = ""
        self.quantity = 0

CircularQueue = [SaleRecord() for _ in range(5)]
Head = 0
Tail = 0
NumberOfItems = 0

def EnqueueRecord(record):
    global CircularQueue, Head, Tail, NumberOfItems
    if NumberOfItems == 5:
        return -1
    CircularQueue[Tail] = record
    Tail = (Tail + 1) % 5
    NumberOfItems = NumberOfItems + 1
    return 1

def DequeueRecord():
    global CircularQueue, Head, Tail, NumberOfItems
    if NumberOfItems == 0:
        return None
    record = CircularQueue[Head]
    Head = (Head + 1) % 5
    NumberOfItems = NumberOfItems - 1
    return record
```

## 关键区别

| 特性 | 线性队列 | 循环队列 |
|------|---------|---------|
| Tail 变化 | Tail = Tail + 1 | Tail = (Tail + 1) % size |
| 满判断 | Tail >= size | NumberItems == size |
| 空判断 | Head == -1 or Head >= Tail | NumberItems == 0 |

## 常见错误

- 忘记 MOD 运算实现回绕
- 未更新 NumberItems
- 出队/入队顺序搞错
