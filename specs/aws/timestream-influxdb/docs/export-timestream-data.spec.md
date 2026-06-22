---
id: "@specs/aws/timestream-influxdb/docs/export-timestream-data"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Exporting Timestream data to Amazon S3"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Exporting Timestream data to Amazon S3

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/export-timestream-data
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Exporting Timestream data to Amazon S3
<a name="export-timestream-data"></a>

Irrespective of the target service for migration, we recommend following the below best practices for exporting your Timestream for LiveAnalytics data to Amazon S3, creating a durable intermediate storage layer that serves as the foundation for subsequent database-specific ingestion.

To reliably export data from Timestream for LiveAnalytics tables to Amazon S3, we recommend using [Timestream for LiveAnalytics export tool](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/unload/README.md), which uses the Timestream [UNLOAD](https://docs.aws.amazon.com//timestream/latest/developerguide/supported-sql-constructs.UNLOAD.html) feature — designed for large-scale data exports.

**Timestream for LiveAnalytics export tool**

*Time-based chunking strategy*

Time-based chunking is essential when migrating large volumes of time-series data. This approach breaks down the export process into manageable units that can be independently processed and re-tried on failures, significantly reducing migration risks. It creates checkpoints for easier progress tracking and adds the ability to resume after interruptions. For organizations with continuous data ingestion, this allows newer data to be exported in separate time chunks, enabling better coordination between ongoing operations and migration. The tool uses day-based chunking, storing each day's data with S3 bucket prefix for efficient management. Additionally, chunking can be based on hour, day, month, or year.

*Monitoring migration*

The tool provides an option to capture the migration statistics in a DynamoDB table, tracking metrics such as configurations used, records exported, and other data points for validating the completeness of your migration. We recommend monitoring these metrics closely during your migration and validation. You can also use the logging provided within your orchestration script, capturing execution timestamps, chunk boundaries, and any error conditions encountered. The tool also provides SNS notification if you want to integrate your downstream system to take action on failures.

## Recommendations and best practices
<a name="recommendations-best-practices"></a>

The Timestream for LiveAnalytics export tool provides a flexible and robust solution for exporting data to S3 with various configuration options tailored to your target system requirements. If your target is Timestream for InfluxDB, use [Parquet](https://parquet.apache.org/docs/overview/) format without compression to ensure compatibility with ingestion scripts. For optimal tracking and monitoring, enable DynamoDB logging and configure SNS notifications to receive alerts about export failures or completions.

The tool leverages the Timestream for LiveAnalytics [UNLOAD](https://docs.aws.amazon.com//timestream/latest/developerguide/supported-sql-constructs.UNLOAD.html) feature while overcoming its [partition for query limitations](https://docs.aws.amazon.com//timestream/latest/developerguide/export-unload-limits.html) by automatically exporting data in batches based on your specified time range. You can customize data partitioning by hour, day, month, or year, day being the default. Each partition must remain under approximately 350 GB to avoid memory-related errors, such as query computation exceeding maximum available memory. For example, if your yearly data exceeds 350 GB, consider using monthly partitions or even more granular options like daily or hourly partitioning. If you choose hourly and still get a "The query computation exceeds maximum available memory" error, you can reduce the [number of partitions](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/unload/README.md#optional-parameters), making sure your exports are successful.

The tool offers flexibility in the scope of export, allowing you to export a single table, an entire database, or all databases in your account. For more specialized requirements, such as exporting multiple specific databases, you can build a custom wrapper around this automation. Additionally, you can choose to export the most recent data first by enabling the reverse chronological order option. When restarting after failures, you can either continue with the same migration tag to keep all files under the same S3 prefix or omit the tag to create files under a new prefix. As the tool exports the data in batches, if you encounter failures we recommend starting from the failed batch rather than restarting from the original start time. If you don't specify an end timestamp, the tool automatically uses the current timestamp (UTC) to ensure consistent exports and validation.

## Basic commands
<a name="basic-commands"></a>

**Example : Export a table with DynamoDB logging enabled**  

```
python3.9 unload.py \
    --export-table \
    --database Demo \
    --table Demo \
    --start-time '2020-03-26 17:24:38' \
    --enable-dynamodb_logger true
```

**Example : Export entire database**  

```
python3.9 unload.py \
    --export-database \
    --database Demo \
    --start-time '2020-03-26 17:24:38'
```

**Example : Export all databases**  

```
python3.9 unload.py \
    --export-all_databases \
    --start-time '2020-03-26 17:24:38'
```

**Example : Advanced export with more options**  

```
python unload.py \
    --export-table \
    --database MyDB \
    --table MyTable \
    --start-time '2024-05-14 00:00:00' \
    --end-time '2025-05-14 00:00:00' \
    --partition month \
    --export-format PARQUET \
    --compression GZIP \
    --region us-east-1 \
    --s3-uri s3://my-bucket \
    --enable-dynamodb_logger \
    --sns-topic_arn arn:aws:sns:region:account-id:topic-name
```

For more information, see the unload script's [README.](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/unload/README.md)