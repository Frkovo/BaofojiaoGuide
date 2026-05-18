---
title: 题型分析
sidebar_position: 2
---

# 题型分析

| 题型 | 分值 | 频率 | 难度 |
|------|------|------|------|
| Enqueue with circular wrap-around | 6 marks | High | ★★★ |
| Dequeue with circular wrap-around | 6 marks | High | ★★★ |
| Full / empty state detection | 2–3 marks | Medium | ★★ |

---

## Q1: Enqueue (6 marks)

**Identify**: Prompt says *"add an item to the circular queue"* or *"enqueue with wrap-around"*.

**Method**:
1. Check if queue is full
2. Update `TailPointer` with wrap
3. Insert item
4. Increment `NumberOfItems`

**MS Pattern**:

<details>
<summary><strong>M1</strong> Check if full (1 mark)</summary>

- `IF NumberOfItems = QueueSize THEN` or equivalent
</details>

<details>
<summary><strong>A1</strong> Wrap TailPointer (1 mark)</summary>

- `TailPointer ← (TailPointer + 1) MOD QueueSize`
- Must use MOD, not manual `IF`
</details>

<details>
<summary><strong>A1</strong> Insert item (1 mark)</summary>

- `Queue[TailPointer] ← NewItem`
</details>

<details>
<summary><strong>A1</strong> Increment NumberOfItems (1 mark)</summary>

- `NumberOfItems ← NumberOfItems + 1`
</details>

<details>
<summary><strong>A1</strong> Output full message (1 mark)</summary>

- Appropriate message when `NumberOfItems == QueueSize`
</details>

<details>
<summary><strong>A1</strong> Correct <code>ENDIF</code>, variable types (1 mark)</summary>

- Proper structure and typed parameters
</details>

**Traps**:
- ❌ Using `TailPointer ← TailPointer + 1` without MOD — only gets **M1**, loses **A1**
- ❌ Checking `IF TailPointer == QueueSize THEN TailPointer = 0` — not accepted, must use MOD
- ❌ Forgetting to increment `NumberOfItems`
- ❌ Inserting item before wrapping `TailPointer`

---

## Q2: Dequeue (6 marks)

**Identify**: Prompt says *"remove an item from the circular queue"* or *"dequeue with wrap-around"*.

**Method**:
1. Check if queue is empty
2. Wrap `HeadPointer`
3. Retrieve item
4. Decrement `NumberOfItems`
5. Return item

**MS Pattern**:

<details>
<summary><strong>M1</strong> Check if empty (1 mark)</summary>

- `IF NumberOfItems = 0 THEN` or equivalent
</details>

<details>
<summary><strong>A1</strong> Wrap HeadPointer (1 mark)</summary>

- `HeadPointer ← (HeadPointer + 1) MOD QueueSize`
</details>

<details>
<summary><strong>A1</strong> Retrieve item (1 mark)</summary>

- `Item ← Queue[HeadPointer]`
</details>

<details>
<summary><strong>A1</strong> Decrement NumberOfItems (1 mark)</summary>

- `NumberOfItems ← NumberOfItems - 1`
- Must be after retrieval
</details>

<details>
<summary><strong>A1</strong> Return item (1 mark)</summary>

- `RETURN Item` or equivalent output
</details>

<details>
<summary><strong>A1</strong> Output empty message (1 mark)</summary>

- Appropriate message when `NumberOfItems == 0`
</details>

**Traps**:
- ❌ Wrapping `HeadPointer` before checking empty — algorithm breaks
- ❌ Returning item before decrementing — `NumberOfItems` out of sync
- ❌ Using `HeadPointer - 1` or wrong MOD direction

---

## 真题示例

| Exam | Paper | Question | Type |
|------|-------|----------|------|
| 9618/s25/qp/41 | Paper 4 | Q1 | Enqueue + Dequeue |
| 9618/s23/qp/42 | Paper 4 | Q2 | Enqueue with wrap |

:::note[复习建议]

For each past paper, practice writing the full procedure from memory before checking the mark scheme. Pay special attention to the MOD operation — it is the single most common place to lose marks.

:::
