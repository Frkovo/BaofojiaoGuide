---
title: 考前速记
sidebar_position: 7
---

# 考前速记

## 10 Second Recall

```
Node = {Data, NextPointer}
Head → first node
Tail → last node
Free → first available slot
-1 = null / end of list
```

---

## Traversal Cheat Sheet

```
Current ← Head
WHILE Current <> -1
    OUTPUT Node[Current].Data
    Current ← Node[Current].NextPointer
ENDWHILE
```

Three lines inside the loop (declare, output, advance) &mdash; never forget the advance line.

---

## Insert at End (7-mark answer)

| Step | Code |
|------|------|
| Allocate | `NewNode ← Free` `Free ← Node[Free].NextPointer` |
| Store | `Node[NewNode].Data ← Value` `Node[NewNode].NextPointer ← -1` |
| Empty? | `IF Head = -1 THEN Head ← NewNode` `Tail ← NewNode` |
| Else | `Node[Tail].NextPointer ← NewNode` `Tail ← NewNode` |

---

## Delete at Any Position

| Step | Code |
|------|------|
| Search | Find target + predecessor via `WHILE` loop |
| Head case | `Head ← Node[Head].NextPointer` |
| Other case | `Node[Previous].NextPointer ← Node[Current].NextPointer` |
| Tail case | `IF Current = Tail THEN Tail ← Previous` |
| Free list | `Node[Current].NextPointer ← Free` `Free ← Current` |

---

## Insert at Start

```
Node[NewNode].NextPointer ← Head
Head ← NewNode
IF Tail = -1 THEN Tail ← NewNode
```

---

## Common Edge Cases

| Case | What to check |
|------|---------------|
| Empty list | `Head = -1` &rarr; no traversal, separate insert path |
| Single node | Deletion &rarr; `Head` and `Tail` both become `-1` |
| Insert into empty | Both `Head` and `Tail` point to new node |
| Full free list | `Free = -1` &rarr; no more nodes available (rarely tested) |
| Delete last node | `Tail ← Previous` (which may be `-1`) |

---

## Pointer Rules

- `Head` only changes on insert-at-start or delete-at-start
- `Tail` only changes on insert-at-end or delete-at-end
- `Free` changes on every allocation and every return-to-free-list
- `Node[i].NextPointer` always holds an `INTEGER` index or `-1`

---

## Last-minute checklist

- [ ] `TYPE Node` has `Data` and `NextPointer`
- [ ] Traversal never modifies `Head`
- [ ] `Free` is updated when allocating
- [ ] Empty list case handled
- [ ] `Node[NewNode].NextPointer` set to `-1` for end insertion
- [ ] Deleted node returned to free list
- [ ] `Tail` updated after deletion if needed

:::note[Exam Day]

If you blank on a linked list question, write the traversal loop first &mdash; it earns 3&ndash;4 marks immediately and builds confidence.

:::
