---
title: Queues
sidebar_position: 1
---

# Queues（队列）

## 考纲要求

- 19.1.6 Queue ADT：入队（enqueue）、出队（dequeue）
- 用数组实现线性队列

## 核心代码模板

### 线性队列
```python
Queue = [""] * 20
QueueHead = -1
QueueTail = -1

def Enqueue(data):
    global Queue, QueueHead, QueueTail
    if QueueTail == 19:
        return False
    if QueueHead == -1:
        QueueHead = 0
    QueueTail = QueueTail + 1
    Queue[QueueTail] = data
    return True

def Dequeue():
    global Queue, QueueHead, QueueTail
    if QueueHead < 0 or QueueHead > QueueTail:
        return "false"
    item = Queue[QueueHead]
    QueueHead = QueueHead + 1
    return item
```

### 另一种指针约定（Head=-1, Tail=0）
```python
Queue = [""] * 50
HeadPointer = -1
TailPointer = 0

def Enqueue(item):
    global Queue, HeadPointer, TailPointer
    if TailPointer >= 50:
        print("Queue full")
        return
    if HeadPointer == -1:
        HeadPointer = 0
    Queue[TailPointer] = item
    TailPointer = TailPointer + 1

def Dequeue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer == -1 or HeadPointer >= TailPointer:
        return "Empty"
    item = Queue[HeadPointer]
    HeadPointer = HeadPointer + 1
    return item
```

## 常见错误

- 忘记在函数内声明 global
- 入队时没有处理第一个元素的情况（设 Head=0）
- 出队时没有检查空队列
- 指针语义搞混（Front/Rear 不同约定）
