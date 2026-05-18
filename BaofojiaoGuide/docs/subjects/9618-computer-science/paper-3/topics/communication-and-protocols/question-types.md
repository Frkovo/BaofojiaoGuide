---
title: 题型分析
---

# 题型分析：Communication and Internet Technologies

---

## 题型 1：TCP/IP 协议栈

### 题目特征

- 要求列出 TCP/IP 协议栈的四层
- 描述每一层的功能
- 给出各层对应的协议

:::note[标准解题方法]

1. 四层顺序（从上到下）：Application → Transport → Internet → Link
2. 每一层的核心功能：
   - Application：为特定应用程序提供协议（HTTP、FTP、SMTP 等）
   - Transport：确保端到端可靠传输；分段数据；流量控制（TCP/UDP）
   - Internet：跨网络路由数据包；添加 IP 地址；处理寻址和路由
   - Link：在物理介质上传输原始数据；处理 MAC 地址；帧封装
3. 记忆技巧：从上到下 = "All Teachers In Love"（Application, Transport, Internet, Link）

:::

:::info[评分标准（MS 模式）]

- **B1**：Application layer — 用户面向的协议（HTTP、FTP、SMTP 等）
- **B1**：Transport layer — 分段、可靠性、端到端传输
- **B1**：Internet layer — 路由、IP 寻址
- **B1**：Link layer — 物理传输、MAC 寻址

:::

### 典型例题 1：9618/s24/qp/31 Q2(a)(b)

> (a) List the four layers of the TCP/IP protocol stack in order.
> (b) Describe the function of each layer.

<details>
<summary>📝 MS 展开查看</summary>

| Layer | Function |
|-------|----------|
| Application | Provides protocols for specific applications (HTTP, FTP, SMTP, etc.) |
| Transport | Ensures reliable end-to-end delivery; segments data; flow control (TCP/UDP) |
| Internet | Routes packets across networks; adds IP addresses; handles addressing and routing |
| Link | Transmits raw data over physical medium; handles MAC addresses; framing |

- **B1**：Application layer — 用户面向的协议
- **B1**：Transport layer — 分段、可靠性、端到端
- **B1**：Internet layer — 路由、IP 寻址
- **B1**：Link layer — 物理传输、MAC 寻址

</details>

### 典型例题 2：TCP/IP 协议匹配

> Which layer of the TCP/IP protocol stack is responsible for:
> (a) Ensuring data arrives in the correct order
> (b) Adding MAC addresses to frames
> (c) Routing packets between different networks

<details>
<summary>📝 MS 展开查看</summary>

- **B1**：(a) Transport layer — TCP handles sequencing and ordering
- **B1**：(b) Link layer — MAC addresses are added to frames at this layer
- **B1**：(c) Internet layer — routing occurs at the Internet layer using IP addresses

</details>

---

## 题型 2：协议匹配

### 题目特征

- 给出多个协议名称和描述
- 要求将协议与正确描述配对
- 理解各协议的应用场景

:::note[标准解题方法]

1. 熟悉常见协议及其用途：
   - HTTP — 传输网页
   - HTTPS — 安全传输网页（HTTP + SSL/TLS）
   - FTP — 文件传输
   - SMTP — 发送电子邮件
   - POP3 — 下载电子邮件到本地
   - IMAP — 在服务器端管理电子邮件
   - BitTorrent — P2P 文件共享
2. 注意区分相似协议（POP3 vs IMAP，HTTP vs HTTPS）

:::

:::info[评分标准（MS 模式）]

- **B1**：每个正确匹配得 1 分
- 通常有 5-7 个协议需要匹配，总分相应分配
- 部分题目要求同时给出全称

:::

### 典型例题 1：9618/w23/qp/31 Q2

> Match each protocol to its correct description.

| Protocol | Description |
|----------|-------------|
| HTTP | Transfer web pages |
| HTTPS | Secure transfer of web pages |
| FTP | File transfer |
| SMTP | Send email |
| POP3 | Retrieve email (download) |
| IMAP | Retrieve email (server-side) |
| BitTorrent | Peer-to-peer file sharing |

<details>
<summary>📝 MS 展开查看</summary>

- **B1**：HTTP — 传输网页（Hypertext Transfer Protocol）
- **B1**：HTTPS — 安全传输网页
- **B1**：FTP — 文件传输（File Transfer Protocol）
- **B1**：SMTP — 发送电子邮件
- **B1**：POP3 — 下载电子邮件到本地
- **B1**：IMAP — 服务器端管理电子邮件
- **B1**：BitTorrent — P2P 文件共享

