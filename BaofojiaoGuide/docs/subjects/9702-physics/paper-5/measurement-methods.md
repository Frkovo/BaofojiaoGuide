---
title: 测量方法秘籍（完整版）
sidebar_position: 11
---

# 测量方法秘籍（完整版）

Paper 5 Q1 核心技能：**说到什么量，立刻知道用什么测、怎么测、MS 认什么不认什么。**

---

## 一、长度测量

### 仪器选择总表

| 场景 | 仪器 | 精度 | 操作方法 | MS 给分关键词 | MS 不给分 |
|------|------|------|---------|-------------|----------|
| 线/丝/细棒直径 $d$ | 千分尺 micrometer screw gauge | $\pm 0.01$ mm | 夹住线径，读取刻度，不同位置测 3 次取平均 | "measure diameter using micrometer" | "use ruler"（精度不够） |
| 弹簧金属丝厚度 $t$ | 千分尺 micrometer | $\pm 0.01$ mm | 同线径 | "use micrometer to measure thickness" | "use ruler" |
| 弹簧自然长度/伸长 $x$ | 米尺 metre ruler | $\pm 1$ mm | 先测初始长度，加载后测最终长度，相减得伸长 | "measure initial and final positions using ruler and subtract" | 不说明 initial+final |
| 两线圈中心距离 $d$ | 米尺 metre ruler | $\pm 1$ mm | 线圈中心对齐 ruler 刻度 | "measure distance between centres using metre ruler" | "estimate by eye" |
| 弦/绳/ cord 长度 $L$ | 米尺 metre ruler | $\pm 1$ mm | 拉直后用 ruler 测量 | "measure length using ruler" | 不拉直直接测 |
| 驻波波长 $\lambda$ | 米尺 metre ruler | $\pm 1$ mm | 测相邻 node 间距 ×2，或测 $n$ 个 node 间距 ÷$n$×2 | "measure distance between adjacent nodes using ruler" | 只说 "measure wavelength" |
| 管/筒/柱的直径 $D$ | 游标卡尺 vernier calipers | $\pm 0.1$ mm | 卡住最宽处测量 | "use vernier calipers" | "use ruler"（直径小） |
| 液面高度 $h$（毛细管） | 读数显微镜 travelling microscope | $\pm 0.1$ mm | 对焦液面，读取刻度 | "use travelling microscope" | "use ruler"（精度不够） |
| 板的长宽 $l \times w$ | 米尺 / 卡尺 | $\pm 1$ / $\pm 0.1$ mm | 根据尺寸大小选 | "measure length and width using ruler / calipers" | — |
| 两点间位移 $s$ | 米尺 / 卷尺 | $\pm 1$ mm | 测量起点到终点的直线距离 | "measure distance using ruler / tape measure" | — |

### 各场景详细方法

#### 1. 测金属丝/弹簧丝直径 $d$ ★★★★★（每年必考）

**为什么重要：** 几乎所有机械类实验都需要从 $d$ 算横截面积 $A$。

:::note[标准操作]
1. 使用 micrometer screw gauge
2. 在金属丝的不同位置（至少 3 处）测量直径
3. 计算平均值 $\bar{d}$
4. 横截面积 $A = \pi \bar{d}^2 / 4$
5. 每次测量前检查 zero error
:::

**MS 评分标准：**
- **M1**: "measure diameter $d$ using micrometer" — 说出正确仪器就得 1 分
- **A1**: "repeat measurements at different positions and average"
- **不接受**: "use ruler to measure diameter"（精度不够）
- **不接受**: 只测一次不重复

**过去试卷中出现的方式：**
- s20_51: "measure $A$ using micrometer/calipers ($A = \pi d^2/4$)"
- w20_51: "measure $t$ using micrometer"
- s20_52: "use micrometer to measure diameter of cord"

**安全注意事项：**  micrometer 的 ratchet 应轻柔旋紧，不要夹得太紧导致丝变形。

---

#### 2. 测弹簧伸长量 $x$ ★★★★★

**常见错误：** 直接说 "measure $x$"，不说明怎么测。

:::note[标准操作]
1. 用 ruler 测量弹簧自然状态下的初始长度 $L_0$
2. 挂上负载后测量最终长度 $L$
3. 伸长量 $x = L - L_0$
4. 确保弹簧垂直（用 set square 检查 ruler 是否垂直）
5. 在不同位置测 $L$ 取平均（或重复实验）
:::

**MS 评分标准：**
- **M1**: "measure initial and final positions using ruler" — 必须强调 initial + final
- **M1**: "use set square to ensure ruler is vertical"
- **不接受**: 只说 "measure extension with ruler" 没有 initial/final

