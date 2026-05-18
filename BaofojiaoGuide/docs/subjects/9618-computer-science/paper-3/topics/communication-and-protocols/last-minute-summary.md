---
title: 考前速记
---

# 考前速记

## 协议速查表
| 协议 | 全称 | 功能 |
|------|------|------|
| **HTTP** | HyperText Transfer Protocol | 传输网页 |
| **HTTPS** | HTTP + SSL/TLS | 加密传输网页 |
| **FTP** | File Transfer Protocol | 文件上传/下载 |
| **SMTP** | Simple Mail Transfer Protocol | 发送邮件 |
| **POP3** | Post Office Protocol v3 | 下载邮件到本地 |
| **IMAP** | Internet Message Access Protocol | 在服务器管理邮件 |
| **BitTorrent** | — | P2P 文件共享 |

## TCP/IP 四层模型
| Layer | 功能 | 协议举例 |
|-------|------|---------|
| Application | 应用层协议 | HTTP, FTP, SMTP |
| Transport | 端到端传输 | TCP, UDP |
| Internet | 路由寻址 | IP |
| Link | 物理传输 | Ethernet |

## Packet vs Circuit Switching 对比
| | Circuit Switching | Packet Switching |
|---|-----------------|-----------------|
| Path | Dedicated | Shared |
| Delay | Low, constant | Variable |
| Bandwidth | Guaranteed | Best effort |
| Efficiency | Low (burst) | High |
| Fault tolerance | Low | High |
| 例子 | Phone network | Internet |

## 必考答题模板

### Describe a protocol
> [Protocol name] is used for [purpose]. It [key function].

### Compare switching methods
> Circuit switching establishes a dedicated path while packet switching splits data into packets. An advantage of circuit switching is guaranteed bandwidth, while a disadvantage is inefficiency for burst traffic.

## Red Flags 🚩
- SMTP = **Send** Mail，不是 receive
- TCP/IP 是 **四层** 不是七层
- Router 看 **IP 地址**，不是 MAC 地址
- HTTPS 的 S 代表 **SSL/TLS**
- BitTorrent 是 **P2P**，不是 client-server

## 考试快速检查清单
- [ ] 协议功能是否匹配正确？
- [ ] TCP/IP 层序是从上到下？
- [ ] Circuit vs Packet 的优点缺点都写了？
- [ ] Router 功能提到 IP address + routing table？
