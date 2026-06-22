---
id: "@specs/aws/timestream-influxdb/docs/metrics-dimensions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Metrics and dimensions"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Metrics and dimensions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/metrics-dimensions
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Timestream for LiveAnalytics metrics and dimensions
<a name="metrics-dimensions"></a>

When you interact with Timestream for LiveAnalytics, it sends the following metrics and dimensions to Amazon CloudWatch. All metrics are aggregated and reported every minute. You can use the following procedures to view the metrics for Timestream for LiveAnalytics.

**To view metrics using the CloudWatch console**

Metrics are grouped first by the service namespace, and then by the various dimension combinations within each namespace.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. If necessary, change the Region. On the navigation bar, choose the Region where your AWS resources reside. For more information, see [AWS Service Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html).

1. In the navigation pane, choose **Metrics**.

1. Under the **All metrics** tab, choose `AWS/Timestream for LiveAnalytics.`

**To view metrics using the AWS CLI**
+ At a command prompt, use the following command.

  ```
  1. aws cloudwatch list-metrics --namespace "AWS/Timestream"
  ```

## Dimensions for Timestream for LiveAnalytics metrics
<a name="mcs-metric-dimensions"></a>

The metrics for Timestream for LiveAnalytics are qualified by the values for the account, table name, or operation. You can use the CloudWatch console to retrieve Timestream for LiveAnalytics data along any of the dimensions in the following table:


|  Dimension  |  Description  | 
| --- | --- | 
|  DatabaseName  | This dimension limits the data to a specific Timestream for LiveAnalytics database. This value can be any database in the current Region and the current AWS account  | 
|  Operation  | This dimension limits the data to one of the Timestream for LiveAnalytics operations, such as `Storage`, `WriteRecords`, `BatchLoad`, or `ScheduledQuery`. See the Timestream for LiveAnalytics Query API Reference for a list of available values. | 
|  TableName  | This dimension limits the data to a specific table in a Timestream for LiveAnalyticss database.  | 

**Important**  
`CumulativeBytesMetered`, `UserErrors` and `SystemErrors` metrics only have the `Operation` dimension. `SuccessfulRequestLatency` metrics always have `Operation` dimension, but may also have the `DatabaseName` and `TableName` dimensions too, depending on the value of `Operation`. This is because Timestream for LiveAnalytics table-level operations have `DatabaseName` and `TableName` as dimensions, but account level operations do not.

## Timestream for LiveAnalytics metrics
<a name="mcs-metrics"></a>

**Note**  
Amazon CloudWatch aggregates all the following Timestream for LiveAnalytics metrics at one-minute intervals.


**General metrics**  

| Metric | Description | 
| --- | --- | 
| `SuccessfulRequestLatency` | The successful requests to Timestream for LiveAnalytics during the specified time period. SuccessfulRequestLatency can provide two different kinds of information:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html)<br />SuccessfulRequestLatency reflects activity only within Timestream for LiveAnalytics and does not take into account network latency or client-side activity.<br /> Units: `Milliseconds`[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html)<br />Valid Statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html) | 


**Writing and storage metrics**  

| Metric | Description | 
| --- | --- | 
| `MagneticStoreRejectedRecordCount` | The number of magnetic store written records that were rejected asynchronously. This can happen if the new record has a version that is less than the current version or the new record has version equal to the current version but has different data.<br /> Units: `Count`[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html)<br />Valid Statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html) | 
| `MagneticStoreRejectedUploadUserFailures` | The number of magnetic store rejected record reports that were not uploaded due to user errors. This can be due to IAM permissions not configured correctly or a deleted S3 bucket.<br /> Units: `Count`[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html)<br />Valid Statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html) | 
| `MagneticStoreRejectedUploadSystemFailures` | The number of magnetic store rejected record reports that were not uploaded due to system errors. <br /> Units: `Count`[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html)<br />Valid Statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html) | 
| `ActiveMagneticStorePartitions` | The number of magnetic store partitions actively ingesting data at a given time.<br /> Units: `Count`[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html)<br />Valid Statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html) | 
| `MagneticStorePendingRecordsLatency` | The oldest write to a magnetic store that is not available for query. Records written to the magnetic store will be available for querying within 6 hours. <br /> Units: `Milliseconds`[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html)<br />Valid Statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html) | 
| `MemoryCumulativeBytesMetered` | The amount of data stored in memory store, in bytes<br /> Units: `Bytes`<br /> Dimensions: `Operation`<br />Valid Statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html) | 
| `MagneticCumulativeBytesMetered` | The amount of data stored in magnetic store, in bytes<br /> Units: `Bytes`<br /> Dimensions: `Operation`<br />Valid Statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html) | 
| `CumulativeBytesMetered` | The amount of data metered by ingestion to Timestream for LiveAnalytics, in bytes.<br /> Units: `Bytes`<br />Dimensions: `Operation`<br />Valid Statistics: `Sum` | 
| `NumberOfRecords` | The number of records ingested into Timestream for LiveAnalytics.<br /> Units: `Count`<br />Dimensions: `Operation`<br />Valid Statistics: `Sum` | 


**Query metrics**  

| Metric | Description | 
| --- | --- | 
| `CumulativeBytesMetered` | The amount of data scanned by queries sent to Timestream for LiveAnalytics, in bytes. <br /> Units: `Bytes`<br /> Dimensions: `Operation`<br />Valid Statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html) | 
| ResourceCount | The Timestream Compute Units (TCUs) consumed for query workload in the account. This metric is emitted with maximum and minimum compute units for every minute during active query workload from the account.<br />Units: `Count`<br />Valid Statistics: Minimum, Maximum<br />Dimensions: `Service: Timestream`, `Resource: QueryTCU`, `Type: Resource`, `Class: OnDemand` | 


**Error metrics**  

| Metric | Description | 
| --- | --- | 
| `SystemErrors` | The requests to Timestream for LiveAnalytics that generate a SystemError during the specified time period. A SystemError usually indicates an internal service error. <br /> Units: `Count`<br /> Dimensions: `Operation`<br />Valid Statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html) | 
| `UserErrors` | Requests to Timestream for LiveAnalytics that generate an InvalidRequest error during the specified time period. An InvalidRequest usually indicates a client-side error, such as an invalid combination of parameters, an attempt to update a nonexistent table, or an incorrect request signature. UserErrors represents the aggregate of invalid requests for the current AWS Region and the current AWS account. <br /> Units: `Count`<br /> Dimensions: `Operation`<br />Valid Statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html) | 

**Important**  
Not all statistics, such as `Average` or `Sum`, are applicable for every metric. However, all of these values are available through the Timestream for LiveAnalytics console, or by using the CloudWatch console, AWS CLI, or AWS SDKs for all metrics. 