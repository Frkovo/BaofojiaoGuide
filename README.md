# 抱佛脚 Guide

> **CIE IGCSE / AS / A Level 临时抱佛脚复习指南**

一个基于 [Docusaurus](https://docusaurus.io/) 构建的 Cambridge International 考试复习网站，提供科目概览、试卷策略、逐 Topic 复习指南、评分标准关键词分析、常见错误及考前速通清单。

## 项目结构

```
BaofojiaoGuide/          # Docusaurus 网站源码
├── docs/                # 文档内容（MDX/Markdown）
│   ├── intro.md         # 网站介绍
│   ├── guide/           # 使用指南
│   └── subjects/        # 各科目复习资料
├── src/                 # React 组件和样式
├── blog/                # 博客
├── data/                # 考纲 PDF 和提取文本
└── papers/              # Past papers 和 Mark schemes

data/                    # 数据处理脚本
├── extract_pdfs.py      # PDF 文本提取
├── fix_admonitions.py   # 格式修复脚本
└── syllabuses/          # 考纲 PDF

fetch_papers.py          # Past papers 自动下载脚本
```

## 快速开始

```bash
cd BaofojiaoGuide
npm install
npm start
```

启动本地开发服务器，打开浏览器访问 `http://localhost:3000`。

## 构建

```bash
npm run build
```

生成静态文件到 `build/` 目录，可部署到任何静态托管服务。

## 科目

- **9702 Physics** — CIE AS & A Level 物理
- **9231 Further Mathematics** — CIE A Level 进阶数学
- **9618 Computer Science** — CIE A Level 计算机科学（Paper 3 & Paper 4）

## 作者: Deepseek V4 Flash

本项目内容由 Deepseek V4 Flash 生成。

## 许可

[MIT](LICENSE)
