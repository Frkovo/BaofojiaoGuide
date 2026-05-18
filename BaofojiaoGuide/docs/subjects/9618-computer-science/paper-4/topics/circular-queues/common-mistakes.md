---
title: 常见错误
sidebar_position: 5
---

# 常见错误

---

## 🔴 Mistake 1: `HeadPointer == TailPointer` 判断 Full / Empty

```python
# ❌ Wrong — fails when queue is full
IF HeadPointer = TailPointer THEN
    OUTPUT "Queue is empty"
ENDIF

# ✅ Correct — use NumberOfItems
IF NumberOfItems = 0 THEN
    OUTPUT "Queue is empty"
ENDIF
```

In a circular queue, `HeadPointer == TailPointer` when the queue is **both empty and full**. You cannot distinguish the two states without `NumberOfItems`.

---

## 🔴 Mistake 2: Manual wrapping without MOD

```python
# ❌ Wrong — handwritten IF gets -1
IF TailPointer = QueueSize - 1 THEN
    TailPointer = 0
ELSE
    TailPointer = TailPointer + 1
ENDIF

# ✅ Correct — single MOD line
TailPointer = (TailPointer + 1) MOD QueueSize
```

The mark scheme insists on the `MOD` operator. Manual wrapping with `IF` is not accepted.

---

## 🔴 Mistake 3: Off-by-one in MOD direction

```python
# ❌ Wrong — should be (P + 1), not (P - 1)
TailPointer = (TailPointer - 1) MOD QueueSize

# ✅ Correct
TailPointer = (TailPointer + 1) MOD QueueSize
```

---

## 🔴 Mistake 4: Decrementing `NumberOfItems` before retrieval

```python
# ❌ Wrong — loses item reference
NumberOfItems = NumberOfItems - 1
Item = Queue[HeadPointer]

# ✅ Correct — retrieve first, then decrement
Item = Queue[HeadPointer]
NumberOfItems = NumberOfItems - 1
```

---

## 🔴 Mistake 5: Forgetting to wrap `HeadPointer` before dequeue

```python
# ❌ Wrong — HeadPointer never wraps
Item = Queue[HeadPointer]
HeadPointer = HeadPointer + 1

# ✅ Correct — wrap first, then access
HeadPointer = (HeadPointer + 1) MOD QueueSize
Item = Queue[HeadPointer]
```

---

## 🔴 Mistake 6: Not initialising pointers to `-1`

```python
# ❌ Wrong — starts at 0, first enqueue goes to index 1
HeadPointer = 0
TailPointer = 0

# ✅ Correct
HeadPointer = -1
TailPointer = -1
```

:::note[注意]

While starting at `0` can work with a different algorithm (enqueue first, then wrap), the standard convention in 9618 is `-1`. Stick with `-1` to avoid confusion.

:::

---

## 🔴 Mistake 7: Full check using `TailPointer == QueueSize - 1`

```python
# ❌ Wrong — circular queue wraps around!
IF TailPointer = QueueSize - 1 THEN
    OUTPUT "Queue is full"
ENDIF

# ✅ Correct
IF NumberOfItems = QueueSize THEN
    OUTPUT "Queue is full"
ENDIF
```

In a circular queue, `TailPointer` can be anywhere — even `0` — when the queue is full. Only `NumberOfItems` reliably indicates fullness.

---

## 🔴 Mistake 8: Null / None return from Dequeue

```python
FUNCTION DeQueue()
    # ❌ Wrong — returns nothing in failure case
    IF NumberOfItems = 0 THEN
        OUTPUT "Empty"
        # Missing RETURN
    ENDIF
    ...

    # ✅ Correct
    IF NumberOfItems = 0 THEN
        OUTPUT "Empty"
        RETURN Null  # or RETURN ""
    ENDIF
```

If the function has a return type, **every** branch must return a value.