**特殊场景：** 如果 $x$ 很小（< 1 cm），应考虑用 vernier calipers 代替 ruler，或者增加质量使伸长量更大。

---

#### 3. 测绳/弦/ cord 的线密度 $\mu$ ★★★★

:::note[标准操作]
1. 用 ruler 量出一段已知长度 $L$ 的 cord（越长越好，减少误差）
2. 用 top-pan balance 称量这段 cord 的质量 $m$
3. 线密度 $\mu = m / L$
4. 重复 3 次取平均
:::

**MS 评分标准：**
- **M1**: "measure mass of a known length using top-pan balance"
- **A1**: "repeat and average"
- **不接受**: 直接说 "use $\mu$" 没有说明如何测量

---

#### 4. 测驻波波长 $\lambda$ ★★★★

:::note[标准操作]
1. 找到波腹（antinode）位置或节点（node）位置
2. 用 ruler 测量相邻两个节点之间的距离 $d$
3. 波长 $\lambda = 2d$（因为节点间距是半波长）
4. 或测量 $n$ 个节点跨越的总距离 $D$，$\lambda = 2D/(n-1)$
5. 在该状态下固定频率，重复测量取平均
:::

**MS 评分标准：**
- **M1**: "measure distance between adjacent nodes using ruler"
- **M1**: "$\lambda = 2 \times$ distance between adjacent nodes"
- **不接受**: "measure wavelength directly"

---

#### 5. 测液面高度 $h$ ★★★

**三种场景不同方法：**

| 场景 | 方法 | MS |
|------|------|-----|
| 烧杯/量筒中液面 | 用 ruler 测水面到杯底的距离 | "use ruler to measure height of liquid" |
| 毛细管中液面 | 用 travelling microscope 对焦弯月面底部 | "use travelling microscope focused on meniscus" |
| 连通管/容器中液面 | 用 ruler + set square 确保水平视线 | "use set square to avoid parallax error" |

---

## 二、时间测量

### 仪器选择总表

| 场景 | 仪器 | 精度 | 操作方法 | MS 给分 | MS 不给分 |
|------|------|------|---------|--------|----------|
| 单摆/振荡周期 | stopwatch | $\pm 0.1$ s | 测 10-20 个周期，除以次数 | "time 10 oscillations using stopwatch" | 只测 1 个周期 |
| 物体通过光 gate | light gate + timer | $\pm 0.001$ s | 卡片通过时自动计时 | "use light gate connected to timer/data logger" | 用 stopwatch 测 |
| 两个光 gate 求加速度 | 2 light gates + ruler | $\pm 0.001$ s | 测通过每 gate 的时间和间距 | "use two light gates and measure distance between them" | — |
| 电容放电 $t$ | stopwatch | $\pm 0.1$ s | 开关打开时开始计时 | "start stopwatch when switch is opened" | 不说明何时开始 |
| 频闪/振动 $f$ | oscilloscope | $\pm 0.01$ s | 看波形读周期 | "use CRO to measure period, $f=1/T$" | 用 stopwatch 测 |
| 快速运动（落体） | video camera | $\pm 0.02$ s | 逐帧回放 | "use video camera with frame-by-frame analysis" | 用 stopwatch 目测 |
| 连续自动记录 | data logger | $\pm 0.001$ s | 传感器接 data logger | "use data logger to record data automatically" | 手工记录 |

### 各场景详细方法

#### 1. 测周期 $T$（单摆/弹簧振子/振荡） ★★★★★

:::note[标准操作]
1. 让系统开始振荡，等待几秒使运动稳定
2. 用 stopwatch 测量 10 个（或 20 个）完整周期的时间 $t$
3. 周期 $T = t / 10$
4. 重复实验 3 次取平均
5. 不确定度 = 半范围 / 次数
:::

**MS 评分标准：**
- **M1**: "time 10 oscillations using stopwatch and divide by 10"
- **A1**: "repeat and calculate mean"
- **不接受**: "time one oscillation"（误差太大）
- **不接受**: "use stopwatch" 没有说明测量多少个周期

**常见陷阱：**
- 计数时从 0 开始而不是从 1（"0, 1, 2, ... 10" = 10 个周期）
- 振幅过大（应保持小振幅，$<10^\circ$ 对于单摆）

---

#### 2. 测速度 $v$（light gate 法） ★★★★

:::note[标准操作]
1. 在运动物体上固定一片已知长度 $l$ 的 card（interrupt card）
2. 用 ruler 测量 card 的长度 $l$
3. 物体通过 light gate，timer 记录遮挡时间 $t$
4. 速度 $v = l / t$
5. 重复实验取平均
:::

