---
title: 方法总结
---

# 方法总结

## Binary Search 模板

```
low ← 0
high ← len(arr) - 1
WHILE low <= high
    mid ← (low + high) DIV 2
    IF arr[mid] = target THEN RETURN mid
    ELSE IF arr[mid] < target THEN low ← mid + 1
    ELSE high ← mid - 1
ENDWHILE
RETURN -1
```

## Linear Search 模板

```
FOR i ← 0 TO len(arr) - 1
    IF arr[i] = target THEN RETURN i
ENDFOR
RETURN -1
```

## Insertion Sort 模板

```
FOR i ← 1 TO len(arr) - 1
    key ← arr[i]
    j ← i - 1
    WHILE j >= 0 AND arr[j] > key
        arr[j+1] ← arr[j]
        j ← j - 1
    ENDWHILE
    arr[j+1] ← key
ENDFOR
```

## Stack — Push & Pop

| 操作 | 检查 | 指针 | 数据 |
|------|------|------|------|
| Push(v) | Full? (ptr = Max) | ptr++ → 然后存 v | Stack[ptr] ← v |
| Pop() | Empty? (ptr = 0) | 取 v ← Stack[ptr] 然后 ptr-- | RETURN v |

## Queue — Enqueue & Dequeue

| 操作 | 检查 | 指针 | 数据 |
|------|------|------|------|
| Enqueue(v) | Full? (Rear = Max) | Rear++ | Queue[Rear] ← v; 首项时 Front ← 1 |
| Dequeue() | Empty? (Front=0 OR Front > Rear) | 取 v ← Queue[Front]; Front++ | RETURN v |

## Linked List 遍历

```
Current ← HeadPointer
WHILE Current <> -1
    OUTPUT List[Current].Data
    Current ← List[Current].Pointer
ENDWHILE
```

## Big O 速查

| 算法 | Big O |
|------|-------|
| Linear Search | O(n) |
| Binary Search | O(log n) |
| Bubble Sort | O(n²) |
| Insertion Sort | O(n²) |
| Stack Push/Pop | O(1) |
| Queue Enqueue/Dequeue | O(1) |
