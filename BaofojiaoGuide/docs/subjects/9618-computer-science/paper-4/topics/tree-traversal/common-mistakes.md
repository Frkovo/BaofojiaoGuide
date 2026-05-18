---
title: 常见错误
sidebar_position: 5
---

# 常见错误

## 错误 1: 缺少 Base Case (无限递归)

**错误表现**:
```
PROCEDURE InOrder(Index)
    CALL InOrder(Tree[Index][1])
    OUTPUT Tree[Index][0]
    CALL InOrder(Tree[Index][2])
ENDPROCEDURE
```

**后果**: 当 `Index = -1` 时依然递归, 访问 `Tree[-1]` 导致数组越界 → runtime error

**正解**: 每次进入递归先检查空节点:
```
IF Index = -1 THEN RETURN
```

## 错误 2: 遍历顺序混淆

**错误表现**: 题目要求 in-order (左根右), 写成 pre-order (根左右) 或 post-order (左右根)

**正解**:
- In-order: 左递归 → OUTPUT → 右递归
- Pre-order: OUTPUT → 左递归 → 右递归
- Post-order: 左递归 → 右递归 → OUTPUT

**记忆口诀**: "左根右是 in-order, 根左右是 pre-order, 左右根是 post-order"

## 错误 3: 2D Array 列索引错误

**错误表现**:
```
OUTPUT Tree[Index][1]   // 写成了 Left 列
CALL InOrder(Tree[Index][0])  // 写成了 Data 列
```

**正解**: 明确数组列含义 — `Tree[Index][0]` = Data, `Tree[Index][1]` = Left, `Tree[Index][2]` = Right

## 错误 4: OOP 中 Null 检查错误

**错误表现**:
```
IF CurrentNode <> -1 THEN   // 用 -1 而非 NULL 检查对象
```

**正解**: 对象引用使用 `NULL`, 数组索引使用 `-1`
```
IF CurrentNode <> NULL THEN
```

## 错误 5: OOP 中直接访问私有属性

**错误表现**:
```
OUTPUT CurrentNode.Data     // Data 是 PRIVATE
```

**正解**: 使用 Getter 方法访问:
```
OUTPUT CurrentNode.GetData()
```

## 错误 6: 硬编码起始索引而非使用 RootPointer

**错误表现**:
```
CALL InOrder(0)             // 假设根总是在 0
```

**正解**:
```
CALL InOrder(RootPointer)   // 从根节点开始
```

## 错误 7: 递归参数错误 (传值而非传引用)

**错误表现**: 在递归过程中修改了参数值, 导致回溯时参数错误

**正解**: 递归参数应作为输入值, 不在过程中修改

## 错误 8: 混淆 IF 包裹 vs IF RETURN

**两种写法均可, 但易犯错误**:
```
// 写法 A (推荐): 先检查空节点再执行
IF Index = -1 THEN RETURN
// 执行递归逻辑

// 写法 B: 用条件包裹
IF Index <> -1 THEN
    // 递归逻辑
ENDIF
```

**注意**: 写法 B 中不能有 ELSE 分支干扰主逻辑
