---
title: 常见陷阱
sidebar_position: 10
---

# 常见陷阱

## Trap 1：全局变量忘记 global 声明

在函数内赋值全局变量必须加 `global`，否则 Python 会创建一个新的局部变量。

## Trap 2：二分查找未预先排序

二分查找假设数组已排序。对未排序数组执行二分查找得到的结果完全错误但不报错。

## Trap 3：队列指针语义混淆

不同题目可能用不同的指针约定：
- Front 指向第一个元素 vs 指向第一个元素的前一个位置
- Rear 指向最后一个元素 vs 指向下一个空位
**对策**：仔细读题，严格按照题目定义实现。

## Trap 4：循环队列用 Head==Tail 判断空/满

循环队列中 Head==Tail 既可以表示空也可以表示满（取决于实现）。必须用 `NumberOfItems` 计数器区分。

## Trap 5：Python 的 / 和 // 混用

索引运算必须用 `//`（整数除法），`/` 返回 float 会导致 TypeError。

## Trap 6：递归函数忘记 return

递归调用必须 `return recCall()`，只调用不返回会导致外层函数返回 None。

## Trap 7：OOP 方法定义忘记 self

```python
def GetName(self):  # 必须有 self
    return self.__Name
```

## Trap 8：OOP 继承忘记调用父类构造器

```python
class Child(Parent):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2)  # 必须调用
        self.__Attr3 = p3
```

## Trap 9：哈希表碰撞处理遗漏

Key MOD 200 计算出的索引已被占用时，不要覆盖，要存到 Spare 数组。

## Trap 10：2D 数组二叉树指针更新顺序

插入新节点时，先把节点存入 `ArrayNodes[FreeNode]`，再更新父节点指针指向 `FreeNode`，最后递增 `FreeNode`。

## Trap 11：链表插入时忘记更新 emptyList

从空闲链取出节点后，必须更新 `emptyList` 指向下一个空闲节点。

## Trap 12：字符串排序用 MID 而不是索引

```python
# 正确：按首字母排序
if arr[j][0] > arr[j+1][0]:
```

## Trap 13：文件读取时未处理换行符

```python
# 使用 strip() 或 splitlines() 去除换行
data = f.read().splitlines()  # 自动去除换行符
```

## Trap 14：出题人换套路

不同年份的变体（41/42/43）题目完全不同。不要只刷一种变体，三个变体都要看。
