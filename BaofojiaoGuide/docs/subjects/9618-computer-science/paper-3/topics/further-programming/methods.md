---
title: 方法总结
---

# 方法总结

## Prolog 语法速记

```
% Facts (常量小写, 句点结尾)
likes(john, apple).

% Rule (:- 表示 IF)
happy(X) :- likes(X, apple).

% Query (?- 表示问询)
?- happy(john).

% Variables (大写开头)
?- likes(john, What).
```

| Prolog | Meaning |
|--------|---------|
| `.` | End of fact/rule |
| `:-` | IF (left-right) |
| `,` | AND |
| `;` | OR |
| `not` | Negation |
| UPPERCASE | Variable |
| lowercase | Constant |

## OOP Class 模板

```
CLASS ClassName
    PRIVATE DECLARE attr1 : Type
    PRIVATE DECLARE attr2 : Type

    PUBLIC PROCEDURE NEW(p1: Type, p2: Type)
        attr1 ← p1
        attr2 ← p2
    ENDPROCEDURE

    PUBLIC FUNCTION GetAttr1() RETURNS Type
        RETURN attr1
    ENDFUNCTION

    PUBLIC PROCEDURE SetAttr1(v: Type)
        attr1 ← v
    ENDPROCEDURE
ENDCLASS
```

### Inheritance

```
CLASS SubClass EXTENDS SuperClass
    PUBLIC PROCEDURE NEW(...)
        CALL SuperClass::NEW(...)
        // additional init
    ENDPROCEDURE
ENDCLASS
```

## RPN 栈求值步骤

```
1. Scan tokens left to right
2. If operand → PUSH to stack
3. If operator → POP b (second), POP a (first)
                 result ← a op b
                 PUSH result
4. End → POP final result
```

### RPN — 注意顺序

| Expression | Result |
|-----------|--------|
| `a b -` | a − b |
| `a b /` | a ÷ b |
| `a b ^` | a^b |

## File Processing 模板

```
handle ← OPENFILE("name.txt", "r")
WHILE NOT EOF(handle)
    line ← READFILE(handle)
    process line
ENDWHILE
CLOSEFILE(handle)
```

| Mode | Meaning |
|------|---------|
| `"r"` | Read |
| `"w"` | Write (overwrite) |
| `"a"` | Append |

## Exception Handling 模板

```
TRY
    // risky code
EXCEPT
    // error handling code
ENDTRY
```

## Paradigm Identification 速查

| 范式 | 特征词 |
|------|--------|
| Low-level | registers, memory addresses, MOV, ADD |
| Imperative | FOR, WHILE, IF, assignment ← |
| OOP | CLASS, OBJECT, method, attribute |
| Declarative | facts, rules, Prolog, `?-` |
