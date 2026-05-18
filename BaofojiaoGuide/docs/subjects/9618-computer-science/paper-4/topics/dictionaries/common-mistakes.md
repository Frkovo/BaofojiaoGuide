
title: "常见错误"

# 常见错误

### Mistake 1 — Treating dictionary keys like array indices

❌ "Dictionary key 只能是整数"

✅ Dictionary 的 key 可以是任何数据类型：`string`, `integer`, 甚至自定义类型

:::note[Key Point]

字典不是数组。数组使用连续整数索引，字典使用任意唯一键。不能假定 key 的顺序有意义。

:::

---

### Mistake 2 — Assuming keys are stored in sorted order

❌ 在字典中按 key 升序遍历

✅ 字典不保证键的顺序（除非使用特定有序实现）

---

### Mistake 3 — Forgetting unique key constraint

❌ "将两个相同 key 的不同 value 分别存入字典"

✅ 字典要求 key 唯一 — 重复添加相同 key 会覆盖原 value

---

### Mistake 4 — Confusing time complexity of different operations

❌ "`add` 操作永远是 O(1)"

✅ 当需要先查找 key 时，`add` 的最坏情况也是 O(n)

```
// 错误思维
add → 只追加到末尾 → O(1)

// 正确思维
add → 先查找 key 是否存在
      ├── 存在 → 更新 values[i]  (O(n) from search)
      └── 不存在 → 追加到末尾   (O(1) + O(n) from search)
```

---

### Mistake 5 — Incorrect shifting in array-based `remove`

❌ 移除元素后未将后续元素前移

✅ 数组实现中，`remove` 后必须将后面的元素全部左移一位，并递减 `size`

```
remove index 2:

Before:  [A] [B] [C] [D] [E]   size = 5
         After:  [A] [B] [D] [E] [ ]   size = 4
                        ↑ shift left
```

---

### Mistake 6 — Linked list remove not handling head deletion

❌ 只用一种删除逻辑导致 head 节点无法正确删除

✅ 分两种情况：

```
// 删除 head 节点
IF previous = NULL THEN
    head ← head.next
ELSE
    previous.next ← current.next
ENDIF
```
