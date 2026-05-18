---
title: Sorting Algorithms
sidebar_position: 1
---

# Sorting Algorithms（排序算法）

## 考纲要求

- 19.1.3 Bubble sort：实现冒泡排序
- 19.1.4 Insertion sort：实现插入排序（迭代和递归）
- 比较不同排序算法的性能

## 核心代码模板

### 冒泡排序
```python
def BubbleSort(arr, n):
    for i in range(0, n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
```

### 插入排序（迭代）
```python
def InsertionSort(arr, n):
    for i in range(1, n):
        lastItem = arr[i]
        checkItem = i - 1
        while checkItem >= 0 and arr[checkItem] > lastItem:
            arr[checkItem + 1] = arr[checkItem]
            checkItem = checkItem - 1
        arr[checkItem + 1] = lastItem
```

### 插入排序（递归）
```python
def RecursiveInsertion(arr, n):
    if n <= 1:
        return arr
    RecursiveInsertion(arr, n - 1)
    lastItem = arr[n - 1]
    checkItem = n - 2
    loopAgain = True
    if checkItem < 0:
        loopAgain = False
    elif arr[checkItem] <= lastItem:
        loopAgain = False
    while loopAgain:
        arr[checkItem + 1] = arr[checkItem]
        checkItem = checkItem - 1
        if checkItem < 0:
            loopAgain = False
        elif arr[checkItem] <= lastItem:
            loopAgain = False
    arr[checkItem + 1] = lastItem
    return arr
```

### 2D 数组按列排序（插入排序）
```python
def Sort2DByPriority(arr, n):
    for i in range(1, n):
        keyJob = arr[i][0]
        keyPriority = arr[i][1]
        j = i - 1
        while j >= 0 and arr[j][1] > keyPriority:
            arr[j + 1][0] = arr[j][0]
            arr[j + 1][1] = arr[j][1]
            j = j - 1
        arr[j + 1][0] = keyJob
        arr[j + 1][1] = keyPriority
```

## 常见错误

- 冒泡排序内循环次数写错（应该是 n-1 不是 n）
- 插入排序忘记在循环外赋值 arr[checkItem + 1] = lastItem
- 递归插入排序 base case 没有 return
- 比较方向反了（升序用 `>`，降序用 `<`）
