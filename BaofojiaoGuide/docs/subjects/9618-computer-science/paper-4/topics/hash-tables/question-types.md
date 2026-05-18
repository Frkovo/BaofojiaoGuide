---
title: 题型分析
sidebar_position: 2
---

# 题型分析

## Q1: Record Type Declaration for Hash Table (2 分)

**题目识别**: 要求声明哈希表的记录类型, 包含主表数组和 overflow 数组

**标准解法**:
1. 定义 `HashTableRecord` 类型
2. 包含两个数组字段: `HashTable` (主表) 和 `OverflowArray` (溢出数组)
3. 指定数组大小和元素类型 (通常为 INTEGER 或 STRING)
4. 声明 `OverflowPointer` 变量追踪 overflow 数组下一个空闲位置

**评分标准模式**:

<details>
<summary>MS 示例</summary>

**M1** 正确定义记录类型名和主表数组 (含大小和类型)

**A1** 声明 overflow 数组和 `OverflowPointer` (或 `NextFreeOverflow`) 字段

</details>

**真题示例**:

- **9618/s25/qp/42 Q2(a)**: 声明 `HashTableRecord` 包含 `HashTable[0:9]` 和 `OverflowArray[1:10]`

**陷阱**:
- 主表大小和 overflow 数组大小混淆
- 数组类型不匹配 (题目要求 INTEGER 却声明为 STRING)
- 忘记声明 `OverflowPointer` 变量

---

## Q2: Hash Function — CalculateHash() Using MOD (2 分)

**题目识别**: 要求实现 `CalculateHash` 函数, 使用 MOD 运算将键映射到数组下标

**标准解法**:
1. 函数接收一个键 (KEY) 作为参数
2. 返回 `KEY MOD TableSize` 作为哈希值
3. 确保返回值在 `0` 到 `TableSize - 1` 范围内

**评分标准模式**:

<details>
<summary>MS 示例</summary>

**M1** 正确定义函数签名 (接收 KEY, 返回 INTEGER)

**A1** 正确实现 `KEY MOD TableSize` 并返回结果

</details>

**真题示例**:

- **9618/s25/qp/42 Q2(b)**: 实现 `CalculateHash(ByVal Key : INTEGER) RETURNS INTEGER`

**陷阱**:
- MOD 运算两边写反 (`TableSize MOD Key`)
- 忘记 `RETURN` 语句
- 参数类型或返回值类型与题目要求不符

---

## Q3: InsertIntoHash() with Collision Handling (6 分)

**题目识别**: 要求实现 `InsertIntoHash` 过程, 处理碰撞时将数据放入 overflow 数组

**标准解法**:
1. 调用 `CalculateHash` 计算哈希值
2. 检查主表中该位置是否为空
3. 如果为空: 直接放入主表
4. 如果不为空 (碰撞): 放入 overflow 数组, `OverflowPointer` 递增
5. 更新相关指针/计数器

**评分标准模式**:

<details>
<summary>MS 示例</summary>

**M1** 调用 `CalculateHash` 计算 `Index`

**A1** 检查主表 `HashTable[Index]` 状态

**M1** 主表为空时插入主表

**A1** 主表被占用时将值放入 overflow 数组

**A1** 正确更新 `OverflowPointer` (递增)

**A1** 更新 `OverflowCount` 或相关统计数据

</details>

**真题示例**:

- **9618/s25/qp/42 Q2(c)**: 实现 `InsertIntoHash` 过程处理碰撞, 6 marks

**陷阱**:
- 碰撞时放入了 overflow 但忘记递增 `OverflowPointer`
- 未调用 `CalculateHash` 而是自己算一遍
- 主表和 overflow 数组搞混 (该放主表的放 overflow)
- 使用 `&lt;--` 而非 `&lt;-` 赋值

---

## Q4: Create Hash Table from File (5 分)

**题目识别**: 要求从文件中读取数据并插入哈希表

**标准解法**:
1. 打开文件 (`OpenFile`)
2. 循环读取每条记录
3. 对每条记录调用 `CalculateHash` 和 `InsertIntoHash`
4. 关闭文件

**评分标准模式**:

<details>
<summary>MS 示例</summary>

**M1** 正确定义主表和 overflow 数组

**A1** 打开文件并循环读取数据

**M1** 对每条记录调用 `CalculateHash`

**A1** 调用 `InsertIntoHash` 插入哈希表

**A1** 关闭文件, 处理所有记录

</details>

**真题示例**:

- **9618/s25/qp/42 Q2(d)**: 从文件读取数据填充哈希表, 5 marks

**陷阱**:
- 文件路径写错或忘记指定文件模式
- 循环结束后忘记关闭文件
- 读取记录时字段类型不匹配
- 未处理文件为空或文件不存在的异常情况

---

## Q5: Print Collision Array (2 分)

**题目识别**: 要求遍历并输出 overflow 数组中的所有值

**标准解法**:
1. 使用循环遍历 overflow 数组
2. 输出每个非空元素的值 (或输出所有元素)
3. 使用 `OverflowCount` 或直接遍历固定范围

**评分标准模式**:

<details>
<summary>MS 示例</summary>

**M1** 正确定义循环遍历 overflow 数组

**A1** 输出元素值 (通常结合格式说明)

</details>

**真题示例**:

- **9618/s25/qp/42 Q2(e)**: 输出 overflow 数组的所有元素, 2 marks

**陷阱**:
- 遍历了主表而非 overflow 数组
- 忘记限制遍历范围 (遍历整个数组容量而非已使用部分)
- 输出格式与题目要求不符
