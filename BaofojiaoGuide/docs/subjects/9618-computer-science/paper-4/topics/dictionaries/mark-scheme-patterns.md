
title: "评分标准模式"

# 评分标准模式

## Pattern 1 — Define / Explain Dictionary

<details>
<summary>Scoring breakdown (4 marks)</summary>

**M1:** States dictionary stores `(key, value)` pairs. (1 mark)

**A1:** Explains each key is unique. (1 mark)

**A1:** Explains value is retrieved by key (not by index). (1 mark)

**A1:** Mentions at least two operations: `add`, `get`, `remove`, `contains`. (1 mark)
</details>

---

## Pattern 2 — Pseudocode Implementation

<details>
<summary>Scoring breakdown (6 marks)</summary>

**M1:** Correct declaration of data structures (parallel arrays OR linked list nodes). (1 mark)

**M1:** Correct loop to search for key. (1 mark)

**M1:** Correct comparison `keys[i] = key` (or node.key = key). (1 mark)

**A1:** Correct return / update of value when key found. (1 mark)

**A1:** Correct "not found" handling — append new pair OR return `null`. (1 mark)

**A1:** Index / pointer management is correct throughout. (1 mark)
</details>

---

## Pattern 3 — Time Complexity

<details>
<summary>Scoring breakdown (3 marks)</summary>

**M1:** Correct complexity stated (e.g. O(n) for `get` on array). (1 mark)

**A1:** Correct justification — "must search through all elements in worst case". (1 mark)

**A1:** Distinguishes between different operations if asked. (1 mark)
</details>

---

## Pattern 4 — Compare Dictionary with Other ADTs

<details>
<summary>Scoring breakdown (4 marks)</summary>

**M1:** States dictionary uses key-value pairs / array uses indices. (1 mark)

**A1:** States dictionary keys can be any data type / array indices are integers. (1 mark)

**A1:** States dictionary is more flexible for lookup by meaning. (1 mark)

**A1:** States array may be faster for positional access. (1 mark)
</details>
