---
title: Stack Calculation
sidebar_position: 1
---

# Stack Calculation（栈计算）

## 考纲要求

- 19.1.5 Stack ADT：用栈实现表达式计算

## 核心代码模板

```python
Stack = []
TopOfStack = -1

def Push(item):
    global Stack, TopOfStack
    Stack.append(item)
    TopOfStack = TopOfStack + 1

def Pop():
    global Stack, TopOfStack
    if TopOfStack == -1:
        return ""
    item = Stack[TopOfStack]
    Stack.pop()
    TopOfStack = TopOfStack - 1
    return item
```

### 从栈取值计算
```python
def Calculate():
    global Stack, TopOfStack
    total = int(Pop())
    while TopOfStack >= 0:
        operator = Pop()
        number = int(Pop())
        if operator == "+":
            total = total + number
        elif operator == "-":
            total = total - number
        elif operator == "*":
            total = total * number
        elif operator == "/":
            total = total // number
        elif operator == "^":
            total = total ** number
    return total
```

### 从文件读取数据到栈
```python
def ReadData(filename):
    global Stack, TopOfStack
    try:
        f = open(filename, 'r')
        lines = f.read().splitlines()
        f.close()
        for i in range(len(lines)):
            if TopOfStack < 19:
                Push(lines[i])
            else:
                print("Stack full")
    except:
        print("File not found")
```

## 常见错误

- Pop 顺序搞反（先 pop 的是栈顶，后 pop 的是下面的）
- 忘记把字符串转 int
- 除法用 `/` 而不是 `//`（整数除法）
