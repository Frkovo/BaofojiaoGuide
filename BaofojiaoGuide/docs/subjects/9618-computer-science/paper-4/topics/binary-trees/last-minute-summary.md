---
title: 考前速记
sidebar_position: 7
---

# 考前速记

## 结构速记

```
TreeNode: [Data] [Left -> -1] [Right -> -1]
TreeClass: RootPointer = -1 (空树)
               Tree[0:MaxNodes-1] OF TreeNode
               FreePointer = 0
```

## InsertNode 速记

```
1. 新节点 &lt;- FreePointer; FreePointer++
2. IF RootPointer = -1 -> RootPointer &lt;- 新节点; 结束
3. CurrentPointer &lt;- RootPointer
4. 循环:
   Value < Current.Data? -> 左, 否则 -> 右
   子 = -1? -> 插入, 退出
   否则 -> CurrentPointer &lt;- 子, 继续
```

**小左大右** — 比 Data 小向左走, 比 Data 大 (含等于) 向右走

## OutputTree (In-order) 速记

```
IF CurrentPointer = -1 THEN RETURN
左递归 -> 输出 -> 右递归
```

**In-order = 左根右** (输出升序)
**Pre-order = 根左右**
**Post-order = 左右根**

## TreeNode Class 速记

```
CLASS TreeNode
    Data : INTEGER
    LeftPointer : INTEGER  (= -1)
    RightPointer : INTEGER (= -1)
    CONSTRUCTOR(NewData)
        Data &lt;- NewData
        LeftPointer &lt;- -1
        RightPointer &lt;- -1
```

## 指针指向速记

| 指针 | 初始值 | 含义 |
|------|--------|------|
| `RootPointer` | `-1` | `-1` = 空树 |
| `FreePointer` | `0` | 下一个可用位置 |
| `LeftPointer` | `-1` | `-1` = 无左子 |
| `RightPointer` | `-1` | `-1` = 无右子 |

:::note[考试当天]
**口诀**: 指针为空永远是 `-1`, 不是 `0`!

**Insert**: 小左大右, 找到空位插进去, 别忘了更新父节点指针

**Output**: 先左, 再自己, 再右 — 这是 in-order; 顺序错 = pre-order 分

**别忘了**: `RootPointer = -1` 空树特判, `FreePointer` 要递增, `=` 比较 `&lt;-` 赋值
:::

## 扣分重灾区

```
M1 丢失: 没有 base case (OutputTree)
A1 丢失: 比较方向反了 (小右大左)
A1 丢失: 插入后未更新父节点指针
A1 丢失: 忘记 FreePointer++
A1 丢失: 忘记处理空树
```

## 一句话箴言

> **小左大右, 空树特判, 指针-1, 左根右出**

