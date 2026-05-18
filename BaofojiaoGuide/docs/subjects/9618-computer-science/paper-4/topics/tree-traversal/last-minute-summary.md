---
title: 考前速记
sidebar_position: 7
---

# 考前速记

## 遍历口诀

```
In-order:  左 → 输出 → 右   (BST 升序)
Pre-order: 输出 → 左 → 右   (根最先)
Post-order:左 → 右 → 输出   (根最后)
```

## 递归模板速记

```
IF 空节点 THEN RETURN
左递归
输出           ← 位置决定遍历类型
右递归
```

## 2D Array 写法速记

```
PROCEDURE InOrder(Index)
    IF Index <> -1 THEN
        CALL InOrder(Tree[Index][1])   // 左 [1]
        OUTPUT Tree[Index][0]           // 数据 [0]
        CALL InOrder(Tree[Index][2])   // 右 [2]
    ENDIF
ENDPROCEDURE

CALL InOrder(RootPointer)
```

## OOP 写法速记

```
PROCEDURE InOrder(Node)
    IF Node <> NULL THEN
        CALL InOrder(Node.GetLeft())
        OUTPUT Node.GetData()
        CALL InOrder(Node.GetRight())
    ENDIF
ENDPROCEDURE

CALL InOrder(RootNode)
```

## 数组列索引速记

| 列 | 含义 |
|----|------|
| `[0]` | Data |
| `[1]` | Left |
| `[2]` | Right |

## Null 表示速记

| 实现方式 | 空节点表示 |
|----------|-----------|
| 2D Array | `-1` |
| OOP | `NULL` |

:::note[考试当天]

**检查清单**:
- Base case 写了吗？(无 base case → 无限递归 → **M1** 丢失)
- 遍历顺序对吗？(中序: 左→输出→右)
- 列索引用对了吗？(`[0]` Data, `[1]` Left, `[2]` Right)
- 从 `RootPointer` 开始调用？(不是硬编码 `0`)
- OOP 用 Getter 了吗？(不要直接访问私有属性)
- OOP 用 `NULL` 了吗？(不要用 `-1` 检查对象)

**一句话**: 递归遍历三步走 — 左递归, 输出, 右递归; 顺序错了全白给

:::

## 扣分重灾区

```
M1 丢失: 没有 base case
A1 丢失: 遍历顺序错了 (in-order ↔ pre-order)
A1 丢失: 2D array 列索引用错
A1 丢失: OOP 没用 Getter / 用了 -1 而非 NULL
M1 丢失: 没从 RootPointer 开始调用
```

## 一句话箴言

> **空则返, 左递归, 输数据, 右递归 — in-order 就是左根右**
