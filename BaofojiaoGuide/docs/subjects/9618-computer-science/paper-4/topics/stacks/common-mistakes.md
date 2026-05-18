---
title: 常见错误
sidebar_position: 5
---

# 常见错误

## Top Pointer 混淆

**错误**: 不清楚 `top` 指向栈顶元素还是下一个空位。

**正确**: CIE 默认 `top` 指向**栈顶元素的下标**（即最后一个压入的元素）。初始 `top = -1`。

| `top` 含义 | Push 顺序 | Pop 顺序 |
|------------|-----------|----------|
| 指向栈顶元素（CIE 标准） | 先 `top+1`，再赋值 | 先取值，再 `top-1` |
| 指向下一个空位 | 先赋值，再 `top+1` | 先 `top-1`，再取值 |

:::warning[Warning]
**不要混用两种模型！** CIE 考卷统一使用指向栈顶元素的模型。如果使用另一种模型必须完全一致，否则扣分。
:::

## 溢出/下溢检查遗漏

**错误**:

```
// Push — 忘了检查满栈
top ← top + 1
stack[top] ← item
```

**后果**: 当 `top = maxSize - 1` 时，`top` 变为 `maxSize`，数组越界，程序崩溃。

**改正**: 任何 Push/Pop 操作前必须先检查条件。

## 指针更新顺序颠倒

**错误（Push）**:

```
stack[top] ← item  // 先赋值
top ← top + 1      // 后自增
```

**问题**: 如果 `top = -1`，则 `stack[-1] ← item` → 下标越界。

**错误（Pop）**:

```
top ← top - 1      // 先自减
item ← stack[top]  // 后取值
```

**问题**: 少取了栈顶元素，取了下一个位置的值（未定义或旧值）。

## 忘记 RETURN

Pop 的 **function** 必须 `RETURN item`。写成 procedure（无返回值）得 0 分。

## 混淆 isEmpty / isFull

| 条件 | 含义 |
|------|------|
| `top = -1` | 栈空（isEmpty） |
| `top = maxSize - 1` | 栈满（isFull） |
| `top &lt; maxSize - 1` | 还有空间 |

## 初始化遗漏

**错误**: 声明 `top` 后未初始化。

**正确**: `top ← -1`

未初始化的变量默认值不确定，会导致条件判断 `top = -1` 恒不成立。

## 边界条件 — 最大下标

**错误**: `IF top = maxSize` 判断满栈。

**正确**: 数组下标从 `0` 到 `maxSize - 1`，满栈时 `top = maxSize - 1`。

:::note[记忆口诀]
Push — **先加后放**；Pop — **先取后减**；检查 — **先做后动**。
:::
