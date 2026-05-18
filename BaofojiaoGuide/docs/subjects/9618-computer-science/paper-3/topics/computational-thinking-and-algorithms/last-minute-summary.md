---
title: 考前速记
---

# 考前速记

## Search

| | Linear | Binary |
|--|--------|--------|
| Data | Unsorted OK | Must be sorted |
| Complexity | O(n) | O(log n) |
| Method | One by one | Divide & conquer |

## Sort

| | Bubble | Insertion |
|--|--------|-----------|
| Method | Swap adjacent | Insert into sorted part |
| Complexity | O(n²) | O(n²) |

## Stack vs Queue

| | Stack | Queue |
|--|-------|-------|
| Principle | LIFO | FIFO |
| Add | Push | Enqueue |
| Remove | Pop | Dequeue |
| Pointer | StackPointer | Front / Rear |

## Linked List

```
Node: [Data][Pointer]
HeadPointer → Node1 → Node2 → NULL(-1)
FreePointer → available nodes
```

Insert: get from FreeList → update pointers
Delete: bypass node → return to FreeList

## Recursion — Checklist

- [ ] Base case exists?
- [ ] Recursive call moves toward base case?
- [ ] Call stack managed correctly?

## Big O — Speed Ranking

$$O(1) > O(\log n) > O(n) > O(n \log n) > O(n^2)$$

Binary search → O(log n) ✓
Linear search → O(n) ✓
Bubble/Insertion sort → O(n²) ✓
