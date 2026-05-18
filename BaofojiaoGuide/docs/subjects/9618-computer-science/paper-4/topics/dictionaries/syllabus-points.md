
title: "考纲要点"

# 考纲要点

## 19.1.10 Dictionary ADT

### What you must know:

| # | 要点 | 掌握程度 |
|---|------|----------|
| 1 | Define dictionary ADT | Must be able to describe in words |
| 2 | Key-value pair concept | Must be able to explain with examples |
| 3 | Operations: `add`, `get`, `remove`, `isEmpty`, `size` | Must be able to write pseudocode |
| 4 | Implementation using parallel arrays | Must be able to write and trace |
| 5 | Implementation using linked list | Must be able to write and trace |
| 6 | Time complexity of each operation | Must be able to state and justify |

### Syllabus terminology checklist:

| Term | Meaning |
|------|---------|
| **Dictionary** | ADT storing `(key, value)` pairs, key must be unique |
| **Key** | Unique identifier used for lookup |
| **Value** | Data associated with a key |
| **Mapping** | Relationship from key to value |
| **Parallel arrays** | Two arrays of same length sharing same index for key and value |
| **Collision** | (Not in 9618 syllabus, but be aware it exists for hash table implementations) |

### Quick self-test questions:

1. What is the difference between a dictionary and a 1D array?
2. Write pseudocode for `get(key)` using parallel arrays.
3. Write pseudocode for `remove(key)` using a linked list.
4. State the worst-case time complexity of `get(key)` on an unsorted array implementation.
5. Can two different keys map to the same value? — (Yes, only keys must be unique, not values)
