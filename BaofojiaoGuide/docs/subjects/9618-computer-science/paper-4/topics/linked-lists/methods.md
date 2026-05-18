---
title: 解题方法
sidebar_position: 3
---

# 解题方法

## 1. Record Type Declaration

For a single node:

```
TYPE Node
    DECLARE Data       : INTEGER
    DECLARE NextPointer : INTEGER
ENDTYPE
```

For the full linked list ADT:

```
TYPE LinkedList
    DECLARE Head    : INTEGER
    DECLARE Tail    : INTEGER
    DECLARE Current : INTEGER
ENDTYPE
```

Then instantiate as an array:

```
DECLARE Node : ARRAY[1:10] OF Node
```

:::note

In Python, use a class with `__init__`:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = -1
```

:::

---

## 2. Traversal

**Pseudocode**:

```
CurrentPointer ← Head
WHILE CurrentPointer <> -1
    OUTPUT Node[CurrentPointer].Data
    CurrentPointer ← Node[CurrentPointer].NextPointer
ENDWHILE
```

**Key points**:
- Always save `Head` into a working variable; never modify `Head` during a read-only traversal
- The loop guard is `CurrentPointer <> -1` (or `CurrentPointer <> Null`)
- The advancement `CurrentPointer ← Node[CurrentPointer].NextPointer` must be the last line inside the loop

**Python equivalent**:

```python
def traverse():
    current = head
    while current != -1:
        print(nodes[current].data)
        current = nodes[current].next
```

---

## 3. Insertion

### Insert at End (most common)

```
PROCEDURE InsertNode(Value : INTEGER)
    DECLARE NewNode : INTEGER
    NewNode ← Free
    Free ← Node[Free].NextPointer

    Node[NewNode].Data ← Value
    Node[NewNode].NextPointer ← -1

    IF Head = -1 THEN
        Head ← NewNode
        Tail ← NewNode
    ELSE
        Node[Tail].NextPointer ← NewNode
        Tail ← NewNode
    ENDIF
ENDPROCEDURE
```

### Insert at Start

```
PROCEDURE InsertAtStart(Value : INTEGER)
    DECLARE NewNode : INTEGER
    NewNode ← Free
    Free ← Node[Free].NextPointer

    Node[NewNode].Data ← Value
    Node[NewNode].NextPointer ← Head
    Head ← NewNode

    IF Tail = -1 THEN
        Tail ← NewNode
    ENDIF
ENDPROCEDURE
```

### Insert in Middle (after a given node)

```
PROCEDURE InsertAfter(Value : INTEGER, AfterNode : INTEGER)
    DECLARE NewNode : INTEGER
    NewNode ← Free
    Free ← Node[Free].NextPointer

    Node[NewNode].Data ← Value
    Node[NewNode].NextPointer ← Node[AfterNode].NextPointer
    Node[AfterNode].NextPointer ← NewNode
ENDPROCEDURE
```

---

## 4. Deletion

```
PROCEDURE DeleteNode(Value : INTEGER)
    DECLARE Current : INTEGER
    DECLARE Previous : INTEGER

    Current ← Head
    Previous ← -1

    WHILE Current <> -1 AND Node[Current].Data <> Value
        Previous ← Current
        Current ← Node[Current].NextPointer
    ENDWHILE

    IF Current <> -1 THEN
        IF Previous = -1 THEN
            Head ← Node[Current].NextPointer
        ELSE
            Node[Previous].NextPointer ← Node[Current].NextPointer
        ENDIF

        IF Current = Tail THEN
            Tail ← Previous
        ENDIF

        // Return to free list
        Node[Current].NextPointer ← Free
        Free ← Current
    ENDIF
ENDPROCEDURE
```

---

## 5. Search

```
FUNCTION Search(Value : INTEGER) RETURNS INTEGER
    DECLARE Current : INTEGER
    Current ← Head
    WHILE Current <> -1 AND Node[Current].Data <> Value
        Current ← Node[Current].NextPointer
    ENDWHILE
    RETURN Current
ENDFUNCTION
```

:::note[Tip]

Always trace your pointer updates on paper before writing code. Use a small example with 3&ndash;4 nodes and label each pointer explicitly.

:::
