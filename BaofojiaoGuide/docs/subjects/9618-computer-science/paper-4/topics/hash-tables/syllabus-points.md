---
title: 考纲要点
sidebar_position: 6
---

# 考纲要点

## Syllabus 13.2 — Hashing Algorithms

### 核心知识点

1. **哈希表 (Hash Table) 定义**: 一种使用哈希函数将键映射到数组下标的 ADT
   - 直接访问: 通过哈希值可在 `O(1)` 时间内定位
   - 空间换时间: 需要预分配一定大小的数组

2. **哈希函数 (Hash Function)**:
   - 公式: `Index = Key MOD TableSize`
   - 输入: 键值 (Key)
   - 输出: 数组下标 (0 到 TableSize - 1)
   - 要求: 计算简单, 分布均匀

3. **碰撞 (Collision)**:
   - 定义: 两个不同键映射到同一个数组下标
   - 原因: 哈希函数不是一一映射, 表大小有限
   - 不可避免, 需要碰撞处理策略

4. **碰撞处理 — 分离溢出数组 (Separate Overflow Array)**:
   - 主表 (Main Table): 存放首次映射成功的元素
   - 溢出数组 (Overflow Array): 存放碰撞元素, 按到达顺序依次存放
   - 溢出指针 (OverflowPointer): 指向 overflow 数组下一个空闲位置
   - 查找时: 先查主表 `HashTable[Index]`, 若被占用则遍历 overflow 数组

### Syllabus 19.1 — ADTs

5. **记录类型 (Record Type) 声明**:
   - 使用 `TYPE ... ENDTYPE` 封装主表和 overflow 数组
   - 主表: 固定大小的数组
   - Overflow 数组: 通常大小等于主表
   - `OverflowPointer` 或 `OverflowCount` 变量

6. **核心操作**:
   - `CalculateHash(Key)`: 计算哈希值
   - `InsertIntoHash(Table, Value)`: 插入值并处理碰撞
   - `PrintOverflowArray(Table)`: 输出碰撞数据

### 典型考题要求

- 声明记录类型 (TYPE) 包含主表和 overflow 数组
- 实现 `CalculateHash` 函数 (MOD 运算)
- 实现 `InsertIntoHash` 过程 (碰撞处理)
- 从文件读取数据构建哈希表
- 输出 overflow 数组内容
- （较少考）从哈希表中搜索特定值

### 与其他主题的联系

- **Arrays**: 哈希表底层使用数组实现
- **File Handling**: 从文件读取数据构建哈希表
- **Data Structures**: 哈希表是一种重要的 ADT, 与其他 ADT (栈、队列、树) 并列
- **Searching**: 哈希表提供近似 `O(1)` 的查找效率
