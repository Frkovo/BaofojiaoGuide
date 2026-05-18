---
title: 解题方法
sidebar_position: 3
---

# 解题方法

## 递归遍历通用模板

三种遍历方式的区别仅在于 `OUTPUT` 语句的位置:

```
PROCEDURE Traverse(ByVal NodeIndex : INTEGER)
    IF NodeIndex = -1 THEN       // Base case: 空节点
        RETURN
    ENDIF

    // In-order:  左 → 输出 → 右
    CALL Traverse(LeftSubtree)   // 1. 递归左子树
    OUTPUT NodeData              // 2. 输出当前节点
    CALL Traverse(RightSubtree)  // 3. 递归右子树

    // Pre-order:  输出 → 左 → 右
    OUTPUT NodeData              // 1. 输出当前节点
    CALL Traverse(LeftSubtree)   // 2. 递归左子树
    CALL Traverse(RightSubtree)  // 3. 递归右子树

    // Post-order: 左 → 右 → 输出
    CALL Traverse(LeftSubtree)   // 1. 递归左子树
    CALL Traverse(RightSubtree)  // 2. 递归右子树
    OUTPUT NodeData              // 3. 输出当前节点
ENDPROCEDURE
```

## 2D Array 实现 (w21_qp_41 题型)

```
DECLARE Tree : ARRAY[0:9, 0:2] OF INTEGER
// Tree[i][0] = Data, Tree[i][1] = Left, Tree[i][2] = Right
// -1 表示空节点

PROCEDURE InOrder(ByVal Index : INTEGER)
    IF Index <> -1 THEN
        CALL InOrder(Tree[Index][1])    // 左子树
        OUTPUT Tree[Index][0]           // 输出 Data
        CALL InOrder(Tree[Index][2])    // 右子树
    ENDIF
ENDPROCEDURE

// 主程序调用
CALL InOrder(RootPointer)
```

**关键要点**:
- `RootPointer` 存储根节点的数组行索引
- `Tree[Index][1]` 是左子节点索引, `Tree[Index][2]` 是右子节点索引
- Base case: `Index = -1` 时停止 (空节点)
- 递归过程不修改数组, 仅读取

## OOP 实现 (s25_qp_41 题型)

```
CLASS TreeNode
    PRIVATE Data : INTEGER
    PRIVATE Left : TreeNode
    PRIVATE Right : TreeNode

    PUBLIC FUNCTION GetData() RETURNS INTEGER
        RETURN Data
    ENDFUNCTION

    PUBLIC FUNCTION GetLeft() RETURNS TreeNode
        RETURN Left
    ENDFUNCTION

    PUBLIC FUNCTION GetRight() RETURNS TreeNode
        RETURN Right
    ENDFUNCTION
ENDCLASS

// 递归遍历过程
PROCEDURE InOrder(ByVal CurrentNode : TreeNode)
    IF CurrentNode <> NULL THEN
        CALL InOrder(CurrentNode.GetLeft())
        OUTPUT CurrentNode.GetData()
        CALL InOrder(CurrentNode.GetRight())
    ENDIF
ENDPROCEDURE

// 主程序调用
CALL InOrder(RootNode)
```

**关键要点**:
- 参数类型为 `TreeNode` (对象引用), 而非 `INTEGER`
- Base case: `CurrentNode = NULL` (而非 `-1`)
- 通过 Getter 方法访问属性 (遵循封装原则)
- 若题目使用 `LeftPointer` / `RightPointer` INTEGER 索引, 则参数类型为 `INTEGER`

## 方法速查

| 步骤 | 2D Array 写法 | OOP 写法 |
|------|--------------|---------|
| 参数 | `Index : INTEGER` | `Node : TreeNode` |
| Base case | `IF Index = -1 THEN RETURN` | `IF Node = NULL THEN RETURN` |
| 左递归 | `CALL InOrder(Tree[Index][1])` | `CALL InOrder(Node.GetLeft())` |
| 输出 | `OUTPUT Tree[Index][0]` | `OUTPUT Node.GetData()` |
| 右递归 | `CALL InOrder(Tree[Index][2])` | `CALL InOrder(Node.GetRight())` |
| 首次调用 | `CALL InOrder(RootPointer)` | `CALL InOrder(RootNode)` |
