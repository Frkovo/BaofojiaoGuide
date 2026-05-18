# CIE Exam Revision Guide — Docusaurus Project Prompt

## 任务目标

为一个 Cambridge International AS & A Level 科目生成完整的考前复习指南 Docusaurus 网站。网站使用单语言（简体中文），安装 KaTeX LaTeX 渲染。

## 第一步：信息收集

先向用户询问以下信息：
1. **Syllabus Code**（如 9702, 9231, 9618）
2. **科目名称**（如 Physics, Further Mathematics）
3. **Paper 编号**（如 2, 4 等）
4. **考纲 PDF 链接**（来自 cambridgeinternational.org）
5. **其他Paper-Specific要求** 有些Paper很抽象或者需要更多的东西,请问用户获取

## 第二步：下载与提取数据

### 下载
1. 下载考纲 PDF 到 `data/syllabuses/{code}_syllabus.pdf`
2. 使用 `fetch_papers.py` 下载对应科目的 past papers 和 mark schemes：
   ```
   python fetch_papers.py --subject {CODE} --years 2020-2025 --season Jun,Nov --out papers --paper {PAPER} --ms
   ```

### PDF 提取（必须对每份 PDF 逐份处理）
使用 **pdfplumber**（不是 PyMuPDF）提取每份 PDF 的文本，因为 pdfplumber 对 CIE 试卷的提取质量更好：
```
提取到 data/extracted/papers/ 和 data/extracted/ms/
```
**重要：** 提取后必须读取每份文本的内容，理解实际考题，而不是只写脚本批量处理。20-25全部年份，全部考季，全部Variant，应该是6*2*3份卷子。因为考题会有多种变体，请你老老实实把所有考题全部读完，不要偷懒，作为一个经验丰富的老师这是基本功，请你认真静下心来读完所有的Paper和Mark Scheme.

### 阅读考纲
从 syllabus PDF 中提取：
- 每个 Topic 的详细考纲要求
- 考试结构（时长、分值、题量）
- 各 Topic 在考纲中的编号
- 前置知识要求
- Assessment Objectives

### 阅读试卷
从每份 question paper 中提取：
- 每道题的完整题目文字
- 题号与分值
- 题目属于哪个 Topic

### 阅读 Mark Scheme
从每份 mark scheme 中提取：
- 每题的具体评分点
- M1/A1/B1 标记的分配
- 每个得分点的具体要求

## 第三步：生成文档

### 目录结构

每个科目的文档统一放在：
```
docs/subjects/{subject-code}-{subject-name-slug}/
   paper-N/
   ├── index.md                    # 页面入口（Paper 总览、快速信息、复习清单）
   ├── exam-structure.md           # 考试结构（时长、分值、题型分布、答题规范）
   ├── syllabus-overview.md        # 考纲总览（知识点列表、前置要求、AO 占比）
   ├── last-minute-guide.md        # 考前速通（必记公式、见到什么做什么、时间分配）
   ├── common-mistakes.md          # 常见错误（各 topic 易错点整理）
   ├── common-ms-keywords.md       # MS 关键词速查（评分标准术语对照）
   ├── common-traps.md             # 常见陷阱
   ├── question-types.md           # 题型总览（各题型识别方法、标准解法、评分模式）
   ├── strategy.md                 # 详细策略
   ├── time-management.md          # 时间管理
   └── topics/                     # 该 Paper 专属的 topic 目录
      ├── topic-a/
      │   ├── index.md
      │   ├── question-types.md
      │   ├── syllabus-points.md
      │   ├── methods.md
      │   ├── mark-scheme-patterns.md
      │   ├── common-mistakes.md
      │   └── last-minute-summary.md
      ├── topic-b/
      └── ...
   每个 topic 下 7 个文件是固定模板，每个 Paper 完全自包含，不依赖外部。
```

### 语言标准（严格遵循）

| 内容类型 | 语言 | 示例 |
|---------|------|------|
| 题型名称（标题） | 英文 | `## Question Type 3: Solving hyperbolic equations` |
| 原题原文 | 英文 | `> Solve the equation $\cosh x - 3\sinh x = 4$` |
| Mark Scheme 原文 | 英文 | `**M1**: writes $\frac{e^x+e^{-x}}{2} - ...$` |
| 所有解释说明 | 中文 | `### 如何识别`、`标准方法`、`常见陷阱` |
| 解题方法 | 中文 | `1. 代入指数形式`、`2. 化简得到方程` |
| 常见错误 | 中文 | `- 忘记 $e^x > 0$，把两个根都取 log` |
| Topic 文件夹名 | 英文 kebab-case | `hyperbolic-functions` |
| Topic 首页标题 | 英文 | `title: Hyperbolic Functions` |
| 子页面标题 (frontmatter) | 中文 | `title: 题型分析`、`title: 解题方法` |

### 文档格式标准（Visual Formatting）

