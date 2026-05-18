---
title: 解题方法
sidebar_position: 3
---

# 解题方法

## Binary Tree with Array — 完整实现方法

### Step 1: 声明 TreeNode Class

```
CLASS TreeNode
    PRIVATE Data : INTEGER
    PRIVATE LeftPointer : INTEGER
    PRIVATE RightPointer : INTEGER

    PUBLIC CONSTRUCTOR(ByVal NewData : INTEGER)
        Data &lt;- NewData
        LeftPointer &lt;- -1
        RightPointer &lt;- -1
    ENDCONSTRUCTOR

    PUBLIC FUNCTION GetData() RETURNS INTEGER
        RETURN Data
    ENDFUNCTION

    PUBLIC PROCEDURE SetLeft(ByVal NewLeft : INTEGER)
        LeftPointer &lt;- NewLeft
    ENDPROCEDURE

    PUBLIC FUNCTION GetLeft() RETURNS INTEGER
        RETURN LeftPointer
    ENDFUNCTION

    PUBLIC PROCEDURE SetRight(ByVal NewRight : INTEGER)
        RightPointer &lt;- NewRight
    ENDPROCEDURE

    PUBLIC FUNCTION GetRight() RETURNS INTEGER
        RETURN RightPointer
    ENDFUNCTION
ENDCLASS
```

**要点**:
- `$Data$` 可以为 INTEGER 或 STRING, 视题目要求
- `$LeftPointer$` 和 `$RightPointer$` 存储数组下标, `$-1$` 表示无子节点
- Getter/Setter 方法封装数据访问 (题目可能要求或不需要)

### Step 2: 声明 TreeClass

```
CLASS BinaryTree
    PRIVATE Tree : ARRAY[0:MaxNodes-1] OF TreeNode
    PRIVATE RootPointer : INTEGER
    PRIVATE FreePointer : INTEGER

    PUBLIC CONSTRUCTOR()
        DECLARE Count : INTEGER
        RootPointer &lt;- -1
        FreePointer &lt;- 0
        FOR Count &lt;- 0 TO MaxNodes - 1
            Tree[Count] &lt;- NEW TreeNode(0)
        NEXT Count
    ENDCONSTRUCTOR

    PUBLIC PROCEDURE InsertNode(ByVal NewData : INTEGER)
        ...
    ENDPROCEDURE

    PUBLIC PROCEDURE OutputTree()
        CALL RecursiveOutput(RootPointer)
    ENDPROCEDURE

    PRIVATE PROCEDURE RecursiveOutput(ByVal CurrentPointer : INTEGER)
        ...
    ENDPROCEDURE
ENDCLASS
```

**要点**:
- `$RootPointer$` 指向根节点在数组中的下标, `$-1$` 表示空树
- `$FreePointer$` 追踪下一个可用位置, 新节点放入 `$Tree[FreePointer]$` 后 `$FreePointer$` 递增
- 或者用 `$NextFreePointer$` 管理空闲节点

### Step 3: InsertNode 算法

```
PUBLIC PROCEDURE InsertNode(ByVal NewData : INTEGER)
    DECLARE NewNode : INTEGER
    DECLARE CurrentPointer : INTEGER

    NewNode &lt;- FreePointer
    FreePointer &lt;- FreePointer + 1
    Tree[NewNode] &lt;- NEW TreeNode(NewData)

    IF RootPointer = -1 THEN
        RootPointer &lt;- NewNode
    ELSE
        CurrentPointer &lt;- RootPointer
        WHILE TRUE
            IF NewData < Tree[CurrentPointer].GetData() THEN
                IF Tree[CurrentPointer].GetLeft() = -1 THEN
                    CALL Tree[CurrentPointer].SetLeft(NewNode)
                    EXIT WHILE
                ELSE
                    CurrentPointer &lt;- Tree[CurrentPointer].GetLeft()
                ENDIF
            ELSE
                IF Tree[CurrentPointer].GetRight() = -1 THEN
                    CALL Tree[CurrentPointer].SetRight(NewNode)
                    EXIT WHILE
                ELSE
                    CurrentPointer &lt;- Tree[CurrentPointer].GetRight()
                ENDIF
            ENDIF
        ENDWHILE
    ENDIF
ENDPROCEDURE
```

**关键检查点**:
- 空树处理: `$RootPointer = -1$` 时新节点成为根
- 比较方向: `$NewData < Current.Data$` 走左, `$>=`$ 走右
- 空位判断: 子指针为 `$-1$` 时插入, 否则继续遍历
- 父节点指针更新: 插入后必须更新父节点的 `$LeftPointer$` 或 `$RightPointer$`

### Step 4: OutputTree — In-order Traversal

```
PRIVATE PROCEDURE RecursiveOutput(ByVal CurrentPointer : INTEGER)
    IF CurrentPointer <> -1 THEN
        CALL RecursiveOutput(Tree[CurrentPointer].GetLeft())
        OUTPUT Tree[CurrentPointer].GetData()
        CALL RecursiveOutput(Tree[CurrentPointer].GetRight())
    ENDIF
ENDPROCEDURE
```

**遍历顺序**:
- In-order: left → root → right (输出升序)
- Pre-order: root → left → right
- Post-order: left → right → root

**关键检查点**:
- Base case: `$CurrentPointer = -1$` 时返回 (停止递归)
- 递归左子树: 先处理所有左子节点
- 输出: 在左右递归之间输出当前节点值
- 递归右子树: 最后处理所有右子节点

### Step 5: 主程序

```
DECLARE TreeObj : BinaryTree
DECLARE Choice : INTEGER
DECLARE InputValue : INTEGER

TreeObj &lt;- NEW BinaryTree()
REPEAT
    OUTPUT "1. Insert a number"
    OUTPUT "2. Output tree (in-order)"
    OUTPUT "3. Exit"
    INPUT Choice
    IF Choice = 1 THEN
        INPUT InputValue
        CALL TreeObj.InsertNode(InputValue)
    ELSE IF Choice = 2 THEN
        CALL TreeObj.OutputTree()
    ENDIF
UNTIL Choice = 3
```

---

## 非 OOP 实现 (过程式)

若题目不要求 OOP, 可以使用全局数组和过程:

```
CONSTANT MaxNodes &lt;- 20
DECLARE TreeData : ARRAY[0:MaxNodes-1] OF INTEGER
DECLARE TreeLeft : ARRAY[0:MaxNodes-1] OF INTEGER
DECLARE TreeRight : ARRAY[0:MaxNodes-1] OF INTEGER
DECLARE RootPointer : INTEGER
DECLARE FreePointer : INTEGER
```

**初始化**:
- `$RootPointer \gets -1$`
- `$FreePointer \gets 0$`
- 所有 `$TreeLeft[i] \gets -1$`, `$TreeRight[i] \gets -1$`

插入和输出逻辑与 OOP 版本相同, 仅语法不同.

---

## 二叉树变量命名对照表

| 变量 | 常用名 | 说明 |
|------|--------|------|
| 节点数组 | Tree, BinaryTree, TreeNodeArray | 存储所有节点的数组 |
| 根指针 | RootPointer, Root | 指向根节点下标, -1 为空 |
| 空闲指针 | FreePointer, NextFree, NextFreePointer | 下一个可用的数组位置 |
| 节点数据 | Data, Item, Value | 节点存储的具体数据 |
| 左指针 | LeftPointer, Left, LPointer | 左子节点下标 |
| 右指针 | RightPointer, Right, RPointer | 右子节点下标 |
