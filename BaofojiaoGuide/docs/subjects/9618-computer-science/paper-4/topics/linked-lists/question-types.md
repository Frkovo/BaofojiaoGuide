---
title: 题型分析
sidebar_position: 2
---

# 题型分析

## Question Type 1: Declare Node Type and Array（2-4 分）

### 如何识别
要求声明链表节点类型（data + nextNode）和初始化数组。

:::note[标准解题方法]
1. 用 `class node:` 定义节点类型
2. 声明长度为 N 的数组 `linkedList = [node() for _ in range(N)]`
3. 根据题目表格初始化每个节点的 data 和 nextNode
4. 声明 `startPointer` 和 `emptyList` 指针
:::

**Example 1 — 9618/s21/qp/41 Q1(a)(b):**

> TYPE node: DECLARE data: INTEGER, DECLARE nextNode: INTEGER
> Declare a 1D array of type node with identifier linkedList with 10 elements.

## Question Type 2: Traverse and Output（6 分）

### 如何识别
要求遍历链表并输出每个节点的数据。

:::note[标准解题方法]
1. 从 startPointer 开始
2. 不断跟随 nextNode
3. 直到遇到 -1 停止
4. 每次输出当前节点的 data
:::

:::info[评分标准]
**M1**: 过程头，参数为数组和 startPointer
**M1**: 从 startPointer 开始
**M1**: 循环条件为 current != -1
**M1**: 输出 data
**M1**: 更新 current = linkedList[current].nextNode
**A1**: 正确遍历
:::

**Example 1 — 9618/s21/qp/41 Q1(c):**

> The procedure outputNodes() takes the array and startPointer as parameters and outputs data.

## Question Type 3: Insert Node at End（7 分）

### 如何识别
要求从用户输入数据，插入到链表末尾。

:::note[标准解题方法]
1. 检查 emptyList == -1（空闲链表满）则返回 False
2. 从 emptyList 取出新节点
3. 更新 emptyList 指向下一个空闲节点
4. 设置新节点的 data 和 nextNode = -1
5. 如果链表为空（startPointer == -1），新节点成为头节点
6. 否则遍历到末尾，更新末尾节点的 nextNode
7. 返回 True, 更新后的 startPointer 和 emptyList
:::

**Example 1 — 9618/s21/qp/41 Q1(d):**

> The function addNode() takes the linked list and pointers, adds a node at the end.

## Question Type 4: Find Node（4-5 分）

### 如何识别
要求在链表中查找包含特定数据的节点。

:::note[标准解题方法]
1. 从 startPointer 开始遍历
2. 如果当前节点的 data == target，返回当前索引
3. 否则继续跟随 nextNode
4. 如果遍历完没找到，返回 -1
:::

## Question Type 5: Delete Node（6-8 分）

### 如何识别
要求删除链表中包含特定数据的节点。

:::note[标准解题方法]
1. 检查空链表
2. 如果要删的是头节点：更新 startPointer，把原头节点归还空闲链表
3. 否则遍历找到目标节点的前一个节点
4. 跳过目标节点：previous.nextNode = target.nextNode
5. 将目标节点归还空闲链表
6. 返回 True/False
:::
