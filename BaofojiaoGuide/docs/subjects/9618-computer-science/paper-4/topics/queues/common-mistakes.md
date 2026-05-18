---
title: 常见错误
sidebar_position: 5
---

# 常见错误

## 错误 1：Front/Rear 指针语义混淆

入队时操作 Front，出队时操作 Rear，或者认为 Rear 指向最后一个有效元素（实际指向下一个空位会导致指针更新逻辑错误）。

**正解**：
- Front：指向第一个有效元素
- Rear/Tail：指向下一个空闲位置

## 错误 2：出队时忘记检查空队列

```python
def Dequeue():
    value = Queue[Front]  # 若队列为空会越界
    Front += 1
    return value
```

**正解**：先检查 `Front == -1 or Front >= Rear`，空则返回 "Empty" 或 "false"。

## 错误 3：入队时忘记处理第一个元素

当队列为空时入队，必须将 Front 设为 0（除非指针初始化方式不同）。

## 错误 4：入队后忘记更新 Rear

```python
Queue[Rear] = data
# 忘记 Rear += 1
```

## 错误 5：全局变量声明遗漏

在函数内修改队列指针必须先用 `global` 声明。

## 错误 6：队列满/空判断条件写错

线性队列的满条件是 `Rear >= 数组大小`，空条件是 `Front == -1 or Front >= Rear`。

## 错误 7：Dequeue 返回值类型不一致

题目要求返回字符串 "false" 时不要返回布尔值 False，反之亦然。严格按照题目要求。

## 错误 8：主程序初始化为空值遗漏

每个元素必须初始化为空字符串 `""` 或 `None`，不能只声明数组。
