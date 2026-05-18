---
title: 知识点总结
---

## Encryption Basics（加密基础）

- **Plain text（明文）**: 未加密的原始信息
- **Cipher text（密文）**: 加密后的信息
- **Key（密钥）**: 用于加密和解密的参数
- **Encryption（加密）**: Plain text + Key → Cipher text
- **Decryption（解密）**: Cipher text + Key → Plain text
- 安全目标：机密性（Confidentiality）、完整性（Integrity）、认证（Authentication）

### Symmetric vs Asymmetric

| 特性 | Symmetric | Asymmetric |
|------|-----------|------------|
| 密钥数 | 1 个共享密钥 | 2 个（公钥 + 私钥） |
| 速度 | 快 | 慢 |
| 密钥分发 | 困难（需安全通道） | 公钥可公开 |
| 典型算法 | AES, DES, 3DES | RSA, ECC |

## Symmetric Cryptography（对称加密）

- 加密和解密使用 **同一密钥**
- 优点：速度快，适合大量数据加密
- 缺点：密钥分发困难，n 个用户需要 $$\frac{n(n-1)}{2}$$ 个密钥对

:::warning[对称加密的关键问题]
如何安全地将密钥传递给通信对方？若密钥被截获，加密即失效
:::

## Asymmetric Cryptography（非对称加密）

- **Public Key（公钥）**: 公开分发，用于加密
- **Private Key（私钥）**: 保密保存，用于解密
- 公钥加密的信息只能用对应的私钥解密
- 反之：私钥签名，公钥验证（数字签名）

$$\text{Plain text} \xrightarrow{\text{公钥}} \text{Cipher text} \xrightarrow{\text{私钥}} \text{Plain text}$$

## Digital Certificates（数字证书）

- 由 **CA** (Certificate Authority) 颁发
- 用于绑定公钥和身份信息

### 证书内容

- 持有者的**公钥**
- 持有者的**身份信息**（域名/组织名）
- **有效期**（Not Before / Not After）
- CA 的**数字签名**
- 证书序列号、签名算法标识

### 获取过程

1. 实体生成密钥对，向 CA 提交公钥和身份信息
2. CA 验证身份后，签发数字证书
3. 实体将证书部署到服务器

## Digital Signatures（数字签名）

- 用于验证信息完整性、来源真实性（不可否认性）

### 签名流程

1. 对消息计算 **Hash**（哈希值/摘要）
2. 用**发送方私钥**加密 Hash → 数字签名
3. 发送消息 + 签名给接收方

### 验证流程

1. 接收方用**发送方公钥**解密签名 → 得到 Hash
2. 对消息重新计算 Hash
3. 比较两个 Hash：一致则签名有效

:::tip[]
数字签名 ≠ 加密。签名验证身份，加密保护内容，两者可结合使用
:::

## SSL/TLS（安全传输协议）

- **SSL** (Secure Sockets Layer) / **TLS** (Transport Layer Security)
- 目的：在客户端和服务器之间建立加密通信通道
- 位于传输层和应用层之间

### TLS Handshake（握手过程）

1. **Client Hello**: 客户端发送支持的 TLS 版本、加密套件列表
2. **Server Hello**: 服务器选择版本和加密套件，发送数字证书
3. **Certificate Verification**: 客户端验证服务器证书（检查 CA 签名、有效期）
4. **Key Exchange**: 客户端生成 Pre-master Secret，用服务器公钥加密发送
5. **Session Keys**: 双方根据 Pre-master Secret 生成对称会话密钥
6. **Secure Communication**: 使用对称密钥加密通信

:::warning[]
握手完成后使用**对称加密**（效率高），非对称加密仅用于密钥交换阶段
:::

## Quantum Cryptography（量子密码学）

### 原理

- 利用量子力学特性（如量子态不可克隆定理）实现安全通信
- **QKD** (Quantum Key Distribution): 使用光子偏振态传递密钥
- 任何窃听行为都会改变量子态，从而被检测到

### Benefits（优势）

- **可检测窃听**（Eavesdropping Detection）：量子态被测量即改变，通信方立即知晓
- 理论上无条件安全（不依赖计算复杂度）

### Drawbacks（局限性）

- **昂贵**: 需要专用硬件（单光子源、探测器）
- **距离限制**: 量子信号在光纤中衰减快，目前需中继器（几百公里上限）
- 技术尚不成熟，难以大规模商用部署