**MS 评分标准：**
- **M1**: "measure length of card using ruler"
- **M1**: "measure time using light gate connected to timer"
- **A1**: "$v = \text{length of card} / \text{time}$"
- **不接受**: 不说明 card 长度如何测量
- **不接受**: 用 stopwatch 测速度

---

#### 3. 测加速度 $a$（两光 gate 法） ★★★★

:::note[标准操作]
1. 沿运动路径放置两个 light gates，间距 $s$
2. 用 ruler 测量两个 light gate 之间的距离 $s$
3. 物体依次通过两个 gate，分别记录时间 $t_1$ 和 $t_2$
4. 计算经过每个 gate 的速度：
   - $v_1 = l / t_1$，$v_2 = l / t_2$（$l$ 为 card 长度）
5. $v_2^2 = v_1^2 + 2as \Longrightarrow a = (v_2^2 - v_1^2) / (2s)$
:::

**MS 评分标准：**
- **M1**: "use two light gates, measure distance between them using ruler"
- **M1**: "calculate velocity at each gate using $v = l / t$"
- **A1**: "$a = (v_2^2 - v_1^2) / 2s$"
- **不接受**: 直接测加速度（加速度不能直接测量）

**也可以：** 如果物体从静止释放，可以用一个 light gate 测不同位置 $s$ 处的 $v$，画 $v^2$ vs $s$，梯度 $= 2a$。

---

#### 4. 测频率 $f$（oscilloscope 法） ★★★

:::note[标准操作]
1. 将信号输入 oscilloscope
2. 调整 time-base 旋钮使屏幕上显示 1-3 个完整周期
3. 读取一个周期在屏幕上的水平距离 $D$（格数）
4. 读取 time-base 设定值 $T_{\text{base}}$（秒/格）
5. 周期 $T = D \times T_{\text{base}}$
6. 频率 $f = 1 / T$
:::

**MS 评分标准：**
- **M1**: "use CRO / oscilloscope to measure period"
- **M1**: "$T = \text{time-base} \times \text{horizontal distance}$"
- **A1**: "$f = 1 / T$"
- **不接受**: 不知道 time-base 的含义

**关于电压测量（同一仪器）：**
$$V_{\text{peak}} = \text{y-gain} \times \text{vertical distance（格数）}$$

---

## 三、质量与力的测量

### 质量测量

| 仪器 | 精度 | 适用范围 | MS 关键词 |
|------|------|---------|----------|
| top-pan balance（托盘天平） | $\pm 0.1$ g | 通用，可称弹簧/重物/液体 | "use top-pan balance" |
| digital balance（电子天平） | $\pm 0.01$ g 或 $\pm 0.001$ g | 精密称量 | "use digital balance" |
| spring balance（弹簧秤） | $\pm 0.1$ N | 直接测力，不精确 | "use spring balance / newton meter" |

**MS 注意事项：**
- "measure mass using top-pan balance" 就已足够，不需要说平衡步骤
- 如果质量已知（如标准砝码），说 "use masses of known value" 即可
- **不接受**: "weigh it"（太模糊，要说明用什么称）

### 力的测量

#### 方法 1：用已知质量产生力 ★★★★★

:::note[标准操作]
1. 用 top-pan balance 测量质量 $m$
2. 重力 $F = mg$（$g = 9.81\ \text{m s}^{-2}$）
3. 适用于：绳子张力、弹簧拉力、斜面上的分力
:::

**MS 评分标准：**
- **M1**: "add masses of known mass to produce force $mg$"
- **A1**: "measure mass using balance"
- **不接受**: 只说 "use force" 不说明怎样产生

#### 方法 2：用 newton meter 直接测力

- **M1**: "use newton meter to measure force"
- 适用于：摩擦力、推力、弹簧弹力的直接测量
- 注意 newton meter 需要先检查 zero error

#### 方法 3：弹簧常数 $k$ 的测定 ★★★★★

:::note[标准操作]
1. 将弹簧固定，挂上已知质量 $m$ 的砝码
2. 用 ruler 测伸长量 $x$
3. 由 $F = kx$ 得 $k = mg / x$
4. 换不同质量重复，画 $F$ vs $x$，梯度 $= k$
:::

**MS 评分标准：**
- **M1**: "determine $k$ from $F = kx$ by adding masses and measuring extension"
- **A1**: "plot graph of $F$ against $x$, gradient $= k$"

---

## 四、温度测量

### 仪器选择总表

