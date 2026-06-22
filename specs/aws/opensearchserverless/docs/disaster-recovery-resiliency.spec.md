---
id: "@specs/aws/opensearchserverless/docs/disaster-recovery-resiliency"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Resilience"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Resilience

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/disaster-recovery-resiliency
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Resilience in Amazon OpenSearch Service
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

In addition to the AWS global infrastructure, OpenSearch Service offers several features to help support your data resiliency and backup needs:
+ [Multi-AZ domains and replica shards](managedomains-multiaz.md)
+ [Automated and manual snapshots](managedomains-snapshots.md)