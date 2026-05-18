---
title: File Handling
sidebar_position: 1
---

# File Handling（文件处理）

## 考纲要求

- 20.2 File Processing：open/close（读、写、追加模式）
- 从文件读取记录、写入记录到文件
- Serial、sequential、random 文件操作
- Exception handling（try/except）

## 常见题型

| 题型 | 分值 | 示例 |
|------|------|------|
| 读取文件到数组 | 4-7 | w22_qp_41 Q1b |
| 读取 CSV 格式文件创建对象 | 7 | s24_qp_41 Q2b |
| 写入数据到文件 | 5 | s25_qp_41 Q2c |
| 从文件读取并处理（search/sort） | 4-6 | w22_qp_41 Q1 |
| 异常处理 | 1-2 | 伴随文件操作 |

## 核心代码模板

### 读取文件（全部行）
```python
def ReadFile(filename):
    try:
        f = open(filename, 'r')
        data = f.read().splitlines()
        f.close()
        return data
    except:
        print("File not found")
        return []
```

### 读取文件（逐行）
```python
def ReadFile(filename):
    try:
        f = open(filename, 'r')
        data = []
        line = f.readline()
        while line != "":
            data.append(line.strip())
            line = f.readline()
        f.close()
        return data
    except:
        print("File not found")
        return []
```

### 读取固定行数
```python
def ReadFile(filename):
    try:
        f = open(filename, 'r')
        data = []
        for i in range(25):
            line = f.readline().strip()
            data.append(int(line))
        f.close()
        return data
    except:
        print("File not found")
        return []
```

### 写入文件
```python
def WriteFile(filename, data):
    try:
        f = open(filename, 'w')
        for i in range(len(data)):
            f.write(str(data[i]) + "\n")
        f.close()
    except:
        print("Error writing to file")
```

### 追加到文件
```python
def AppendFile(filename, data):
    try:
        f = open(filename, 'a')
        f.write(str(data) + "\n")
        f.close()
    except:
        print("Error appending to file")
```

### 读取 CSV 格式
```python
def ReadCSV(filename):
    try:
        f = open(filename, 'r')
        lines = f.read().splitlines()
        f.close()
        result = []
        for i in range(len(lines)):
            parts = lines[i].split(",")
            # parts[0], parts[1], ... 是分割后的字段
            result.append(parts)
        return result
    except:
        print("File not found")
        return []
```

### 顺序文件访问（读取并处理）
```python
def ProcessSequential(filename):
    try:
        f = open(filename, 'r')
        total = 0
        count = 0
        line = f.readline()
        while line != "":
            num = int(line.strip())
            total = total + num
            count = count + 1
            line = f.readline()
        f.close()
        return total, count
    except:
        print("File not found")
        return 0, 0
```

### 随机文件访问（使用哈希）
```python
class Record:
    def __init__(self):
        self.key = -1
        self.data = -1

def ReadRandomRecord(filename, recordSize, recordNum):
    try:
        f = open(filename, 'r')
        lines = f.read().splitlines()
        f.close()
        if recordNum < len(lines):
            parts = lines[recordNum].split(",")
            r = Record()
            r.key = int(parts[0])
            r.data = int(parts[1])
            return r
        return None
    except:
        print("File not found")
        return None
```

## 文件模式

| 模式 | 含义 | 文件存在时 | 文件不存在时 |
|------|------|-----------|-------------|
| 'r' | 读取 | 正常读取 | 报错 |
| 'w' | 写入 | 覆盖原有内容 | 创建新文件 |
| 'a' | 追加 | 在末尾添加 | 创建新文件 |

## 常见错误

- 忘记 try/except（题目明确要求时必须加）
- 忘记关闭文件（用完必须 f.close()）
- read() 读取后忘记 splitlines() 处理换行符
- CSV 分割后忘记 int() 转换
- 写入时忘记 str() 转换和加换行符 "\n"
- 文件路径写死成绝对路径而不是只用文件名
