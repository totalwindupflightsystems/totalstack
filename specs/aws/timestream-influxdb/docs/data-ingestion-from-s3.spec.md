---
id: "@specs/aws/timestream-influxdb/docs/data-ingestion-from-s3"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Ingesting data from Amazon S3 to Timestream for InfluxDB automation"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Ingesting data from Amazon S3 to Timestream for InfluxDB automation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/data-ingestion-from-s3
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Ingesting data from Amazon S3 to Timestream for InfluxDB automation
<a name="data-ingestion-from-s3"></a>

After the Timestream for LiveAnalytics export tool completes the unload process, the next step in the automation process begins. This automation uses [InfluxDB's import tools](https://docs.influxdata.com/influxdb/v2/write-data/) to transfer the data into its specialized time-series structure. The process transforms Timestream's data model to match InfluxDB' s concepts of measurements, tags, and fields. Finally, it loads the data efficiently using [InfluxDB's line protocol](https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/).

The workflow for completing a migration is separated into four stages:

1. Unload data using Timestream for LiveAnalytics export tool.

1. [Data transformation](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/targets/timestream_for_influxdb/transform/README.md): Converting Timestream for LiveAnalytics data into InfluxDB line protocol format (Based on the schema defined after the cardinality assessment) using [Amazon Athena](https://docs.aws.amazon.com//athena/latest/ug/when-should-i-use-ate.html).

1. [Data ingestion](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/targets/timestream_for_influxdb/ingestion/README.md): Ingest the line protocol dataset to your Timestream for InfluxDB instance.

1. [Validation](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/targets/timestream_for_influxdb/validation/README.md): Optionally, you can validate that every line protocol point has been ingested (Requires `--add-validation-field true` during data transformation step).

**Data Transformation **

For data transformation, we developed a script to convert Timestream for LiveAnalytics exported data parquet format into InfluxDB's Line Protocol format using Amazon Athena. Amazon Athena provides a serverless query service and a cost-effective way to transform large volumes of time-series data without requiring dedicated compute resources.

The script does the following:
+ Loads exported Timestream for LiveAnalytics data from an Amazon S3 bucket into an Amazon Athena table.
+ Performs data mapping and transformation from the data stored in the Athena table into line protocol and stores it in the S3 bucket.

**Data Mapping**

The following table shows how Timestream for LiveAnalytics data is mapped to line protocol data.


| Timestream for LiveAnalytics Concept | Line Protocol Concept | 
| --- | --- | 
| [Table Name](https://docs.aws.amazon.com//timestream/latest/developerguide/API_Table.html) | [Measurement](https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/#measurement) | 
| [Dimensions](https://docs.aws.amazon.com//timestream/latest/developerguide/API_Dimension.html) | [Tags](https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/#tag-set) | 
| [Measure name](https://docs.aws.amazon.com//timestream/latest/developerguide/data-modeling.html#data-modeling-measurenamemulti) | Tag (Optional) | 
| [Measures](https://docs.aws.amazon.com//timestream/latest/developerguide/API_MeasureValue.html) | [Fields](https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/#field-set) | 
| [Time](https://docs.aws.amazon.com///timestream/latest/developerguide/writes.html#writes.data-types) | [Timestamp](https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/#timestamp) | 

**Prerequisites and Installation**

See the Prerequisites and Installation sections in the [transformation script’s README](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/targets/timestream_for_influxdb/transform/README.md#prerequisites).

**Usage**

To transform data stored in the bucket example\_s3\_bucket from the Timestream for LiveAnalytics table example\_table in example\_database, run the following command:

```
python3 transform.py \
        --database-name example_database \
        --tables example_table \
        --s3-bucket-path example_s3_bucket \
        --add-validation-field false
```

After the script is completed, 
+ In Athena, the table example\_database\_example\_table will be created, containing Timestream for LiveAnalytics data.
+ In Athena, the table lp\_example\_database\_example\_table will be created, containing Timestream for LiveAnalytics data transformed to line protocol points.
+ In the S3 bucket example\_s3\_bucket, within the path ` example_database/example_table/unload-<%Y-%m-%d-%H:%M:%S>/line-protocol-output`, line protocol data will be stored.

**Recommendations**

Refer to the [transformation script’s README](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/targets/timestream_for_influxdb/transform/README.md#prerequisites) for more details on the latest usage of the script and outputs are required for later steps of the migration, such as validation. If you excluded dimensions in order to improve cardinality, adjust the schema to reduce cardinality by using the `--dimensions-to-fields` argument to change particular dimensions to fields. 

*Adding a Field for Validation*

For information on how to add a field for validation, see the [Adding a Field for Validation](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/targets/timestream_for_influxdb/transform/README.md#adding-a-field-for-validation) section in the transformation script’s README. 

## Data ingestion into Timestream for InfluxDB
<a name="data-ingestion-influxdb"></a>

The InfluxDB ingestion script ingests compressed line protocol datasets to Timestream for InfluxDB. A directory containing gzip compressed line protocol files is passed in as a command line argument along with the ingestion destination InfluxDB bucket. This script was designed to ingest multiple files at a time using multi-processing to utilize the resources with InfluxDB and the machine executing the script.

The script does following:
+ Extracts zipped files and ingests them into InfluxDB.
+ Implements retry mechanisms and error handling.
+ Tracks successful and failed ingestions for resuming.
+ Optimizes I/O operations when reading from line protocol dataset.

**Prerequisites and installation**

See the Prerequisites and Installation section in the ingestion script's [README](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/README.md#installation) in GitHub.

**Data preparation**

The zipped line protocol files required for ingestion are generated by the data transform scripts. Follow these steps to prepare your data:

1. Set up an EC2 instance with sufficient storage to hold the transformed dataset.

1. Sync the transformed data from the S3 bucket to your local directory:

   ```
   aws s3 sync \
       s3://your-bucket-name/path/to/transformed/data \
       ./data_directory
   ```

1. Make sure you have read access to all files in the data directory.

1. Run the following ingestion script to ingest data into Timestream for InfluxDB.

**Usage**

```
python influxdb_ingestion.py <bucket_name> <data_directory> [options]
```

**Basic usage**

```
python influxdb_ingestion.py my_bucket ./data_files
```

**Ingestion rates**

We have run some tests for Ingestion rates. Ingestion tests using a C5N.9XL EC2 instance executing the ingestion script with 10 Workers, and ingesting \~500 GB line protocol to 8XL Timestream for InfluxDB instances:
+ 3K IOPS 15.86 GB/hour.
+ 12K IOPS 70.34 GB/hour.
+ 16K IOPS 71.28 GB/hour.

**Recommendations**
+ Use an EC2 instance with sufficient CPU cores to handle parallel processing.
+ Ensure the instance has enough storage to hold the entire transformed dataset with additional room for extraction.
  + The number of files extracted at one time is equal to the number of workers configured during script execution.
+ Position the EC2 instance in the same region and AZ (if possible) as your InfluxDB instance to minimize latency.
+ Consider using instance types optimized for network operations, for example C5N.
+ If high ingestion rates are required, at least 12K IOPS is recommended for the Timestream for InfluxDB instance. Additional optimizations can be gained by increasing the worker count for the script dependent on Timestream for InfluxDB instance size.

For more information, see the ingestion script's [README](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/README.md#installation).