| 场景 | 仪器 | 精度 | 响应速度 | MS 关键词 |
|------|------|------|---------|----------|
| 常规液体/空气温度 | 玻璃液体 thermometer | $\pm 0.5^\circ$C | 慢（需等待热平衡） | "use thermometer" |
| 高温炉 / 快速变化 | 热电偶 thermocouple | $\pm 0.1^\circ$C | 快 | "use thermocouple" |
| 连续监测 + 记录 | 热敏电阻 thermistor + data logger | $\pm 0.1^\circ$C | 快 | "use temperature sensor connected to data logger" |
| 表面温度 / 不能接触 | 红外测温仪 infrared thermometer | $\pm 0.5^\circ$C | 瞬时 | "use infrared thermometer" |

### 各场景详细方法

#### 1. 冷却/加热实验 ★★★★★

:::note[标准操作]
1. 将 thermometer 浸入液体中（完全浸没，不碰底）
2. 等待读数稳定后再记录（热平衡）
3. 每次读数前搅拌液体使温度均匀
4. 按设定的时间间隔（如每 30 s）记录温度
5. 室温用另一支 thermometer 放在远离实验台的地方测量
:::

**MS 评分标准：**
- **M1**: "measure temperature using thermometer"
- **M1**: "stir liquid before each reading"
- **M1**: "measure room temperature using separate thermometer"
- **A1**: "allow time for thermal equilibrium"
- **不接受**: 不搅拌直接读

#### 2. 比热容实验

:::note[标准操作]
1. 用 top-pan balance 测物体的质量 $m$
2. 用电加热器加热，记录加热功率 $P$ 和时间 $t$
3. 用 thermometer 测温度变化 $\Delta\theta$
4. $E = Pt = mc\Delta\theta$
:::

---

## 五、电学测量

### 仪器总表

| 仪器 | 符号 | 测量量 | 接法 | MS 关键词 |
|------|------|-------|------|----------|
| ammeter | $A$ | 电流 $I$ | **串联** in series with component | "ammeter in series" |
| voltmeter | $V$ | 电压 $V$ | **并联** in parallel across component | "voltmeter in parallel" |
| ohmmeter | $\Omega$ | 电阻 $R$ | 直接接被测元件两端 | "use ohmmeter / multimeter set to $\Omega$" |
| multimeter | — | $I$/$V$/$R$ | 选择对应模式 | "use digital multimeter" |
| oscilloscope / CRO | — | 电压/频率/周期 | 探头并接 | "use oscilloscope / CRO" |
| signal generator | — | 输出交流信号 | 接电路 | "use signal generator" |
| Hall probe | — | 磁通密度 $B$ | 垂直磁场，接 voltmeter | "use Hall probe connected to voltmeter" |
| search coil | — | 磁通密度 $B$ | 靠近磁场，接 CRO | "use search coil + CRO" |

### 关键注意事项（MS 特别看重的）

:::warning[电学接法红线]
- **ammeter 必须串联**，不能并接（否则短路烧毁）
- **voltmeter 必须并联**，不能串接（否则开路）
- 如果不确定，就说 "connect multimeter in series to measure current, in parallel to measure voltage"
- **电源极性**：注意正负极不要接反（直流）
- **开关**：改接电路前先断开开关
:::

### 各场景详细方法

#### 1. 测电阻 $R$（伏安法）★★★★

:::note[标准操作]
1. 用 voltmeter 并接在电阻两端测 $V$
2. 用 ammeter 串接在电路中测 $I$
3. $R = V/I$
4. 改变电源电压（或变阻器）得到多组 $(V, I)$
5. 画 $V$ vs $I$ 图，梯度 $= R$
:::

**MS 评分标准：**
- **M1**: "measure $V$ using voltmeter in parallel and $I$ using ammeter in series"
- **A1**: "$R = V/I$"
- **不接受**: 只说 "use ohmmeter"（有些场景必须伏安法）
- **不接受**: 伏安法但接反 ammeter 和 voltmeter 的位置

#### 2. 测电阻 $R$（ohmmeter direct）★★★

**适用范围：** 电阻不在通电电路中，单独测量时。

**MS**: "use ohmmeter / multimeter set to resistance mode"

#### 3. 测电源电动势 $\mathcal{E}$ 和内阻 $r$ ★★★★

:::note[标准操作]
1. 将电源、开关、变阻器 $R$、ammeter 串联
2. voltmeter 并接在电源两端
3. 改变 $R$，记录多组 $(V, I)$
4. 由 $V = \mathcal{E} - Ir$ 得：
   - 画 $V$ vs $I$，y-intercept $= \mathcal{E}$，gradient $= -r$
:::

**MS 评分标准：**
- **M1**: "record current $I$ and terminal p.d. $V$ for different $R$"
- **M1**: "plot graph of $V$ against $I$"
- **A1**: "$y$-intercept $= \mathcal{E}$, gradient $= -r$"

#### 4. 测电容 $C$（RC 放电法）★★★★★

