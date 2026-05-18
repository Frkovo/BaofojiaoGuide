---
title: Hash Tables
sidebar_position: 1
---

# Hash Tables（哈希表）

## 考纲要求

- 13.2 哈希算法：用 Key MOD TableSize 计算存储位置
- 碰撞处理：存入辅助数组 Spare

## 核心代码模板

```python
class NewRecord:
    def __init__(self):
        self.__Key = -1
        self.__Item1 = -1
        self.__Item2 = -1

    def GetKey(self):
        return self.__Key

    def SetKey(self, k):
        self.__Key = k

    def GetItem1(self):
        return self.__Item1

    def SetItem1(self, i):
        self.__Item1 = i

    def GetItem2(self):
        return self.__Item2

    def SetItem2(self, i):
        self.__Item2 = i

HashTable = [NewRecord() for _ in range(200)]
Spare = [NewRecord() for _ in range(100)]

def Initialise():
    global HashTable, Spare
    for i in range(200):
        HashTable[i] = NewRecord()
    for i in range(100):
        Spare[i] = NewRecord()

def CalculateHash(key):
    return key % 200

def InsertIntoHash(record):
    global HashTable, Spare
    hashVal = CalculateHash(record.GetKey())
    if HashTable[hashVal].GetKey() == -1:
        HashTable[hashVal] = record
    else:
        for i in range(100):
            if Spare[i].GetKey() == -1:
                Spare[i] = record
                break

def PrintSpare():
    global Spare
    for i in range(100):
        if Spare[i].GetKey() != -1:
            print(Spare[i].GetKey())

def CreateHashTable():
    global HashTable, Spare
    try:
        f = open("HashData.txt", 'r')
        lines = f.read().splitlines()
        f.close()
        for i in range(len(lines)):
            parts = lines[i].split(",")
            r = NewRecord()
            r.SetKey(int(parts[0]))
            r.SetItem1(int(parts[1]))
            r.SetItem2(int(parts[2]))
            InsertIntoHash(r)
    except:
        print("File not found")
```

## 常见错误

- 没有初始化数组为空记录（Key=-1）
- 碰撞时覆盖了原有数据（应该存到 Spare）
- MOD 运算写成 `/` 而不是 `%`
- 忘记把字符串转 int
