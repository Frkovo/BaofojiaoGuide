# Riemann Sums — Solution Methods

## Method 1: Upper and Lower Bounds

### 步骤框架
1. **分割区间** $[a,b]$ 为 $n$ 等份，$\Delta x = \frac{b-a}{n}$
2. **判断单调性**：$f(x)$ 在区间上是递增还是递减？
3. **确定端点**：
   - 递增函数：上界 = 右端点，下界 = 左端点
   - 递减函数：上界 = 左端点，下界 = 右端点
4. **求和**：$\sum f(x_i)\Delta x$
5. **化简**：使用求和公式

### 快速判断表

| 函数类型 | 上界 (Upper) | 下界 (Lower) |
|----------|-------------|-------------|
| 递增 ($f' &gt; 0$) | 右端点 | 左端点 |
| 递减 ($f' &lt; 0$) | 左端点 | 右端点 |

:::note[示例]
$f(x) = x^2$ 在 $[0,1]$ 上递增，所以：

- 上界 = $\sum_{i=1}^n \left(\frac{i}{n}\right)^2 \cdot \frac{1}{n}$
- 下界 = $\sum_{i=0}^{n-1} \left(\frac{i}{n}\right)^2 \cdot \frac{1}{n}$
:::

## Method 2: Summation Formulae

### 核心求和公式

$$\sum_{r=1}^n r = \frac{n(n+1)}{2}$$

$$\sum_{r=1}^n r^2 = \frac{n(n+1)(2n+1)}{6}$$

$$\sum_{r=1}^n r^3 = \frac{n^2(n+1)^2}{4}$$

$$\sum_{r=1}^n 1 = n$$

### 偏移索引技巧
当求和从 $r=0$ 到 $r=n-1$ 时：

$$\sum_{r=0}^{n-1} r = \frac{(n-1)n}{2}$$

$$\sum_{r=0}^{n-1} r^2 = \frac{(n-1)n(2n-1)}{6}$$

$$\sum_{r=0}^{n-1} r^3 = \frac{(n-1)^2 n^2}{4}$$

## Method 3: Stirling-Type Approximation

### 估计 $\ln N!$

**核心不等式**（$\ln x$ 递增）：

$$\int_1^N \ln x\,dx \le \sum_{r=2}^N \ln r \le \int_1^N \ln x\,dx + \ln N$$

即：

$$N\ln N - N + 1 \le \ln N! \le N\ln N - N + 1 + \ln N$$

**步骤**：
1. 识别 $\ln N! = \sum_{r=1}^N \ln r = \sum_{r=2}^N \ln r$（因 $\ln 1 = 0$）
2. 取 $f(x) = \ln x$ 在 $[1, N]$ 上的 Riemann 和
3. 左端点（递减函数性质）给出上界，右端点给出下界——注意 $\ln x$ 是递增的
4. 计算 $\int_1^N \ln x\,dx = N\ln N - N + 1$
5. 建立关于 $\ln N!$ 的双边不等式

:::tip[精确 Stirling 公式（不需证明，但可验证）]

$$\ln N! = N\ln N - N + \frac{1}{2}\ln(2\pi N) + O\left(\frac{1}{N}\right)$$
:::

## Method 4: Riemann Sum to Definite Integral

**核心公式**：

$$\lim_{n\to\infty} \frac{1}{n}\sum_{r=1}^n f\left(\frac{r}{n}\right) = \int_0^1 f(x)\,dx$$

更一般地：

$$\lim_{n\to\infty} \frac{b-a}{n}\sum_{r=1}^n f\left(a + \frac{r(b-a)}{n}\right) = \int_a^b f(x)\,dx$$

**步骤**：
1. 将求和写成 $\frac{1}{n}\sum f(\frac{r}{n})$ 的形式
2. 识别 $f(x)$ 和区间 $[0,1]$
3. 取极限得到定积分
4. 计算积分
