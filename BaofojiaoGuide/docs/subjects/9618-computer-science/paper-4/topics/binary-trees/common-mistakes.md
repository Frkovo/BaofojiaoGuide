---
title: 常见错误
sidebar_position: 5
---

# 常见错误

## 错误 1：比较方向搞反

新节点数据小于当前节点应走左边，大于应走右边。记反了会导致树结构错乱。

## 错误 2：忘记处理空树情况

插入第一个节点时，必须先检查树是否为空（`FirstNode == -1`），直接设为根节点。

## 错误 3：插入后忘记更新 NumberNodes

每次成功插入节点后必须 `NumberNodes += 1`，否则后续插入位置错误。

## 错误 4：忘记更新父节点指针

插入非空树时，找到正确位置后，必须更新父节点的左指针或右指针指向新节点索引。

## 错误 5：Python 中忘记 `self.__` 私有属性前缀

```python
def __init__(self, data):
    self.__LeftPointer = -1  # 必须是双下划线
    self.__Data = data
```

## 错误 6：getter/setter 方法与属性名混淆

getter 内要 `return self.__Data`，不是 `return Data`。

## 错误 7：OutputTree 中遍历范围错误

只输出已插入的节点，不是全部 20 个空位。循环范围为 `0` 到 `NumberNodes - 1`。

## 错误 8：递归中序遍历缺少 base case

递归遍历时先检查参数是否为 null/None，否则无限递归导致栈溢出。
