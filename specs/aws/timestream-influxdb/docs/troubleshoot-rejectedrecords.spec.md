---
id: "@specs/aws/timestream-influxdb/docs/troubleshoot-rejectedrecords"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Handling rejected records"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Handling rejected records

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/troubleshoot-rejectedrecords
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Handling rejected records
<a name="troubleshoot-rejectedrecords"></a>

If Timestream rejects records, you will receive a `RejectedRecordsException` with details about the rejection. Please refer to [Handling write failure](https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.write.html#code-samples.write.rejectedRecordException) for more information on how to extract this information from the WriteRecords response.

 All rejections will be included in this response **with the exception of updates to the magnetic store where the new record's version is less than or equal to the existing record's version**. In this case, Timestream will not update the existing record that has the higher version. Timestream will reject the new record with lower or equal version and write these errors asynchronously to your S3 bucket. In order to receive these asynchronous error reports, you should set the `MagneticStoreRejectedDataLocation` property in `MagneticStoreWriteProperties` on your table. 