:::note[标准操作]
1. 将电容 $C$ 通过电阻 $R$ 充电至电压 $V_0$
2. 断开电源，开始放电，同时启动 stopwatch
3. 用 voltmeter 记录不同时间 $t$ 的电压 $V$
4. 由 $V = V_0 e^{-t/RC}$：
   - 画 $\ln V$ vs $t$，gradient $= -1/RC$
   - $C = -1 / (R \times \text{gradient})$
:::

**MS 评分标准：**
- **M1**: "charge capacitor then discharge through known resistance $R$"
- **M1**: "measure $V$ at different $t$ using voltmeter and stopwatch"
- **A1**: "plot $\ln V$ against $t$, use gradient to find $C$"

#### 5. 用 oscilloscope 测交流信号 ★★★

**电压测量：**
$$V_{\text{peak}} = \text{y-gain setting (V/div)} \times \text{peak-to-peak height (div)} / 2$$

**频率测量：**
$$T = \text{time-base setting (s/div)} \times \text{one cycle width (div)}$$
$$f = 1/T$$

**MS 评分标准：**
- **M1**: "use CRO to measure voltage: $V = \text{y-gain} \times \text{vertical displacement}$"
- **M1**: "use CRO to measure frequency: $T = \text{time-base} \times \text{horizontal distance}$"

#### 6. 测电阻率 $\rho$（金属丝）★★★★

:::note[标准操作]
1. 用 micrometer 在多个位置测金属丝直径 $d$，平均
2. 横截面积 $A = \pi d^2/4$
3. 用 ruler 测金属丝长度 $L$
4. 用 ohmmeter 测电阻 $R$
5. $\rho = RA / L$
:::

**MS 评分标准：**
- **M1**: "measure $d$ using micrometer, $L$ using ruler, $R$ using ohmmeter"
- **A1**: "$\rho = RA/L$"

#### 7. 用 Hall probe 测磁场 $B$ ★★★

:::note[标准操作]
1. 将 Hall probe 放入磁场中，**探头平面垂直于磁场方向**
2. 将 Hall probe 连接到 voltmeter（或 data logger）
3. 读取 Hall 电压 $V_H$
4. $B = V_H / (kI)$（其中 $k$ 为探头灵敏度，$I$ 为探头电流）
5. 在不同位置测量 $B$，研究磁场分布
:::

**MS 评分标准：**
- **M1**: "use Hall probe connected to voltmeter"
- **M1**: "ensure probe is perpendicular to magnetic field"
- **不接受**: 将 Hall probe 平行于磁场放置

#### 8. 用 search coil 测交流磁场 ★★

:::note[标准操作]
1. 将 search coil 靠近磁场源，两端接 oscilloscope
2. 由感应电压 $V_{\text{ind}}$ 和频率 $f$ 推算 $B$
3. $V_{\text{ind}} = 2\pi f NAB$（其中 $N$ 为 coil 匝数，$A$ 为面积）
:::

---

## 六、角度测量

### 仪器选择

| 场景 | 仪器 | MS 关键词 |
|------|------|----------|
| 需要直接读数 | protractor 量角器 | "use protractor to measure angle" |
| 倾斜面角度 | protractor + set square | "measure angle using protractor" |
| 从长度算角度 | $\tan\theta = \text{opp}/\text{adj}$ | "determine $\theta$ from measured lengths" |
| 小角度近似 | $\sin\theta \approx \theta \approx \tan\theta$ | "use small angle approximation" |
| 需要高精度 | inclinometer / tilt sensor | "use inclinometer" |

### 测角度时的注意事项

**用 protractor 时：**
- 确保 protractor 的基线与被测边对齐
- 视线垂直刻度以减少 parallax error
- 用 set square 辅助对齐

**用长度算出角度时：**
$$\theta = \tan^{-1}\left(\frac{\text{opposite}}{\text{adjacent}}\right)$$

这种方法通常比 protractor 更精确，MS 也接受。

---

## 七、密度、面积、体积

### 横截面积 $A$

**圆形（wire/string/cord）：**
$$A = \frac{\pi d^2}{4}$$
- **必须用 micrometer** 测直径 $d$（因为 $d$ 通常小于 1 mm）
- 多处测量取平均

**矩形板/条：**
$$A = l \times w$$
- 用 ruler 或 vernier calipers 测量长和宽

**方形线：**
$$A = \text{side}^2$$
- 测边长用 micrometer

### 体积 $V$

**规则物体：** $V = l \times w \times h$（用 ruler 测尺寸）

**不规则物体：**
- 排水法 — 用 measuring cylinder
- MS: "measure volume using displacement method with measuring cylinder"

