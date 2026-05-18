---
title: 教学大纲要点
---

# Section 19: Computational Thinking and Algorithms

## 19.1 Computational Thinking

### Decomposition（分解）
- 将复杂问题分解为更小、更易管理的子问题

### Pattern Recognition（模式识别）
- 识别问题中的模式和趋势
- 利用已知解决方案处理类似问题

### Abstraction（抽象）
- 关注重要细节，忽略不相关的信息
- 使用 models 和 representations

### Algorithm Design（算法设计）
- 逐步设计解决方案
- 使用 pseudocode 或 flowchart 表达

## 19.2 Algorithms

### 搜索算法

**Linear Search**
- 从第一个元素开始逐个比较
- 时间复杂度：**O(n)**
- 优点：不需要排序
- 缺点：大数据集效率低

**Binary Search**
- 需要已排序的数据
- 每次比较将搜索范围减半
- 时间复杂度：**O(log n)**

### 排序算法

**Bubble Sort**
- 重复扫描数组，比较相邻元素并交换
- 每轮将最大/最小值移动到正确位置
- 时间复杂度：**O(n²)**

**Insertion Sort**
- 将数组分为已排序和未排序两部分
- 每次从未排序部分取出一个元素，插入到已排序部分的正确位置
- 时间复杂度：**O(n²)**

### 抽象数据类型（ADTs）

**Stack（栈）**
- LIFO（Last In, First Out）
- 操作：Push（压栈），Pop（出栈），Peek/Top（查看栈顶）
- 应用：函数调用栈、undo 操作

**Queue（队列）**
- FIFO（First In, First Out）
- 操作：Enqueue（入队），Dequeue（出队），IsEmpty
- 应用：打印机队列、广度优先搜索

**Linked List（链表）**
- 节点包含 Data 和 Pointer（指向下一个节点）
- 动态大小，不需要连续内存
- 操作：插入、删除、搜索、遍历

**Binary Tree（二叉树）**
- 每个节点最多有两个子节点（left, right）
- 遍历方式：Pre-order, In-order, Post-order
- Binary Search Tree: left < parent < right

**Graph（图）**
- 节点（vertices）和边（edges）
- 有向/无向、有权/无权

**Dictionary（字典）**
- 键值对（key-value pairs）
- 通过 key 快速访问 value

### Recursion（递归）

- 递归函数调用自身
- 必须包含 base case（终止条件）
- 每次递归向 base case 逼近
- 使用 call stack 管理调用

### Big O Notation

- 描述算法的时间复杂度（算法执行时间的增长率）
- 关注最坏情况（worst-case）
- 常用复杂度（由快到慢）：
  $$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(2^n) < O(n!)$$
