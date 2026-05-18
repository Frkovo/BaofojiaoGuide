---
title: 考纲要点
sidebar_position: 6
---

# 考纲要点

---

## 9618 Syllabus Extract — Queue ADT

| 考点 | 要求 | 常见题型 |
|------|------|----------|
| Define a queue as an abstract data type | Understand FIFO principle | Theory (Q1) |
| Implement a circular queue using a static array | Fixed-size array + pointers | Practical (6–12 marks) |
| Enqueue operation with wrap-around | MOD operator | Code writing (6 marks) |
| Dequeue operation with wrap-around | MOD operator | Code writing (6 marks) |
| Distinguish full vs empty states | `NumberOfItems` counter | Code + explanation (2–3 marks) |
| Initialise queue structure | Pointers at `-1`, items at `None` | Code (1–2 marks) |

---

## 必须掌握的能力

1. **Write** `Enqueue` procedure from scratch
2. **Write** `Dequeue` function from scratch
3. **Write** `IsFull` / `IsEmpty` boolean functions
4. **Trace** a circular queue through multiple enqueue/dequeue operations
5. **Explain** why `NumberOfItems` is needed (not just pointer comparison)
6. **Identify** when a queue is circular (look for MOD, `NumberOfItems`)

---

## 考试常见设问方式

| 设问 | 分值 | 提示词 |
|------|------|--------|
| *"Write a procedure to add an item to the queue"* | 6 | `Enqueue`, `AddItem`, `Insert` |
| *"Write a function to remove and return an item"* | 6 | `Dequeue`, `RemoveItem`, `Pop` |
| *"State what is meant by a circular queue"* | 2 | Explanation, diagram |
| *"Explain why NumberOfItems is needed"* | 2 | Full vs empty ambiguity |
| *"Amend the linear queue to be circular"* | 4 | Add MOD, add counter |

---

## 与 Linear Queue 的考点对比

| Aspect | Linear Queue考点 | Circular Queue考点 |
|--------|-----------------|-------------------|
| Pointer update | `+ 1` only | `(+ 1) MOD Size` |
| Full condition | `Tail == Size - 1` | `NumberOfItems == Size` |
| Empty condition | `Head == Tail` | `NumberOfItems == 0` |
| Space reuse | ❌ Not tested | ✅ Key feature |
| Harder question | Resizing | Wrap + counter logic |

---

:::note[考纲分析]

The circular queue typically appears in Section A of Paper 4 (Q1 or Q2). It is one of the most predictable 6-mark questions. The exam routine is almost always: *"Write a procedure to enqueue an item into a circular queue"* or *"Write a function to dequeue an item from a circular queue"*.

Master this topic — it is a guaranteed 6 marks.

:::
