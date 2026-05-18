---
title: 题型分析
---

# 题型分析：Security and Encryption

---

## 题型 1：对称加密与非对称加密（Symmetric vs Asymmetric Encryption）

### 题目特征

- 比较两种加密方式
- 完成表格
- 解释密钥管理过程

:::note[标准解题方法]

1. Symmetric：同一把 key 加密和解密
2. Asymmetric：公钥加密，私钥解密（或私钥签名，公钥验证）
3. 比较维度：密钥数量、速度、安全性、密钥分发难度
4. 对称加密速度快但密钥分发困难，非对称加密解决密钥分发但速度慢

:::

:::info[评分标准（MS 模式）]

- **M1**：正确指出对称加密使用 shared key
- **A1**：正确指出非对称加密使用 key pair
- **B1**：比较速度或安全性

:::

### 典型例题 1：9618/w22/qp/32 Q6(a)

> (a) Describe the difference between symmetric encryption and asymmetric encryption.

<details>
<summary>📝 MS 展开查看</summary>

- **M1**：Symmetric encryption uses the same key for both encryption and decryption
- **A1**：Asymmetric encryption uses a pair of keys: a public key and a private key
- **A1**：In asymmetric encryption, the public key encrypts and the private key decrypts
- **B1**：Symmetric encryption is faster / asymmetric encryption solves the key distribution problem

</details>

### 典型例题 2：9618/s23/qp/32 Q5(b)

> A website uses asymmetric encryption to securely receive data from customers.
> (b) Explain how asymmetric encryption ensures that only the website can read the data sent by a customer.

<details>
<summary>📝 MS 展开查看</summary>

- **M1**：Customer encrypts data using the website's public key
- **A1**：Only the website's private key can decrypt the data
- **B1**：The private key is kept secret / known only to the website
- **B1**：Even if the data is intercepted, without the private key it cannot be decrypted

</details>

---

## 题型 2：数字证书（Digital Certificates）

### 题目特征

- 解释数字证书的获取方式
- 描述证书内容
- 说明证书验证流程

:::note[标准解题方法]

1. 证书由 CA (Certificate Authority) 签发
2. 证书将公钥绑定到持有者身份
3. 获取流程：生成 key pair → 提交 CSR → CA 验证 → 签发证书
4. 证书内容：持有者信息、公钥、CA 信息、有效期、CA 数字签名
5. 验证流程：浏览器用 CA 公钥验证 CA 签名，检查有效期，匹配域名

:::

:::info[评分标准（MS 模式）]

- **M1**：CA (Certificate Authority) 的角色
- **A1**：证书的内容
- **B1**：验证证书有效性的方法

:::

### 典型例题 1：9618/w22/qp/32 Q6(b)

> (b) A website uses a digital certificate to prove its identity. Describe how the website obtains a digital certificate.

<details>
<summary>📝 MS 展开查看</summary>

- **M1**：网站生成 public key 和 private key
- **A1**：网站将 public key 和身份信息发送给 CA (Certificate Authority)
- **B1**：CA 验证网站的身份
- **B1**：CA 签发 digital certificate，用 CA's private key 签名

</details>

### 典型例题 2：9618/s22/qp/32 Q7

> (a) State **three** items of information that are contained in a digital certificate.
> (b) Describe how a web browser uses a digital certificate to verify the identity of a website.

<details>
<summary>📝 MS 展开查看</summary>

(a) Items (any 3):
- **M1**：持有者的公钥（public key of the certificate holder）
- **A1**：持有者的身份信息（name / organisation of holder）
- **A1**：CA 的名称和数字签名
- **B1**：有效期（validity period / expiry date）
- **B1**：证书序列号（serial number）

(b) Verification process:
- **M1**：Browser checks the CA's digital signature using CA's public key
- **A1**：Browser checks the certificate has not expired
- **A1**：Browser confirms the certificate matches the website being visited

</details>

---

## 题型 3：数字签名（Digital Signatures）

### 题目特征

- 解释数字签名如何验证发送者身份和消息完整性
- 说明 non-repudiation 的实现

:::note[标准解题方法]

1. Sender：对 message 做 hash → 用 private key 加密 hash → digital signature
2. Receiver：用 sender's public key 解密 signature 得到 digest1
3. Receiver：对收到的 message 做同样的 hash 得到 digest2
4. 比较 digest1 和 digest2：一致则 signature valid

:::

:::info[评分标准（MS 模式）]

- **M1**：用发送者的私钥签名
- **A1**：用发送者的公钥验证
- **B1**：使用 hash / message digest
- **B2**：提供 authentication, integrity, non-repudiation

:::

### 典型例题 1：9618/w22/qp/33 Q6(c)

> A software company distributes updates with digital signatures. Explain how a digital signature is used to verify that an update has come from the company and has not been altered.

<details>
<summary>📝 MS 展开查看</summary>

- **M1**：The company creates a hash (message digest) of the update file
- **A1**：The hash is encrypted with the company's private key — this is the digital signature
- **B1**：The user decrypts the signature using the company's public key to obtain the original hash
- **B1**：The user hashes the downloaded update and compares it with the decrypted hash
- **B2**：If they match — file is authentic (from the company) and has not been tampered with

