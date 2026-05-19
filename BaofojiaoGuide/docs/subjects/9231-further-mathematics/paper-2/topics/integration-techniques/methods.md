# Integration Techniques — Solution Methods

## Method 1: Reduction Formulae

**核心思想**：建立 $I_n$ 与 $I_{n-k}$ 之间的递推关系，通过降次逐步计算。

### 步骤框架
1. **定义** $I_n = \int_a^b f(x,n)\,dx$
2. **改写被积函数**，拆分出与递推相关的因子
3. **分部积分**，设 $u$ 为含幂次的函数，$dv$ 为可积函数
4. **建立关系**：得到形如 $I_n = A(n) \cdot I_{n-k} + g(x)$ 的等式
5. **边界条件**：计算 $I_0$ 或 $I_1$
6. **迭代计算**：递推至目标 $n$

### 常用模式

| 类型 | 拆分策略 | $u$ 选择 | $dv$ 选择 |
|------|----------|----------|-----------|
| $\int \sin^n x\,dx$ | $\sin^{n-1}x \cdot \sin x$ | $\sin^{n-1}x$ | $\sin x\,dx$ |
| $\int \cos^n x\,dx$ | $\cos^{n-1}x \cdot \cos x$ | $\cos^{n-1}x$ | $\cos x\,dx$ |
| $\int (1-x^2)^{n/2}\,dx$ | $(1-x^2)\cdot(1-x^2)^{(n-2)/2}$ | 拆分后分部 | $x\cdot(1-x^2)^{(n-2)/2}$ |
| $\int x^n e^x\,dx$ | 直接分部 | $x^n$ | $e^x\,dx$ |
| $\int x^n \ln x\,dx$ | 直接分部 | $\ln x$ | $x^n\,dx$ |

:::tip[分部积分技巧]
递推公式中 $u$ 通常选含 $n$ 的函数，$dv$ 选易积分的部分。

注意在得到 $I_n$ 与 $I_{n-2}$（或其他下标）的关系后，检查系数是否正确。
:::

## Method 2: Integration by Parts

**公式**：

$$\int u\,dv = uv - \int v\,du$$

### LIATE 法则 — 选择 $u$ 的优先级
| 优先级 | 函数类型 | 例子 |
|--------|----------|------|
| 1 (最高) | Log | $\ln x$ |
| 2 | Inverse trig | $\sin^{-1}x$, $\tan^{-1}x$ |
| 3 | Algebraic | $x^n$ |
| 4 | Trig | $\sin x$, $\cos x$ |
| 5 (最低) | Exponential | $e^x$ |

### 多次分部技巧
当 $u$ 的导数多次分部后才能简化时，需重复应用分部积分。

## Method 3: Integration by Substitution

**步骤**：
1. 选择替换 $x = g(u)$ 或 $u = h(x)$
2. 计算 $dx = g'(u)du$ 或 $du = h'(x)dx$
3. 替换被积函数中的所有 $x$ 和 $dx$
4. 定积分需调整积分限
5. 积分后换回原变量

### 常见替换

| 被积函数特征 | 替换 |
|-------------|------|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ |
| $f(e^x)$ | $u = e^x$ |
| $f(\sqrt{x})$ | $u = \sqrt{x}$ |

## Method 4: Integration of Rational Functions

**步骤**：
1. **多项式除法**：若分子次数 $\ge$ 分母次数，先做除法
2. **部分分式分解**：
   - 线性因子：$\frac{A}{x-a}$
   - 重复线性因子：$\frac{A}{x-a} + \frac{B}{(x-a)^2} + \cdots$
   - 二次因子：$\frac{Ax+B}{x^2 + c^2}$
3. **求解系数**：通分后比较系数或代入特殊值
4. **逐项积分**：
   - $\int \frac{1}{x-a}\,dx = \ln|x-a|$
   - $\int \frac{1}{(x-a)^n}\,dx = \frac{(x-a)^{-n+1}}{-n+1}$
   - $\int \frac{1}{x^2+a^2}\,dx = \frac{1}{a}\tan^{-1}\frac{x}{a}$
   - $\int \frac{x}{x^2+a^2}\,dx = \frac{1}{2}\ln(x^2+a^2)$
