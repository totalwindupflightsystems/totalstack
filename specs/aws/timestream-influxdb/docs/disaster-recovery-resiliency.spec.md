---
id: "@specs/aws/timestream-influxdb/docs/disaster-recovery-resiliency"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Resilience"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Resilience

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/disaster-recovery-resiliency
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Resilience in Amazon Timestream Live Analytics
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

For information about data protection functionality for Timestream available through AWS Backup, see [Working with AWS Backup](backups.md).