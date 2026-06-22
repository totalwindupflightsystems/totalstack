---
id: "@specs/aws/timestream-influxdb/docs/customer-defined-partition-keys-low-cardinality-dimensions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Customer-defined partition keys and low cardinality dimensions"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Customer-defined partition keys and low cardinality dimensions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/customer-defined-partition-keys-low-cardinality-dimensions
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Customer-defined partition keys and low cardinality dimensions
<a name="customer-defined-partition-keys-low-cardinality-dimensions"></a>

If you decide to use a partition key with very low cardinality, such as a specific region or state, it is important to note that the data for for other entities such as `customerID`, `ProductCategory`, and others, could end up spread across too many partitions sometimes with little or no data present. This can lead to inefficient query execution and decreased performance.

To avoid this, we recommend you choose dimensions that are not only part of your key filtering condition but have higher cardinality. This will help ensure that the data is evenly distributed across the partitions and improve query performance.