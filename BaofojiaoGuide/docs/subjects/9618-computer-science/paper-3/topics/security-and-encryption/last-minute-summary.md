---
title: 考前速记
---

## 对称 vs 非对称加密

| 特征 | Symmetric | Asymmetric |
|------|-----------|------------|
| 密钥 | 共享密钥（1个） | 密钥对（公钥 + 私钥） |
| 速度 | 快 | 慢 |
| 密钥分发 | 需要安全信道 | 公钥可公开 |
| 典型算法 | AES, DES | RSA |

## 数字签名流程

```
Sender:
  Message → Hash → Digest → Sign with private key → Signature

Receiver:
  Signature → Verify with public key → Digest1
  Message → Hash → Digest2
  Compare Digest1 == Digest2 → Valid
```

- 提供：authentication, integrity, non-repudiation

## 数字证书

- 由 **CA (Certificate Authority)** 签发
- 包含：身份信息、公钥、有效期、CA 数字签名
- 用途：绑定 public key 到持有者身份

## SSL/TLS 握手

```
Client → Server: Client Hello (支持的算法)
Server → Client: Server Hello (选择算法) + 数字证书
Client → Server: 验证证书 + 发送加密的 session key
双方 → 用 session key 进行对称加密通信
```

## 量子密码学

- 利用量子力学原理检测窃听
- 优势：理论上安全，窃听可检测
- 限制：距离短、成本高、技术不成熟
