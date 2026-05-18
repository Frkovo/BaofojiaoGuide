---
title: MS 关键词速查
sidebar_position: 10
---

# MS 关键词速查

## M1 / A1 / B1 注解模式

| 标记 | 全称 | 含义 | 示例 |
|------|------|------|------|
| **M1** | Method mark | 方法正确即得分，即使最终答案有算术错误 | 写出标准化公式 M1 |
| **A1** | Accuracy mark | 需要结果完全正确（通常依赖前一个 M1） | 正确算出浮点数 A1 |
| **B1** | Independent mark | 独立给分，不依赖其他步骤 | 写出 bias 值 B1 |
| **M1 dep** | Dependent method | 依赖前一个 M mark 正确才能得分 | 正确标准化后求 exponent |
| **A1 ft** | Follow through | 即使前一步错了，后续步骤正确仍给分（ft = follow through） | exponent 算错但后续 bias 减对了 |
| **B1 ft** | Follow through (independent) | 独立 follow through | 答案基于上一步错误但推导正确 |

---

## 浮点数（Floating Point）

| MS 关键词 | 含义 | 如何得分 |
|-----------|------|---------|
| "normalises mantissa" | 将尾数调整到标准化形式 | 左移/右移 mantissa；正数 0.1xxx，负数 1.0xxx **M1** |
| "adjusts exponent accordingly" | 指数随着 mantissa 移动相应增减 | shift 一位指数 ±1，方向与 mantissa 相反 **M1** |
| "correct two's complement" | 负数尾数正确取补码 | 取反加一半步要给分，最终值正确 **M1 A1** |
| "applies bias correctly" | 正确使用 excess/bias | 写出 bias 值 **B1**；actual = stored - bias **M1** |
| "states value in denary" | 最终数值以十进制写出 | 结合 mantissa × 2^exponent 计算 **A1** |
| "identifies precision issue" | 指出有限位导致精度损失 | "limited mantissa bits cause rounding error" **B1** |
| "range" | 可表示数值的上下界 | exponent 能取的最大最小值决定 **B1** |
| "precision" | 相邻可表示数的间隔 | mantissa 位数决定精度（位数越多越精确）**B1** |

---

## 布尔代数 & K-map（Boolean Algebra & K-maps）

| MS 关键词 | 含义 | 如何得分 |
|-----------|------|---------|
| "De Morgan's applied" | 应用了 De Morgan's 定律 | 翻转 AND/OR + 各自取反 **M1** |
| "simplifies expression" | 表达式化简到最简形式 | 正确应用恒等式逐步化简 **M1 A1** |
| "groups cells correctly" | K-map 中正确分组 | 圈出 1/2/4/8/16 个相邻 1 **B1 per group** |
| "largest possible group" | 使用了尽可能大的组 | group 不可再扩大（prime implicant）**A1** |
| "wraps around edges" | 利用边缘相邻性 | K-map 上下/左右边缘看作相邻 **B1** |
| "removes redundant terms" | 消除了冗余项 | Don't care(X) 合理利用来扩大 group **M1** |
| "draws logic circuit" | 画出逻辑门电路 | 每个 AND/OR/NOT gate 对应一项 **M1**；连线正确 **A1** |
| "uses NAND/NOR only" | 用单一逻辑门实现 | 将 AND/OR 替换为 NAND/NOR 等效电路 **M1 A1** |

---

## 逆波兰表达式（RPN）

| MS 关键词 | 含义 | 如何得分 |
|-----------|------|---------|
| "correct RPN conversion" | 中缀转后缀结果正确 | 操作数和操作符顺序正确 **M1 A1** |
| "observes precedence" | 考虑了运算符优先级 | ×/÷ 先于 +/− **M1** |
| "correct use of stack" | RPN 求值时正确使用栈 | operand → push；operator → pop ×2 → push 结果 **M1 per step** |
| "correct order of operands" | 运算时操作数顺序正确 | pop a / pop b / 计算 b op a（减法和除法关键）**M1** |
| "final result" | 最终结果正确 | 最终栈顶元素 = 答案 **A1** |
| "stack empty at end" | 求值结束后栈为空 | 合法表达式 → 最终栈空（如果有多个结果可能错了）**B1** |
| "parentheses handled" | 括号处理正确 | 左括号 push，右括号 pop 到遇左括号 **M1** |

---

## 伪代码 & 算法（Pseudocode & Algorithms）

| MS 关键词 | 含义 | 如何得分 |
|-----------|------|---------|
| "correct loop structure" | 循环结构正确 | WHILE/REPEAT/FOR 开头 + 对应 ENDWHILE/UNTIL/NEXT **B1** |
| "correct selection" | 选择结构正确 | IF/THEN/ELSE/ENDIF 或 CASE/OF/ENDCASE **B1** |
| "correct array declaration" | 数组声明正确 | `DECLARE arr : ARRAY[1:n] OF datatype` **B1** |
| "correct assignment" | 赋值语句正确 | 使用 `←` 而非 `=` **B1** |
| "correct procedure call" | 过程调用正确 | `CALL ProcedureName(params)` **B1** |
| "correct return value" | 函数返回值正确 | `RETURN expression` 在 FUNCTION 中 **B1** |
| "adequate testing" | 提供了足够的测试用例 | normal / boundary / erroneous 三类测试 **B1 each** |
| "trace table completed" | 跟踪表填写完整 | 每轮循环变量值正确，包含条件判断结果 **M1 A1** |

---

## 面向对象编程（OOP）

