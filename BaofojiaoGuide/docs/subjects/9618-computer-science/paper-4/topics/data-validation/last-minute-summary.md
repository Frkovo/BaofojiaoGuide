---
title: "考前速记"
---

# 考前速记

---

## 三大必背模板

### 1. Range Validation

```
INPUT x
WHILE x < min OR x > max
    OUTPUT "Invalid"
    INPUT x
ENDWHILE
```

> 关键：**invalid 用 OR，valid 用 AND**

### 2. Check Digit（Mod-11）

```
sum ← 0
FOR i ← 1 TO len
    sum ← sum + digit[i] × weight[i]
r ← sum MOD 11
IF r = 0 THEN cd ← 0
ELSE cd ← 11 - r
IF cd = 10 THEN cd ← "X"
```

> 关键：**余数 10 → X，余数 0 → 0**

### 3. Repeat-Until + Flag

```
valid ← FALSE
REPEAT
    INPUT x
    IF check passes THEN valid ← TRUE
    ELSE OUTPUT error
UNTIL valid
```

> 关键：**flag 必须初始化，loop 内有 input**

---

## 五条避坑口诀

1. **AND 还是 OR？** — invalid 条件用 `OR`，valid 条件用 `AND`
2. **&lt;= 还是 &lt;？** — 检查题目说 inclusive 还是 exclusive
3. **FLAG 初始化了吗？** — `valid ← FALSE` 不能忘
4. **RE-INPUT 了吗？** — loop 内部必须有 `INPUT`
5. **CHECK DIGIT 特殊值？** — Mod-11: `10→X`, `0→0`；Mod-10: `10→0`

---

## Validation vs. Verification 一句话

| | Validation | Verification |
|--|-----------|-------------|
| **检查对象** | 数据 vs. 规则 | 数据 vs. 原始来源 |
| **例子** | 年龄≥0，邮箱含@ | 两次输入一致，人工核对 |
| **目的** | 防止无效数据 | 防止转录错误 |

---

## 考场上 30 秒检查清单

- [ ] 条件用 `OR`（invalid）还是 `AND`（valid）？
- [ ] 边界符号是否和题目一致（`&lt;=` vs `&lt;`）？
- [ ] Loop 内部有没有重新 `INPUT`？
- [ ] Boolean flag 有没有初始化？
- [ ] Check digit 的特殊情况处理了吗？
- [ ] 输出了有意义的错误信息吗？
