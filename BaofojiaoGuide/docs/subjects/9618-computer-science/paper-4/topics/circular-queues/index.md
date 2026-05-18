---
title: Circular Queues
sidebar_position: 1
---

# Circular Queues（循环队列）

## 考纲要求

- 19.1.6 Queue ADT 扩展：用 MOD 实现循环回绕

## 核心代码模板

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

### 循环队列 + 记录类型版本
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
| Head 变化 | Head = Head + 1 | Head = (Head + 1) % size |

## 常见错误

- 用 Head == Tail 判断空/满（不可靠，只能用 NumberItems）
- 忘记更新 NumberItems
- MOD 运算错误
