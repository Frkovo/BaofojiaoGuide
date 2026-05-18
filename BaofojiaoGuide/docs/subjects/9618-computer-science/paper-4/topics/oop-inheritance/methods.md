---
title: "解题方法"
sidebar_position: 3
---

# 解题方法

## Python Inheritance Syntax 模板

```python
# Parent class (given in question)
class Parent:
    def __init__(self, attr1, attr2):
        self._attr1 = attr1
        self._attr2 = attr2

    def method(self):
        return f"{self._attr1}, {self._attr2}"

# Child class (you write this)
class Child(Parent):
    def __init__(self, attr1, attr2, attr3):
        super().__init__(attr1, attr2)     # call parent constructor
        self._attr3 = attr3                # new attribute

    def method(self):                      # override
        parent_part = super().method()     # call parent version
        return f"{parent_part}, {self._attr3}"
```

## Step-by-Step

1. **Class header** — `class ChildName(ParentName):` with colon
2. **Constructor** — `def __init__(self, all_params_including_parents):`
3. **super().__init__()** — pass only the parent's parameters (NOT `self`, NOT child-only params)
4. **Child attributes** — `self._new_attr = param` for each new attribute
5. **Override method** — same name and same parameters as parent
6. **super().method()** — call parent version if needed (usually for accumulation)
7. **Add new logic** — append / modify the result for child-specific behaviour

## Key Rules

- `super().__init__(...)` must be the **first line** in the child constructor
- Constructor parameters **include** parent parameters **plus** any new ones
- Overridden method must have **exactly** the same signature (name + params) as parent
- Use `super().method()` to call parent's version — do **not** repeat parent logic manually
- New attributes / methods not in parent are **only** available on child objects

## Common Variations

| Variation | Pattern |
|---|---|
| Parent with default params | `super().__init__()` with matching defaults |
| Parent without constructor | Child may not need `super().__init__()` but still call it for clarity |
| Chained inheritance | `class GrandChild(Child):` with `super().__init__()` through the chain |
| Read file → create objects | Parse data, use `if` to decide parent or child constructor |
