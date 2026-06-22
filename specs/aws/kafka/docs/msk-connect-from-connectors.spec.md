---
id: "@specs/aws/kafka/docs/msk-connect-from-connectors"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Connecting from connectors"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Connecting from connectors

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-connect-from-connectors
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Connecting from connectors
<a name="msk-connect-from-connectors"></a>

The following best practices can improve the performance of your connectivity to Amazon MSK Connect.

## Do not overlap IPs for Amazon VPC peering or Transit Gateway
<a name="CIDR-ip-ranges"></a>

If you are using Amazon VPC peering or Transit Gateway with Amazon MSK Connect, do not configure your connector for reaching the peered VPC resources with IPs in the CIDR ranges:
+ "10.99.0.0/16"
+ "192.168.0.0/16"
+ "172.21.0.0/16"