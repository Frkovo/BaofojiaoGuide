---
title: "常见错误"
---

# 常见错误

---

## 1. AND / OR 混淆 ❌

**错误**: `IF value >= 1 AND value <= 100 THEN` 用于 invalid 判断  
**原因**: 这个条件判断的是 valid 值，而 loop 需要的是 invalid 条件  
**正确**: `IF value < 1 OR value > 100 THEN`

**记忆口诀**: "Invalid 用 OR，valid 用 AND"

---

## 2. Loop 内缺少重新输入 ❌

```pseudocode
// ❌ 错误
INPUT value
WHILE value < 1 OR value > 100
    OUTPUT "Invalid"
ENDWHILE  // 永不退出
```

```pseudocode
// ✅ 正确
INPUT value
WHILE value < 1 OR value > 100
    OUTPUT "Invalid"
    INPUT value
ENDWHILE
```

---

## 3. 不等号边界错误 ❌

| 题目要求 | 错误写法 | 正确写法 |
|----------|----------|----------|
| 1–100 inclusive | `value > 0 AND value < 101` | `value >= 1 AND value <= 100` |
| 1–100 exclusive | `value >= 1 AND value <= 100` | `value > 1 AND value < 100` |

---

## 4. Check Digit 权重顺序错误 ❌

- 未看清题目要求的 weight 分配方向（从左到右还是从右到左）
- 常见 ISBN-13: odd position weight = 1, even position weight = 3
- 注意 position 通常从 1 开始计数

---

## 5. Mod-11 余数 10 未处理 ❌

```pseudocode
// ❌ 错误
checkDigit ← 11 - (total MOD 11)
// 当 total MOD 11 = 1 时，checkDigit = 10，但 check digit 是一位数字

// ✅ 正确
remainder ← total MOD 11
IF remainder = 0 THEN
    checkDigit ← 0
ELSE
    checkDigit ← 11 - remainder
    IF checkDigit = 10 THEN
        checkDigit ← "X"
    ENDIF
ENDIF
```

---

## 6. Flag 未初始化 ❌

```pseudocode
// ❌ 错误
REPEAT
    INPUT value
    IF value >= 1 AND value <= 100 THEN
        valid ← TRUE
    ENDIF
UNTIL valid  // valid 未定义
```

```pseudocode
// ✅ 正确
valid ← FALSE
REPEAT
    ...
UNTIL valid
```

---

## 7. Validation 与 Verification 混淆 ❌

| 概念 | 定义 | 例子 |
|------|------|------|
| **Validation** | 检查数据是否符合预设规则 | 年龄不能为负数，邮箱格式检查 |
| **Verification** | 检查数据是否与原始来源一致 | 两次输入密码，人工核对纸质表格 |

---

## 8. 多重验证逻辑混乱 ❌

```pseudocode
// ❌ 错误：多个独立的 IF 而不是 ELSEIF
IF empty THEN invalid ← TRUE
IF not numeric THEN invalid ← TRUE
// 可能后一个覆盖前一个的错误
```

```pseudocode
// ✅ 正确：ELSEIF 链或逐层检查
IF empty THEN
    OUTPUT "Empty"
ELSEIF NOT numeric THEN
    OUTPUT "Not numeric"
ELSEIF out of range THEN
    OUTPUT "Out of range"
ELSE
    valid ← TRUE
ENDIF
```
