---
title: 常见错误
---

## 错误 1：混淆公钥和私钥的角色

**错误表现**：
- 认为公钥用于解密，私钥用于加密
- 认为所有人都可以使用私钥

**纠正**：
- **Public key**: 公开发布，用于加密或验证签名
- **Private key**: 保密存储，用于解密或签名
- 非对称加密中：公钥加密 → 私钥解密
- 数字签名中：私钥签名 → 公钥验证

## 错误 2：数字签名流程错误

**错误表现**：
- 认为签名是用接收方的私钥
- 认为验证是用发送方的私钥
- 混淆加密和签名的目的

**纠正**：
- **签名**：sender 用 own private key 对 hash(digest) 加密 → digital signature
- **验证**：receiver 用 sender's public key 解密 signature → 比较 digest
- 签名 ≠ 加密。签名验证身份和完整性，加密保护隐私

## 错误 3：混淆 SSL/TLS 与数字证书

**错误表现**：
- 认为 SSL/TLS 和 digital certificate 是同一回事
- 不理解证书在 TLS 握手中的作用

**纠正**：
- **Digital certificate**: 证明持有者身份和公钥归属的文件，由 CA 签发
- **SSL/TLS**: 安全通信协议，使用证书进行身份验证，协商 session key
- 证书是 TLS 握手的一部分：服务器在握手中发送证书供客户端验证

## 错误 4：对称加密的密钥分发问题

**错误表现**：
- 忽略对称加密需要安全信道传输密钥的问题
- 认为对称加密不需要密钥管理

**纠正**：
- Symmetric encryption 最大的挑战是 key distribution
- 如何安全地将 shared key 传递给对方？
- 实践中常结合 asymmetric encryption 来安全传递对称密钥

## 错误 5：混淆加密和哈希

**错误表现**：
- 认为 hash 是加密的一种形式
- 认为 hash 可以解密

**纠正**：
- **Encryption**: 可逆（有密钥可以解密）
- **Hash**: 不可逆（one-way function），用于完整性验证
- 数字签名中使用 hash 生成 message digest，但 hash ≠ encryption

## 错误 6：量子密码学误解

**错误表现**：
- 认为量子密码学已广泛商用
- 混淆量子密码学和量子计算

**纠正**：
- Quantum cryptography 利用量子力学原理（如 quantum key distribution）
- 理论上可检测窃听（任何测量都会改变量子态）
- 目前限制：距离短、成本高、技术尚未成熟
- 量子密码学 ≠ 量子计算机
