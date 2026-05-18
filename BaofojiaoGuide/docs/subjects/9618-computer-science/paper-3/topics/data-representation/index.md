---
title: Data Representation
---

# Data Representation

## 核心考点
- **用户自定义数据类型（User-defined data types）**：enumerated type, pointer type, record type
- **文件组织与存取方式（File organisation and access）**：serial, sequential, random access
- **哈希算法（Hashing algorithms）**：hash function, collision handling (open addressing, chaining)
- **浮点数表示（Floating-point representation）**：mantissa, exponent, normalisation, underflow, overflow, two's complement

## Syllabus 覆盖范围
| Section | 内容 |
|---------|------|
| 13.1 | User-defined data types |
| 13.2 | File organisation and access |
| 13.3 | Floating-point numbers, hashing |

## 常见题型分布
| 题型 | 典型分值 | 出现频率 |
|------|---------|---------|
| 浮点数 normalisation / denary 转换 | 5-8 分 | 必考 |
| TYPE 定义与 pseudocode | 4-6 分 | 高频 |
| 文件组织方式对比 | 3-5 分 | 中频 |
| 哈希算法与碰撞处理 | 4-6 分 | 中频 |

## 核心公式速览
- 浮点数值 = Mantissa × 2^Exponent
- Normalisation 条件：mantissa 前两位不同（正数 0.1...，负数 1.0...）
- Two's complement：取反（NOT）加 1
- Hash function: key mod table_size
