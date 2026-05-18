---
title: "常见错误"
sidebar_position: 5
---

# 常见错误

## 1. 未排序数据使用 Binary Search

:::danger[致命错误]

Binary Search 要求在**已排序**数据上运行。对未排序数组使用 binary search 结果不可预测。

```python
# 错误: arr 未排序
arr = [5, 3, 8, 1, 9]
binary_search(arr, 5)  # 可能找不到!
```

```python
# 正确: 先排序
arr = [5, 3, 8, 1, 9]
arr.sort()
binary_search(arr, 5)
```

:::

---

## 2. Integer Division vs Regular Division

:::caution[类型错误]

Python 中 `mid` 必须是整数下标。使用 `/` 会返回 `float`，导致下标无效。

| 错误 | 正确 |
|------|------|
| `mid = (first + last) / 2` | `mid = (first + last) // 2` |
| 返回 `float` | 返回 `int` |
| `TypeError: list indices must be integers` | 正常执行 |

:::

---

## 3. 递归缺少 `return`

:::note[易错点]

递归调用**必须**有 `return`，否则函数返回 `None`。

```python
# 错误: 缺少 return
def search(arr, x, f, l):
    if f > l:
        return -1
    mid = (f + l) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        search(arr, x, mid + 1, l)  # 忘记 return!
    else:
        search(arr, x, f, mid - 1)  # 忘记 return!

# 正确: 显式 return
def search(arr, x, f, l):
    if f > l:
        return -1
    mid = (f + l) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return search(arr, x, mid + 1, l)
    else:
        return search(arr, x, f, mid - 1)
```

:::

---

## 4. Off-by-One 错误

| 错误写法 | 问题 | 正确写法 |
|---------|------|---------|
| `while first < last` | 漏掉 `first == last` 的情况 | `while first &lt;= last` |
| `first = mid` | mid 已被检查过，造成死循环 | `first = mid + 1` |
| `last = mid` | mid 已被检查过，造成死循环 | `last = mid - 1` |

---

## 5. Base Case 遗漏或错误

:::caution[无限递归]

```python
# 错误: 无 base case
def binary_search(arr, x, f, l):
    mid = (f + l) // 2          # 永远会执行
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binary_search(arr, x, mid + 1, l)
    else:
        return binary_search(arr, x, f, mid - 1)
# 当 x 不存在时 → RecursionError
```

```python
# 正确: base case 在最前
def binary_search(arr, x, f, l):
    if f > l:
        return -1          # ← base case 必须先出现
    mid = (f + l) // 2
    ...
```

:::

---

## 6. 混淆下标和元素值

```python
# 错误: 比较下标而非元素
if i == target:       # ← i 是下标, 不是元素!

# 正确: 比较元素
if arr[i] == target:  # ← arr[i] 才是元素
```

---

## 7. 在循环内提前返回未找到

```python
# 错误: 每次比较都返回 -1
for i in range(len(arr)):
    if arr[i] == target:
        return i
    else:
        return -1    # ← 只比较了第一个元素就返回

# 正确: 循环结束后才返回 -1
for i in range(len(arr)):
    if arr[i] == target:
        return i
return -1           # ← 遍历完全部元素后返回
```

---

## 8. Wrapper 函数缺失

有时试卷要求提供一个 wrapper 函数来简化递归调用:

```python
# 错误: 直接暴露递归接口
result = binary_search(arr, x, 0, len(arr)-1)  # 调用者必须传 first/last

# 正确: wrapper 函数
def search(arr, x):
    return binary_search(arr, x, 0, len(arr) - 1)  # 封装细节

def binary_search(arr, x, first, last):
    # recursive implementation
    ...
```
