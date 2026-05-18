---
title: 知识点总结
---

## Programming Paradigms — 编程范式

### Low-Level (Assembly) — 低级语言（汇编）

- **Addressing modes**:
  - **Immediate — 立即寻址**: operand is the actual value (e.g. `MOV R1, #42`)
  - **Direct — 直接寻址**: operand is a memory address (e.g. `MOV R1, 2000`)
  - **Indirect — 间接寻址**: operand is a memory address that holds the target address (e.g. `MOV R1, (2000)`)
  - **Indexed — 变址寻址**: address = base + index register (e.g. `MOV R1, 2000(R2)`)
  - **Relative — 相对寻址**: address = current PC + offset (used for branching)

### Imperative / Procedural — 命令式 / 过程式

- Uses **variables**, **sequence** (statements execute in order), **selection** (IF/ELSE), **iteration** (loops)
- Organised into **procedures** and **functions**
- Procedure: performs an action (may not return a value)
- Function: computes and returns a value
- Top-down design: break problems into smaller sub-procedures

### Object-Oriented (OOP) — 面向对象

- **Class — 类**: blueprint / template for objects
- **Object — 对象**: instance of a class
- **Encapsulation — 封装**: bundling data + methods, hiding internal state via private/public
- **Inheritance — 继承**: a class derives properties and methods from a parent class
- **Polymorphism — 多态**: same interface, different implementations (method overriding / overloading)
- **Containment / Composition — 组合**: one class contains an instance of another as a field

### Declarative — 声明式

- Describes **what** to achieve, not **how** (logic programming)
- **Facts — 事实**: statements that are unconditionally true (e.g. `parent(john, mary).`)
- **Rules — 规则**: conditional statements (e.g. `grandparent(X, Z) :- parent(X, Y), parent(Y, Z).`)
- **Queries — 查询**: questions asked of the system (e.g. `?- grandparent(john, Who).`)
- **Backward chaining — 反向链**: starts from the goal/query and works backward, matching rules and facts to find a solution (Prolog-style inference)

:::tip[...]
Backward chaining is goal-driven — it starts with the conclusion and searches for supporting evidence.
:::

## RPN (Reverse Polish Notation) — 逆波兰表示法

- Also called **postfix notation** — 后缀表示法
- Operator **follows** its operands (e.g. `3 4 +` instead of `3 + 4`)
- **No brackets needed** — order of operations is unambiguous
- Evaluated using a **stack**:
  1. Read tokens left to right
  2. If operand → push onto stack
  3. If operator → pop required number of operands, apply operator, push result back
- Examples:
  - Infix: `(3 + 4) × 5` → RPN: `3 4 + 5 ×`
  - Infix: `3 + 4 × 5` → RPN: `3 4 5 × +`

:::warning[...]
Always pay attention to the **order** of operands when popping from the stack — subtraction and division are not commutative.
:::

## File Processing — 文件处理

- **OPENFILE**: opens a file for reading/writing/appending
- **READFILE**: reads data from an open file
- **WRITEFILE**: writes data to an open file
- **CLOSEFILE**: closes the file and releases resources
- **File modes**:
  - **Read** — 读取: file must already exist
  - **Write** — 写入: creates new file or overwrites existing
  - **Append** — 追加: adds data to end of existing file
- **Access methods**:
  - **Serial — 串行**: data stored/read in order (e.g. tape)
  - **Sequential — 顺序**: records accessed one after another from start
  - **Random / Direct — 随机 / 直接**: access any record directly using its address/key

## Exception Handling — 异常处理

- Mechanism to handle **runtime errors** gracefully without crashing the program
- Structure: **TRY...EXCEPT** (or TRY...CATCH in some languages)
- Common exception types:
  - **IOError**: input/output operation failure (e.g. file not found, disk full)
  - **ValueError**: operation receives an argument of correct type but invalid value
  - **IndexError**: accessing an index outside the bounds of a sequence
  - **KeyError**: accessing a non-existent key in a dictionary
  - **TypeError**: operation applied to object of inappropriate type
- Use exceptions when:
  - The error is **unpredictable** (e.g. network failure, missing file)
  - The normal flow of logic should **not** be cluttered with error-checking code
  - The error must propagate **up the call stack**

:::warning[...]
Do **not** use exceptions for normal control flow — they should be reserved for genuinely exceptional conditions.
:::
