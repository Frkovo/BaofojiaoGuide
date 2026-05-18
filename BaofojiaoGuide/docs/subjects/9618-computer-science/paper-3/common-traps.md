---
title: 常见陷阱
sidebar_position: 11
---

# 常见陷阱

:::warning[Trap 1: Two's Complement 溢出（Overflow）]
**描述：** 两个正数相加得到负数，或两个负数相加得到正数。最常见是在 floating point exponent 计算或 two's complement 加法运算中。

**后果：** 最终结果符号错误，导致后续所有计算全错。

**对策：** 检查 operands 和 result 的 sign bit。如果两个正数相加 MSB=1，或两个负数相加 MSB=0，则一定溢出了。在 CIE 考试中一般会给定位数，超出范围要注明 "overflow occurs"。
:::

:::warning[Trap 2: 浮点数正负数标准化规则相反]
**描述：** 正数的标准化 mantissa 以 `0.1` 开头，但**负数的 two's complement mantissa** 标准化后以 `1.0` 开头 — 这和直觉（以为负数全是 1.x）不同。

**后果：** 负数标准化的结果判断错误，误以为 `1.1110` 已标准化（实际上是 `1.0xxx` 开头才是标准化的，`1.1110` 需要左移）。

**对策：** 正数检查 `0.1`，负数检查 `1.0`。如果负 mantissa 不是 `1.0` 开头，反复左移直到开头为 `1.0`（右端补 1），exponent 相应递减。
:::

:::warning[Trap 3: K-map Wrapping（边界相邻）被忽略]
**描述：** K-map 的最上/最下行、最左/最右列是相邻的，可以跨边界合并成更大的 group。很多考生只考虑内部相邻，丢失化简机会。

**后果：** 表达式不是最简，逻辑门数量多余，丢简化分。

**对策：** 画 K-map 时想象它是一个 torus（环面），上下边缘相接、左右边缘相接。检查是否可以利用 wrapping 合并更大的 powers-of-2 group。
:::

:::warning[Trap 4: RPN 减法和除法的操作数顺序]
**描述：** RPN 求值时，`a ← POP, b ← POP, result = b op a`。常⻅陷阱是先弹出的 a 当作左操作数，`a op b` 导致减法/除法结果错误。

**后果：** `5 3 -` 算成 `3 - 5 = -2`（正确应为 `5 - 3 = 2`）。除法同理。

**对策：** 牢记 stack 中先 push 的在下面（左操作数），后 push 的在上面（右操作数）。POP 顺序：a = right operand, b = left operand。每次计算都写 `b op a`。
:::

:::warning[Trap 5: 二分查找死循环（边界更新缺少 ±1）]
**描述：** 更新 low/high 时没有 ±1，而是直接用 `low ← mid` 或 `high ← mid`。当 target 不等于 arr[mid] 时，边界不缩小，导致无限循环。

**后果：** trace table 无限循环，程序不终止；实现代码永远跑不完。

**对策：** 确定 target 不在 mid 位置后，排除 mid：`IF target > arr[mid] THEN low ← mid + 1 ELSE high ← mid - 1`。记住 mid 已经检查过了，不需要保留在下一轮的搜索范围中。
:::

:::warning[Trap 6: 伪代码赋值与比较的符号混淆]
**描述：** CIE 伪代码中赋值用 `←`，比较用 `=`。但考生常混用两种符号，或者在比较时用 `==`（那是别的语言的习惯）。

**后果：** 语法错误直接扣分，mark scheme 明确检查 `←` 使用。

**对策：** 写伪代码时强制养成习惯：赋值永远用 `←`，判断条件用 `=`。写完后通读一遍检查所有赋值符号。
:::

:::warning[Trap 7: 递归缺少 Base Case（栈溢出）]
**描述：** 定义了递归函数但没有终止条件（base case），或者 base case 的条件永远无法满足。

**后果：** 无限递归 → stack overflow → 程序崩溃（runtime error）。

**对策：** 每写一个递归函数，先写 base case（`IF … THEN RETURN`），再写 recursive case。base case 必须能使参数最终达到（如参数递减到 0）。
:::

:::warning[Trap 8: 文件忘记关闭导致数据丢失]
**描述：** 写文件操作完成后没有调用 `CloseFile`，或者程序异常退出前未关闭文件。

**后果：** 写入的数据可能还在缓冲区中未刷入磁盘，导致部分或全部数据丢失。

**对策：** 写文件的伪代码中，写完最后一行数据后立刻写 `CloseFile(filePtr)`。养成 OpenFile 和 CloseFile 成对出现的习惯。
:::

:::warning[Trap 9: OOP 中混淆继承方向]
**描述：** 认为父类从子类继承功能，或认为子类比父类功能更少。

**后果：** 答题时继承关系写反，子类/父类属性描述错误，丢概念分。

**对策：** 继承关系 = "is-a" 关系。"A Dog is an Animal" → Dog extends Animal。子类拥有父类所有属性/方法 + 额外特性，所以子类功能更多或相等，绝不会更少。
:::

:::warning[Trap 10: Declarative Programming 查询变量未大写]
**描述：** Prolog / CIE 声明式伪代码中，大写字母开头的标识符是变量（会被绑定），小写是常量（直接匹配）。查询时用了小写 → 明明是变量却被当作常量字面量匹配。

**后果：** `?- likes(john, X).` 找到所有 likes 关系 ✅；`?- likes(john, x).` 只找精确匹配 x 这个常量，返回 false ❌。

**对策：** 所有需要系统填充/绑定的查询变量都用大写字母开头（X, Y, Result, Person）。匿名变量用 `_`。
:::

:::warning[Trap 11: 浮点数 Range 和 Precision 的权衡关系]
**描述：** 考题问 "increase exponent bits" 或 "increase mantissa bits" 的影响时，回答不完整。

**后果：** 只说一方影响，漏掉 trade-off 关系。

**对策：** 所有类似问题用如下结构回答：
- **Increase mantissa bits ↑** → precision ↑, but range ↓（因为 exponent bits 减少）
- **Increase exponent bits ↑** → range ↑, but precision ↓（因为 mantissa bits 减少）
必须同时说清 "more… but less…" 的权衡关系。
:::

:::warning[Trap 12: Trace Table 中数组索引漏标或越界]
**描述：** 做 trace table 时数组变量的索引没有列全，或者循环中索引超出数组声明范围。

**后果：** trace 到一半越界，无法继续；或漏掉关键中间状态。

**对策：** 每个数组变量保留单独列（如 `arr[1]`、`arr[2]`、`arr[3]`...），每次赋值更新对应列。循环时检查索引边界：`FOR i ← 1 TO n` 确保 n 不超过数组声明上限。
:::

:::warning[Trap 13: 伪代码 TYPE 声明中缺少 ENDTYPE]
**描述：** 使用 `TYPE` 自定义复合数据类型（类似 struct / record），忘记用 `ENDTYPE` 闭合。

**后果：** 语法不完整，直接扣 1 分。

**对策：** 写完 TYPE 声明体后立刻写 ENDTYPE：
```pseudocode
TYPE Student
  DECLARE Name : STRING
  DECLARE Age : INTEGER
ENDTYPE
```
:::

:::warning[Trap 14: 逻辑门化简忽略 Multiple-Level 化简]
**描述：** 将布尔表达式直接转为逻辑门，不做任何化简。比如 `A·B + A·¬B` 直接用两个 AND + 一个 OR 实现，但实际上可以化简为 `A`。

**后果：** 电路不是最简形式，丢 simplification 分。

**对策：** 画 logic circuit 前先用 Boolean algebra 或 K-map 化简到最简 SOP 形式。然后检查是否有共同子表达式可以复用。
:::

:::warning[Trap 15: Section B 选做题没有标记题目编号]
**描述：** 答题纸上没有圈选 / 填写所选的题号（Q5 或 Q6）。

**后果：** 阅卷人不知道你答的是哪一题，可能给 0 分。

**对策：** 交卷前最后一步：确认答题纸上的题号（Q5 / Q6）已圈选或填涂。这是 0 成本的保命操作。
:::