每正确匹配一个得 **B1**

</details>

### 典型例题 2：协议辨析

> Identify which protocol (HTTP, HTTPS, FTP, SMTP, POP3, IMAP) would be used for each scenario:
> (a) A user wants to send an email to a colleague
> (b) A user wants to download emails to read offline
> (c) A user wants to upload files to a web server

<details>
<summary>📝 MS 展开查看</summary>

- **B1**：(a) SMTP — 用于发送电子邮件
- **B1**：(b) POP3 — 下载邮件到本地离线阅读
- **B1**：(c) FTP — 上传文件到服务器

</details>

---

## 题型 3：Packet Switching vs Circuit Switching

### 题目特征

- 比较两种交换方式的原理
- 给出各自的优点和缺点
- 给出使用场景举例

:::note[标准解题方法]

1. Circuit Switching：
   - 通信前建立专用物理通路
   - 优点：低延迟、带宽保证
   - 缺点：线路利用率低、不适合突发流量
   - 例子：传统电话网络

2. Packet Switching：
   - 数据分包独立传输，不建立专用通路
   - 优点：带宽利用率高、容错性好
   - 缺点：可变延迟、数据包可能乱序到达
   - 例子：互联网

:::

:::info[评分标准（MS 模式）]

- **B1**：正确解释 circuit switching 的定义
- **B1**：正确解释 packet switching 的定义
- **B1**：给出 circuit switching 的有效优点
- **B1**：给出 circuit switching 的有效缺点
- **B1**：给出 packet switching 的有效优点
- **B1**：给出 packet switching 的有效缺点

:::

### 典型例题 1：9618/s21/qp/31 Q6

> Compare packet switching and circuit switching. Give one advantage and one disadvantage of each.

<details>
<summary>📝 MS 展开查看</summary>

| | Circuit Switching | Packet Switching |
|---|-------------------|-----------------|
| 原理 | 建立专用物理通路 | 数据分包独立传输 |
| 优点 | Low latency, guaranteed bandwidth | Efficient use of bandwidth, fault tolerant |
| 缺点 | Inefficient for burst traffic | Variable delay, packets may arrive out of order |
| 例子 | Telephone network | Internet |

- **B1**：Correct definition of circuit switching
- **B1**：Correct definition of packet switching
- **B1**：Valid advantage for circuit switching
- **B1**：Valid disadvantage for circuit switching
- **B1**：Valid advantage for packet switching
- **B1**：Valid disadvantage for packet switching

</details>

### 典型例题 2：交换方式应用

> A company is choosing between circuit switching and packet switching for its video conferencing system. Which method would you recommend and why?

<details>
<summary>📝 MS 展开查看</summary>

- **M1**：Recommend circuit switching for video conferencing
- **A1**：Circuit switching provides guaranteed bandwidth and low latency
- **B1**：Video conferencing requires consistent data flow without delay variation
- **B1**：Packet switching may introduce variable delay (jitter) which degrades video quality

</details>

---

## 题型 4：Router 功能

### 题目特征

- 解释 router 如何在不同网络间转发数据包
- 描述 routing 过程

:::note[标准解题方法]

1. Router 接收数据包
2. 读取目标 IP 地址
3. 查询 routing table
4. 选择最佳路径转发到下一跳
5. 在 packet switching 网络中重复此过程直到到达目标

:::

:::info[评分标准（MS 模式）]

- **B1**：读取目标 IP 地址
- **B1**：使用 routing table 选择路径
- **B1**：将数据包转发到下一跳 / 下一个网络

:::

### 典型例题

> Explain how a router forwards a packet from one network to another.

<details>
<summary>📝 MS 展开查看</summary>

- **B1**：Reads destination IP address from the packet header
- **B1**：Looks up routing table to determine the best path
- **B1**：Forwards packet to the next hop / next network

</details>

---

:::warning[常见陷阱]

- 混淆 TCP/IP 四层顺序（尤其是 Internet 和 Link 层的顺序）
- 混淆 POP3 和 IMAP 的区别（下载 vs 服务器端管理）
- 认为 circuit switching 不适合实时通信（实际电话网就是 circuit switching）
- 混淆 router 和 switch 的功能（router 连接不同网络，switch 在同一网络内转发）
- 忽略 HTTPS = HTTP + SSL/TLS
- 认为 Internet 层仅负责寻址（实际上也负责路由）

:::
