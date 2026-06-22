---
id: "@specs/aws/kafka/docs/port-info"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Port information"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Port information

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/port-info
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Port information
<a name="port-info"></a>

Use the following port numbers so that Amazon MSK can communicate with client machines:
+ To communicate with brokers in plaintext, use port 9092.
+ To communicate with brokers with TLS encryption, use port 9094 for access from within AWS and port 9194 for public access.
+ To communicate with brokers with SASL/SCRAM, use port 9096 for access from within AWS and port 9196 for public access.
+ To communicate with brokers in a cluster that is set up to use [IAM access control](iam-access-control.md), use port 9098 for access from within AWS and port 9198 for public access.
+ To communicate with brokers using IPv6 network type in plaintext, use port 20092
+ To communicate with brokers in a cluster that is set up to use IAM access control using IPv6, use port 20098.
+ To communicate with brokers with SASL/SCRAM using IPv6, use port 20096.
+ To communicate with brokers with TLS encryption using IPv6, use port 20094.