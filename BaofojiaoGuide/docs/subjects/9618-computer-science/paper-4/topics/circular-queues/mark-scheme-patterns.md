---
title: 评分标准模式
sidebar_position: 4
---

# 评分标准模式

---

## Enqueue 评分结构 (6 marks)

<details>
<summary><strong>M1</strong> — Check if full (1 mark)</summary>

- `IF NumberOfItems = QueueSize THEN`
- Accept: `IF NumberOfItems &gt;= QueueSize`, `IF TailPointer + 1 MOD = HeadPointer` (rare)
- **Not accept**: `IF Queue[0] = None`, `IF HeadPointer = TailPointer`
</details>

<details>
<summary><strong>A1</strong> — Wrap TailPointer (1 mark)</summary>

- `TailPointer ← (TailPointer + 1) MOD QueueSize`
- **Must** use MOD operator (not `IF TailPointer = Size THEN TP = 0`)
- **Must** be executed when there is space
</details>

<details>
<summary><strong>A1</strong> — Assign item (1 mark)</summary>

- `Queue[TailPointer] ← NewItem`
- Variable name must match declaration
</details>

<details>
<summary><strong>A1</strong> — Increment counter (1 mark)</summary>

- `NumberOfItems ← NumberOfItems + 1`
- Must be after successful insertion
</details>

<details>
<summary><strong>A1</strong> — Output full message (1 mark)</summary>

- `OUTPUT "Queue is full"` or `PRINT "Queue is full"`
- Must be in the `ELSE` / failure branch
</details>

<details>
<summary><strong>A1</strong> — Structure (1 mark)</summary>

- Correct `ENDIF`, `ENDPROCEDURE`
- Parameter declared correctly (e.g. `ByVal Item AS INTEGER`)
- No syntax errors
</details>

---

## Dequeue 评分结构 (6 marks)

<details>
<summary><strong>M1</strong> — Check if empty (1 mark)</summary>

- `IF NumberOfItems > 0 THEN`
- Accept: `IF NumberOfItems != 0`, `IF NOT IsEmpty()`
- **Not accept**: `IF Queue[HeadPointer] = None`
</details>

<details>
<summary><strong>A1</strong> — Wrap HeadPointer (1 mark)</summary>

- `HeadPointer ← (HeadPointer + 1) MOD QueueSize`
- Same MOD requirement as enqueue
</details>

<details>
<summary><strong>A1</strong> — Retrieve item (1 mark)</summary>

- `Item ← Queue[HeadPointer]`
- Must use the updated `HeadPointer`
</details>

<details>
<summary><strong>A1</strong> — Decrement counter (1 mark)</summary>

- `NumberOfItems ← NumberOfItems - 1`
- Must be after retrieval (otherwise index error)
</details>

<details>
<summary><strong>A1</strong> — Return item (1 mark)</summary>

- `RETURN Item` or `OUTPUT Item`
- Must be in the success branch
</details>

<details>
<summary><strong>A1</strong> — Output empty message (1 mark)</summary>

- `OUTPUT "Queue is empty"` or `RETURN ""` / `RETURN Null`
- Must be in the failure branch
</details>

---

## 常见扣分点

| Mistake | Marks Lost |
|---------|-----------|
| No MOD operation (manual IF wrapping) | −1 |
| No `NumberOfItems` check (using pointer compare) | −1 (M1) |
| Wrong MOD direction (`(P - 1) MOD size`) | −1 |
| `NumberOfItems` not incremented/decremented | −1 |
| MOD executed outside full check | −1 |
| Returning wrong variable | −1 |
| Missing `ENDIF` / `ENDPROCEDURE` | −1 |

---

:::note[阅卷人提示]

Examiners report that the most common error in circular queue questions is the **confusion between full and empty states**. A surprising number of candidates use `HeadPointer == TailPointer` to detect emptiness, which fails when the queue is full. Always use `NumberOfItems`.

:::
