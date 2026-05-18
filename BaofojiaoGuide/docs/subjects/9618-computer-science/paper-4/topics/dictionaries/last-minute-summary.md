
title: "考前速记"

# 考前速记

## 三句话核心

1. Dictionary = collection of `(key, value)` pairs, **keys are unique**
2. Keys can be **any data type** — access by key, **not** by index
3. **Paper 4 won't ask for full code** — but you must write **pseudocode snippets** using parallel arrays or linked lists

## 操作速查

| 操作 | 平行数组 | 链表 |
|------|----------|------|
| `get(key)` | `for i ← 0 to size-1` 对比 `keys[i]` | `while current ≠ NULL` 对比 `current.key` |
| `add(key, value)` | 找到则 `values[i] ← value`，否则追加 | 找到则更新，否则插入新节点 |
| `remove(key)` | 找到后移位（`for j ← i to size-2`） | 找到后 unlink（注意 head 特判） |

## 复杂度速记

| 实现方式 | `get` | `add` | `remove` |
|----------|-------|-------|----------|
| 无序数组 | O(n) | O(n) | O(n) |
| 无序链表 | O(n) | O(n) | O(n) |
| 有序数组 | O(log n) | O(n) | O(n) |

:::note[关键提醒]

- 字典**不保证顺序**
- key 必须唯一，value 可以重复
- 数组实现 `remove` 后要**移位**并递减 `size`
- 链表实现 `remove` 要处理 **head 删除**的特殊情况

:::
