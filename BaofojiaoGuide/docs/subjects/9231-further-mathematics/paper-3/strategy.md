---
title: 答题策略
sidebar_position: 9
---

# Paper 3 答题策略

## 前 5 分钟

1. 快速浏览全部题目（5–7 题）
2. 标记每个题的 Topic——每题通常只考 1–2 个 Topic
3. 优先做最擅长的 Topic，保证基础分
4. 注意题中给的数值——$g$ 通常取 10，特殊值会说明
5. 留意是否要"保留精确形式"还是"3 s.f."

## 各 Topic 策略

### 3.1 Motion of a projectile（7–10 分）
- **第一时间写出** $x = Vt\cos\theta$、$y = Vt\sin\theta - \frac12 gt^2$
- 求轨迹方程时，用 $t = x/(V\cos\theta)$ 代入 $y$ 表达式
- 求最大高度：$v_y = 0$ 时
- 求水平射程：$y = 0$ 时
- 关键：速度方向用 $\tan\alpha = v_y/v_x$，速率用 $v = \sqrt{v_x^2 + v_y^2}$

:::tip[高频考点]
抛射点与落地点不在同一水平面——此时不能直接用公式 $R = V^2\sin 2\theta/g$，需从头列方程。
:::

### 3.2 Equilibrium of a rigid body（8–12 分）
- **受力图是第一关**——所有力的作用点必须准确标注
- 力矩平衡：选择使未知力最少的点取矩（通常选支点或接触点）
- 木梯问题（ladder）：地面和墙壁都有法向力和摩擦力
- Toppling：检查重心是否超出支撑面边界
- 滑动条件：$F \le \mu R$，临界时取等号

:::warning[常见遗漏]
力矩方程中只考虑**垂直于力臂方向的分量**。力臂长度是点到力的垂直距离。
:::

### 3.3 Circular motion（7–10 分）
- 向心力**不是独立力**，是合力沿径向的分量
- 水平圆周：$T\sin\theta = mr\omega^2$、$T\cos\theta = mg$
- 竖直圆周：能量守恒求速度，$F_{\text{centripetal}} = mg\cos\theta + R$
- "失去接触" = $R = 0$，此时向心力完全由重力分量提供

### 3.4 Hooke's law（7–10 分）
- **务必区分 natural length $l$ 和 extension $x$**
- $T = \frac{\lambda}{l} \times \text{extension}$
- 弹性势能公式注意 $\frac12$ 因子
- 多段弹性绳：总 EPE 是各段之和
- 能量守恒法通常比牛顿法更快

### 3.5 Linear motion under a variable force（7–10 分）
- 解题三步：**(1) 列方程 (2) 分离变量 (3) 积分 + 初值条件**
- 阻力 $kv$：$\frac{dv}{dt} = -g - kv$（下抛）或 $-g + kv$（上抛），注意符号
- Terminal speed：令 $dv/dt = 0$ 解得
- $v\frac{dv}{dx}$ 方法适合求 $v$ 关于 $x$ 的表达式

### 3.6 Momentum（6–9 分）
- 正碰：动量守恒 + NEL，解二元一次方程组
- 斜碰：沿碰撞线（line of centres）方向分析，**垂直方向速度不变**
- 球与球之间的碰撞：分清哪个是 $u_1, u_2, v_1, v_2$
- 冲量 $I$：对 A 是 $m(v_A - u_A)$，对 B 是 $m(v_B - u_B)$，大小相等方向相反

:::info[能量损失]
碰撞动能损失 $= \frac12 (1-e^2) \times \frac{m_1 m_2}{m_1+m_2} (u_1 - u_2)^2$，直接使用需证明或熟记。
:::

## 最后 10 分钟

- [ ] 所有数值答案标单位了？
- [ ] 答案精度符合要求（3 s.f.，角度 1 d.p.）？
- [ ] 微分方程代初值了？
- [ ] 轨迹方程、速度公式的符号检查过？
- [ ] 动量守恒的方向符号一致？
- [ ] 是否有题目空着？至少写个公式或受力图
- [ ] 检查 $g$ 用的是 10 还是 9.8？
- [ ] 弹性势能公式 $\frac{\lambda x^2}{2l}$ 不是 $\frac12 kx^2$？
