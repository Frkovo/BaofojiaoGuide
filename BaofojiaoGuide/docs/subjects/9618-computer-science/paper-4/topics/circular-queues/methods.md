---
title: 解题方法
sidebar_position: 3
---

# 解题方法

---

## 方法概览

```
Circular Queue = Linear Queue + Wrap-around + Counter
```

The key difference from a linear queue is the **MOD operation**: `(Pointer + 1) MOD QueueSize` instead of `Pointer + 1`.

---

## Step 1: 初始化

```python
Queue = [None] * QueueSize
HeadPointer = -1
TailPointer = -1
NumberOfItems = 0
```

- All pointers start at `-1` (empty queue convention)
- `QueueSize` is typically `10` or a parameterised constant

---

## Step 2: Enqueue 方法

```python
PROCEDURE EnQueue(ByVal Item)
    IF NumberOfItems < QueueSize THEN
        TailPointer = (TailPointer + 1) MOD QueueSize
        Queue[TailPointer] = Item
        NumberOfItems = NumberOfItems + 1
    ELSE
        OUTPUT "Queue is full"
    ENDIF
ENDPROCEDURE
```

**Key points**:
- `(TailPointer + 1) MOD QueueSize` produces `0` when `TailPointer == QueueSize - 1`
- Check `NumberOfItems` not `TailPointer` to decide if full
- For first item: `(-1 + 1) MOD QueueSize == 0` ✅

---

## Step 3: Dequeue 方法

```python
FUNCTION DeQueue() RETURNS ItemType
    IF NumberOfItems > 0 THEN
        HeadPointer = (HeadPointer + 1) MOD QueueSize
        Item = Queue[HeadPointer]
        NumberOfItems = NumberOfItems - 1
        RETURN Item
    ELSE
        OUTPUT "Queue is empty"
        RETURN Null
    ENDIF
ENDFUNCTION
```

**Key points**:
- Wrap `HeadPointer` *before* accessing `Queue[HeadPointer]`
- Decrement `NumberOfItems` *after* retrieving the item
- First dequeue: `(-1 + 1) MOD QueueSize == 0` ✅

---

## Step 4: 判断 Full / Empty

```python
FUNCTION IsFull() RETURNS BOOLEAN
    RETURN NumberOfItems == QueueSize
ENDFUNCTION

FUNCTION IsEmpty() RETURNS BOOLEAN
    RETURN NumberOfItems == 0
ENDFUNCTION
```

:::note[Critical]

NEVER compare `HeadPointer == TailPointer` to detect full/empty. This condition occurs in **both** states. Always rely on `NumberOfItems`.

:::

---

## 初始化 convention 对比

| Convention | HeadPointer | TailPointer | First Enqueue | First Dequeue |
|-----------|-------------|-------------|---------------|---------------|
| -1 start | `-1` | `-1` | `(-1+1) MOD size = 0` | `(-1+1) MOD size = 0` |
| 0 start | `0` | `0` | `(0+1) MOD size = 1` | `(0+1) MOD size = 1` |

Both work — the mark scheme accepts either as long as it is consistent.

---

## 伪代码模板 (exam-ready)

```
PROCEDURE Enqueue(item)
    IF NumberOfItems < MaxSize THEN
        TailPointer ← (TailPointer + 1) MOD MaxSize
        Queue[TailPointer] ← item
        NumberOfItems ← NumberOfItems + 1
    ELSE
        OUTPUT "Queue full"
    ENDIF
ENDPROCEDURE

FUNCTION Dequeue() RETURNS STRING
    IF NumberOfItems > 0 THEN
        HeadPointer ← (HeadPointer + 1) MOD MaxSize
        Item ← Queue[HeadPointer]
        NumberOfItems ← NumberOfItems - 1
        RETURN Item
    ELSE
        OUTPUT "Queue empty"
        RETURN ""
    ENDIF
ENDFUNCTION
```
