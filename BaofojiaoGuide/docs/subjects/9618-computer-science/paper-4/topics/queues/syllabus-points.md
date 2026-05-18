---
title: 考纲要点
sidebar_position: 6
---

# 考纲要点

## Syllabus 19.1.6 — Queue ADT

### 核心知识点

1. **Queue 定义**: 一种先进先出 (FIFO) 的抽象数据结构
   - 新元素从队尾 (rear) 加入
   - 元素从队首 (front) 移除
   - 类比: 排队买票, 先到先服务

2. **Queue ADT 基本操作**:
   | 操作 | 描述 | 时间复杂度 |
   |------|------|-----------|
   | `Enqueue(x)` | 将元素 `x` 添加到队尾 | O(1) |
   | `Dequeue()` | 移除并返回队首元素 | O(1) |
   | `isEmpty()` | 检查队列是否为空 | O(1) |
   | `isFull()` | 检查队列是否已满 (数组实现) | O(1) |
   | `Peek()` | 返回队首元素但不移除 | O(1) |

3. **实现方式** (考纲要求):
   - **Static array-based linear queue** — 数组 + 两个指针 + 计数器
   - 理解 circular queue (概念性, 非所有考卷必考)

4. **Linear Queue (Array) 核心机制**:
   - 使用静态数组 `$Queue[0:QueueSize-1]$`
   - `$Front$` 指针指向第一个元素 (初始 0)
   - `$Rear$` 指针指向下一个空位置 (初始 0)
   - `$NumberInQueue$` 跟踪当前元素数量
   - Enqueue: 在 `$Queue[Rear]$` 写入, `$Rear$` 递增, 计数器递增
   - Dequeue: 读取 `$Queue[Front]$`, `$Front$` 递增, 计数器递减

5. **Linear Queue 的局限性**:
   - 出队后 `$Front$` 前的空间**无法重用** (假溢出)
   - 即使数组前部有空位, `$Rear$` 到达 `$QueueSize$` 后无法入队
   - 解决方案: circular queue (回绕指针) 或动态数组

6. **Circular Queue 关键公式**:
   - 指针后移: `$ptr \gets (ptr + 1) \bmod QueueSize$`
   - Full condition: `$(Rear + 1) \bmod QueueSize = Front$`
   - Empty condition: `$Front = Rear$`

### 典型考题要求

- 实现 enqueue 和 dequeue 操作
- 完成队列初始化和显示队列内容
- 使用队列管理数据 (如缓冲区、打印队列)
- 编写主程序提供菜单交互
- 追踪队列状态变化 (trace)

### 与其他主题的联系

- **Array**: 队列以数组作为底层存储
- **File handling**: 从文件读取数据入队
- **Records/Classes**: 可使用 record/class 封装队列结构
- **Linked lists** (A2): queue 也可用 linked list 实现 (A2 范围)