#### 1. Admonitions（告示块）
使用 Docusaurus **标准语法**（标题用 `[...]` 方括号，不是空格）：

```
:::note[标准解题方法]
步骤内容
:::

:::info[评分标准（MS 模式）]
**M1**: 内容
**A1**: 内容
:::

:::warning[常见陷阱]
- 陷阱1
- 陷阱2
:::

:::tip[必须背熟的公式]
$$\sinh^{-1} x = \ln(x + \sqrt{x^2+1})$$
:::

:::danger[最常见的错误]
$\frac{d^2y}{dx^2} \neq \frac{d^2y/dt^2}{d^2x/dt^2}$
:::
```

每个 `:::` 必须配对关闭。标题在方括号内，不在冒号后面。

#### 2. Mark Scheme 格式
每条 MS 必须是独立段落，格式统一：
```
**M1**: description of mark point
**A1**: description of accuracy mark
```
- M1/A1/B1 **必须加粗**
- 每个 mark 单独一行，用 `-` 开头
- 整个 MS 包裹在 `<details><summary>📝 MS 展开查看</summary>...</details>` 中
- 默认折叠，用户点击展开

#### 3. 例题格式
```
**Example 1 — 9231/s20/qp/22 Q5(c) (5 marks):**

> 题目原文（用 blockquote）
> 如有多行继续用 >
> 公式用 $$...$$

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: mark point 1
- **A1**: mark point 2

</details>
```

#### 4. 排版要求
- 每个公式单独一行，不塞在段落里
- 每个解释步骤单独一行
- 原题引用用 `>` blockquote
- 列表项用 `-`，每项独立一行
- 不用 HTML 表格以外的复杂格式

### 每类文件的详细内容要求

#### subject-level/index.md
- 科目快速信息表（code, level, syllabus link, papers, duration, marks）
- 各知识点一览表（# / Topic / 题型示例）
- 核心公式速查（topic 名 + 公式）

#### subject-level/syllabus-overview.md
- 知识点列表（# / Topic / 核心内容）
- 考试形式（时长、分值、题量、计算器要求、公式表）
- 前置知识要求
- AO 比重

#### subject-level/exam-structure.md
- 试卷概况表
- 各知识点典型分值分布
- 指令词表（command word + 中文要求）

#### subject-level/last-minute-guide.md
- 各 topic 核心公式（display math $$）
- "见到什么先做什么"对照表
- 时间分配表（分值→分钟）
- 卡住时的对策
- 交卷前检查清单

#### subject-level/common-ms-keywords.md
- 按 topic 组织的表格（MS 原句 + 中文含义）
- 每种题型 keywords 单独一个 section

#### subject-level/common-mistakes.md
- 按 topic 组织的中文错误说明
- 每个错误附带正确/错误公式对比
- 致命错误用 `:::danger`

#### paper-{n}/index.md
- 试卷概况表
- 整体策略
- 各题型策略一句话总结
- 复习检查清单

#### paper-{n}/question-types.md
- 六种核心题型总览表
- 每个题型链接到对应 topic 的详细分析

#### paper-{n}/strategy.md
- 前 5 分钟策略
- 每个知识点的具体答题策略
- 最后 10 分钟检查清单

#### paper-{n}/time-management.md
- 分值预算表（mark → minutes）
- 分阶段策略（浏览→第一轮→第二轮→补漏→检查）
- 卡住决策表（情况→对策）

#### paper-{n}/common-traps.md
- 10 个独立 trap，每个包含：问题描述 / 后果 / 对策

#### topics/{topic}/index.md
- `## 考纲要求` — 编号列表
- `## 常见题型` — 列表，每个带链接到 question-types.md
- `## 核心公式` — display math
- `## 常见错误` — bullet points

#### topics/{topic}/question-types.md（核心文件）

**每个 Question Type 的结构：**
```
## Question Type N: English Name

### 如何识别
一句话 + 关键词

:::note[标准解题方法]
每个步骤一行
:::

:::info[评分标准（MS 模式）]
每个 M1/A1/B1 一行
:::

### 完整原题
至少 3 个 Example，每个带 MS

Example 1 — source:
> question text
<details><summary>MS</summary>...M1A1...</details>

Example 2 — source:
> question text
<details><summary>MS</summary>...M1A1...</details>

:::warning[常见陷阱]
bullet points
:::
```

**必须覆盖所有可能出现的题型。** 每个题型至少 3 个例题（如试卷中不够除外）。

#### topics/{topic}/methods.md
每个解题方法一个 section：
```
## Method 1: Name

### When to use it

### Steps
1. step one
2. step two

### Formula
$$formula$$

### Mistakes to avoid
```

#### topics/{topic}/mark-scheme-patterns.md
- Key command words
- Common accepted phrases
- Mark allocation by question part
- How to write answers efficiently

