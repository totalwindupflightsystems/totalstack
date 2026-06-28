---
id: "@specs/aws/datasync/docs/internetwork-traffic-privacy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Internetwork traffic privacy"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Internetwork traffic privacy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/internetwork-traffic-privacy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Internetwork traffic privacy
<a name="internetwork-traffic-privacy"></a>

We recommend configuring your source and destination locations with the highest level of security that each one supports. When connecting to a location, AWS DataSync works with the most secure version of the data access protocol that the storage system uses. Additionally, consider limiting subnet traffic to known protocols and services.

DataSync secures the connection between locations—including between AWS accounts, AWS Regions, and Availability Zones—by using Transport Layer Security (TLS) 1.3.