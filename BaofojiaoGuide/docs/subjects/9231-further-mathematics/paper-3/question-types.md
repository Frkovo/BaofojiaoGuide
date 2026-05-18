---
title: 题型分析
sidebar_position: 8
---

# Paper 3 题型总览

## 六种核心题型

| 题型 | 所属 Topic | 典型分值 |
|------|-----------|---------|
| Type 1: 抛射运动参数与轨迹 | Motion of a projectile | 7–10 |
| Type 2: 刚体平衡 & 倾倒判断 | Equilibrium of a rigid body | 8–12 |
| Type 3: 圆周运动向心力分析 | Circular motion | 7–10 |
| Type 4: 胡克定律与弹性系统 | Hooke's law | 7–10 |
| Type 5: 变力下的微分方程建模 | Linear motion under a variable force | 7–10 |
| Type 6: 碰撞与恢复系数 | Momentum | 6–9 |

## 详细题型分析

### Type 1: Motion of a projectile（抛射运动）

| 项目 | 内容 |
|------|------|
| **识别方法** | 题目中出现 particle projected、initial speed $V$、angle $\theta$、above horizontal 等关键词 |
| **标准解法** | (1) 建立 $x = Vt\cos\theta$、$y = Vt\sin\theta - \frac12 gt^2$；(2) 联立消去 $t$ 得轨迹方程；(3) 求最大高度、水平射程、某时刻速度 |
| **评分模式** | 参数方程 **M1**、消 $t$ 得轨迹 **M1**、代入数值 **A1** |
| **变体** | 不同水平面抛射、抛射点不在原点、求包络线（envelope） |

### Type 2: Equilibrium of a rigid body（刚体平衡）

| 项目 | 内容 |
|------|------|
| **识别方法** | rod、ladder、beam、toppling、slipping、coefficient of friction $\mu$ |
| **标准解法** | (1) 画受力图，标注所有力的作用点；(2) $\sum F_x=0$、$\sum F_y=0$；(3) 取某点力矩平衡 $\sum M=0$；(4) 联立求解 |
| **评分模式** | 正确受力图 **M1**、力矩方程 **M1**、解得正确值 **A1** |
| **变体** | 组合体质心计算、最小 $\mu$ 分析、同时考虑倾覆与滑动 |

### Type 3: Circular motion（圆周运动）

| 项目 | 内容 |
|------|------|
| **识别方法** | conical pendulum、banked track、vertical circle、loses contact、$R=0$ |
| **标准解法** | (1) 确定向心力方向（指向圆心）；(2) $F_{\text{centripetal}} = mr\omega^2 = mv^2/r$；(3) 水平圆周用 $T\sin\theta$ 或 $N\sin\theta$ 提供向心力；(4) 竖直圆周结合能量守恒求不同位置速度 |
| **评分模式** | 向心力表达式 **M1**、能量守恒方程 **M1**、代入求解 **A1** |
| **变体** | 倾斜轨道、光滑/粗糙表面、带 $g$ 的数值计算 |

### Type 4: Hooke's law（胡克定律）

| 项目 | 内容 |
|------|------|
| **识别方法** | 题目提到 elastic string/spring、natural length $l$、modulus of elasticity $\lambda$ |
| **标准解法** | (1) 判断伸长量 $x$；(2) 弹力 $T = \frac{\lambda}{l}x$；(3) 弹性势能 $\text{EPE} = \frac{\lambda x^2}{2l}$；(4) 结合能量守恒 $KE + GPE + EPE = \text{constant}$ |
| **评分模式** | 弹力公式正确 **M1**、弹性势能公式正确 **M1**、能量守恒方程 **M1**、最终答案 **A1** |
| **变体** | 多弹性体系统、弹性绳与刚体的连接、SHM 简谐振动前兆 |

### Type 5: Linear motion under a variable force（变力作用下的直线运动）

| 项目 | 内容 |
|------|------|
| **识别方法** | resistance $kv$ / $kv^2$、variable force、$F = m\frac{dv}{dt}$、$v\frac{dv}{dx}$、terminal speed |
| **标准解法** | (1) 根据 $F=ma$ 写出 $m\frac{dv}{dt} = \text{net force}$；(2) 分离变量求解 $v(t)$ 或 $x(t)$；(3) 或用 $v\frac{dv}{dx}$ 转化为关于位移的形式 |
| **评分模式** | 微分方程正确 **M1**、分离变量/积分 **M1**、初值条件代入 **A1** |
| **变体** | 阻力与速度成正比 $kv$、与 $v^2$ 成正比、同时含其他力（重力、牵引力） |

### Type 6: Momentum（动量）

| 项目 | 内容 |
|------|------|
| **识别方法** | collision、impact、coefficient of restitution $e$、direct/oblique impact、impulse |
| **标准解法** | (1) 正碰：动量守恒 + NEL 联立；(2) 斜碰：沿 line of centres 方向用 NEL，垂直方向速度不变；(3) 球与固定面：$e = \frac{\text{speed after}}{\text{speed before}}$、冲量 $I = m(v-u)$ |
| **评分模式** | 动量守恒 **M1**、NEL 正确 **M1**、联立求解 **A1** |
| **变体** | 三球连续碰撞、斜碰+求能量损失比例、碰撞后运动方向分析 |
