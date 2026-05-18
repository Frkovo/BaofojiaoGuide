
title: "解题方法"

# 解题方法

## Method 1 — Describing Dictionary ADT

**Step 1:** Define the abstraction — "A dictionary stores data as `(key, value)` pairs where each key is unique."

**Step 2:** Describe basic operations — "It supports `add(key, value)` to insert/update, `get(key)` to retrieve the value by key, and `remove(key)` to delete a pair."

**Step 3:** Compare with array — "Unlike an array which uses integer indices, a dictionary uses arbitrary keys (strings, integers, etc.) for direct access."

**MS framing:**

<details>
<summary>Example answer framework</summary>

**M1:** Clear definition of key-value pair concept.

**A1:** Explanation that keys are unique and enable direct value retrieval.

**A1:** Mention of at least two operations (`add`, `get`, `remove`).
</details>

---

## Method 2 — Implementing Dictionary Using Parallel Arrays

**Step 1:** Declare two arrays — `keys[N]` and `values[N]`, plus `size` variable.

**Step 2:** `get(key)` — loop from `i = 0` to `size - 1`, if `keys[i] = key` return `values[i]`.

**Step 3:** `add(key, value)` — first call `get(key)`, if found update `values[i]`; if not, append to end.

**Step 4:** `remove(key)` — find index, shift remaining elements left, decrement `size`.

**MS framing:**

<details>
<summary>Example answer framework</summary>

**M1:** Correct loop structure to search `keys[]`.

**M1:** Correct handling of "found" case (returning or updating `values[i]`).

**A1:** Correct handling of "not found" case (returning `null` or appending).

**A1:** Proper maintenance of index / size counter.
</details>

---

## Method 3 — Implementing Dictionary Using Linked List

**Step 1:** Define node structure — `key`, `value`, `next`.

**Step 2:** `get(key)` — traverse from head; if node.key = key, return node.value.

**Step 3:** `add(key, value)` — traverse first; if key exists update value; if not, insert new node at head or tail.

**Step 4:** `remove(key)` — traverse with `current` and `previous` pointers; unlink node.

**MS framing:**

<details>
<summary>Example answer framework</summary>

**M1:** Correct traversal of linked list comparing keys.

**M1:** Correct update of existing node's value.

**A1:** Correct insertion of new node (linking properly).

**A1:** Correct unlinking in `remove` (handle head deletion separately).
</details>

---

## Method 4 — Time Complexity Analysis

**Step 1:** Identify the underlying data structure.

**Step 2:** Determine what operation dominates each dictionary method.

**Step 3:** State Big O complexity with justification.

**Common justifications:**

| Dictionary method | Dominant cost | Complexity (array/linked list) |
|-------------------|---------------|-------------------------------|
| `get(key)` | Sequential search | O(n) — must scan all elements worst-case |
| `add(key, value)` | Search + O(1) update/append | O(n) worst-case (when updating existing) |
| `remove(key)` | Search + O(n) shift (array) | O(n) |
