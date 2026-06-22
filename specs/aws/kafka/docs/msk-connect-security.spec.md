---
id: "@specs/aws/kafka/docs/msk-connect-security"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Security"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Security

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-connect-security
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Security for MSK Connect
<a name="msk-connect-security"></a>

You can use an Interface VPC Endpoint, powered by AWS PrivateLink, to prevent traffic between your Amazon VPC and Amazon MSK-Connect compatible APIs from leaving the Amazon network. Interface VPC endpoints don't require an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. For more information, see [Use Amazon MSK APIs with Interface VPC Endpoints](privatelink-vpc-endpoints.md).