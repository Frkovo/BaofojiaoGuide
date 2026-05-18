---
title: 评分标准模式
sidebar_position: 4
---

# 评分标准模式

## General MS Structure

| Mark | Description |
|------|-------------|
| **M1** | Correct algorithm structure / loop / condition |
| **A1** | Correct variable usage (e.g. `CurrentPointer` initialised to `Head`) |
| **A2** | Correct pointer update (e.g. `CurrentPointer ← Node[CurrentPointer].NextPointer`) |
| **A3** | Correct output / return value |
| **A4** | Handling edge cases (empty list, single node) |

---

## Q1: Type Declaration (2 &ndash; 4 marks)

<details>
<summary>Typical Mark Scheme</summary>

| Mark | Requirement |
|------|-------------|
| **M1** | Declares a record/type for a node |
| **A1** | Includes `Data` field with correct type |
| **A2** | Includes `NextPointer` field with type `INTEGER` |
| **A3** | Declares `LinkedList` type with `Head`, `Tail`, `Current` (if asked) |

</details>

---

## Q2: Traversal / Output (4 &ndash; 6 marks)

<details>
<summary>Typical Mark Scheme</summary>

| Mark | Requirement |
|------|-------------|
| **M1** | Initialise `Current` to `Head` |
| **A1** | `WHILE` loop with correct condition (`Current <> -1`) |
| **A2** | Output `Node[Current].Data` (or equivalent) |
| **A3** | Update `Current ← Node[Current].NextPointer` |
| **A4** | Correct structure (procedure / function, correct parameters) |
| **A5** | No logical errors (e.g. not modifying `Head` directly) |

</details>

**Common MS phrasing**: "Award **M1** for initialising current pointer. Award **A1** for loop structure. Further marks awarded for correct output and pointer advancement."

---

## Q3: Insert Node (7 marks)

<details>
<summary>Typical Mark Scheme</summary>

| Mark | Requirement |
|------|-------------|
| **M1** | Allocate a new node from the free list (`NewNode ← Free`) |
| **A1** | Update free pointer (`Free ← Node[Free].NextPointer`) |
| **A2** | Store data in new node (`Node[NewNode].Data ← Value`) |
| **A3** | Set new node's `NextPointer` to `-1` |
| **A4** | Handle empty list case (`Head = -1` &rarr; update `Head` and `Tail`) |
| **A5** | Link current tail to new node (`Node[Tail].NextPointer ← NewNode`) |
| **A6** | Update `Tail ← NewNode` |
| **A7** | Correct use of `IF/ELSE` structure |

</details>

**Alternative mark distribution** (for insertion at start):

| Mark | Requirement |
|------|-------------|
| **M1** | Allocate node & update free pointer |
| **A1** | Set `Node[NewNode].NextPointer ← Head` |
| **A2** | Update `Head ← NewNode` |
| **A3** | Handle tail if needed |

---

## Q4: Delete Node (6 &ndash; 8 marks)

<details>
<summary>Typical Mark Scheme</summary>

| Mark | Requirement |
|------|-------------|
| **M1** | Search loop to find target node and predecessor |
| **A1** | Correct loop conditions |
| **A2** | Handle deletion of head node |
| **A3** | Handle deletion of middle/last node |
| **A4** | Update predecessor's `NextPointer` |
| **A5** | Return deleted node to free list |
| **A6** | Update `Tail` if last node deleted |

</details>

---

## MS Keywords

| Keyword | Meaning |
|---------|---------|
| "Award **M1** for ..." | Method mark &ndash; general approach |
| "Award **A1** for ..." | Accuracy mark &ndash; correct implementation |
| "If no marks otherwise, award **M1** for ..." | Fallback mark for partial attempt |
| "Correct context" | The mark is only available in the correct scenario |
| "Dependent on **M1**" | Can only get A-mark if the corresponding M-mark was awarded |

:::note

Always write the complete structure even if unsure. Examiners give **M1** for the correct shape of code, even with minor errors.

:::
