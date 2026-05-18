---
title: 解题方法
sidebar_position: 3
---

# 解题方法

## Array-based Stack（数组实现栈）

### 数据结构定义

```
CONSTANT maxSize ← 10
DECLARE stack : ARRAY[0 : maxSize - 1] OF INTEGER
DECLARE top : INTEGER  // 初始值 ← -1
```

- `top` 指向当前栈顶元素的**下标**
- 空栈时 `top = -1`
- 满栈时 `top = maxSize - 1`

### Push — 三步骤

| 步骤 | 伪代码 | 说明 |
|------|--------|------|
| 1. 检查 | `IF top = maxSize - 1` | 是否溢出 |
| 2. 自增 | `top ← top + 1` | **先**移动指针 |
| 3. 赋值 | `stack[top] ← item` | **再**放入元素 |

### Pop — 三步骤

| 步骤 | 伪代码 | 说明 |
|------|--------|------|
| 1. 检查 | `IF top = -1` | 是否下溢 |
| 2. 取值 | `item ← stack[top]` | **先**取出元素 |
| 3. 自减 | `top ← top - 1` | **再**移动指针 |
| 4. 返回 | `RETURN item` | 不要忘记返回值 |

### 函数式写法示例

```
FUNCTION push(BYREF stack[] : ARRAY, BYREF top : INTEGER, item : INTEGER, maxSize : INTEGER) RETURNS BOOLEAN
  IF top = maxSize - 1 THEN
    OUTPUT "Stack Overflow"
    RETURN FALSE
  ELSE
    top ← top + 1
    stack[top] ← item
    RETURN TRUE
  ENDIF
ENDFUNCTION
```

```
FUNCTION pop(BYREF stack[] : ARRAY, BYREF top : INTEGER) RETURNS INTEGER
  IF top = -1 THEN
    OUTPUT "Stack Underflow"
    RETURN -1
  ELSE
    DECLARE item : INTEGER
    item ← stack[top]
    top ← top - 1
    RETURN item
  ENDIF
ENDFUNCTION
```

:::note[Important]
Parameters passed **BYREF** because both `stack[]` and `top` are modified inside the procedure/function.
:::
