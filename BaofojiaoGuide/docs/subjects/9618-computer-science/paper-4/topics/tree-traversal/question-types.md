---
title: 题型分析
sidebar_position: 2
---

# 题型分析

## Q1: Recursive In-order Traversal on 2D Array (7 marks)

**题目识别**: 二叉树用二维数组存储, `Tree[][0]` = Data, `Tree[][1]` = Left, `Tree[][2]` = Right, 要求编写递归过程进行中序遍历

**标准解法**:
1. 定义递归过程 `InOrder(ByVal Index : INTEGER)`
2. Base case: `IF Index = -1 THEN RETURN`
3. 递归左子树: `CALL InOrder(Tree[Index][1])`
4. 输出当前节点: `OUTPUT Tree[Index][0]`
5. 递归右子树: `CALL InOrder(Tree[Index][2])`
6. 主程序调用: `CALL InOrder(RootPointer)`

**评分标准模式**:

<details>
<summary>MS 示例</summary>

**M1** 正确定义递归过程, 接受索引参数

**A1** Base case 正确: `IF Index = -1 THEN RETURN` (或 `IF Index <> -1 THEN` 包裹)

**A1** 递归调用左子树: `CALL InOrder(Tree[Index][1])`

**A1** 输出当前节点数据: `OUTPUT Tree[Index][0]`

**A1** 递归调用右子树: `CALL InOrder(Tree[Index][2])`

**M1** 主程序从根节点开始调用: `CALL InOrder(RootPointer)`

**A1** 递归逻辑完整正确 (顺序不能错)

</details>

**真题示例**:

- **9618/w21/qp/41 Q3(e)**: 给定 `Tree` 二维数组 (10×3), `RootPointer = 4`, 编写递归过程 `InOrder` 输出节点数据, 7 marks. 数组结构: `[Data, Left, Right]`, -1 表示空

**陷阱**:
- 用 `IF Index <> -1 THEN` 包裹而非 `IF Index = -1 THEN RETURN` — 两种写法均可但包裹写法不能有 ELSE 分支干扰
- 使用 `CALL InOrder(0)` 硬编码而非从 `RootPointer` 开始
- 混淆数组列索引: Data 是 `[0]`, Left 是 `[1]`, Right 是 `[2]`
- 忘记传递数组参数 (如果递归过程定义在类外部, 数组需作为参数传入)

---

## Q2: Recursive In-order Traversal on OOP Tree (5 marks)

**题目识别**: 二叉树用 OOP 实现, 有 `TreeNode` 类 (含 `GetData()`, `GetLeft()`, `GetRight()` 方法), 要求编写递归中序遍历

**标准解法**:
1. 定义递归过程 `InOrder(ByVal Node : TreeNode)` 或 `Traverse(ByVal CurrentPointer : INTEGER)`
2. Base case: `IF Node = NULL THEN RETURN` 或 `IF CurrentPointer = -1 THEN RETURN`
3. 递归左子树: `CALL InOrder(Node.GetLeft())`
4. 输出当前节点: `OUTPUT Node.GetData()`
5. 递归右子树: `CALL InOrder(Node.GetRight())`

**评分标准模式**:

<details>
<summary>MS 示例</summary>

**M1** 正确定义递归过程 (参数类型正确)

**A1** Base case 处理: `IF Node = NULL THEN RETURN` (或 null 检查)

**M1** 递归左子树调用: `CALL InOrder(Node.GetLeft())`

**A1** 正确输出节点数据: `OUTPUT Node.GetData()`

**A1** 递归右子树调用: `CALL InOrder(Node.GetRight())`

</details>

**真题示例**:

- **9618/s25/qp/41 Q3(d)**: OOP 二叉树, `TreeNode` 有 `GetData`, `GetLeft`, `GetRight` 方法, 编写递归 `TraverseInOrder`, 5 marks

**陷阱**:
- 参数类型错误: 传入 `INTEGER` 而非 `TreeNode` 引用 (取决于具体实现)
- Null 检查方式错误: 传入 `0` 而非 `NULL` (OOP 中用 `NULL` 而非 `-1`)
- 缺少 Getter 调用: 直接用 `Node.Data` 而非 `Node.GetData()` — 取决于封装级别
- 遍历顺序错: 如果题目要求 in-order 却写成 pre-order 或 post-order
