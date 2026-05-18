---
title: 评分标准模式
sidebar_position: 4
---

# 评分标准模式

## 2D Array Recursive In-order 通用评分标准 (7 marks)

<details>
<summary>MS 逐项解析</summary>

**M1** — 正确定义递归过程, 接收 `INTEGER` 索引参数:
```
PROCEDURE InOrder(ByVal Index : INTEGER)
```

**A1** — Base case 正确处理:
```
IF Index = -1 THEN
    RETURN
ENDIF
```
或使用 `IF Index <> -1 THEN` 包裹递归体

**A1** — 递归调用左子树:
```
CALL InOrder(Tree[Index][1])
```

**A1** — 输出当前节点数据:
```
OUTPUT Tree[Index][0]
```

**A1** — 递归调用右子树:
```
CALL InOrder(Tree[Index][2])
```

**M1** — 主程序从根节点调用:
```
CALL InOrder(RootPointer)
```

**A1** — 递归逻辑无误 (左-输出-右顺序正确)

</details>

## OOP Recursive In-order 通用评分标准 (5 marks)

<details>
<summary>MS 逐项解析</summary>

**M1** — 正确定义递归过程, 参数类型为 `TreeNode` 或 `INTEGER` (视实现方式):
```
PROCEDURE InOrder(ByVal CurrentNode : TreeNode)
```

**A1** — Base case 正确:
```
IF CurrentNode = NULL THEN
    RETURN
ENDIF
```
或 `IF CurrentNode <> NULL THEN` 包裹

**M1** — 递归调用左子树 (通过 Getter):
```
CALL InOrder(CurrentNode.GetLeft())
```

**A1** — 正确输出节点数据:
```
OUTPUT CurrentNode.GetData()
```

**A1** — 递归调用右子树:
```
CALL InOrder(CurrentNode.GetRight())
```

</details>

## Pre-order / Post-order 评分标准 (4 marks)

<details>
<summary>MS 逐项解析</summary>

**M1** — 正确递归过程定义 + base case

**A1** — 在正确位置 `OUTPUT` (决定遍历类型)

**A1** — 递归左子树

**A1** — 递归右子树

**注意**: 如果要求 pre-order 但写了 in-order, 可能得 0 分 — OUTPUT 位置决定了遍历类型

</details>

## 常见扣分点

| 错误 | 扣分 |
|------|------|
| 缺少 base case (`Index = -1` 检查) | **M1** 丢失 |
| 递归调用顺序错误 (非 in-order) | **A1** 丢失 (但可能得 pre-order 分) |
| 2D array 列索引错误 (Data 写成 `[1]` 而非 `[0]`) | **A1** 丢失 |
| OOP 中直接用 `Node.Data` 而非 `Node.GetData()` | 取决于封装 — 若题中为 PRIVATE 则扣分 |
| 主程序调用时硬编码 `CALL InOrder(0)` 而非 `RootPointer` | **M1** 丢失 |
| 参数类型错误 (OOP 用 INTEGER 而非 TreeNode) | **M1** 丢失 |
| OOP 中用 `-1` 而非 `NULL` 做 null 检查 | 语法错误扣分 |
