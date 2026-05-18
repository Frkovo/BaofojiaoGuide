---
title: OOP Inheritance
sidebar_position: 1
---

# OOP Inheritance（继承）

## 考纲要求

- 20.1.2 OOP：继承、多态、方法重写

## 核心代码模板

### 父类定义
```python
class Vehicle:
    def __init__(self, ID, maxSpeed, increaseAmount):
        self.__ID = ID
        self.__MaxSpeed = maxSpeed
        self.__IncreaseAmount = increaseAmount
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def SetCurrentSpeed(self, speed):
        self.__CurrentSpeed = speed

    def SetHorizontalPosition(self, pos):
        self.__HorizontalPosition = pos

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed
```

### 子类继承 + 方法重写
```python
class Helicopter(Vehicle):
    def __init__(self, ID, maxSpeed, increaseAmount, verticalChange, maxHeight):
        super().__init__(ID, maxSpeed, increaseAmount)
        self.__VerticalPosition = 0
        self.__VerticalChange = verticalChange
        self.__MaxHeight = maxHeight

    def GetVerticalPosition(self):
        return self.__VerticalPosition

    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        super().IncreaseSpeed()
```

### 另一个继承例子（Manager 继承 Employee）
```python
class Employee:
    def __init__(self, hourlyPay, empNum, jobTitle):
        self.__HourlyPay = hourlyPay
        self.__EmployeeNumber = empNum
        self.__JobTitle = jobTitle
        self.__PayYear = [0.0] * 52

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, weekNum, hours):
        self.__PayYear[weekNum] = self.__HourlyPay * hours

    def GetTotalPay(self):
        total = 0.0
        for i in range(52):
            total = total + self.__PayYear[i]
        return total

class Manager(Employee):
    def __init__(self, hourlyPay, empNum, jobTitle, bonusValue):
        super().__init__(hourlyPay, empNum, jobTitle)
        self.__BonusValue = bonusValue

    def SetPay(self, weekNum, hours):
        hours = hours + hours * self.__BonusValue / 100.0
        super().SetPay(weekNum, hours)
```

### 主程序创建对象
```python
car = Vehicle("Tiger", 100, 20)
heli = Helicopter("Lion", 350, 40, 3, 100)

car.IncreaseSpeed()
car.IncreaseSpeed()
print(car.GetCurrentSpeed(), car.GetHorizontalPosition())

heli.IncreaseSpeed()
heli.IncreaseSpeed()
print(heli.GetCurrentSpeed(), heli.GetHorizontalPosition())
print(heli.GetVerticalPosition())
```

## 常见错误

- 子类构造器忘记调用 `super().__init__()`
- 重写方法时签名不一致
- 忘记把属性设为 private（`self.__`）
- 访问父类私有属性（应该通过 getter/setter）
