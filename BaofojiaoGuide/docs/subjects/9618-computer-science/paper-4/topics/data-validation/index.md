---
title: Data Validation
sidebar_position: 1
---

# Data Validation（数据验证）

## 考纲要求

- 6.2 数据验证：range check, presence check
- 19.1 Check digit 计算和验证

## 核心代码模板

### 输入范围验证
```python
def GetValidInput():
    valid = False
    while valid == False:
        num = int(input("Enter a number between 1 and 20: "))
        if num >= 1 and num <= 20:
            valid = True
        else:
            print("Invalid input")
    return num
```

### 字符串长度验证
```python
def GetStringOfLength(len):
    valid = False
    while valid == False:
        s = input("Enter a 7-character string: ")
        if len(s) == 7:
            valid = True
        else:
            print("Must be exactly 7 characters")
    return s
```

### Check Digit 计算（交替乘 1 和 3）
```python
def CalculateCheckDigit(data):
    total = 0
    for i in range(6):
        digit = int(data[i])
        if i % 2 == 0:
            total = total + digit * 1
        else:
            total = total + digit * 3
    checkDigit = total // 10
    if checkDigit == 10:
        return 'X'
    return str(checkDigit)

def ValidateData(data):
    if len(data) != 7:
        return False
    expected = CalculateCheckDigit(data)
    if expected == 'X':
        return data[6] == 'X'
    return data[6] == expected
```

### 验证循环直到输入正确
```python
found = False
while found == False:
    choice = input("Enter character name: ")
    for i in range(len(characters)):
        if characters[i].GetName() == choice:
            found = True
            index = i
    if found == False:
        print("Character not found")
```

## 常见错误

- 验证条件写反（`< 1 or > 20` 写成 `< 1 and > 20`）
- check digit 除法用 `/` 而不是 `//`
- check digit 为 10 时处理成 'X'
- 忘记把输入字符串转 int