</details>

### 典型例题 2：Non-repudiation

> (c) Explain how a digital signature provides non-repudiation.

<details>
<summary>📝 MS 展开查看</summary>

- **M1**：Non-repudiation means the sender cannot deny having sent the message
- **A1**：The digital signature is created using the sender's private key
- **B1**：Only the sender has access to their private key
- **B1**：If the signature is verified with the sender's public key, it proves the sender signed it

</details>

---

## 题型 4：SSL / TLS

### 题目特征

- 解释 SSL/TLS 的目的
- 描述握手过程
- 说明如何建立安全连接

:::note[标准解题方法]

1. SSL/TLS 在传输层之上为应用层提供安全通信
2. Handshake 过程：
   - Client Hello：发送支持的 cipher suites
   - Server Hello：选择 cipher suite，发送数字证书
   - Client：验证证书，生成 pre-master secret，用 server 公钥加密发送
   - Server：用私钥解密得到 pre-master secret，生成 session key
   - 双方：使用 session key 进行对称加密通信
3. 混合使用 asymmetric（握手）和 symmetric（数据传输）

:::

:::info[评分标准（MS 模式）]

- **M1**：SSL/TLS 目的 — 为网络通信提供加密
- **A1**：Handshake 过程描述
- **B1**：区分握手使用 asymmetric 和后续通信使用 symmetric

:::

### 典型例题 1：9618/w21/qp/31 Q8

> (a) State the purpose of SSL/TLS.
> (b) Describe the SSL/TLS handshake process that establishes a secure connection between a browser and a web server.

<details>
<summary>📝 MS 展开查看</summary>

(a) Purpose:
- **M1**：为网络通信提供加密（encryption）和身份验证（authentication）
- **A1**：确保数据传输的保密性和完整性

(b) Handshake:
- **M1**：Browser sends "Client Hello" with supported encryption algorithms
- **A1**：Server responds with "Server Hello", chooses algorithm, sends digital certificate
- **A1**：Browser verifies the certificate against a trusted CA
- **B1**：Browser generates pre-master secret, encrypts with server's public key, sends to server
- **B1**：Server decrypts with private key; both use pre-master secret to generate session key
- **B1**：All subsequent data is encrypted using the symmetric session key

</details>

### 典型例题 2：SSL/TLS 安全性

> A student connects to an online banking website using HTTPS. Explain how SSL/TLS ensures that the data exchanged is secure.

<details>
<summary>📝 MS 展开查看</summary>

- **M1**：SSL/TLS 使用 asymmetric encryption 在握手阶段安全交换 session key
- **A1**：使用 symmetric encryption 加密后续的所有通信（更快）
- **A1**：数字证书确保用户连接的是真正的银行服务器
- **B1**：消息完整性通过 MAC (Message Authentication Code) 保证

</details>

---

## 题型 5：量子密码学（Quantum Cryptography）

### 题目特征

- 描述量子密码学的优势
- 列出局限性
- 解释如何检测窃听

:::note[标准解题方法]

1. 利用量子力学原理（量子叠加、不确定性原理）
2. QKD (Quantum Key Distribution)：使用光子传输密钥
3. 任何窃听行为都会改变量子态，从而被检测到
4. 优势：理论上绝对安全
5. 局限性：距离限制、设备昂贵、技术不成熟

:::

:::info[评分标准（MS 模式）]

- **M1**：解释量子密码学的基本原理
- **A1**：列出优势（理论上安全、可检测窃听）
- **B1**：列出局限性（当前限制）

:::

### 典型例题 1：9618/s23/qp/31 Q9(b)

> (b) Describe **one** benefit and **one** drawback of using quantum cryptography compared to traditional encryption methods.

<details>
<summary>📝 MS 展开查看</summary>

Benefit:
- **M1**：理论上绝对安全（theoretically unbreakable）
- **A1**：任何窃听尝试都会改变量子态，可被检测到（eavesdropping is detectable）

Drawback:
- **B1**：距离限制 — 量子信号在光纤中传输距离有限
- **B1**：设备成本高 / 技术要求高
- **B1**：技术尚不成熟，未广泛商用

</details>

### 典型例题 2：窃听检测

> (a) Explain how quantum cryptography can detect if a message has been intercepted during transmission.

<details>
<summary>📝 MS 展开查看</summary>

- **M1**：量子密码学使用量子态（如光子偏振）传输密钥
- **A1**：根据量子力学的不确定性原理，观测会改变量子态
- **A1**：如果窃听者拦截并测量光子，量子态会改变
- **B1**：接收方发现错误率异常升高，即可判断存在窃听

</details>

---

:::warning[常见陷阱]

- 混淆公钥和私钥的用途（加密 vs 签名场景）
- 数字签名流程中混淆加密解密的密钥方向
- 认为 SSL/TLS 和数字证书是同一概念
- 忽略对称加密的密钥分发问题
- 混淆 hash 和 encryption 的区别
- 错误认为量子密码学已广泛商用
- 混淆 SSL/TLS 握手中 asymmetric 和 symmetric 加密的使用阶段
- 认为非对称加密比对称加密更安全（实际各有适用场景）

:::