**液体体积：**
- 用 measuring cylinder
- MS: "measure volume using measuring cylinder"
- 注意读弯月面底部（透明液体）/ 顶部（不透明液体）

### 密度 $\rho$

$$\rho = \frac{m}{V}$$

**标准操作：**
1. 用 top-pan balance 测质量 $m$
2. 用上述方法测体积 $V$
3. 重复 3 次取平均

---

## 八、光学测量

### 透镜焦距 $f$

:::note[标准操作]
1. 将透镜放在光具座（optical bench）上
2. 物（ illuminated object）放在透镜一侧
3. 屏（screen）放在另一侧，移动直到成清晰像
4. 用 ruler 测量物距 $u$ 和像距 $v$
5. $$\frac{1}{f} = \frac{1}{u} + \frac{1}{v}$$
6. 改变 $u$ 得到多组 $(u, v)$，画 $1/v$ vs $1/u$ 或直接用上式计算
:::

**MS 评分标准：**
- **M1**: "measure $u$ and $v$ using ruler on optical bench"
- **A1**: "use $1/f = 1/u + 1/v$"
- **不接受**: 直接用尺量焦距（除非太阳光法）

### 放大率 $m$

$$m = \frac{\text{image height}}{\text{object height}} = \frac{v}{u}$$

- 用 ruler 测像高和物高
- MS: "measure object height and image height using ruler"

### 波长测量（衍射光栅）

$$d \sin \theta = n\lambda$$

**标准操作：**
1. 用 ruler 测光栅到屏的距离 $D$
2. 测量中央明纹到第 $n$ 级明纹的距离 $x$
3. $\sin\theta = x / \sqrt{x^2 + D^2}$
4. 已知光栅常数 $d = 1/N$（$N$ 为每毫米线数）

---

## 九、Paper 5 出场率最高的测量组合

以下是从 2020-2025 年所有试卷中统计的 **最常见测量组合**：

| 组合 | 出现次数 | 试卷示例 |
|------|---------|---------|
| 用 micrometer 测直径，算 $A = \pi d^2/4$ | 12 次 | s20_51, w20_51, s20_52, s21_52... |
| 用 stopwatch 测 10 个周期取平均 | 8 次 | s20_52, w22_51, s23_51, s24_51... |
| 用 ruler 测弹簧伸长（initial + final） | 6 次 | s20_51, w20_51, w21_52... |
| 用 top-pan balance 测质量 | 10 次 | w20_51, s21_52, s23_51, w23_52... |
| 用 ruler 测长度（$L$, $d$, $x$ 等） | 25+ 次 | 几乎每张卷子 |
| 用 ohmmeter / multimeter 测电阻 | 5 次 | s21_51, s22_52... |
| 用 voltmeter + stopwatch 测电容放电 | 6 次 | s20_51, s20_53, w21_51... |
| 用 protractor 测角度 | 4 次 | w21_52, s23_51... |
| 用 oscilloscope 测频率/电压 | 5 次 | w22_52, s23_52, s24_51... |
| 用 light gate 测速度 | 3 次 | s21_51, s21_53... |
| 用 thermometer 测温度 | 5 次 | s21_52, s24_51, s23_52... |
| 用 signal generator 提供频率 | 4 次 | s20_52, s23_52, w21_51... |

---

## 十、"见 X 测 Y" 快速口诀

:::tip[实战口诀]

**见到 length → micrometer / ruler（先看量级）**
**见到 time → stopwatch / light gate（看精度需求）**
**见到 mass → top-pan balance（永远）**
**见到 force → $mg$ 或 newton meter（$mg$ 更稳）**
**见到 temp → thermometer + stir（别忘了搅拌）**
**见到 current → ammeter in series（不要并）**
**见到 voltage → voltmeter in parallel（不要串）**
**见到 resistance → ohmmeter 或 $V/I$（看场景）**
**见到 angle → protractor 或 $\tan^{-1}$（从长度算更准）**
**见到 frequency → oscilloscope / signal generator**
**见到 magnetic field → Hall probe / search coil**
**见到 speed → light gate + card**
**见到 acceleration → two light gates**

:::

---

## 十一、测量不确定度速查

每次描述测量方法后加一句：

| 你的操作 | MS 给分 |
|---------|---------|
| "repeat measurements and calculate mean" | **D1** |
| "measure three times at different positions and average" | **D1** |
| "use a set square to avoid parallax error" | **D1** |
| "check for zero error before measuring" | **D1** |
| "use a large range of values" | **D1** |
| "use a data logger to reduce random error" | **D1** |

这些附加细节是 Q1 最后 5 分 **Additional Detail** 的主要来源。

---

## 十二、补充器材库（参考资料新增）

以下器材在原表基础上补充：

### 力学补充

