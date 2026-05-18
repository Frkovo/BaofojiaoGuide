---
title: 解题方法
sidebar_position: 3
---

# 解题方法

## Hash Table with Overflow Array — 完整实现方法

### Step 1: 声明 Record 类型

```
TYPE HashTableRecord
    DECLARE HashTable : ARRAY[0:9] OF INTEGER
    DECLARE OverflowArray : ARRAY[1:10] OF INTEGER
    DECLARE OverflowPointer : INTEGER
ENDTYPE
```

**要点**:
- `HashTable` 为主表, 大小由 `TableSize` 决定 (通常用常量 `MaxSize`)
- `OverflowArray` 为溢出数组, 大小通常与主表相同或略大
- `OverflowPointer` 追踪 overflow 数组中下一个空闲位置, 初始为 `1` (或 `0`)
- 有些题目使用 `OverflowCount` 记录 overflow 中已有元素个数

### Step 2: 初始化哈希表

```
DECLARE MyHashTable : HashTableRecord
DECLARE Count : INTEGER

// 初始化主表: 空值通常为 -1 或 0 (视题目定义)
FOR Count &lt;- 0 TO 9
    MyHashTable.HashTable[Count] &lt;- -1
NEXT Count

// 初始化 overflow 数组
FOR Count &lt;- 1 TO 10
    MyHashTable.OverflowArray[Count] &lt;- -1
NEXT Count

MyHashTable.OverflowPointer &lt;- 1
```

**要点**:
- 空值标记: 通常用 `-1` 表示空 (若数据为正整数), 或用 `0` (若数据为正且 0 不作为有效键)
- 必须初始化所有元素, 不能只声明
- `OverflowPointer` 初始指向 overflow 数组的第一个位置

### Step 3: CalculateHash 函数

```
FUNCTION CalculateHash(ByVal Key : INTEGER) RETURNS INTEGER
    DECLARE Index : INTEGER
    Index &lt;- Key MOD 10     // 10 为 TableSize
    RETURN Index
ENDFUNCTION
```

**关键检查点**:
- `Key MOD TableSize` — 键 `MOD` 表大小, 不是 `TableSize MOD Key`
- 返回值范围: `0` 到 `TableSize - 1`
- 函数必须返回 INTEGER 类型
- 表大小通常为常量 (如 `ArrayLength`), 从上下文中获取

### Step 4: InsertIntoHash 过程

```
PROCEDURE InsertIntoHash(ByRef HTable : HashTableRecord, ByVal NewValue : INTEGER)
    DECLARE Index : INTEGER

    Index &lt;- CalculateHash(NewValue)

    IF HTable.HashTable[Index] = -1 THEN
        HTable.HashTable[Index] &lt;- NewValue
    ELSE
        HTable.OverflowArray[HTable.OverflowPointer] &lt;- NewValue
        HTable.OverflowPointer &lt;- HTable.OverflowPointer + 1
    ENDIF
ENDPROCEDURE
```

**关键检查点**:
- 先调用 `CalculateHash` 获取下标
- 检查主表对应位置是否为空 (`-1`)
- 空则放入主表, 不空则放入 overflow 数组
- **`OverflowPointer` 必须递增** — 这是最常见的踩分点
- `ByRef` 传递记录类型使得过程可以修改内容

### Step 5: 从文件创建哈希表

```
PROCEDURE LoadHashTableFromFile(ByRef HTable : HashTableRecord)
    DECLARE FileData : STRING
    DECLARE Value : INTEGER

    OpenFile("hashdata.txt", FileData)
    ReadFile(FileData, Value)
    WHILE NOT EOF(FileData)
        CALL InsertIntoHash(HTable, Value)
        ReadFile(FileData, Value)
    ENDWHILE
    CloseFile(FileData)
ENDPROCEDURE
```

**关键检查点**:
- 处理文件读取循环: 先读, 循环内插入后再读
- 每条记录都需要计算哈希并插入
- 使用 `EOF` 控制循环结束

### Step 6: 输出 Overflow 数组

```
PROCEDURE PrintOverflowArray(ByRef HTable : HashTableRecord)
    DECLARE Count : INTEGER

    FOR Count &lt;- 1 TO 10
        IF HTable.OverflowArray[Count] &lt;&gt; -1 THEN
            OUTPUT HTable.OverflowArray[Count]
        ENDIF
    NEXT Count
ENDPROCEDURE
```

**替代写法** (使用 `OverflowPointer` 控制范围):

```
FOR Count &lt;- 1 TO HTable.OverflowPointer - 1
    OUTPUT HTable.OverflowArray[Count]
NEXT Count
```

---

## 哈希表变量命名对照表

| 变量 | 常用名 | 说明 |
|------|--------|------|
| 主表 | HashTable, MainTable, Table | 存储键值对的数组 |
| 溢出数组 | OverflowArray, CollisionArray, Overflow | 存储碰撞元素的数组 |
| 溢出指针 | OverflowPointer, NextFreeOverflow, OFPtr | overflow 数组下一个空闲位置 |
| 表大小 | TableSize, MaxSize, Size | 哈希表大小 (MOD 运算的分母) |
| 哈希值 | Index, HashIndex, Location | `Key MOD TableSize` 的结果 |
| 空标记 | EmptyFlag, NullValue | 表示空位的值, 通常为 `-1` |
