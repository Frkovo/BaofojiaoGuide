---
title: "解题方法"
---

# 解题方法

---

## 一、Range Validation（范围验证）

### 适用场景
用户输入必须在指定的数值区间内（如年龄 0–120，分数 0–100）。

### 方法步骤

1. **确定边界**：确认题目要求的是 inclusive（含边界）还是 exclusive（不含边界）
   - "between 1 and 100 inclusive" → `value >= 1 AND value <= 100`
   - "between 1 and 100 exclusive" → `value > 1 AND value < 100`

2. **写 invalid 条件**：用 `OR` 连接两个越界条件
   - `value < lower OR value > upper`

3. **选择循环结构**：
   - **While loop**: 先检查再输入，适合首次输入也需要验证的场景
   - **Repeat-until**: 先输入再检查，保证至少执行一次

4. **验证标志位**：使用 `valid` 布尔变量控制循环退出

### 代码模板

```pseudocode
// Template 1: WHILE with re-prompt
INPUT value
WHILE value < min OR value > max
    OUTPUT "Please enter a valid value"
    INPUT value
ENDWHILE

// Template 2: REPEAT…UNTIL with flag
valid ← FALSE
REPEAT
    INPUT value
    IF value >= min AND value <= max THEN
        valid ← TRUE
    ENDIF
UNTIL valid
```

---

## 二、Check Digit Algorithm（校验位算法）

### 适用场景
需要计算或验证某数字串的最后一位校验位（常见于 ISBN, barcode, 账号等）。

### Modulo-11 方法步骤

1. **提取每位数字**：将数字串作为字符串处理，逐位取出并转为整数
2. **分配权重**：通常从右到左或按题目给定的 weight pattern
3. **计算加权和**：`sum = Σ (digit[i] × weight[i])`
4. **取模**：`remainder = sum MOD 11`
5. **计算校验位**：`checkDigit = 11 - remainder`
6. **处理特殊情况**：如果 `checkDigit = 10`，则输出 `X`

### Modulo-10 方法步骤（ISBN-13 模式）

1. 奇数位（1,3,5,…）权重 = 1，偶数位（2,4,6,…）权重 = 3
2. 计算加权和 `sum`
3. `checkDigit = 10 - (sum MOD 10)`
4. 如果结果 = 10，check digit = 0

### 代码模板

```pseudocode
// Check digit calculation (Modulo-11)
FUNCTION CalculateCheckDigit(digits : STRING) RETURNS CHAR
    total ← 0
    FOR i ← 1 TO LEN(digits)
        digit ← VAL(Mid(digits, i, 1))
        weight ← LEN(digits) + 1 - i  // 从右到左权重递增
        total ← total + digit * weight
    NEXT i
    remainder ← total MOD 11
    checkDigit ← 11 - remainder
    IF checkDigit = 10 THEN
        RETURN "X"
    ELSE
        RETURN CHR(checkDigit + 48)  // convert to char
    ENDIF
ENDFUNCTION
```

---

## 三、Repeat-Until 验证模式

### 适用场景
要求"持续输入直到合法"的一类问题，通常涉及多重验证。

### 标准模式

```
valid ← FALSE
REPEAT
    OUTPUT "Enter input:"
    INPUT value

    // 执行所有验证检查
    IF NOT presenceCheck(value) THEN
        OUTPUT "Input cannot be empty"
    ELSEIF NOT typeCheck(value) THEN
        OUTPUT "Must be numeric"
    ELSEIF NOT rangeCheck(value) THEN
        OUTPUT "Out of range"
    ELSE
        valid ← TRUE
    ENDIF
UNTIL valid
```

### 关键要点

- `valid` 标志必须在循环开始前初始化为 `FALSE`
- 每个验证失败后都应输出对应错误信息
- 只有当所有 check 都通过时才设置 `valid ← TRUE`
- 使用 `ELSEIF` 确保一次只报一个错，避免混淆
