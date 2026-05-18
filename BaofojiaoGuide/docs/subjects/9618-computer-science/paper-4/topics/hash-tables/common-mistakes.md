---
title: 常见错误
sidebar_position: 5
---

# 常见错误

## 错误 1：未初始化数组为空记录

哈希表和 Spare 数组的每个元素必须初始化为空记录（所有字段为 -1），否则插入时无法判断槽位是否为空。

## 错误 2：MOD 运算错误

```python
# 错误：用除号
hashVal = key / 200  # 返回 float

# 正确：用取模
hashVal = key % 200  # 返回 int
```

## 错误 3：碰撞时未正确存储到 Spare

发现 HashTable 对应位置非空时，应将记录存入 Spare 的下一个空位，不是覆盖原有数据。

## 错误 4：忘记记录类型实现

Python 中没有内置 record 类型，需要用 class 实现。必须实现构造器和 getter 方法。

## 错误 5：文件读取时未正确处理 CSV

```python
# 正确做法
parts = line.split(",")
record = NewRecord()
record.SetKey(int(parts[0]))
record.SetItem1(int(parts[1]))
record.SetItem2(int(parts[2]))
```

## 错误 6：PrintSpare 遍历范围错误

Spare 数组有 100 个元素，但只需输出已填充的记录（Key != -1 的记录）。
