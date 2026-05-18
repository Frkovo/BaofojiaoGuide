---
title: 常见错误
sidebar_position: 8
---

# 常见错误

## 数组相关问题

### 1. 忘记 global 声明
:::danger

```python
def Initialise():
    DataStored.append(5)  # NameError: DataStored is not defined
```
:::
**修正**：
```python
def Initialise():
    global DataStored
    DataStored.append(5)
```

### 2. 数组越界
```
range(NumberItems)  →  0 到 NumberItems-1 ✓
range(1, NumberItems)  →  1 到 NumberItems-1 ✓
```
循环时注意 Python 的 `range()` 不包括上限。

### 3. 混淆 1D 和 2D 数组
题目要求 1D 数组存储结构体时，数组元素应为对象/记录，不是嵌套数组。

## 排序算法

### 4. 冒泡排序比较方向错误
```
# 正确：相邻元素比较
if arr[j] > arr[j+1]:
```
不是 `arr[i] > arr[j]`。

### 5. 插入排序索引错误
```
arr[checkItem + 1] = lastItem  # 在循环外
```

## 查找算法

### 6. 二分查找忘记先排序
二分查找只适用于**已排序**的数组。

### 7. 二分查找 mid 计算溢出
```python
mid = (first + last) // 2  # ✓ 整数除法
```
不要用 `/`（得到 float），要用 `//`。

### 8. 递归二分查找忘记返回值
```python
return BinarySearch(arr, first, mid-1, target)  # ✓ 必须 return
```

## 队列

### 9. 队列空/满条件错误
常见错误：`HeadPointer` 和 `TailPointer` 的初始化和更新逻辑错误。
```
# 初始化
HeadPointer = -1  # 没有元素
TailPointer = 0   # 下一个空位

# 检查空
HeadPointer == -1 or HeadPointer >= TailPointer
```

## 链表

### 10. 遍历时死循环
```python
while current != -1:
    # ...
    # 忘记更新 current！
```
**必须更新**：`current = linkedList[current].nextNode`

## 二叉树

### 11. 比较方向混淆
新节点数据**小于**当前节点 → 走左边
新节点数据**大于**当前节点 → 走右边

## 递归

### 12. 忘记 base case
无限递归导致 stack overflow。

### 13. 问题规模未缩小
递归调用必须用更小的参数（如 `n-1`）。

## OOP

### 14. 忘记 self
```python
class Card:
    def __init__(self, num, col):
        num = num      # 错误：没有 self.
        self.__col = col  # 正确
```

### 15. Python 私有属性命名
```
self.__AttributeName  # ✓ 双下划线前缀
```
不要用 `self._AttributeName`（单下划线，不是真正的 private）。

## 文件处理

### 16. 忘记 try/except
当题目说明 "use appropriate exception handling" 时必须用。

### 17. 文件路径错误
数据文件与程序在同一目录，直接用文件名即可：
```python
open("Trees.txt")  # ✓
```

## 数据类型

### 18. int() / float() 转换错误
```python
int(input())  # ✓ 直接转 int
```
输入默认是 string，需要数学运算时必须转类型。

### 19. return 丢失
函数所有分支都必须有 return：
```python
def LinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True  # 这里 return 了
    return False  # 这里也要 return！
```
