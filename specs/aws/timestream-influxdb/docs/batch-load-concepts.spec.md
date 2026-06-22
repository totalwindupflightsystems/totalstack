---
id: "@specs/aws/timestream-influxdb/docs/batch-load-concepts"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Concepts"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Concepts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/batch-load-concepts
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Batch load concepts in Timestream
<a name="batch-load-concepts"></a>

Review the following concepts to better understand batch load functionality. 

**Batch load task** – The task that defines your source data and destination in Amazon Timestream. You specify additional configuration such as the data model when you create the batch load task. You can create batch load tasks through the AWS Management Console, the AWS CLI, and the AWS SDKs. 

**Import destination** – The destination database and table in Timestream. For information about creating databases and tables, see [Create a database](console_timestream.md#console_timestream.db.using-console) and [Create a table](console_timestream.md#console_timestream.table.using-console).

**Data source** – The source CSV file that is stored in an S3 bucket. For information about preparing the data file, see [Preparing a batch load data file](batch-load-preparing-data-file.md). For information about S3 pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

**Batch load error report** – A report that stores information about the errors of a batch load task. You define the S3 location for batch load error reports as part of a batch load task. For information about information in the reports, see [Using batch load error reports](batch-load-using-error-reports.md).

**Data model mapping** – A batch load mapping for time, dimensions, and measures that is from a data source in an S3 location to a target Timestream for LiveAnalytics table. For more information, see [Data model mappings for batch load](batch-load-data-model-mappings.md).