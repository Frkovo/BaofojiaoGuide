---
title: 常见错误
sidebar_position: 5
---

# 常见错误

## 1. Infinite Loop in Traversal

```
// WRONG — missing pointer advancement
Current ← Head
WHILE Current <> -1
    OUTPUT Node[Current].Data
    // Missing: Current ← Node[Current].NextPointer
ENDWHILE
```

**Fix**: Always include `Current ← Node[Current].NextPointer` as the last line of the loop body.

---

## 2. Modifying `Head` During Traversal

```
// WRONG — destroys the head reference
WHILE Head <> -1
    OUTPUT Node[Head].Data
    Head ← Node[Head].NextPointer
ENDWHILE
```

**Fix**: Use a working variable `Current ← Head`; never reassign `Head` unless intentionally changing the list's start.

---

## 3. Forgetting to Update `Free` Pointer

```
// WRONG — free pointer never advances
NewNode ← Free
// Missing: Free ← Node[Free].NextPointer
Node[NewNode].Data ← Value
```

**Fix**: Immediately after `NewNode ← Free`, update `Free ← Node[Free].NextPointer`.

---

## 4. Not Handling Empty List

```
// WRONG — assumes Tail always exists
Node[Tail].NextPointer ← NewNode
```

When the list is empty (`Head = -1`), `Tail` is also `-1`, so `Node[Tail]` is an invalid index.

**Fix**: Check `IF Head = -1 THEN` before accessing `Node[Tail]`.

---

## 5. Setting Wrong `NextPointer` for New Node

```
// WRONG for insert-at-end
Node[NewNode].NextPointer ← Head
```

For end insertion, `Node[NewNode].NextPointer` must be `-1`.

**Fix**: `Node[NewNode].NextPointer ← -1` (end insertion) or `Node[NewNode].NextPointer ← Head` (start insertion).

---

## 6. Confusing Index with Data

```
OUTPUT Node[Current].NextPointer  // WRONG — outputs pointer, not data
OUTPUT Current                     // WRONG — outputs index, not data
```

**Fix**: `OUTPUT Node[Current].Data` is what the question asks for.

---

## 7. Off-by-One in Deletion Loop

```
WHILE Current <> -1
    IF Node[Current].Data = Value THEN
        // delete
    ENDIF
    Current ← Node[Current].NextPointer
ENDWHILE
```

This works but is inefficient &mdash; the better pattern searches for the *predecessor* so you can relink without a second pass.

---

## 8. Not Returning Deleted Nodes to Free List

After deletion, the removed node's index should be prepended to the free list:

```
Node[Current].NextPointer ← Free
Free ← Current
```

---

## 9. Confusing `Tail` Update After Deletion

If the last node is deleted, `Tail` must be set to the new last node (or `-1` if list becomes empty).

---

## 10. Parameter Passing Errors

When passing the linked list to a procedure that modifies it, pass by reference (or use global variables). In pseudocode, this usually means operating on a global array `Node[]` and global pointers `Head`, `Tail`, `Free`.

<details>
<summary>Memory Aid: DEBUG checklist</summary>

- **D**ata &mdash; did I store/read `Data` and not the pointer?
- **E**mpty &mdash; did I handle the empty-list case?
- **B**ounds &mdash; am I accessing a valid array index?
- **U**pdate &mdash; did I advance both the working pointer AND `Free`?
- **G**uard &mdash; does my loop condition prevent infinite looping?

</details>
