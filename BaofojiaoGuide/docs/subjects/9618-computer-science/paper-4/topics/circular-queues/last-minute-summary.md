---
title: 考前速记
sidebar_position: 7
---

# 考前速记

---

## 关键公式

```
Enqueue:  TailPointer = (TailPointer + 1) MOD QueueSize
Dequeue: HeadPointer = (HeadPointer + 1) MOD QueueSize
```

---

## 初始化

```
HeadPointer = -1
TailPointer = -1
NumberOfItems = 0
Queue = [None] * QueueSize
```

---

## Enqueue — 4行核心

```
IF NumberOfItems < QueueSize THEN
    TailPointer = (TailPointer + 1) MOD QueueSize
    Queue[TailPointer] = NewItem
    NumberOfItems = NumberOfItems + 1
```

---

## Dequeue — 4行核心

```
IF NumberOfItems > 0 THEN
    HeadPointer = (HeadPointer + 1) MOD QueueSize
    Item = Queue[HeadPointer]
    NumberOfItems = NumberOfItems - 1
    RETURN Item
```

---

## Full / Empty

| State | Check | Action |
|-------|-------|--------|
| Full | `NumberOfItems == QueueSize` | Reject enqueue |
| Empty | `NumberOfItems == 0` | Reject dequeue |

---

## 高频陷阱

- ❌ **Manual IF wrapping** → always use `MOD`
- ❌ **Pointer compare for full/empty** → use `NumberOfItems`
- ❌ **Decrement before retrieval** → retrieve, then decrement
- ❌ **No return in empty branch** → return `Null` or `""`

---

## 伪代码速查模板

```python
// --- Enqueue ---
PROCEDURE Enqueue(Item)
    IF NumberOfItems < MaxSize THEN
        TailPointer = (TailPointer + 1) MOD MaxSize
        Queue[TailPointer] = Item
        NumberOfItems = NumberOfItems + 1
    ELSE
        OUTPUT "Queue full"
    ENDIF
ENDPROCEDURE

// --- Dequeue ---
FUNCTION Dequeue() RETURNS STRING
    IF NumberOfItems > 0 THEN
        HeadPointer = (HeadPointer + 1) MOD MaxSize
        Item = Queue[HeadPointer]
        NumberOfItems = NumberOfItems - 1
        RETURN Item
    ELSE
        OUTPUT "Queue empty"
        RETURN ""
    ENDIF
ENDFUNCTION
```

---

:::note[最后提醒]

- **M1** is always the full/empty check — worth 1 mark, do not skip it
- **MOD** is worth 1 mark — the easiest mark to lose
- Write pseudocode, not Python, unless the question asks for Python

:::
