---
title: 考纲要点
sidebar_position: 6
---

# 考纲要点

## 19.1.7 Linked List (Linear) ADT

### What you must know

| # | Point | Exam Frequency |
|---|-------|----------------|
| 1 | Define a linked list as a collection of nodes where each node contains data and a pointer/reference to the next node | Low |
| 2 | Use a `NODE` record type with `Data` and `NextPointer` fields | **High** |
| 3 | Use a `LinkedList` record type with `Head`, `Tail`, `CurrentPointer` fields | Medium |
| 4 | Traverse a linked list and output data | **High** |
| 5 | Insert a node at the start of a linked list | Medium |
| 6 | Insert a node at the end of a linked list | **High** |
| 7 | Insert a node into the middle of a linked list | Medium |
| 8 | Delete a node from a linked list (any position) | **High** |
| 9 | Understand free list / free pointer (`Free` / `NextFree`) | Medium |
| 10 | Implement search in a linked list | Medium |

### What linked lists are used for

- Dynamic memory allocation where size is not known in advance
- Efficient insertion/deletion compared to arrays (no shifting)
- Implementing queues, stacks, and other abstract data types

### Linked list vs Array

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Access by index | O(1) | O(n) |
| Insert at start | O(n) &mdash; shift all elements | O(1) &mdash; update head pointer |
| Insert at end | O(1) &mdash; if space available | O(1) &mdash; via tail pointer |
| Delete | O(n) &mdash; shift elements | O(n) &mdash; search then O(1) relink |
| Memory | Contiguous, fixed size | Non-contiguous, overhead per node |

### Typical setup in exam questions

```
// Global declarations
DECLARE Node : ARRAY[1:10] OF Node
DECLARE Head  : INTEGER
DECLARE Tail  : INTEGER
DECLARE Free  : INTEGER

// Initialisation
Head ← -1
Tail ← -1
Free ← 1
FOR i ← 1 TO 9
    Node[i].NextPointer ← i + 1
NEXT i
Node[10].NextPointer ← -1
```

### Expected pseudocode constructs

| Construct | Example |
|-----------|---------|
| Record | `TYPE Node ... ENDTYPE` |
| Array of records | `DECLARE Node : ARRAY[1:10] OF Node` |
| Field access | `Node[Current].Data` |
| Assignment | `Current ← Node[Current].NextPointer` |
| Loop | `WHILE Current <> -1` |
| Condition | `IF Head = -1 THEN` |
| Procedure | `PROCEDURE InsertNode(Value : INTEGER)` |
| Function | `FUNCTION Search(Value : INTEGER) RETURNS INTEGER` |

:::note

The exam expects **pseudocode**, not a specific programming language. Use `←` for assignment, `<>` for not-equal, `DECLARE` for variable creation, and `TYPE ... ENDTYPE` for records.

:::
