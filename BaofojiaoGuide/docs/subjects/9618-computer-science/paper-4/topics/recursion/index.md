---
title: Recursion
sidebar_position: 1
---

# Recursion（递归）

## 考纲要求

- 19.2 Recursion：写递归算法、追踪递归过程

## 核心代码模板

### 递归基本结构
```python
def RecursiveFunc(n):
    if base_condition:
        return base_value
    else:
        return operation(RecursiveFunc(smaller_n))
```

### 递归计算阶乘
```python
def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n - 1)
```

### 递归计算除数之和
```python
def RecursiveValue(number, toFind):
    if number == 0:
        return 0
    else:
        if toFind % number == 0:
            return number + RecursiveValue(number - 1, toFind)
        else:
            return RecursiveValue(number - 1, toFind)
```

### 递归计数字符串中元音
```python
def RecursiveVowels(value):
    if len(value) == 0:
        return 0
    first = value[0]
    if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
        return 1 + RecursiveVowels(value[1:])
    else:
        return RecursiveVowels(value[1:])
```

### 递归计算队列总和
```python
def RecursiveOutput(queue, start, headPointer):
    total = 0
    if start - 1 < headPointer:
        return 0
    else:
        return queue[start - 1] + RecursiveOutput(queue, start - 1, headPointer)
```

### 迭代转递归的通用方法
```
1. 识别循环的终止条件 → 成为 base case
2. 循环体中的操作 → 成为 recursive case
3. 循环变量 → 成为递归参数
```

## 常见错误

- 没有 base case（无限递归）
- 递归调用没有 return
- 递归参数没有缩小问题规模
- 递归层次太深导致栈溢出
