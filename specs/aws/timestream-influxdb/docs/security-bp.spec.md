---
id: "@specs/aws/timestream-influxdb/docs/security-bp"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Security"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Security

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/security-bp
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Security
<a name="security-bp"></a>
+ For continuous access to Timestream for LiveAnalytics, ensure that encryption keys are secured and are not revoked or made inaccessible.
+ Monitor API access logs from AWS CloudTrail. Audit and revoke any anomalous access pattern from unauthorized users. 
+ Follow additional guidelines described in [Security best practices for Amazon Timestream for LiveAnalytics](best-practices-security.md).