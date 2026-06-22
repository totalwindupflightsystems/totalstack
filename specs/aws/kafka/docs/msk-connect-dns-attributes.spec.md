---
id: "@specs/aws/kafka/docs/msk-connect-dns-attributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configure DNS attributes"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Configure DNS attributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-connect-dns-attributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure DNS attributes for your VPC
<a name="msk-connect-dns-attributes"></a>

Make sure you have the VPC DNS attributes correctly configured as described in [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support) and [DNS hostnames](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-hostnames) in the *Amazon VPC User Guide*.

See [Resolving DNS queries between VPCs and your network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html) in the *Amazon Route 53 Developer Guide* for information on using inbound and outbound resolver endpoints to connect other networks to your VPC to work with your connector.