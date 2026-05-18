---
title: "常见错误"
sidebar_position: 5
---

# 常见错误

## Mistake 1: Forgetting `super().__init__()`

```python
# Wrong — parent attributes never initialised
class Manager(Employee):
    def __init__(self, name, id, salary, bonus):
        self._name = name       # duplicated parent logic
        self._bonus = bonus
```

```python
# Correct
class Manager(Employee):
    def __init__(self, name, id, salary, bonus):
        super().__init__(name, id, salary)
        self._bonus = bonus
```

## Mistake 2: Passing `self` to `super().__init__()`

```python
# Wrong — Python passes self automatically
super().__init__(self, name, id, salary)
```

```python
# Correct
super().__init__(name, id, salary)
```

## Mistake 3: Wrong method signature when overriding

```python
# Parent
def display_info(self):
    return f"Name: {self._name}"

# Wrong — extra parameter changes signature
def display_info(self, extra):
    return f"Name: {self._name}, {extra}"
```

The overridden method must have **exactly** the same name and parameters as the parent.

## Mistake 4: Not calling `super().method()` when required

If the question asks the child method to include parent behaviour plus new behaviour, you **must** call `super().method()`.

```python
# Wrong — reinventing parent logic
def get_info(self):
    return f"Manufacturer: {self._manufacturer}, Model: {self._model}, Blades: {self._blades}"
```

```python
# Correct — reuse parent then extend
def get_info(self):
    parent_info = super().get_info()
    return f"{parent_info}, Blades: {self._blades}"
```

## Mistake 5: Wrong attribute naming

```python
# Wrong — accessing parent private attribute incorrectly
print(self._Manufacturer__manufacturer)
```

Parent attributes accessed via `self._attr` in child class (same as parent, assuming single underscore convention).

## Mistake 6: Misaligned constructor parameters

Parent constructor expects `(name, id)` but child passes `(id, name)`. The parameter order in `super().__init__()` must **exactly** match the parent's parameter list.

## Mistake 7: Forgetting to convert types when reading from file

```python
# Wrong — all values treated as strings
age = parts[2]   # "25" instead of 25
```

```python
# Correct — convert numeric fields
age = int(parts[2])
```

## Mistake 8: Wrong indentation after `if` / `elif` in file reading

Objects created inside `if` block but not accessible outside. Use a list to store all objects.

```python
# Wrong — obj not accessible after if
if type_flag == "P":
    obj = Parent(...)
else:
    obj = Child(...)
```

```python
# Correct — store in list
objects = []
if type_flag == "P":
    objects.append(Parent(...))
else:
    objects.append(Child(...))
```
