---
title: 考前速通
sidebar_position: 4
---

# 考前速通

## 核心代码模板

### 数组声明
```python
DataStored = [0] * 20
NumberItems = 0
```

### 2D 数组声明
```python
ArrayNodes = [[0, 0, 0] for _ in range(20)]
RootPointer = -1
FreeNode = 0
```

### 冒泡排序
```python
def BubbleSort(arr, n):
    for i in range(0, n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
```

### 插入排序（迭代）
```python
def InsertionSort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
```

### 插入排序（递归）
```python
def RecursiveInsertion(arr, n):
    if n <= 1:
        return arr
    RecursiveInsertion(arr, n - 1)
    lastItem = arr[n - 1]
    checkItem = n - 2
    loopAgain = True
    if checkItem < 0:
        loopAgain = False
    elif arr[checkItem] <= lastItem:
        loopAgain = False
    while loopAgain:
        arr[checkItem + 1] = arr[checkItem]
        checkItem = checkItem - 1
        if checkItem < 0:
            loopAgain = False
        elif arr[checkItem] <= lastItem:
            loopAgain = False
    arr[checkItem + 1] = lastItem
    return arr
```

### 二分查找（迭代）
```python
def BinarySearch(arr, n, target):
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return -1
```

### 二分查找（递归）
```python
def BinarySearchRecursive(arr, first, last, target):
    if first > last:
        return -1
    mid = (first + last) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return BinarySearchRecursive(arr, first, mid - 1, target)
    else:
        return BinarySearchRecursive(arr, mid + 1, last, target)
```

### 线性队列
```python
Queue = [""] * 20
QueueHead = -1
QueueTail = -1

def Enqueue(data):
    global Queue, QueueHead, QueueTail
    if QueueTail == 19:
        return False
    if QueueHead == -1:
        QueueHead = 0
    QueueTail = QueueTail + 1
    Queue[QueueTail] = data
    return True

def Dequeue():
    global Queue, QueueHead, QueueTail
    if QueueHead < 0 or QueueHead > QueueTail:
        return "false"
    item = Queue[QueueHead]
    QueueHead = QueueHead + 1
    return item
```

### 循环队列
```python
Queue = [-1] * 20
HeadPointer = -1
TailPointer = -1
NumberItems = 0

def Enqueue(item):
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems == 20:
        return False
    if HeadPointer == -1:
        HeadPointer = 0
    TailPointer = (TailPointer + 1) % 20
    Queue[TailPointer] = item
    NumberItems = NumberItems + 1
    return True

def Dequeue():
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems == 0:
        return -1
    item = Queue[HeadPointer]
    HeadPointer = (HeadPointer + 1) % 20
    NumberItems = NumberItems - 1
    return item
```

### 栈
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

### 链表遍历
```python
def OutputNodes(linkedList, startPointer):
    current = startPointer
    while current != -1:
        print(linkedList[current].data)
        current = linkedList[current].nextNode
```

### 链表插入
```python
def AddNode(linkedList, startPointer, emptyList):
    data = int(input("Enter data: "))
    if emptyList == -1:
        return False, startPointer, emptyList
    newNode = emptyList
    emptyList = linkedList[emptyList].nextNode
    linkedList[newNode].data = data
    linkedList[newNode].nextNode = -1
    if startPointer == -1:
        startPointer = newNode
    else:
        current = startPointer
        while linkedList[current].nextNode != -1:
            current = linkedList[current].nextNode
        linkedList[current].nextNode = newNode
    return True, startPointer, emptyList
```

### 中序递归遍历
```python
def InOrder(nodeIndex):
    global ArrayNodes
    if nodeIndex == -1:
        return
    InOrder(ArrayNodes[nodeIndex][0])
    print(ArrayNodes[nodeIndex][1])
    InOrder(ArrayNodes[nodeIndex][2])
```

### OOP 类模板
```python
class ClassName:
    def __init__(self, param1, param2):
        self.__Attr1 = param1
        self.__Attr2 = param2

    def GetAttr1(self):
        return self.__Attr1

    def SetAttr1(self, value):
        self.__Attr1 = value
```

### OOP 继承
```python
class Parent:
    def __init__(self, p1):
        self.__P1 = p1

class Child(Parent):
    def __init__(self, p1, p2):
        super().__init__(p1)
        self.__P2 = p2
```

### 文件读取
```python
def ReadFile(filename):
    try:
        f = open(filename, 'r')
        lines = f.read().splitlines()
        f.close()
        return lines
    except:
        print("File not found")
        return []
```

### 文件写入
```python
def WriteFile(filename, data):
    try:
        f = open(filename, 'w')
        for i in range(len(data)):
            f.write(str(data[i]) + "\n")
        f.close()
    except:
        print("Error writing file")
```

### 哈希表
```python
def CalculateHash(key):
    return key % 200

def InsertIntoHash(record):
    h = CalculateHash(record.GetKey())
    if HashTable[h].GetKey() == -1:
        HashTable[h] = record
    else:
        for i in range(100):
            if Spare[i].GetKey() == -1:
                Spare[i] = record
                break
```

### 递归模板
```python
def RecursiveFunc(n):
    if base_condition:
        return base_value
    else:
        return RecursiveFunc(smaller_n)
```

## 时间分配表

| 阶段 | 时间 | 任务 |
|------|------|------|
| 浏览题目 | 5 min | 了解 3 道题要求 |
| Q1 | 45 min | 完成 + 截图 |
| Q2 | 50 min | 完成 + 截图 |
| Q3 | 40 min | 完成 + 截图 |
| 检查 | 10 min | 截图全部保存 |

## 卡住时的对策

| 情况 | 对策 |
|------|------|
| 函数不返回 | 检查所有分支都有 return |
| 数组越界 | 检查 `range(n)` 不是 `range(n+1)` |
| 无限循环 | while 条件最终会变 False |
| 全局变量不更新 | 函数内加 `global` |
| OOP 报错 | 方法第一个参数是 `self` |
| 递归溢出 | 检查 base case |
| 二分查找不对 | 确认数组已排序 |
| 队列不对 | 检查指针语义 |
| 哈希表不对 | 检查 MOD 和碰撞处理 |

## 交卷前检查清单

- [ ] 所有程序文件按要求命名
- [ ] 所有代码已复制到 evidence document
- [ ] 所有测试截图已粘贴
- [ ] evidence document 已保存
- [ ] 每道题所有子问题都已作答
