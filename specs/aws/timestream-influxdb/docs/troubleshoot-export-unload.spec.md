---
id: "@specs/aws/timestream-influxdb/docs/troubleshoot-export-unload"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Troubleshooting UNLOAD"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Troubleshooting UNLOAD

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/troubleshoot-export-unload
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Troubleshooting UNLOAD from Timestream for LiveAnalytics
<a name="troubleshoot-export-unload"></a>

Following is guidance for troubleshooting related to the UNLOAD command.



- **S3 Key length**
  - **Error message:** UNLOAD result file key when using the S3 prefix [%s] provided in the destination will exceed the S3 allowed key length. See documentation for more details. / **How to troubleshoot:** When exporting query results using the `UNLOAD` statement, the [S3 key length](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html), comprising of sum of the length of S3 bucket name and prefix exceeds the maximum supported S3 key length. We recommend to reduce your prefix or bucket name length.
  - **Error message:** UNLOAD result file key when using partitioned\_by [%s] will exceed the S3 allowed key length. See documentation for more details. / **How to troubleshoot:** When exporting query results using the `UNLOAD` statement, the S3 Key length using the partitioned\_by column exceeds the maximum supported [S3 key length](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html). We recommend to partition with an alternate column or reduce the length of the partitioned\_column (if feasible).
  - **Error message:** UNLOAD result file key when using the S3 prefix [%s] along with the partitioned\_by [%s] will exceed the S3 allowed key length. See documentation for more details. / **How to troubleshoot:** When exporting query results using the `UNLOAD` statement, the S3 Key length, comprising of sum of the length of S3 bucket name, the prefix, and the partitioned\_by column name exceeds the maximum supported [S3 key length](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html). We recommend to reduce your prefix, bucket name length, or use an alternate column to partition your data. 
  - **Error message:** The generated S3 object key: %s is too long. See documentation for more details. / **How to troubleshoot:** While processing your query using the `UNLOAD` statement, one of the values in the partitioned column exceeds the maximum supported [S3 key length](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html). The partition column and value can be found in the object key generated. 

- **S3 throttles**
  - **Error message:** We have detected that Amazon S3 is throttling the writes from UNLOAD command. See Amazon Timestream documentation for more information
  - **How to troubleshoot:** Refer to S3 documentation [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html). S3 API call rate could be throttled when multiple readers/writers access the same folder. Please audit the call volume to the bucket provided. If you are using same bucket for multiple concurrent `UNLOAD` queries, try using different buckets for the same. If you are using same bucket for multiple operations other than Timestream for LiveAnalytics `UNLOAD`, consider moving `UNLOAD` results to separate bucket.

