---
title: 考前速记
sidebar_position: 7
---

# 考前速记

## 结构速记

```
TYPE HashTableRecord
    HashTable[0:9] OF INTEGER            (空值 = -1)
    OverflowArray[1:10] OF INTEGER        (空值 = -1)
    OverflowPointer : INTEGER             (初始 = 1)
ENDTYPE
```

## CalculateHash 速记

```
FUNCTION CalculateHash(Key)
    RETURN Key MOD 10
ENDFUNCTION
```

**Key MOD TableSize** — 不是 TableSize MOD Key!

## InsertIntoHash 速记

```
1. Index &lt;- CalculateHash(Value)
2. HashTable[Index] = -1 ?
   是 -> HashTable[Index] &lt;- Value
   否 -> OverflowArray[OverflowPtr] &lt;- Value
         OverflowPtr &lt;- OverflowPtr + 1  ← 千万别忘!
```

## 初始化速记

```
FOR Count &lt;- 0 TO 9
    HashTable[Count] &lt;- -1
NEXT Count
FOR Count &lt;- 1 TO 10
    OverflowArray[Count] &lt;- -1
NEXT Count
OverflowPointer &lt;- 1
```

## 变量对照速记

| 变量 | 初始值 | 含义 |
|------|--------|------|
| `HashTable[i]` | `-1` | 主表, `-1` = 空 |
| `OverflowArray[i]` | `-1` | 溢出数组, `-1` = 空 |
| `OverflowPointer` | `1` | 下一个可用 overflow 位置 |

:::note[考试当天]
**口诀**: Key MOD 表大小, 主表空了放主表, 主表满了放溢出, 放了溢出递指针

**CalculateHash**: 记住是 `Key MOD Size`, 不是 `Size MOD Key`!

**InsertIntoHash**: 先调函数算下标, 再看主表空不空, 碰撞数据放溢出, 指针递增不能忘!

**别忘了**: 数组要初始化 (全设 `-1`), overflow 指针要递增, `ByRef` 才能改数据
:::

## 扣分重灾区

```
M1 丢失: 没有调用 CalculateHash 函数
A1 丢失: MOD 运算方向错误 (Size MOD Key)
A1 丢失: 碰撞处理逻辑反了 (先 overflow 再主表)
A1 丢失: OverflowPointer 忘记递增
A1 丢失: 哈希表/overflow 数组未初始化
```

## 一句话箴言

> **Key MOD Size 算下标, 主表空就放主表, 碰撞溢出放数组, 指针递增别忘掉**
