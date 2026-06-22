---
id: "@specs/aws/timestream-influxdb/docs/customer-defined-partition-keys-advantages"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Advantages of customer-defined partition keys"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Advantages of customer-defined partition keys

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/customer-defined-partition-keys-advantages
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Advantages of customer-defined partition keys
<a name="customer-defined-partition-keys-advantages"></a>

**Enhanced query performance: **Customer-defined partition keys enable you to optimize your query execution and improve overall query performance. By defining partition keys that align with your query patterns, you can minimize data scanning and optimize data pruning, resulting in lower query latency.

**Better long term performance predictability: **Customer-defined partition keys allow customers to distribute data evenly across partitions, improving the efficiency of data management. This will ensure that your query performance remains stable as your data stored scales over time.