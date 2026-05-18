---
title: 知识点总结
---

## Linear Search — 线性搜索

- Scans each element in sequence until the target is found
- Works on **unsorted** data — 无需排序
- Time complexity: $$O(n)$$
- Space complexity: $O(1)$
- Simple but inefficient for large datasets

## Binary Search — 二分搜索

- Requires **sorted data** — 需要有序数据
- **Divide and conquer** approach — 分治法
- Repeatedly divides search interval in half
- Time complexity: $$O(\log n)$$
- Much faster than linear search on large sorted arrays

:::warning[...]
Binary search only works on sorted data. If the data is unsorted, you must sort first or use linear search.
:::

## Bubble Sort — 冒泡排序

- Repeatedly steps through the list, **compares adjacent elements**
- **Swaps** them if they are in the wrong order
- After each pass, the largest unsorted element "bubbles" to its correct position
- Time complexity: $$O(n^2)$$ in worst / average case
- Best case: $O(n)$ (already sorted, with optimisation flag)
- Simple but inefficient for large datasets

## Insertion Sort — 插入排序

- Builds a **sorted portion** one element at a time
- Takes each new element and **inserts** it into the correct position
- Time complexity: $$O(n^2)$$ in worst / average case
- Best case: $O(n)$ (already sorted)
- More efficient than bubble sort in practice

## Abstract Data Types (ADTs) — 抽象数据类型

### Stack — 栈

- **LIFO** (Last In, First Out) — 后进先出
- Operations: **Push** (add), **Pop** (remove), **Peek/Top** (view top), **IsEmpty**, **IsFull**
- Pointer-based implementation: a **top** pointer tracks the current position
- Applications: function call stack, expression evaluation, undo operations

### Queue — 队列

- **FIFO** (First In, First Out) — 先进先出
- Operations: **Enqueue** (add at rear), **Dequeue** (remove from front), **IsEmpty**, **IsFull**
- Maintains **front** and **rear** pointers
- Applications: task scheduling, print spooling, BFS traversal

### Linked List — 链表

- **Nodes** each containing **data** + a **pointer** to the next node
- Types: singly linked, doubly linked, circular
- Operations: **Insert** (at head, tail, or specific position), **Delete**, **Traverse**
- Dynamic size — no need to pre-allocate memory
- No random access — must traverse from head

### Binary Tree — 二叉树

- **Root**: topmost node (no parent)
- Each node has at most **two children**: left and right
- **Leaf nodes**: nodes with no children
- Operations: **Search** (traverse comparing values), **Insert** (find correct position), **Delete** (handle three cases: leaf, one child, two children)
- Binary Search Tree (BST): left child < parent < right child

### Dictionary / Map — 字典

- Stores **key-value pairs** — 键值对
- Keys are unique; each key maps to exactly one value
- Operations: **Insert**, **Lookup/Search**, **Delete**
- Can be implemented via hash tables or balanced trees

### Graph — 图

- **Vertices** (nodes) + **Edges** (connections)
- **Directed** (digraph): edges have direction — 有向图
- **Undirected**: edges have no direction — 无向图
- **Weighted**: edges have associated costs — 加权图
- Adjacency matrix vs adjacency list representation

## Recursion — 递归

- A function that **calls itself**
- Two essential parts:
  - **Base case**: terminates the recursion (stops infinite calls)
  - **Recursive case**: reduces the problem toward the base case
- **Stack unwinding**: each recursive call is pushed onto the call stack; when the base case is reached, calls are popped off (unwound) in reverse order
- Classic examples:
  - **Factorial**: $$n! = n \times (n-1)!$$, base case: $0! = 1$
  - **Fibonacci**: $$F(n) = F(n-1) + F(n-2)$$, base cases: $F(0) = 0$, $F(1) = 1$

:::tip[...]
Every recursive solution can also be written iteratively, but recursion often leads to cleaner, more expressive code.
:::

## Big O Notation — 大 O 表示法

- Describes the **upper bound** of time/space complexity as input size $n$ grows

| Notation | Name | Example |
|----------|------|---------|
| $$O(1)$$ | Constant time | Array access by index |
| $$O(\log n)$$ | Logarithmic | Binary search |
| $$O(n)$$ | Linear | Linear search |
| $$O(n \log n)$$ | Linearithmic | Merge sort, quicksort (avg) |
| $$O(n^2)$$ | Quadratic | Bubble sort, insertion sort |
| $$O(2^n)$$ | Exponential | Recursive Fibonacci (naive) |

:::warning[...]
Always analyse the **worst-case** scenario when determining Big O complexity unless otherwise stated.
:::
