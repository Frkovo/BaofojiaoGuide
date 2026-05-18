---
title: "考纲要点"
sidebar_position: 6
---

# 考纲要点

## Syllabus 20.1.2 — Inheritance

| # | Point | Exam Frequency |
|---|---|---|
| 1 | Define **inheritance**: deriving a new class from an existing class | ★☆☆ |
| 2 | Understand **parent class** (base/superclass) and **child class** (derived/subclass) | ★★★ |
| 3 | Write `class Child(Parent):` to declare inheritance | ★★★ |
| 4 | Call `super().__init__(params)` in child constructor to initialise inherited attributes | ★★★ |
| 5 | **Override** methods: redefine method with exact same name and parameters in child | ★★★ |
| 6 | Use `super().method_name()` to call parent method from child | ★★★ |
| 7 | Understand that child inherits **all** non-private attributes and methods from parent | ★★☆ |
| 8 | Child class can **add new attributes** and **new methods** not in parent | ★★★ |
| 9 | Create objects of both parent and child classes in main program | ★★★ |
| 10 | Demonstrate **polymorphism**: calling same method on parent and child objects gives different behaviour | ★★☆ |

## Inheritance Hierarchy Keywords

- **Inheritance** — `class Child(Parent):`
- **Constructor chaining** — `super().__init__(...)`
- **Method overriding** — redefine in child
- **Code reuse** — child reuses parent's code via `super()`
- **Polymorphism** — same method name, different implementations

## What You Must Be Able To Do

1. Read a parent class definition and write a child class that:
   - Calls parent constructor
   - Adds new private attributes
   - Overrides at least one method

2. Write a main program that:
   - Creates instances of both parent and child
   - Calls methods on both
   - Outputs results

3. Read data from a text file and create appropriate parent / child objects based on record type

4. Trace through inheritance code and predict output (paper 1 style)
