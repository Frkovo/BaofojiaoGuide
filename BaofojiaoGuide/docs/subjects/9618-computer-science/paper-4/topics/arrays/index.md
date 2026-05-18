---
title: Arrays
sidebar_position: 1
---

# Arrays（数组）

## 考纲要求

- 10.2 Arrays：声明、初始化、遍历、存取

## 核心代码模板

### 声明全局数组和变量
```python
global DataStored
global NumberItems
DataStored = []
NumberItems = 0
```

### 固定大小数组（初始化为空值）
```python
DataStored = [0] * 20
NumberItems = 0
```

### 读取用户输入并存入数组
```python
def Initialise():
    global DataStored, NumberItems
    qty = int(input("How many numbers? "))
    while qty < 1 or qty > 20:
        qty = int(input("How many numbers? "))
    for i in range(0, qty):
        num = int(input("Enter number: "))
        DataStored.append(num)
        NumberItems = NumberItems + 1
```

### 遍历输出数组
```python
for i in range(0, NumberItems):
    print(DataStored[i])
```

### 字符串数组
```python
Animals = [""] * 10
Animals[0] = "horse"
Animals[1] = "lion"
Animals[2] = "rabbit"
# ...
```

## 常见错误

- 忘记 global 声明（在函数内修改全局数组）
- 数组越界（用 `range(len(arr))` 不是 `range(len(arr)+1)`）
- Python 动态列表 vs 固定数组（append 只用于动态列表）
