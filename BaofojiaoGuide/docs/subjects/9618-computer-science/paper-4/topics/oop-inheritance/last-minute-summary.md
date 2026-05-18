---
title: "考前速记"
sidebar_position: 7
---

# 考前速记

## Inheritance Quick Template

```python
class Child(Parent):
    def __init__(self, p1, p2, c1):          # all params including parent's
        super().__init__(p1, p2)             # 1st line — call parent
        self._c1 = c1                        # child-specific attributes

    def override_method(self):
        base = super().override_method()     # reuse parent behaviour
        return base + child_extra            # extend it
```

## 5-Step Checklist

- [ ] 1. `class Child(Parent):` — colon at end
- [ ] 2. `def __init__(self, ...):` — include ALL parent params + new ones
- [ ] 3. `super().__init__(...)` — only parent params, NO `self`
- [ ] 4. `self._new_attr = value` — initialise each new attribute
- [ ] 5. Override method — exact same signature, `super().method()` if needed

## File + Inheritance Pattern

```python
def load(filename):
    items = []
    with open(filename) as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == "P":
                items.append(Parent(data[1], data[2]))
            else:
                items.append(Child(data[1], data[2], data[3]))
    return items
```

## Common Traps — Last Look

| Trap | Fix |
|---|---|
| `super().__init__(self, ...)` | Remove `self` |
| Wrong param order in `super().__init__` | Match parent exactly |
| Missing colon on class header | Add `:` |
| Override with different params | Match parent signature |
| Not converting `int()` from file | Wrap numeric fields |
| Object created inside `if` lost | Use `list.append()` |

## Polymorphism in One Line

```python
for obj in [Parent("a", 1), Child("b", 2, 3)]:
    print(obj.method())            # different output for each
```
