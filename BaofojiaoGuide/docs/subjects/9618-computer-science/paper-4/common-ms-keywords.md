---
title: MS 关键词速查
sidebar_position: 9
---

# MS 关键词速查

## 数组/2D 数组

| MS 原文 | 代码要求 |
|---------|---------|
| Declaration of (global) array with identifier | `global arr` / `arr = []` |
| Initialising elements with null value | `arr = [""] * 20` |
| Looping through each array element | `for i in range(len(arr)):` |
| 2D array declaration | `arr = [[0]*cols for _ in range(rows)]` |

## 排序

| MS 原文 | 代码要求 |
|---------|---------|
| Procedure header and looping | `def Sort():` + 外层循环 |
| Working inner loop | 内层循环遍历 |
| Comparison of elements | `if arr[j] > arr[j+1]:` |
| Swapping of elements | `arr[j], arr[j+1] = arr[j+1], arr[j]` |
| Recursive function with recursive call | 递归调用自身 |
| Correct base case and return | `if n <= 1: return arr` |
| While loop control | `while LoopAgain:` |

## 查找

| MS 原文 | 代码要求 |
|---------|---------|
| Function header taking parameter | `def Search(target):` |
| Calculating the mid value | `mid = (first + last) // 2` |
| Checking if data at mid is parameter | `if arr[mid] == target:` |
| Updating first/last with mid +/- 1 | `last = mid - 1` / `first = mid + 1` |
| Returning -1 when not found | `return -1` |

## 队列

| MS 原文 | 代码要求 |
|---------|---------|
| Checks if queue is full and returns FALSE | `if Rear >= size: return False` |
| Inserts data item and increments pointer | `Queue[Rear] = data; Rear += 1` |
| Assigns Head to 0 when first element | `if Head == -1: Head = 0` |
| Returns TRUE | `return True` |
| Check if queue empty and return "false" | `if Head < 0 or Head > Rear: return "false"` |

## 循环队列

| MS 原文 | 代码要求 |
|---------|---------|
| NumberItems counter for full check | `if NumberItems == size: return False` |
| Wrap-around using MOD | `Tail = (Tail + 1) % size` |
| Head wrap-around | `Head = (Head + 1) % size` |

## 栈

| MS 原文 | 代码要求 |
|---------|---------|
| Check if stack full | `if TopOfStack == size-1: return -1` |
| Store data and increment | `Stack[TopOfStack] = data; TopOfStack += 1` |
| Check if stack empty | `if TopOfStack == -1: return ""` |
| Return top and decrement | `TopOfStack -= 1; return Stack[TopOfStack]` |

## 链表

| MS 原文 | 代码要求 |
|---------|---------|
| Record type declaration | `class Node: def __init__(self, data, next):` |
| Array of nodes initialised | `linkedList = [Node(0, 0) for _ in range(10)]` |
| Traversal by following pointers | `current = startPointer; while current != -1:` |
| Insert at end | `while linkedList[current].nextNode != -1:` |

## 二叉树

| MS 原文 | 代码要求 |
|---------|---------|
| Class declaration with private attributes | `class Node:` + `self.__Data` |
| Constructor taking parameter | `def __init__(self, data):` |
| Get methods returning attributes | `def GetData(self): return self.__Data` |
| Checking if tree empty | `if self.__NumberNodes == 0:` |
| Comparing data for left/right | `if data < current.GetData():` |
| Updating pointer for parent | `self.__Tree[previous].SetLeft(index)` |

## 哈希表

| MS 原文 | 代码要求 |
|---------|---------|
| Hash function using MOD | `return key % 200` |
| Check if slot is empty | `if HashTable[h].GetKey() == -1:` |
| Collision to Spare array | `Spare[i] = record` |
| Initialise all to empty | `key = -1, item1 = -1, item2 = -1` |

## OOP 继承

| MS 原文 | 代码要求 |
|---------|---------|
| Child class inheriting from parent | `class Child(Parent):` |
| Constructor calling parent | `super().__init__(params)` |
| Override method | `def Method(self):` (same name) |

## 文件处理

| MS 原文 | 代码要求 |
|---------|---------|
| Appropriate use of exception handling | `try: ... except: ...` |
| Opening text file to read | `open("file.txt", 'r')` |
| Reading each line | `f.read().splitlines()` |
| Splitting each line | `line.split(",")` |
| Casting to integers | `int(value)` |

## 递归

| MS 原文 | 代码要求 |
|---------|---------|
| Base case return | `if n <= 1: return value` |
| Recursive call with smaller input | `return n * RecursiveFunc(n-1)` |
| Iterative to recursive conversion | 循环体改为递归调用 |

## 字符串处理

| MS 原文 | 代码要求 |
|---------|---------|
| MID function equivalent | `s[start:start+len]` |
| LENGTH function | `len(s)` |
| Character comparison | `if s[i] < s[j]:` |
