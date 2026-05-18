---
title: "题型分析"
---

# 题型分析

---

## Q1: Input Range Validation（2–5 分）

### 识别特征

- 题目要求"validate that the input is within a given range"
- 通常给出上下界（如 `min = 1`, `max = 100`）
- 可能要求 repeated input until valid（含循环）

### 标准解法

```
INPUT value
WHILE value < lower OR value > upper
    OUTPUT "Invalid. Re-enter."
    INPUT value
ENDWHILE
```

### MS 评分模式

| 得分点 | 说明 |
|--------|------|
| **M1** | Correct loop condition using `OR` |
| **A1** | Correct comparison operators (`<` / `>`) |
| **A1** | Re-prompt and re-input inside loop |

### 例题

> Write program code that repeatedly asks the user to enter a number between 1 and 100 inclusive. The program must not continue until a valid number is entered. [4]

### 陷阱

- 使用 `AND` 而非 `OR` — 条件永为假，loop 不会执行
- 忘记在 loop 内部重新 `INPUT`，导致 infinite loop
- 不等号方向写反（如 `value > 1 AND value < 100` 是 valid 条件，不是 invalid 条件）

---

## Q2: Check Digit Calculation & Verification（4–6 分）

### 识别特征

- 题目给出一串数字（如 ISBN, barcode, account number）
- 要求计算 check digit（modulo-11 或 modulo-10）
- 或者给定完整数字串要求验证 check digit 是否正确
- 典型例题：**9618/s24/qp/41 Q3d**

### 标准解法（Modulo-11）

```
total ← 0
FOR i ← 1 TO LEN(digits)
    digit ← Mid(digits, i, 1)
    weight ← 2 + (i - 1)   ' or given weight pattern
    total ← total + digit * weight
NEXT i
check ← 11 - (total MOD 11)
IF check = 10 THEN check ← "X"
```

### MS 评分模式

| 得分点 | 说明 |
|--------|------|
| **M1** | Correct loop over each digit |
| **M1** | Correct weight application and accumulation |
| **A1** | Correct modulo operation and check digit derivation |
| **A1** | Handling remainder = 10 → "X" |

### 例题

> The first 11 digits of an ISBN-13 are 978-0-691-17181. The check digit is calculated by: sum = Σ (digit × weight), where weight is 1 for odd positions and 3 for even positions. check digit = 10 - (sum MOD 10). Calculate the check digit. [5]

### 陷阱

- Weight assignment 顺序错误（从哪一位开始，权重值对调）
- 忘记 position 从 1 开始还是从 0 开始
- Modulo 运算用 `MOD` 或 `%` 写错
- 余数 10 的情况忘记特殊处理为 `X`（mod-11）
- 验证场景下忘记比较 calculated check digit 与 given check digit

---

## Q3: Validation with While Loops / Repeat-Until（3–5 分）

### 识别特征

- 要求"keep asking until valid input is provided"
- 可能涉及多种 check 组合（range + type + presence）
- 通常使用 `REPEAT ... UNTIL` 或 `DO ... WHILE` 结构
- 伪代码题常要求用 `REPEAT ... UNTIL`

### 标准解法

```
valid ← FALSE
REPEAT
    INPUT value
    IF value >= lower AND value <= upper THEN
        valid ← TRUE
    ELSE
        OUTPUT "Invalid"
    ENDIF
UNTIL valid = TRUE
```

### MS 评分模式

| 得分点 | 说明 |
|--------|------|
| **M1** | Correct loop construct (REPEAT…UNTIL or WHILE) |
| **A1** | Boolean flag (`valid`) correctly used |
| **A1** | Condition checked and flag set appropriately |
| **A1** | Re-prompt on invalid input |

### 陷阱

- `REPEAT` 没有 `UNTIL` 或 `WHILE` 缺少条件更新
- 在 loop 外部声明变量后在 loop 内部忘记更新
- 多重条件时用 `OR` 替代 `AND`（valid 条件应该用 `AND`）
- 没有区分 "valid 条件" 和 "invalid 条件" 分别写检查逻辑
