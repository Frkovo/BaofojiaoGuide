---
title: "考前速记"
sidebar_position: 7
---

# 考前速记

## Code Templates (Remember These!)

### Linear Search

```python
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return True
    return False
```

### Iterative Binary Search

```python
def binary_search(arr, x):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            first = mid + 1
        else:
            last = mid - 1
    return False
```

### Recursive Binary Search

```python
def binary_search(arr, x, first, last):
    if first > last:
        return False
    mid = (first + last) // 2
    if arr[mid] == x:
        return True
    elif arr[mid] < x:
        return binary_search(arr, x, mid + 1, last)
    else:
        return binary_search(arr, x, first, mid - 1)
```

---

## When to Use Each

### 选择 Linear Search

数据满足**任一**条件:

- 未排序 (unsorted)
- 数据量很小 ($n < 20$)
- 只需要搜索一次
- 空间敏感

### 选择 Binary Search

数据满足**所有**条件:

- 已排序 (sorted)
- 数据量较大
- 需要多次搜索
- 可以接受先排序的成本

| 场景 | 推荐算法 | 原因 |
|------|---------|------|
| 数组 `[5,1,8,3]` 中找 8 | Linear | 未排序 |
| 数组 `[1,3,5,7,9]` 中找 5 | Binary | 已排序 & 快 |
| 搜索 1000 次 in 10000 个元素 | Binary | $O(\log n)$ vs $O(n)$ |
| 只搜索 1 次 in 10 个元素 | Linear | 无需排序开销 |

---

## 3-Second Checklist

- [ ] 数据排序了吗? (Binary → sorted; Linear → any)
- [ ] `//` 还是 `/`? (Integer division for mid)
- [ ] `first &lt;= last` 还是 `first < last`? (Need `=`!)
- [ ] `mid + 1` / `mid - 1` 还是 `mid`? (Skip mid!)
- [ ] 递归有 `return` 吗? (Must return recursive call)
- [ ] Base case 在最前面? (Check `first > last`)
- [ ] 返回什么? (True/False or index/-1)

---

## Quick Reference: Algorithm Properties

```
                Linear            Binary (Iter)      Binary (Recur)
Time (worst)    O(n)              O(log n)           O(log n)
Time (best)     O(1)              O(1)               O(1)
Space           O(1)              O(1)               O(log n)
Data sorted?    Not required      Required           Required
```
