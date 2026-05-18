---
title: Searching Algorithms
sidebar_position: 1
---

# Searching Algorithms（查找算法）

## 考纲要求

- 19.1.1 Linear search：实现线性查找
- 19.1.2 Binary search：实现二分查找（迭代和递归）
- 二分查找要求数组已排序

## 核心代码模板

### 线性查找
```python
def LinearSearch(arr, n, target):
    for i in range(0, n):
        if arr[i] == target:
            return True
    return False
```

### 返回出现次数
```python
def LinearSearchCount(arr, n, target):
    count = 0
    for i in range(0, n):
        if arr[i] == target:
            count = count + 1
    return count
```

### 二分查找（迭代）
```python
def BinarySearch(arr, n, target):
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return -1
```

### 二分查找（递归）
```python
def BinarySearchRecursive(arr, first, last, target):
    if first > last:
        return -1
    mid = (first + last) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return BinarySearchRecursive(arr, first, mid - 1, target)
    else:
        return BinarySearchRecursive(arr, mid + 1, last, target)
```

## 常见错误

- 二分查找没有先排序
- mid 用 `/` 不用 `//`（浮点除 vs 整数除）
- 递归二分查找忘记 return
- first 和 last 更新公式写反
