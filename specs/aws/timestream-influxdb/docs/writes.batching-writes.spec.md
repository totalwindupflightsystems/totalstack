---
id: "@specs/aws/timestream-influxdb/docs/writes.batching-writes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Batching writes"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Batching writes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/writes.batching-writes
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Batching writes with WriteRecords API
<a name="writes.batching-writes"></a>

Amazon Timestream for Live Analytics enables you to write data points from a single time series and/or data points from many series in a single write request. Batching multiple data points in a single write operation is beneficial from a performance and cost perspective. See [Writes](metering-and-pricing.writes.md) in the Metering and Pricing section for more details.

**Note**  
Your write requests to Timestream for Live Analytics may be throttled as Timestream for Live Analytics scales to adapt to the data ingestion needs of your application. If your applications encounter throttling exceptions, you must continue to send data at the same (or higher) throughput to allow Timestream for Live Analytics to automatically scale to your application's needs. 