#### topics/{topic}/common-mistakes.md
每个错误编号：
```
### 1. Mistake description
*Fix:* Correction strategy with formula
```

#### topics/{topic}/last-minute-summary.md
- Must-know formulas
- Problem patterns to recognise
- Red flags
- Quick checklist

## 质量检查清单（最终必须逐项验证）

1. [ ] 每个 syllabus topic 都有对应 Markdown 文档
2. [ ] 每个 Paper 都有 strategy guide
3. [ ] Markdown frontmatter 正确（title, sidebar_position）
4. [ ] 没有空文档（每个文件 > 500 bytes）
5. [ ] 没有重复 title
6. [ ] 每个 question type 至少包含：
   - 如何识别
   - 解题方法（:::note）
   - MS 模式（:::info）
   - 原题（至少 3 个，带 MS）
   - 常见陷阱（:::warning）
7. [ ] 所有 `:::` 正确配对（open/close 数量一致）
8. [ ] 所有 M1/A1/B1 已加粗
9. [ ] 所有公式使用 LaTeX（$...$ 或 $$...$$）
10. [ ] 没有 `\1`、`\2` 等 regex 残留
11. [ ] MS 折叠在 `<details>` 中
12. [ ] `npx docusaurus build` 构建成功
13. [ ] 语言切换已移除，只有简体中文
14. [ ] sidebar 能正常加载所有页面

## 已知注意事项（避免踩坑）

### 格式坑
- **告示块语法**：`:::note[标题]` 不是 `:::note 标题`。标题用 `[]` 方括号
- `:::` 闭标签 **必须独占一行**，不能附在内容末尾。`内容 :::` 是错的，必须是：
  ```
  内容
  :::
  ```
- `:::` 块的前后**必须有空行**，否则 MDX 解析器会将相邻内容视为同一个段落
- LaTeX 花括号 `{}` 在 MDX 中会被解析为 JSX 表达式，必须放在 `$...$` 或 `$$...$$` 内才安全
- 不要在 table cell 中截断 LaTeX 公式

### MDX 特有坑
- **`<details>` 和 `<summary>` 不能写在同一行**，必须分开：
  ```
  <details>
  <summary>📝 MS 展开查看</summary>
  ```
  写成 `<details><summary>...</summary>` 会导致 `Expected a closing tag for <details>` 错误
- **大写字母在 MDX 正文中会被解析为 JSX 组件名**。例如 `A, B, C` 中的 `A` 会被当作 `<A>` 组件，报 `ReferenceError: A is not defined`。解决方法：
  - 变量名用 `$A$`, `$B$` LaTeX 行内公式包裹
  - 或在 `backticks` 中包裹
  - 或写成 `A、B、C` 用中文顿号分隔
- **`<=` 和 `<` 在 MDX 正文中被视为 JSX 标签开始**。例如 `Low <= High` 中 `<` 后跟 `=` 被认为是 JSX 属性。解决方法：
  - 用 `&lt;=` 和 `&lt;` HTML 实体
  - 或用 `` `<=` `` 反引号包裹
  - 或在 LaTeX 中用 `$\\leq$`
- **反引号内的 `<` 安全**，但需注意前后文不要有未匹配的反引号

### 编码坑
- **永远不要用 PowerShell 的 `Set-Content -NoNewline` 修改含有中文的 Markdown 文件**。PowerShell 默认编码是 Windows-1252，会破坏 UTF-8 多字节字符（如中文、emoji），导致不可逆的乱码
- 如果必须批量修改 → 用 Python 写脚本，明确指定 `encoding='utf-8'`
- 任务生成的 .md 文件是 UTF-8 编码，任何修改工具都必须识别并保持 UTF-8
- 中文乱码一旦写入文件（UTF-8 字节被当作 Latin-1/GBK 解码后再编码），大部分情况下不可逆，只能重新生成文件

### 内容坑
- 不要用 Python 脚本批量修改 markdown 文件（容易引入 regex 残留如 `\1`、`\2`）
- 每个文件的 MS 必须独立检查，不要复用上个例子的 MS
- 原题必须写完整题目，不要只写编号
- 每种题型至少 3 个例题

### 流程坑
- 先提取全部 PDF 文本并**阅读一遍**，理解题目内容，再生成文档
- 生成完成后必须 build 一次检查错误（`npx docusaurus build`）
- 不要一次性生成所有文件后不检查——逐步验证。每次 build 报错只改当前错误，不要一次性改多个问题
- 避免使用 Python 脚本批量修改 markdown 文件，请使用 Opencode 自带的 Edit/Write 工具
- **Task 子代理生成的文件可能会犯同样的格式错误**（如 `<details><summary>` 写在一行），检查后统一修正

## 最终交付物

1. 完整的 Docusaurus 项目，包含上述所有文档
2. 所有 PDF 已提取到 `data/extracted/`
3. 构建成功（`npx docusaurus build` 无错误）
4. 最终的质量检查报告
