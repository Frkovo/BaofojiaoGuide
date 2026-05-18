---
title: 解题方法
---

# 解题方法

---

## 方法 1：协议功能描述

**适用场景**：题目要求描述某个协议的作用。

**答题框架**：
- 协议全称 + 缩写含义
- 在什么场景下使用（发送/接收/传输）
- 关键特征

**示例**：
- **SMTP**：Simple Mail Transfer Protocol，用于 **发送** 邮件，从客户端到服务器或服务器之间
- **POP3**：Post Office Protocol v3，用于 **下载** 邮件到本地客户端
- **IMAP**：Internet Message Access Protocol，用于 **在服务器上管理** 邮件

---

## 方法 2：Compare / Contrast 题

**适用场景**：比较两种技术（circuit switching vs packet switching）。

**答题框架**：
1. 分别描述 A 是什么
2. 分别描述 B 是什么
3. A 的 1 个优点
4. A 的 1 个缺点
5. B 的 1 个优点
6. B 的 1 个缺点
7. （可选）各举一个例子

**关键词**：
| 对比项 | Circuit Switching | Packet Switching |
|--------|------------------|-----------------|
| 路径 | Dedicated path | No dedicated path |
| 延迟 | Low / constant | Variable |
| 带宽 | Guaranteed | Shared |
| 效率 | Inefficient for burst | Efficient |
| 容错 | Single point of failure | Fault tolerant |

---

## 方法 3：TCP/IP 四层模型记忆

**从上到下**：
1. **Application** — 应用层协议（HTTP, FTP, SMTP...）
2. **Transport** — 端到端可靠传输（TCP/UDP）
3. **Internet** — 路由与寻址（IP）
4. **Link** — 物理传输（MAC, Ethernet）

**记忆口诀**：ATIL（Application → Transport → Internet → Link）
