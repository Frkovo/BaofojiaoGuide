---
title: 题型分析
sidebar_position: 2
---

# 题型分析

## Question Type 1: Read File into Array（4-7 分）

### 如何识别
要求从文本文件读取数据，存储到数组中。

:::note[标准解题方法]
1. 函数头，接受文件名参数
2. 用 try 包围文件操作
3. 用 `open(filename, 'r')` 打开文件
4. 读取数据：`read().splitlines()` 或 `readline()` 循环
5. 关闭文件：`f.close()`
6. 返回数据或处理数据
7. except 捕获异常输出错误信息
:::

:::info[评分标准]
**M1**: 过程/函数头，带参数
**M1**: 声明数组
**M1**: 打开文件读取
**M1**: 用异常处理
**M1**: 逐行读取并存储
**M1**: 关闭文件
:::

**Example 1 — 9618/w22/qp/41 Q1(b):**

> The procedure ReadFile() must read in the numbers from the text file and store each one in the array. Use appropriate exception handling.

## Question Type 2: Read CSV and Create Objects（7-8 分）

### 如何识别
要求从 CSV 格式文件读取数据，每行分割后创建对象。

:::note[标准解题方法]
1. 打开文件读取全部行
2. 对每一行用 `split(",")` 分割
3. 将各部分转为正确类型（int、string）
4. 创建对象并存入数组
5. 使用异常处理
:::

**Example 1 — 9618/s24/qp/41 Q2(b):**

> The function ReadData() reads data from Trees.txt, creates a Tree object for each tree, stores in array.

```python
def ReadData():
    TreeObjects = []
    try:
        f = open("Trees.txt", 'r')
        lines = f.read().splitlines()
        f.close()
        for i in range(len(lines)):
            parts = lines[i].split(",")
            name = parts[0]
            growth = int(parts[1])
            maxH = int(parts[2])
            maxW = int(parts[3])
            evergreen = parts[4]
            t = Tree(name, growth, maxH, maxW, evergreen)
            TreeObjects.append(t)
        return TreeObjects
    except:
        print("File not found")
        return []
```

## Question Type 3: Write Data to File（5 分）

### 如何识别
要求将数据写入文本文件。

:::note[标准解题方法]
1. 用 `open(filename, 'w')` 打开（写入模式）
2. 用 `f.write(str(item) + "\n")` 逐行写入
3. 关闭文件
4. 使用异常处理
:::

**Example 1 — 9618/s25/qp/41 Q2(c):**

> The procedure StoreData() takes an array and a filename, appends each item to the file.

## Question Type 4: Sequential Processing（5 分）

### 如何识别
要求从头到尾读取文件并对每条记录进行处理。

:::note[标准解题方法]
1. 打开文件
2. 循环读取每一行直到文件末尾
3. 对每行数据进行处理（计数、累加、搜索等）
4. 关闭文件
:::
