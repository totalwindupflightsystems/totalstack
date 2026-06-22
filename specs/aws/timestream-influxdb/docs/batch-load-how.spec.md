---
id: "@specs/aws/timestream-influxdb/docs/batch-load-how"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Batch load"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Batch load

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/batch-load-how
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Batch load
<a name="batch-load-how"></a>

With *batch load* for Amazon Timestream for LiveAnalytics, you can ingest CSV files stored in Amazon S3 into Timestream in batches. With this new functionality, you can have your data in Timestream for LiveAnalytics without having to rely on other tools or write custom code. You can use batch load for backfilling data with flexible wait times, such as data that isn't immediately required for querying or analysis.

You can create batch load tasks by using the AWS Management Console, the AWS CLI, and the AWS SDKs. For more information, see [Using batch load with the console](batch-load-using-console.md), [Using batch load with the AWS CLI](batch-load-using-cli.md), and [Using batch load with the AWS SDKs](batch-load-using-sdk.md).

For more information about batch load, see [Using batch load in Timestream for LiveAnalytics](batch-load.md).