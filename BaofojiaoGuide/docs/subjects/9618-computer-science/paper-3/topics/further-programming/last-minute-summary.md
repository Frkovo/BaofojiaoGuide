---
title: 考前速记
---

# 考前速记

## Prolog

```
% Fact (lowercase, dot)
likes(john, apple).

% Rule (:- = IF, , = AND)
happy(X) :- likes(X, apple), sweet(apple).

% Query (?- = ask)
?- happy(X).
```

## OOP Keywords

| Concept | Meaning |
|---------|---------|
| CLASS | Template for objects |
| NEW | Constructor |
| PRIVATE | Encapsulation (hide data) |
| EXTENDS | Inheritance |
| Override | Polymorphism |

## RPN Stack Evaluation

```
Token  | Stack
3      | [3]
4      | [3,4]
+      | [7]
2      | [7,2]
×      | [14]
```

⚠ **a b -** = a − b (NOT b − a)
⚠ **a b /** = a ÷ b (NOT b ÷ a)

## File Modes

| Mode | Action |
|------|--------|
| `"r"` | Read |
| `"w"` | Write (overwrite) |
| `"a"` | Append |

**MUST CLOSEFILE!**

## Exception Handling

```
TRY
    // code that might fail
EXCEPT
    // handle error gracefully
ENDTRY
```

Catches **runtime** errors only, not syntax errors.

## Paradigm ID — Quick Check

| Code has... | Paradigm |
|-------------|----------|
| CLASS, methods | OOP |
| facts, rules, ?- | Declarative |
| MOV, registers | Low-level |
| FOR, WHILE, ← | Imperative |
