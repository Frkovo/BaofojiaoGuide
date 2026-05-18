---
title: 考前速记
---

# 考前速记

## 必须记住的公式
| 公式 | 说明 |
|------|------|
| Value = M × 2^E | 浮点数基本公式 |
| Normalised: 01... 或 10... | mantissa 前两位不同 |
| Two's complement: NOT + 1 | 取反加一 |
| Hash: key mod n | 常用哈希函数 |

## 必考题型与套路
| 题型 | 第一步 | 最后一步 | 验证 |
|------|--------|---------|------|
| Denary → floating-point | 转 binary | Two's complement（如果负数） | 转回 denary 验证 |
| Normalise | 左移 mantissa | 减小 exponent | 检查前两位 |
| Denary ← floating-point | 判断正负 | M × 2^E | 反向验证 |

## Red Flags 🚩
| 情况 | 处理 |
|------|------|
| Mantissa 以 00 或 11 开头 | **未 normalised**，需要左移 |
| Exponent 无法再减 | **Underflow**（数太小） |
| Exponent 超出最大值 | **Overflow**（数太大） |
| 小数转换无限循环 | 按指定位数截断，注意进位 |

## 考试快速检查清单
- [ ] Mantissa 和 exponent 位数是否正确？
- [ ] 负数是否做了 two's complement？
- [ ] Normalisation 后前两位是否不同？
- [ ] Exponent 是否也用 two's complement？
- [ ] TYPE 结尾是否有 ENDTYPE？
- [ ] Hash 冲突是否全部处理完毕？
