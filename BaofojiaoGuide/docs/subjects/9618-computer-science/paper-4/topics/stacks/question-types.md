---
title: 题型分析
sidebar_position: 2
---

# 题型分析

## Q1: Push Operation（压栈，4 分）

**Identify**: 考题给出一个数组 `stack[]` 和指针 `top`，要求写出向栈中添加一个元素的 procedure/function。

**Standard Method**:
1. 检查栈是否为满（`top = maxSize - 1`）
2. 若满则输出 ＂Stack Overflow＂
3. 若未满则 `top ← top + 1`，再 `stack[top] ← item`

**MS Pattern**:
<details>
<summary>Mark Scheme – Push</summary>

- **M1** 判断条件 `top = maxSize - 1`
- **M1** 溢出处理（Output 或 Error Handling）
- **A1** 正确更新指针 `top ← top + 1`（先自增）
- **A1** 正确赋值 `stack[top] ← item`

*常见扣分点：在赋值后自增（`stack[top] ← item; top ← top + 1`）会导致元素放到错误位置。*
</details>

**Example**:

```
stack = [_, _, _, _]    // maxSize = 4, top = -1 (empty)
stack = [10, _, _, _]   // push(10): top → 0
stack = [10, 20, _, _]  // push(20): top → 1
```

**Traps**:
- 忘记检查 `isFull` 直接压栈 → 0 分
- 先赋值再移动 `top` 指针 → 逻辑错误
- 混淆 `top` 指向**最后一个元素**还是**下一个空位**（CIE 通常指向最后一个元素）

---

## Q2: Pop Operation（弹栈，3–4 分）

**Identify**: 要求写出从栈中移除并返回栈顶元素的 function/procedure。

**Standard Method**:
1. 检查栈是否为空（`top = -1`）
2. 若空则输出 ＂Stack Underflow＂并返回特殊值（`Null` / `-1`）
3. 若非空则 `item ← stack[top]`，`top ← top - 1`，`RETURN item`

**MS Pattern**:
<details>
<summary>Mark Scheme – Pop</summary>

- **M1** 判断条件 `top = -1`
- **M1** 空栈处理（Output + Return）
- **A1** 正确取值 `item ← stack[top]`
- **A1** 正确更新指针 `top ← top - 1`（先取值后自减）

*常见扣分点：忘记 RETURN 弹出的元素，或 RETURN 了 `top` 而非元素。*
</details>

**Example**:

```
stack = [10, 20, 30, _]  // top = 2
item = pop()             // RETURN 30, top → 1
stack = [10, 20, _, _]
```

**Traps**:
- 忘记 `RETURN` → 最多拿 2/4
- 先自减再取值 → 取到错误元素
- 空栈时返回 `0` 而非 `Null` / 特殊标记 → 可能扣分