| MS 关键词 | 含义 | 如何得分 |
|-----------|------|---------|
| "class defined correctly" | 类定义语法正确 | `CLASS name` ... `ENDCLASS` **B1** |
| "attributes declared" | 属性声明正确 | `DECLARE attr : datatype`（常为 PRIVATE）**B1** |
| "constructor defined" | 构造方法定义 | `PUBLIC PROCEDURE NEW(…)` 初始化属性 **M1 A1** |
| "instantiation" | 创建对象实例 | `obj ← NEW ClassName(args)` **B1** |
| "inheritance" | 继承关系正确 | 子类用 `INHERITS` / `EXTENDS` 父类 **B1** |
| "method overriding" | 方法覆写 | 子类中同名方法取代父类方法 **M1** |
| "encapsulation" | 封装的实现 | private fields + public getters/setters + data hiding **B1** |
| "polymorphism" | 多态的体现 | 同一方法名在不同类中有不同实现 **B1** |
| "getter/setter defined" | 访问器/修改器 | `GET attr()` 返回私有属性值，`SET attr(val)` 修改 **B1 per pair** |

---

## 声明式编程（Declarative Programming）

| MS 关键词 | 含义 | 如何得分 |
|-----------|------|---------|
| "fact defined" | 事实定义正确 | `predicate(arg1, arg2).`（句点结尾，常量小写）**B1** |
| "rule defined" | 规则定义正确 | `head :- body.` **M1**（body 用 `,` 连接条件）|
| "variable correctly used" | 变量使用正确 | 大写字母开头或 `_` **B1** |
| "query formulated" | 给出正确查询 | `?- predicate(arg, Variable).` 返回所有绑定 **M1** |
| "all solutions found" | 找到所有解 | 变量查询返回所有可能的 binding **A1** |
| "recursive rule" | 递归规则 | base fact + recursive rule（条件参数递减）**M1 A1** |

---

## 二分查找 & 排序（Binary Search & Sorting）

| MS 关键词 | 含义 | 如何得分 |
|-----------|------|---------|
| "sorted array" | 指出排序前提 | "Array must be sorted in ascending order" **B1** |
| "midpoint calculation" | 正确计算中间索引 | `mid ← (low + high) DIV 2` **M1** |
| "correct comparison" | 正确比较 target 和 mid | 按 ascending 比较：target > mid → 右半区 **M1** |
| "boundary update" | 更新搜索范围 | `low ← mid + 1` 或 `high ← mid - 1` **M1** |
| "termination condition" | 终止条件正确 | `low > high` 时停止 → not found **M1** |
| "correct trace" | 跟踪二分查找过程 | 每一轮的 low/mid/high 值正确 **A1** |
| "best/worst case" | 最好最坏情况复杂度 | best O(1), worst O(log n) **B1** |
| "bubble sort pass" | 冒泡排序一轮 | 相邻比较 + 如果逆序交换 **M1**；一轮后最大/最小元素归位 **A1** |

---

## 文件操作（File Handling）

| MS 关键词 | 含义 | 如何得分 |
|-----------|------|---------|
| "file opened" | 成功打开文件 | `OpenFile(filePtr, filename, mode)` **B1** |
| "correct mode specified" | 模式指定正确 | READ / WRITE / APPEND 之一 **B1** |
| "read from file" | 从文件读取数据 | `ReadFile(filePtr, variable)` **B1** |
| "write to file" | 向文件写入数据 | `WriteFile(filePtr, value)` **B1** |
| "file closed" | 关闭文件 | `CloseFile(filePtr)` — 释放资源，确保数据写入 **B1** |
| "EOF check" | 检查文件是否结束 | `WHILE NOT EOF(filePtr) DO` **M1** |
| "error handling" | 文件操作错误处理 | 检查文件是否存在、是否成功打开 **B1** |

---

## 处理器 & 汇编（Processor & Assembly）

| MS 关键词 | 含义 | 如何得分 |
|-----------|------|---------|
| "Von Neumann architecture" | 冯·诺依曼架构 | 数据+指令共用内存和总线；顺序执行 **B1** |
| "Harvard architecture" | 哈佛架构 | 数据和指令分开存储，独立总线可并行访问 **B1** |
| "RISC vs CISC" | 精简 vs 复杂指令集 | RISC: 单周期、固定长度；CISC: 可变长度、微程序控制 **B1 each** |
| "pipelining" | 流水线技术 | Fetch → Decode → Execute 重叠 **M1**；增加 throughput **B1** |
| "pipeline hazard" | 流水线冒险 | data hazard / control hazard / structural hazard **B1** |
| "interrupt" | 中断 | 暂停当前执行 → 保存上下文 → 执行 ISR → 恢复 **M1 A1** |
| "addressing mode" | 寻址模式 | immediate(操作数=值) / direct(操作数=地址) / indirect(地址的地址) / indexed(地址+偏移) **B1 each** |
| "LMC instruction" | Little Man Computer | INP/OUT/ADD/SUB/STA/LDA/BRZ/BRP/BRA/HLT 各指令功能 **B1** |

---

## 通信 & 监控（Communication & Monitoring）

| MS 关键词 | 含义 | 如何得分 |
|-----------|------|---------|
| "TCP/IP stack" | TCP/IP 协议栈 | Application → Transport(TCP/UDP) → Internet(IP) → Link **B1 per layer** |
| "CSMA/CD" | 载波监听多点接入/碰撞检测 | 先听后发、边发边听、碰撞停发、随机重发 **M1 A1** |
| "sensor" | 传感器 | 感应物理量（温度/光/声/压力）→ 输出模拟信号 **B1** |
| "ADC" | 模数转换器 | 将模拟信号转换为数字信号供 CPU 处理 **B1** |
| "actuator" | 执行器 | 将数字信号转换为物理动作（马达/阀门/加热器）**B1** |
| "feedback loop" | 反馈回路 | 闭环控制：sensor→measure→compare→adjust→sensor **M1 A1** |
