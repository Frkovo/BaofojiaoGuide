---
title: 解题方法
---

## 1. 加密过程说明题

**方法步骤**：
1. 区分 symmetric 和 asymmetric：
   - **Symmetric**: 同一个 key 加密和解密，需要安全地共享 key
   - **Asymmetric**: public key 加密，private key 解密（或反之）
2. 描述加密流程：明文 → 加密算法 + 密钥 → 密文 → 传输 → 解密 → 明文
3. 指出密钥管理是核心问题

## 2. 数字签名流程

**方法步骤**：
1. 发送方：用 hash 算法生成 message digest → 用 own private key 加密 digest → 生成 digital signature
2. 接收方：用发送方的 public key 解密 signature 得到 digest1 → 对收到的消息执行同样的 hash 得到 digest2
3. 比较 digest1 和 digest2 → 相等则验证成功
4. 关键词：integrity（完整性）、authentication（身份验证）、non-repudiation（不可否认性）

## 3. 数字证书获取与使用

**方法步骤**：
1. 网站生成 public/private key pair
2. 网站向 CA (Certificate Authority) 提交 CSR (Certificate Signing Request)
3. CA 验证网站身份
4. CA 签发数字证书（包含公钥、身份信息、CA 的数字签名）
5. 用户访问网站时获取证书
6. 用户用 CA 的 public key 验证证书的有效性
7. 确认身份后建立加密通信

## 4. SSL/TLS 握手

**方法步骤**：
1. Client Hello：发送支持的加密算法列表
2. Server Hello：选择加密算法，发送数字证书
3. Client：验证证书，生成 session key，用 server 的 public key 加密发送
4. Server：用 private key 解密得到 session key
5. 双方使用 session key 进行对称加密通信
