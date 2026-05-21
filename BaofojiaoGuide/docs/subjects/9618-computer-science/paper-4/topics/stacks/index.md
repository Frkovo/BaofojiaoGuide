---
title: Stacks
sidebar_position: 1
---

# Stacks（栈）

## 考纲要求

- 19.1.5 Stack ADT：push（压栈）、pop（出栈）
- 用数组实现，支持 insert 和 delete

## 核心代码模板

### 方式一：TopOfStack 指向栈顶（-1 表示空）

```python
Stack = [""] * 20
TopOfStack = -1

def Push(item):
    global Stack, TopOfStack
    if TopOfStack == 19:
        return -1
    TopOfStack = TopOfStack + 1
    Stack[TopOfStack] = item
    return 1

def Pop():
    global Stack, TopOfStack
    if TopOfStack == -1:
        return ""
    item = Stack[TopOfStack]
    TopOfStack = TopOfStack - 1
    return item
```

### 方式二：top 指向下一个空位（0 表示空）

```python
class Stack:
    def __init__(self, capacity):
        self.list = [None] * capacity
        self.top = 0
        self.capacity = capacity

    def Push(self, element):
        if self.top == self.capacity:
            print("Stack full")
            return
        self.list[self.top] = element
        self.top = self.top + 1

    def Pop(self):
        if self.top == 0:
            print("Stack empty")
            return None
        self.top = self.top - 1
        return self.list[self.top]
```

### 两个栈（元音/辅音）
```python
StackVowel = [""] * 100
StackConsonant = [""] * 100
VowelTop = 0
ConsonantTop = 0

def PushData(letter):
    global StackVowel, StackConsonant, VowelTop, ConsonantTop
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        if VowelTop < 100:
            StackVowel[VowelTop] = letter
            VowelTop = VowelTop + 1
    else:
        if ConsonantTop < 100:
            StackConsonant[ConsonantTop] = letter
            ConsonantTop = ConsonantTop + 1
```

### 用栈反转数组
```python
def ReverseWithStack(arr):
    s = Stack(len(arr))
    for i in range(len(arr)):
        s.Push(arr[i])
    for i in range(len(arr)):
        arr[i] = s.Pop()
```

## 常见错误

- Push 时忘记检查栈满
- Pop 时忘记检查栈空
- TopOfStack 初始值（-1 vs 0）决定指针操作方式
- 两个栈时搞混指针变量
