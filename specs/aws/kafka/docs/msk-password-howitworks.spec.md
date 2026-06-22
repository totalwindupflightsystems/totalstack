---
id: "@specs/aws/kafka/docs/msk-password-howitworks"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS How sign-in credentials authentication works"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# How sign-in credentials authentication works

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-password-howitworks
> **target_lang:** meta — documentation tier. ALL sections preserved.



# How sign-in credentials authentication works
<a name="msk-password-howitworks"></a>

Sign-in credentials authentication for Amazon MSK uses SASL/SCRAM (Simple Authentication and Security Layer/ Salted Challenge Response Mechanism) authentication. To set up sign-in credentials authentication for a cluster, you create a Secret resource in [AWS Secrets Manager](https://docs.aws.amazon.com//secretsmanager/?id=docs_gateway), and associate sign-in credentials with that secret. 

SASL/SCRAM is defined in [RFC 5802](https://tools.ietf.org/html/rfc5802). SCRAM uses secured hashing algorithms, and does not transmit plaintext sign-in credentials between client and server. 

**Note**  
When you set up SASL/SCRAM authentication for your cluster, Amazon MSK turns on TLS encryption for all traffic between clients and brokers.