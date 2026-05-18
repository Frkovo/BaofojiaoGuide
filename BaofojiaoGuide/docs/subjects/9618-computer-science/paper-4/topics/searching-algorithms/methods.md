---
title: "解题方法"
sidebar_position: 3
---

# 解题方法

## Method 1: Linear Search

### 适用场景
- 数据**未排序**
- 数据量较小
- 只需要找到第一个匹配

### 步骤

1. 用 `for` 循环遍历数组 (range from `0` to `len(arr)-1`)
2. 比较每个元素与目标值
3. 找到匹配则 `return True` (或下标)
4. 循环结束未找到则 `return False` (或 -1)

### 代码

```python
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
```

### 复杂度
- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

---

## Method 2: Iterative Binary Search

### 适用场景
- 数据**已排序**
- 数据量较大
- 需要 $O(\log n)$ 效率

### 步骤

1. 初始化 `first = 0`, `last = len(arr) - 1`
2. `while first &lt;= last`:
   - 计算 `mid = (first + last) // 2`
   - 若 `arr[mid] == target` → 返回
   - 若 `arr[mid] < target` → `first = mid + 1`
   - 若 `arr[mid] > target` → `last = mid - 1`
3. 循环结束返回 `False` / -1

### 代码

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

### 复杂度
- 时间复杂度: $O(\log n)$
- 空间复杂度: $O(1)$

---

## Method 3: Recursive Binary Search

### 适用场景
- 题目要求 "using recursion"
- 函数签名已包含 `first`, `last` 参数

### 步骤

1. **Base case**: `if first > last: return False`
2. 计算 `mid = (first + last) // 2`
3. **Compare**:
   - `arr[mid] == target` → `return True`
   - `arr[mid] < target` → 递归搜索右半部分
   - `arr[mid] > target` → 递归搜索左半部分
4. **必须** `return` 递归调用结果

### 代码

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

### 复杂度
- 时间复杂度: $O(\log n)$
- 空间复杂度: $O(\log n)$ (递归调用栈)

---

## 方法对比

| 特性 | Linear Search | Iterative Binary | Recursive Binary |
|------|--------------|-----------------|-----------------|
| 数据要求 | 无 | 必须排序 | 必须排序 |
| 时间复杂度 | $O(n)$ | $O(\log n)$ | $O(\log n)$ |
| 空间复杂度 | $O(1)$ | $O(1)$ | $O(\log n)$ |
| 实现难度 | 低 | 中 | 中高 |
| 易错点 | 忘记返回值 | Off-by-one | 忘记 `return` |
