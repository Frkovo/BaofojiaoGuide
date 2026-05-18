---
title: 考前速记
sidebar_position: 7
---

# 考前速记

## 队列核心模板

### 线性队列

```python
Queue = [""] * 50
Front = -1
Rear = 0

def Enqueue(item):
    global Queue, Front, Rear
    if Rear >= 50:
        return False
    if Front == -1:
        Front = 0
    Queue[Rear] = item
    Rear += 1
    return True

def Dequeue():
    global Queue, Front, Rear
    if Front == -1 or Front >= Rear:
        return "false"
    item = Queue[Front]
    Front += 1
    return item
```

### 常见指针约定

| 指针 | 初始化 | 含义 |
|------|--------|------|
| Front/Head | -1 | 指向第一个元素 |
| Rear/Tail | 0 或 -1 | 指向下一个空位 |

## 高频 MS 评分点

- **M1**: 队列满检查和返回 FALSE
- **M1**: 插入数据并更新 Rear
- **M1**: 第一个元素时设置 Front=0
- **M1**: 返回 TRUE
- **M1**: 空队列检查和返回 "false"
- **M1**: 返回 Front 处元素并递增 Front

## 考试检查清单

- [ ] Enqueue 中检查队列是否满
- [ ] 第一个元素入队时更新 Front
- [ ] Dequeue 中检查队列是否空
- [ ] 所有队列操作前后全局变量声明正确
- [ ] 返回值类型与题目要求一致
