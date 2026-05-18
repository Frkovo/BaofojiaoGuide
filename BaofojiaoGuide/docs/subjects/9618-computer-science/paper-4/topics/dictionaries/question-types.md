
title: "题型分析"

# 题型分析

## Type 1 — Dictionary Concept Explanation

**特征:** 要求描述字典 ADT 的定义、特性、用途。

**常见问题:**

- "Explain what is meant by a dictionary ADT"
- "Describe the key difference between a dictionary and an array"

**答题要素:**

| 要素 | 说明 |
|------|------|
| Key-value pairs | 字典由若干 `(key, value)` 对组成 |
| Unique keys | 每个 key 唯一，不可重复 |
| Direct access by key | 通过 key 直接访问 value（非索引） |
| Dynamic size | 字典的大小可动态变化 |

---

## Type 2 — Implement Dictionary from Other ADTs

**特征:** 给定一种底层 ADT（如并行数组、链表），要求写出字典操作的伪代码。

**常见问题:**

- "A dictionary is implemented using two parallel arrays `keys[]` and `values[]`. Write pseudocode for the `add(key, value)`, `get(key)`, and `remove(key)` operations."

**答题要素:**

| 要素 | 说明 |
|------|------|
| Search for key | 线性查找 key 在 `keys[]` 中的位置 |
| Return / update value | 找到则返回/更新对应 `values[i]` |
| Handle "not found" | 未找到时返回 `null` 或 `-1` |

**Example structure:**

```
FUNCTION add(key, value)
    index ← findKey(keys, key)
    IF index ≥ 0 THEN
        values[index] ← value       // update existing
    ELSE
        keys[count] ← key
        values[count] ← value       // append new
        count ← count + 1
    ENDIF
ENDFUNCTION
```

---

## Type 3 — Time Complexity Analysis

**特征:** 分析字典各操作的时间复杂度，特别是基于不同底层实现时。

**常见问题:**

- "State the worst-case time complexity of the `get` operation when the dictionary is implemented using a linked list."

**答题要素:**

| 底层实现 | `get(key)` | `add(key, value)` | `remove(key)` |
|----------|------------|-------------------|----------------|
| Unsorted array / linked list | O(n) | O(1) append / O(n) update | O(n) |
| Sorted array | O(log n) (binary search) | O(n) (shift) | O(n) |
| Hash table (not in syllabus) | O(1) avg | O(1) avg | O(1) avg |
