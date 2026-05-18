---
title: "评分标准模式"
sidebar_position: 4
---

# 评分标准模式

## Common Mark Scheme Structure

<details>
<summary>Child Class Declaration (4–5 marks)</summary>

| Mark | Criteria |
|---|---|
| **M1** | Correct class header: `class Child(Parent):` |
| **A1** | Correct `__init__` method signature with all parameters |
| **A1** | Calls `super().__init__(...)` with correct parent parameters |
| **A1** | Initialises all new child attributes with `self._attr = param` |

</details>

<details>
<summary>Method Override (3–4 marks)</summary>

| Mark | Criteria |
|---|---|
| **M1** | Method signature matches parent exactly |
| **A1** | Calls `super().method_name()` at appropriate point |
| **A1** | Adds child-specific logic (new calculation / attribute use) |
| **A1** | Returns correct value (type matches parent) |

</details>

<details>
<summary>Main Program with Inheritance (4–6 marks)</summary>

| Mark | Criteria |
|---|---|
| **A1** | Instantiates parent object with correct arguments |
| **A1** | Instantiates child object with correct arguments |
| **M1** | Calls method on both objects to demonstrate polymorphism |
| **A1** | Outputs/uses the return values correctly |
| **A1** | Correct sequencing / loop structure if processing multiple objects |

</details>

<details>
<summary>File Input + Object Creation (7 marks)</summary>

| Mark | Criteria |
|---|---|
| **M1** | Opens file correctly (`with open` or `open`/`close`) |
| **A1** | Reads all lines / records in a loop |
| **A1** | Splits / parses each line correctly |
| **A1** | Conditional branch to distinguish parent vs child type |
| **M1** | Calls parent constructor with correct parsed arguments |
| **A1** | Calls child constructor with correct parsed arguments |
| **A1** | Stores all objects in a list and returns / processes them |

</details>

## Mark Scheme Keywords

| Keyword | Meaning |
|---|---|
| **M1** | Method mark — awarded for correct **approach** |
| **A1** | Accuracy mark — awarded for correct **implementation** |
| **B1** | Independent mark — not conditional on M marks |
| **Mark** | More than one approach may be accepted |
| **Accept** | Alternative correct syntax is accepted |
| **Not** | Specific error that invalidates the mark |
| **Ignore** | Superfluous code is ignored (not penalised) |

## Common Mark Allocation Patterns

- Child class constructor: **M1 + 3 × A1** = 4 marks
- Override method alone: **M1 + 3 × A1** = 4 marks
- Main program: **2 × A1 + M1 + A1 + A1** = 5 marks
- File + constructor + override combined: **M1 + A1 + M1 + A1 + 3 × A1** = 7 marks
