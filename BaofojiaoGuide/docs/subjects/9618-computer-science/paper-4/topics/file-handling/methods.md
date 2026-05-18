---
title: 解题方法
sidebar_position: 3
---

# 解题方法

## Method 1: Read All Lines

### 适用场景
文件行数已知或未知，需要全部读入数组。

### 步骤
1. `f = open(filename, 'r')`
2. `lines = f.read().splitlines()`
3. `f.close()`
4. 遍历 lines 处理每行数据

```python
def ReadAll(filename):
    try:
        f = open(filename, 'r')
        lines = f.read().splitlines()
        f.close()
        return lines
    except:
        print("File not found")
        return []
```

## Method 2: Read Line by Line

### 适用场景
需要逐行处理，或行数未知。

```python
def ReadLineByLine(filename):
    try:
        f = open(filename, 'r')
        line = f.readline()
        while line != "":
            line = line.strip()
            # 处理这一行
            print(line)
            line = f.readline()
        f.close()
    except:
        print("File not found")
```

## Method 3: Read Fixed Number of Lines

### 适用场景
题目明确指定文件中有固定行数（如 25 行）。

```python
def ReadFixed(filename):
    try:
        f = open(filename, 'r')
        arr = []
        for i in range(25):
            val = int(f.readline().strip())
            arr.append(val)
        f.close()
        return arr
    except:
        print("File not found")
        return []
```

## Method 4: Write to File

### 适用场景
需要将数据保存到文件。

```python
def SaveToFile(filename, data):
    try:
        f = open(filename, 'w')
        for i in range(len(data)):
            f.write(str(data[i]) + "\n")
        f.close()
    except:
        print("Error writing file")
```

## Method 5: Append to File

### 适用场景
需要在文件末尾追加数据而不是覆盖。

```python
def AppendToFile(filename, item):
    try:
        f = open(filename, 'a')
        f.write(str(item) + "\n")
        f.close()
    except:
        print("Error appending to file")
```

## Method 6: Parse CSV Line

### 适用场景
文件每行包含逗号分隔的多个字段。

```python
def ParseCSV(line):
    parts = line.split(",")
    field1 = parts[0]
    field2 = int(parts[1])
    field3 = parts[2]
    # 根据题目需求继续处理
    return field1, field2, field3
```

## Method 7: Exception Handling Pattern

### 适用场景
任何文件操作都需要异常处理。

```python
try:
    f = open("filename.txt", 'r')
    # 文件操作
    f.close()
except FileNotFoundError:
    print("File not found")
except:
    print("An error occurred")
```