| 器材 | 用途 | MS 关键词 |
|------|------|----------|
| 电磁铁 (electromagnet) | 固定后释放物体（如落体实验） | "use electromagnet to release object" |
| 斜面 (inclined plane) | 动力学实验、加速度研究 | "use inclined plane at measured angle" |
| 沙盘 / 沙箱 (sand tray) | 接住坠落重物，安全用 | "place sand tray to catch falling masses" |
| 滑车 / 小车 (trolley) | 轨道动力学实验 | "use trolley on runway" |

### 电学补充

| 器材 | 用途 | MS 关键词 |
|------|------|----------|
| 微安表 (microammeter) | 测微小电流（μA 级） | "use microammeter" |
| 保护电阻 (protective resistor) | 防止电流过大烧毁电路 | "use a protective resistor in series" |
| 开关 (switch) | 通断控制 | "open switch when not taking readings" |

### 压强补充

| 器材 | 用途 | MS 关键词 |
|------|------|----------|
| U 型管压力计 (U-tube manometer) | 测压强差 | "use U-tube manometer" |
| Bourdon gauge | 测气体压强 | "use Bourdon gauge" |
| 气泵 (pump) | 改变容器内气压 | "use pump to vary pressure" |

### 热学补充

| 器材 | 用途 | MS 关键词 |
|------|------|----------|
| 本生灯 (Bunsen burner) | 加热 | "use Bunsen burner" |
| 热板 (hot plate) | 稳定加热 | "use hot plate" |
| 浸入式加热器 (immersion heater) | 加热液体 | "use immersion heater" |
| 温度传感器 (temperature sensor) | 连续记录温度 | "use temperature sensor connected to data logger" |

### 光学补充

| 器材 | 用途 | MS 关键词 |
|------|------|----------|
| 双缝 (double slit) | 干涉实验测波长 | "use double slit, measure fringe spacing with ruler" |
| 光具座 (optical bench) | 透镜实验 | "use optical bench with ruler" |

---

## 十三、实验环境要求

某些实验需要特定的环境条件，说一句就能多得 1 分 **Additional Detail**：

| 实验类型 | 环境要求 | MS 句式 |
|---------|---------|--------|
| 声音实验（驻波/共鸣管） | 安静环境，减少背景噪音干扰 | "carry out experiment in a quiet room" |
| 光学实验（干涉/衍射） | 暗室，减少杂散光 | "carry out experiment in a dark room" |
| 轻物体/精密力学 | 关门窗、关空调，减少气流干扰 | "close windows and switch off air conditioning to reduce air currents" |
| 热学实验（冷却/加热） | 恒温环境，远离热源/通风口 | "ensure room temperature is constant" |
| 磁学实验 | 远离金属物体和电磁干扰源 | "keep away from metal objects and external magnetic fields" |

---

## 十四、安全措施分类大全

Q1 的 safety precaution 只有 1-2 分，**不要笼统说 "be safe"**，要针对具体风险：

| 风险类别 | MS 给分表述 | 适用场景 |
|---------|------------|---------|
| 重物坠落 | "place sand tray / cushion to catch falling masses / weights" | 挂砝码、弹簧、摆锤 |
| 弹簧弹伤 | "wear safety goggles to protect eyes from snapping spring" | 弹簧拉伸实验 |
| 触电 | "switch off power supply / open switch before changing circuit connections" | 任何电路改接 |
| 裸露导线 | "use insulated / shrouded connectors, avoid bare wires" | 高电压电路 |
| 高温烫伤 | "wear heat-proof gloves / use tongs to handle hot objects" | 加热实验、冷却实验 |
| 易燃物 | "keep flammable materials away from Bunsen burner / heat source" | 有明火的实验 |
| 尖锐边缘 | "wear gloves to protect hands from sharp edges / cuts" | 金属片、切割材料 |
| 噪音损伤 | "wear ear defenders / use low volume setting" | 大音量扬声器/声源 |
| 重物砸脚 | "secure apparatus with G-clamp / place weights on base of stand" | 竖立支架、重物悬挂 |
| 眼睛防护 | "wear safety goggles" | 通用（有风险时用） |

---

## 十五、有效数字与对数精度规则（Q2 专用）

### 常规数据有效数字

原始数据的有效数字位数确定计算结果的位数：

| 原始数据 s.f. | 计算结果应保留 |
|-------------|--------------|
| 2 s.f. | 2 s.f. 或 3 s.f. |
| 3 s.f. | 3 s.f. 或 4 s.f. |

**MS 规则：** 计算结果通常与原始数据中 **最少有效数字位数** 相同，或 **多一位**。

### 对数的 decimal places

$$3\ \text{s.f.} \rightarrow 3\ \text{d.p.}$$

