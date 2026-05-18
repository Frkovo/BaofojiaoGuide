---
title: 考前速记
sidebar_position: 7
---

# 考前速记

## 栈核心（Last In, First Out）

| 操作 | 一句话 |
|------|--------|
| Push | 先检查是否满 → `top+1` → 放进去 |
| Pop | 先检查是否空 → 取出来 → `top-1` → **RETURN** |
| Top (Peek) | 直接返回 `stack[top]`（不改 `top`） |
| isEmpty | `top = -1` |
| isFull | `top = maxSize - 1` |

## 指针速记

```
空栈 top = -1
满栈 top = maxSize - 1
Push: ++top → stack[top] = item
Pop:  item = stack[top] → top--
```

## 避坑清单

- [ ] Push 前检查 overflow？
- [ ] Pop 前检查 underflow？
- [ ] Push 顺序：**先加后放**？
- [ ] Pop 顺序：**先取后减**？
- [ ] Pop 有 `RETURN`？
- [ ] 初始 `top ← -1`？

## 题目套路

1. **读题** → 确定 `top` 指向栈顶还是空位（CIE 指向栈顶）
2. **写 Push** → IF full → OUTPUT Overflow / ELSE → top+1 → stack[top]=item
3. **写 Pop** → IF empty → OUTPUT Underflow → RETURN Null / ELSE → item=stack[top] → top-1 → RETURN item
4. **模拟** → 画出每次操作后 `stack[]` 和 `top` 的变化

## 回答模板（30 秒写出骨架）

```
PUSH(stack, top, item, maxSize):
  IF top = maxSize - 1 THEN
    OUTPUT "Stack Overflow"
  ELSE
    top ← top + 1
    stack[top] ← item
  ENDIF

POP(stack, top):
  IF top = -1 THEN
    OUTPUT "Stack Underflow"
    RETURN Null
  ELSE
    item ← stack[top]
    top ← top - 1
    RETURN item
  ENDIF
```

:::note[Last Minute]
如果只记得一句话：**Push 先加后放，Pop 先取后减，别忘了 Check + Return！**
:::
