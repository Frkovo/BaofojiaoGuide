---
title: MS 模式总结
---

## 通用模式

| 题型 | 分值 | 典型得分点 |
|------|------|------------|
| 对称 vs 非对称加密 | 3-4 | **M1** 密钥数量区别；**A1** 速度/安全性比较；**B1** 应用场景 |
| 数字证书 | 3-4 | **M1** CA 签发；**A1** 证书内容；**B1** 验证过程 |
| 数字签名 | 3-4 | **M1** private key 签名；**A1** public key 验证；**B1** digest/hash |
| SSL/TLS | 4-5 | **M1** 握手目的；**A1** session key 协商；**B1** 身份验证 |
| 量子密码学 | 2-3 | **M1** 量子原理；**A1** 优势；**A1** 局限性 |

## 高频得分短语

- **Symmetric encryption** — "same key used for encryption and decryption" / "key must be shared securely"
- **Asymmetric encryption** — "different keys: public and private" / "public key encrypts, private key decrypts"
- **Digital signature** — "signed with sender's private key" / "verified with sender's public key" / "provides authentication and non-repudiation"
- **Digital certificate** — "issued by a Certificate Authority (CA)" / "binds a public key to an entity" / "contains identity information, public key, expiry date, CA's digital signature"
- **SSL/TLS** — "provides secure communication over a network" / "uses handshake to agree on encryption algorithms and exchange keys" / "uses both asymmetric and symmetric encryption"
- **Quantum cryptography** — "uses principles of quantum mechanics" / "detects eavesdropping" / "currently limited by distance and cost"
