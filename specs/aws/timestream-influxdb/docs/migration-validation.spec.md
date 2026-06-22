---
id: "@specs/aws/timestream-influxdb/docs/migration-validation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Migration validation script"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Migration validation script

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/migration-validation
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Migration validation script
<a name="migration-validation"></a>

The validation script compares logical row/point counts between a source table (Amazon Timestream or Amazon Athena) and an InfluxDB bucket measurement, with optional time-range specifications. This tool helps ensure data integrity during migration processes by running parallel queries against both systems and comparing the results.

The validation script supports queries against either the exported dataset in Athena or the original Timestream database/table. Be aware that querying Timestream directly may lead to inaccurate comparisons if data has been written since the export. The validation script can be run anytime after ingestion has begun. It first polls InfluxDB's metrics endpoint to wait for the [WAL (Write-Ahead Log)](https://docs.influxdata.com/influxdb/v2/reference/internals/storage-engine/#write-ahead-log-wal) to flush completely, ensuring all data processing, including post-ingestion file merging and de-duplication, is finished. The script then executes count-only queries over identical time windows, comparing results to highlight matches or mismatches. It supports optional schema/tag filtering for transformed schemas where dimensions are used as fields, and produces human-readable timing and result summaries to facilitate validation of the migration process.

*Prerequisites and installation*

See the prerequisites and installation section in the [Migration Validation Script README](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/README.md#installation).

*Usage*

```
python validator.py [options]
```

All settings can be supplied as CLI flags or environment variables. See the example.env file within the repository.

For troubleshooting and recommendations see the [Migration Validation Script README](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/README.md#installation).

*Cleanup*

After finishing a migration, following resources/artifacts will be created:
+ An Athena table, containing Timestream for LiveAnalytics data. By default, this is <Timestream database name>\_<Timestream table name> in the default Athena database.
+ An Athena table, containing transformed line protocol data. By default, this is lp\_<Athena table name> in the default Athena database.
+ Line protocol data within your S3 bucket, with the path <Timestream database name>/<Timestream table name>/unload-<%Y-%m-%d-%H:%M:%S>/line-protocol-output.
+ Unloaded data that was created as part of Timestream for LiveAnalytics export tool.
+ Downloaded data and logs on your EC2 instance.
+ DynamoDB table if used for logging as part of Timestream for LiveAnalytics export tool.

*Cleaning up Athena resources*

To delete any Athena table, run the following [AWS CLI ](https://aws.amazon.com/cli/)command, replacing <Athena table name> with the name of the table that you want to delete and <Athena database name> with the name of the Athena database that the table resides in:

```
aws glue delete-table \
    --database-name <Athena database name> \
    --name <Athena table name>
```

*Cleaning up S3 resources*

To delete line protocol data within your S3 bucket, run the following AWS CLI command, replacing <S3 bucket name> with the name of your S3 bucket, <Timestream database name> with the name of your Timestream for LiveAnalytics database, <Timestream table name> with the name of your Timestream for LiveAnalytics table, and <timestamp> with the timestamp that forms the unload-<%Y-%m-%d-%H:%M:%S> path in your S3 bucket:

```
aws s3 rm \
    s3://<S3 bucket name>/<Timestream database name>/<Timestream table name>/unload-<timestamp>/line-protocol-output \
    --recursive
```

To delete an S3 bucket, run the following command, replacing <S3 bucket name> with the name of your S3 bucket:

```
aws s3 delete-bucket --bucket <S3 bucket name>
```

*Cleaning up DynamoDB resources*

To delete a DynamoDB table, run the following command, replacing <table name> with the name of the DynamoDB table that you want to delete:

```
aws dynamodb delete-table --table-name <table name>
```