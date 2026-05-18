---
title: 常见错误
---

# 常见错误

## 错误 1：TCP/IP 层数记错
**问题**：混淆 OSI 七层模型（Physical, Data Link, Network, Transport, Session, Presentation, Application）和 TCP/IP 四层模型。
**正确**：CIE 考的是 **TCP/IP 四层模型**：Application, Transport, Internet, Link

## 错误 2：SMTP 与 POP3/IMAP 功能混淆
**问题**：将 SMTP 和 POP3 都说成 "发送邮件" 或 "接收邮件"
**正确**：
- **SMTP**：发邮件（send / push）
- **POP3 / IMAP**：收邮件（retrieve / pull）
- POP3 下载到本地删除服务器副本，IMAP 保留在服务器

## 错误 3：HTTP 与 HTTPS 的区别只说 "secure"
**问题**：只说 HTTPS is secure
**正确**：HTTPS = HTTP + **SSL/TLS encryption**，提供加密传输和身份验证

## 错误 4：Packet switching 和 circuit switching 的例子混淆
**问题**：把 Internet 说成 circuit switching，把电话网络说成 packet switching
**正确**：
- **Circuit switching**：传统电话网络
- **Packet switching**：Internet

## 错误 5：Router 功能与 Switch/Hub 混淆
**问题**：说 router 根据 MAC 地址转发
**正确**：
- **Router**：工作在网络层（Layer 3），根据 **IP 地址** 转发
- **Switch**：工作在数据链路层（Layer 2），根据 **MAC 地址** 转发
- **Hub**：物理层设备，简单广播

## 错误 6：Protocol port numbers 混淆
**问题**：不需要记 port numbers（CIE 不考端口号）
**注意**：CIE 9618 不要求记忆协议端口号，只需知道功能和场景
