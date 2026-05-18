---
title: 题型分析
sidebar_position: 2
---

# 题型分析

## Question Type 1: Node Class with Constructor（4 分）

### 如何识别
要求声明一个类（通常是 Node），包含左指针、数据和右指针三个私有属性以及构造器。

:::note[标准解题方法]
1. 用 `class Node:` 声明类
2. 在 `__init__` 中声明私有属性 `self.__LeftPointer`, `self.__Data`, `self.__RightPointer`
3. 构造器接受数据参数
4. LeftPointer 和 RightPointer 初始化为 -1，Data 初始化为参数值
:::

:::info[评分标准]
**M1**: 类声明
**M1**: 三个私有属性
**M1**: 构造器头含参数
**M1**: 参数赋值 + 指针初始化为 -1
:::

**Example 1 — 9618/s24/qp/42 Q2(a)(i):**

> The class Node stores data about a node with LeftPointer, Data and RightPointer attributes.
> Constructor initialises Data to its parameter value and LeftPointer and RightPointer to -1.
> Write program code to declare the class Node and its constructor.

:::warning[常见陷阱]
Python 中私有属性用 `self.__` 双下划线，不是单下划线。
:::

## Question Type 2: TreeClass with Constructor（4 分）

### 如何识别
要求声明一个 TreeClass，包含 Node 数组、FirstNode 和 NumberNodes。

:::note[标准解题方法]
1. 声明 `self.__Tree = []` 并预填充 20 个 Node(-1)
2. `self.__FirstNode = -1`
3. `self.__NumberNodes = 0`
:::

**Example 1 — 9618/s24/qp/42 Q2(b)(i):**

> The class TreeClass stores the binary tree data in a 1D array of Node objects.

## Question Type 3: InsertNode Method（6 分）

### 如何识别
要求在二叉树中插入新节点，维护二叉搜索树性质。

:::note[标准解题方法]
1. 检查空树 → 直接设为根节点
2. 将新节点存入数组末尾
3. 从根节点开始遍历
4. 比较大小决定方向（小→左，大→右）
5. 更新父节点指针
6. NumberNodes += 1
:::

**Example 1 — 9618/s24/qp/42 Q2(b)(ii):**

> InsertNode() takes a Node object as a parameter and inserts it into the array Tree.

## Question Type 4: OutputTree Method（4 分）

### 如何识别
要求输出二叉树中所有节点的左指针、数据和右指针。

:::note[标准解题方法]
1. 检查空树 → 输出 "No nodes"
2. 循环遍历 0 到 NumberNodes-1
3. 用 getter 获取并输出 LeftPointer, Data, RightPointer
:::

**Example 1 — 9618/s24/qp/42 Q2(b)(iii):**

> OutputTree() outputs the left pointer, data and right pointer for each node that has been inserted.
