---
title: 评分标准模式
sidebar_position: 4
---

# 评分标准模式

## CalculateHash 函数的通用评分标准 (2 分)

<details>
<summary>MS 逐项解析</summary>

**M1** — 正确定义函数签名:
```
FUNCTION CalculateHash(ByVal Key : INTEGER) RETURNS INTEGER
```
或等效的函数定义 (含参数和返回值类型)

**A1** — 正确实现 MOD 运算:
```
Index &lt;- Key MOD 10
RETURN Index
```
或 `RETURN Key MOD TableSize`

</details>

## InsertIntoHash 过程的通用评分标准 (5–6 分)

<details>
<summary>MS 逐项解析</summary>

**M1** — 调用 `CalculateHash` 获取下标:
```
Index &lt;- CalculateHash(NewValue)
```
或 `Index &lt;- NewValue MOD 10`

**A1** — 检查主表对应位置是否为空:
```
IF HashTable[Index] = -1 THEN
```
或 `IF HashTable[Index] = 0 THEN` (空值标记视题目定义)

**M1** — 主表为空时插入:
```
HashTable[Index] &lt;- NewValue
```

**A1** — 主表被占用时放入 overflow 数组:
```
OverflowArray[OverflowPointer] &lt;- NewValue
```

**A1** — 更新 `OverflowPointer` (递增):
```
OverflowPointer &lt;- OverflowPointer + 1
```

**A1** — (可选) 更新 `OverflowCount` 或正确处理溢出统计

</details>

## 从文件加载哈希表的通用评分标准 (5 分)

<details>
<summary>MS 逐项解析</summary>

**M1** — 声明记录类型变量和文件变量

**A1** — 打开文件并初始化哈希表

**M1** — 循环读取文件数据:
```
WHILE NOT EOF(File)
    ReadFile(File, Value)
```

**A1** — 对每条数据调用 `InsertIntoHash`

**A1** — 关闭文件

</details>

## Print Overflow Array 的通用评分标准 (2 分)

<details>
<summary>MS 逐项解析</summary>

**M1** — 循环遍历 overflow 数组 (含正确范围)

**A1** — 输出元素值

</details>

## Record Type 声明的通用评分标准 (2 分)

<details>
<summary>MS 逐项解析</summary>

**M1** — 正确定义 TYPE 名称和主表数组:
```
TYPE HashTableRecord
    DECLARE HashTable : ARRAY[0:9] OF INTEGER
```

**A1** — 声明 overflow 数组和 `OverflowPointer`:
```
    DECLARE OverflowArray : ARRAY[1:10] OF INTEGER
    DECLARE OverflowPointer : INTEGER
ENDTYPE
```

</details>

## 常见 MS 扣分点

| 错误 | 扣分 |
|------|------|
| `CalculateHash` 中 `Key MOD TableSize` 写反 | 相关步骤全扣 |
| 碰撞时未放入 overflow 数组 | M1 丢失 |
| `OverflowPointer` 忘记递增 | A1 丢失 |
| 未调用 `CalculateHash` 直接计算下标 | M1 丢失 |
| 主表和 overflow 数组混用 | 相关步骤全扣 |
| 未初始化哈希表 (空值标记) | A1 丢失 |
| 文件循环中未处理 `EOF` | M1 丢失 |
| `ByRef` 误写为 `ByVal` (需修改参数时) | A1 丢失 |
| 数组下标越界 (如 `HashTable[10]` 当大小为 10 时) | A1 丢失 |
