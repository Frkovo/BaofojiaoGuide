---
title: 考纲要点
sidebar_position: 6
---

# 考纲要点 — 19.1.5 Stack ADT

## 核心要求

### 1. Stack ADT 理解
- 栈是一种 **LIFO（Last In, First Out）** 数据结构
- 主要操作: `Push`, `Pop`, `Peek`（或 `Top`）, `isEmpty`, `isFull`
- 栈有**一个开口**（top），所有操作都在栈顶进行

### 2. 数组实现（Array-based Implementation）
- 静态数组 + `top` 整数指针
- 固定容量 `maxSize`
- 必须处理 overflow 和 underflow

### 3. 操作细节

| 操作 | 前置条件 | 后置条件 | 时间复杂度 |
|------|---------|---------|-----------|
| Push(item) | 栈未满 | `top` 增加 1，元素放入新`top` | $O(1)$ |
| Pop() | 栈非空 | `top` 减少 1，返回原栈顶元素 | $O(1)$ |
| Peek() | 栈非空 | 返回 `stack[top]`，栈不变 | $O(1)$ |
| isEmpty() | 无 | 返回 `top = -1` | $O(1)$ |
| isFull() | 无 | 返回 `top = maxSize - 1` | $O(1)$ |

### 4. 应用场景（面试可能拓展）
- 表达式求值（中缀转后缀）
- 函数调用栈（Call Stack）
- Undo / Redo 功能
- 括号匹配检查

## 必须掌握的伪代码

```
// Push
top ← top + 1
stack[top] ← item

// Pop
item ← stack[top]
top ← top - 1
RETURN item
```

:::note[CIE 要求]
至少能写出 Push 和 Pop 的完整伪代码（含 overflow/underflow 检查），能手动模拟栈操作并给出每一步的 `stack[]` 和 `top` 值。
:::
