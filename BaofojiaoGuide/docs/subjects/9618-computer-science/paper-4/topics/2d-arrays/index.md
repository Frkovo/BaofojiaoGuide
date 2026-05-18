---
title: 2D Arrays
sidebar_position: 1
---

# 2D Arrays（二维数组）

## 考纲要求

- 10.2 Arrays：2D 数组声明和使用
- 用 2D 数组存储二叉树节点（ArrayNodes[row, 0] = LeftPointer, [row, 1] = Data, [row, 2] = RightPointer）

## 核心代码模板

### 声明 2D 数组
```python
ArrayNodes = [[0, 0, 0] for _ in range(20)]
RootPointer = -1
FreeNode = 0
```

### 存储 Job 数据（2D 数组）
```python
Jobs = [[0, 0] for _ in range(100)]
NumberOfJobs = 0

def AddJob(jobNum, priority):
    global Jobs, NumberOfJobs
    if NumberOfJobs < 100:
        Jobs[NumberOfJobs][0] = jobNum
        Jobs[NumberOfJobs][1] = priority
        NumberOfJobs = NumberOfJobs + 1
        print("Added")
    else:
        print("Not added")
```

### 2D 数组按列排序（插入排序）
```python
def InsertionSort():
    global Jobs, NumberOfJobs
    for i in range(1, NumberOfJobs):
        key0 = Jobs[i][0]
        key1 = Jobs[i][1]
        j = i - 1
        while j >= 0 and Jobs[j][1] > key1:
            Jobs[j + 1][0] = Jobs[j][0]
            Jobs[j + 1][1] = Jobs[j][1]
            j = j - 1
        Jobs[j + 1][0] = key0
        Jobs[j + 1][1] = key1
```

### 二叉树用 2D 数组实现
```python
# ArrayNodes[row][0] = LeftPointer
# ArrayNodes[row][1] = Data
# ArrayNodes[row][2] = RightPointer
# RootPointer = -1  (null)
# FreeNode = 0

def AddNode():
    global ArrayNodes, RootPointer, FreeNode
    data = int(input("Enter the data: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = data
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            placed = False
            currentNode = RootPointer
            while placed == False:
                if data < ArrayNodes[currentNode][1]:
                    if ArrayNodes[currentNode][0] == -1:
                        ArrayNodes[currentNode][0] = FreeNode
                        placed = True
                    else:
                        currentNode = ArrayNodes[currentNode][0]
                else:
                    if ArrayNodes[currentNode][2] == -1:
                        ArrayNodes[currentNode][2] = FreeNode
                        placed = True
                    else:
                        currentNode = ArrayNodes[currentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")

def PrintAll():
    global ArrayNodes, FreeNode
    for i in range(0, FreeNode):
        print(ArrayNodes[i][0], ArrayNodes[i][1], ArrayNodes[i][2])
```

### 中序递归遍历（2D 数组版）
```python
def InOrder(nodeIndex):
    global ArrayNodes
    if nodeIndex == -1:
        return
    InOrder(ArrayNodes[nodeIndex][0])
    print(ArrayNodes[nodeIndex][1])
    InOrder(ArrayNodes[nodeIndex][2])
```

## 常见错误

- 2D 数组索引顺序混淆 `arr[row][col]` vs `arr[col][row]`
- 二叉树插入时比较方向搞反
- 忘记更新 FreeNode
- 中序遍历没有 base case
