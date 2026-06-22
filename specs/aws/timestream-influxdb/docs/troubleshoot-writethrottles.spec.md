---
id: "@specs/aws/timestream-influxdb/docs/troubleshoot-writethrottles"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Handling WriteRecords throttles"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Handling WriteRecords throttles

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/troubleshoot-writethrottles
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Handling WriteRecords throttles
<a name="troubleshoot-writethrottles"></a>

Your memory store write requests to Timestream may be throttled as Timestream scales to adapt to the data ingestion needs of your application. If your applications encounter throttling exceptions, you must continue to send data at the same (or higher) throughput to allow Timestream to automatically scale to your application's needs. 

Your magnetic store write requests to Timestream may be throttled if the maximum limit of magnetic store partitions receiving ingestion. You will see a throttle message directing you to check the `ActiveMagneticStorePartitions` Cloudwatch metric for this database. This throttle may take up to 6 hours to resolve. To avoid this throttle, you should use the memory store for any high throughput ingestion workload. For magnetic store ingestion, you can target ingesting into fewer partitions by limiting how many series and the time duration that you ingest into

For more information about data ingestion best practices, see [Writes](data-ingest.md).