---
title: Security and Encryption
---

本主题涵盖加密技术（encryption）、安全协议（SSL/TLS）、数字证书（digital certificates）、数字签名（digital signatures）和量子密码学（quantum cryptography）。

## 加密技术（Encryption）

- **Symmetric encryption**：发送方和接收方使用相同的密钥（shared key）
- **Asymmetric encryption**：使用公钥（public key）和私钥（private key）密钥对

## SSL / TLS

- SSL (Secure Sockets Layer) 和 TLS (Transport Layer Security)
- 为网络通信提供加密和身份验证
- Handshake 协议：协商加密算法、交换密钥、验证身份

## 数字证书（Digital Certificates）

- 由 Certificate Authority (CA) 签发
- 将公钥绑定到持有者身份
- 包含：持有者信息、CA 信息、公钥、有效期、CA 的数字签名

## 数字签名（Digital Signatures）

- 用于验证消息的完整性和发送者身份
- 使用发送者的私钥签名，接收者用公钥验证

## 量子密码学（Quantum Cryptography）

- 利用量子力学原理（如量子纠缠、不确定性原理）
- 理论上可检测任何窃听行为
