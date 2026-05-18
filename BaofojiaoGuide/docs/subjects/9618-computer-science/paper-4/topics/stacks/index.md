---
title: Stacks
sidebar_position: 1
---

# Stacks（栈）

## 考纲要求

- 19.1.5 Stack ADT：push（压栈）、pop（出栈）

## 核心代码模板

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

### 两个栈版本
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

## 常见错误

- 栈空时 Pop 没有返回空值
- 栈满时 Push 没有返回错误码
- TopOfStack 初始化和更新逻辑错误
- 忘记 global 声明