| 原始 $x$ 的有效数字 | $\lg x$ 的小数位数 | $\ln x$ 的小数位数 |
|------------------|------------------|------------------|
| 2 s.f. | 2 d.p. | 2 d.p. |
| 3 s.f. | 3 d.p. | 3 d.p. |
| 4 s.f. | 4 d.p. | 4 d.p. |

### Absolute Uncertainty 的表示

:::note[规则]
- absolute uncertainty **小数点位数** 与对应值的位数一致
- 或保留 **1 位有效数字**
:::

**例：** $V = 6.2 \pm 0.2$ V（一致）

### $\ln$ 和 $\lg$ 的 Absolute Uncertainty

$$\Delta(\ln x) = \left|\ln x - \ln(x - \Delta x)\right|$$

**注意：** 这个公式和 $\Delta(\ln x) = \Delta x / x$ 是等价的（一阶近似），但 MS 都接受。

### 重复测量的不确定度

当一组数据有两次测量值 $m_1$ 和 $m_2$：
$$\Delta m = \frac{|m_1 - m_2|}{2}$$

### 周期数据的处理

如果题目给的时间 $t$ 是 **10 个周期** 的总时间：
- 周期 $T = t / 10$
- 不确定度 $\Delta T = \Delta t / 10$

**不要** 直接把 $t$ 当作周期！

---

## 十六、Hall Probe 进阶用法

:::note[标准操作]
1. 将 Hall probe 与磁场垂直放置
2. 连接至 voltmeter，读取 Hall 电压 $V_H$
3. **反转 probe 180° 再测一次，取平均**（消除零误差和环境磁场影响）
4. 使用前校准 probe（已知磁场中校准）
5. 远离外部交变磁场
:::

**MS 评分标准：**
- **M1**: "use Hall probe connected to voltmeter"
- **M1**: "ensure probe is perpendicular to magnetic field direction"
- **A1**: "reverse probe and average readings to eliminate background field"
- **不接受**: probe 平行于磁场

---

## 十七、万能改进方法（全套话）

无论什么实验，以下套话总能拿分：

### 减少随机误差
| 套话 | 适用 |
|------|------|
| "repeat measurements and calculate mean" | 任何物理量测量 |
| "measure over a larger range to reduce percentage uncertainty" | 需要算梯度时 |
| "use a larger sample / longer length for better precision" | 测微小量时（如直径、厚度） |
| "use light gates / data logger to reduce reaction-time error" | 时间测量 |

### 减少系统误差
| 套话 | 适用 |
|------|------|
| "check / correct for zero error before measurement" | micrometer, newton meter, balance |
| "read scale at eye level to avoid parallax error" | ruler, thermometer, 任何刻度 |
| "use a set square to ensure ruler is vertical" | 任何竖立测量 |
| "stir liquid before reading temperature" | 热学实验 |

### Q1 的五个必写部分（万能模板）

```
1. Purpose: to verify the relationship between X and Y, AND to determine [constant].
2. IV = ..., DV = ..., control = ...
3. Diagram + Method:
   - Measure all control variables first
   - Set up apparatus as shown
   - Vary IV, measure DV
   - Repeat for same IV and average
   - Repeat whole procedure for various IV
4. Analysis:
   - Plot graph of Y against X
   - Straight line → relationship valid
   - Constant = (formula using gradient / intercept)
5. Safety: [specific to risk]
```

---

## 十八、单位的确定方法

在 Q2(d) 中写单位时：

:::tip[单位的确定]
1. **如果这个物理量有明确的物理意义**（如 $C$ = capacitance），直接写其标准单位（F, $\Omega$, V, A, s 等）
2. **如果是推导出的常数**（如 $k$, $n$, $E$），从公式中反推单位
3. **注意组合单位**：如 $\text{J K}^{-1}$、$\text{Pa s}$、$\text{N m}^{-1}$ 等
:::

**常见物理量的标准单位速查：**

| 量 | 单位 |
|---|------|
| 电容 $C$ | F |
| 电阻 $R$ | $\Omega$ |
| 电动势 $\mathcal{E}$ | V |
| 能量 $E$ | J |
| 弹簧常数 $k$ | $\text{N m}^{-1}$ |
| 速度 $v$ | $\text{m s}^{-1}$ |
| 密度 $\rho$ | $\text{kg m}^{-3}$ |
| 黏度 $\eta$ | $\text{Pa s}$ |
| 线密度 $\mu$ | $\text{kg m}^{-1}$ |
| 张力 $T$ | N |
| 频率 $f$ | Hz |
| 磁场强度 $B$ | T |
| 比热容 $c$ | $\text{J kg}^{-1}\text{K}^{-1}$ |
