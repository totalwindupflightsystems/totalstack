---
id: "@specs/aws/datasync/docs/infrastructure-security"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Infrastructure security"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Infrastructure security

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/infrastructure-security
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Infrastructure security in AWS DataSync
<a name="infrastructure-security"></a>

As a managed service, AWS DataSync is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access DataSync through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.