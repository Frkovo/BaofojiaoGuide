---
title: "评分标准模式"
---

# 评分标准模式

以下归纳了数据验证类题目的常见 MS 分值分配模式。

---

## 模式 1：简单 Range Validation（2–3 分）

```
M1  Correct condition to identify invalid input (use of OR, correct comparison)
A1  Appropriate loop structure (WHILE or REPEAT…UNTIL)
A1  Re-input inside loop / flag update
```

- **M1** 给在条件判断的逻辑正确性
- 如果使用 `AND` 替代 `OR`，**M1 不得分**
- 如果不等号方向反了（如检查是否在范围内而非范围外），**最多给 M1**
- Loop 结构正确但缺少内部重新输入 → 仅 M1

---

## 模式 2：Check Digit（4–6 分）

```
M1  Loop over each digit position
M1  Correct weight assignment and accumulation
A1  Correct modulo operation and check digit formula
A1  Special case handling (remainder 10 → "X")
A1  Output / return correct check digit or verification result
```

- **M1-M2** 是 method marks，算法框架正确即可得
- **A1** 要求公式和计算结果完全正确
- 如果权重分配错误（如顺序颠倒），最多得 M1
- 忘记处理 `remainder = 10` → 扣 A1
- 验证场景下需要 explicit comparison `calculated = given` → 额外 A1

---

## 模式 3：Validation with Loop + Flag（3–5 分）

```
M1  Correct loop structure (REPEAT…UNTIL or WHILE)
A1  Boolean flag initialised and used correctly
A1  Condition(s) checked and flag updated appropriately
A1  Appropriate error message on invalid input
A1  Program terminates only when valid input received
```

- Flag 未初始化（如 `valid` 无初始值）→ 扣 A1
- Loop 条件反写（如 `UNTIL valid = FALSE`）→ 不得 A1
- 多重验证未使用 `ELSEIF` 链 → 不扣分但失分风险（可能 A1 不完整）
- 循环内缺少 `INPUT` → 不得分

---

## 模式 4：Validation vs. Verification（2 分）

```
A1  Correct definition of validation
A1  Correct definition of verification
```

- Validation: 检查数据是否符合预设规则/格式
- Verification: 检查数据是否与原始来源一致（如 double entry, visual check）
- 必须写出两者的**本质区别**，仅举例不给满分

---

## MS 常见扣分点汇总

| 错误 | 扣分 |
|------|------|
| Range check 用 `AND` 而非 `OR` | 全扣 M1 |
| 缺少 loop 内部 re-input | 扣 A1 |
| Check digit 权重顺序错误 | 最多 M1 |
| Mod-11 余数 10 未转 `X` | 扣 A1 |
| 未初始化 flag 变量 | 扣 A1 |
| 验证与 verification 概念混淆 | 扣 A1 |
| 不等号方向错误（不含边界时用了 `&lt;=`） | 扣 A1 |
