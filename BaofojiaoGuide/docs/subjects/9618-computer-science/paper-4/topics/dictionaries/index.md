---
title: Dictionaries
sidebar_position: 1
---

# Dictionaries（字典 ADT）

## 考纲要求

- 19.1.10 Dictionary ADT：描述特征和用途
- ADT 可以从其他 ADT 实现

## 核心概念

字典 ADT 是一种键值对（key-value pair）的数据结构：
- 每个 key 唯一对应一个 value
- 通过 key 快速查找 value
- 支持插入、查找、删除操作

## 在 Paper 4 中

字典 ADT 在 Paper 4 中通常是概念性的，不要求写代码实现。但你可以用 Python 内置的 dict 来实现：

```python
# 创建字典
myDict = {}

# 插入键值对
myDict["key1"] = "value1"
myDict["key2"] = "value2"

# 查找
print(myDict["key1"])

# 检查 key 是否存在
if "key1" in myDict:
    print("Found")
```

## 实现方式

字典 ADT 可用以下两种方式实现：
1. **哈希表**（直接实现）：用数组 + 哈希函数
2. **二叉树**：用二叉搜索树存储键值对

## 常见错误

- 访问不存在的 key 导致 KeyError（应该先检查 `in`）
- 混淆字典（无序）和数组（有序）
