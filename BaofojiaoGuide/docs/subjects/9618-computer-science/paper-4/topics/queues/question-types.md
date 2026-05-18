---
title: 题型分析
sidebar_position: 2
---

# 题型分析

## Question Type 1: Enqueue Implementation（4 分）

### 如何识别
要求实现入队函数，将数据插入队列末尾。

:::note[标准解题方法]
1. 检查队列是否已满（TailPointer >= 数组大小）
2. 满则返回 FALSE
3. 如果是第一个元素，设置 HeadPointer = 0
4. 在 TailPointer 位置插入数据
5. TailPointer 递增
6. 返回 TRUE
:::

:::info[评分标准]
**M1**: 函数头和参数
**M1**: 检查队列满
**M1**: 插入数据并更新指针
**M1**: 第一个元素特殊处理
:::

**Example 1 — 9618/s24/qp/41 Q3(b):**

> The function Enqueue() takes the data to insert into the queue as a parameter.
> If the queue is not full, it inserts the parameter, updates the pointers and returns TRUE.

**Example 2 — 9618/w23/qp/41 Q2(a)(ii):**

> The procedure Enqueue() takes a string parameter and inserts it into the queue.

:::warning[常见陷阱]
注意 TailPointer 指向的是"下一个空位"还是"最后一个元素"。题目定义不同，实现不同。
:::

## Question Type 2: Dequeue Implementation（3 分）

### 如何识别
要求实现出队函数，移除并返回队列的第一个元素。

:::note[标准解题方法]
1. 检查队列是否为空（HeadPointer == -1 or HeadPointer >= TailPointer）
2. 空则返回 "false" 或 "Empty"
3. 取出 HeadPointer 位置的元素
4. HeadPointer 递增
5. 返回取出的元素
:::

**Example 1 — 9618/s24/qp/41 Q3(c):**

> The function Dequeue() returns "false" if the queue is empty. Otherwise returns next item.

:::warning[常见陷阱]
出队后不需要清空原位置的元素，只需移动指针即可。
:::

## Question Type 3: Queue with Data Validation（6 分）

### 如何识别
入队前需要进行数据验证（如 check digit 计算），只将有效数据入队。

:::note[标准解题方法]
1. 循环 10 次读取输入
2. 解析字符串前 6 位数字
3. 按规则计算 check digit
4. 与第 7 位比较
5. 有效则调用 Enqueue
6. 统计无效输入数量
:::

**Example 1 — 9618/s24/qp/41 Q3(d):**

> StoreItems() takes ten 7-character strings, validates each using check digit, stores valid ones in queue, counts invalid ones.
