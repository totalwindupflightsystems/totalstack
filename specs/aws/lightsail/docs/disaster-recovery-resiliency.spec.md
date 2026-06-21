---
id: "@specs/aws/lightsail/docs/disaster-recovery-resiliency"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Resilience"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Resilience

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/disaster-recovery-resiliency
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Resilience in Amazon Lightsail
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

In addition to the AWS global infrastructure, Amazon Lightsail offers several features to help support your data resiliency and backup needs.
+ Copying instance and disk snapshots across Regions. For more information, see [Snapshots](understanding-snapshots-in-amazon-lightsail.md).
+ Automating instance and disk snapshots. For more information, see [Snapshots](understanding-snapshots-in-amazon-lightsail.md).
+ Distributing incoming traffic across multiple instances in a single Availability Zone or multiple Availability Zones using a load balancer. For more information, see [Load balancers](understanding-lightsail-load-balancers.md).