---
id: "@specs/aws/timestream-influxdb/docs/customer-defined-partition-keys-schema-validation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Timestream for LiveAnalytics schema validation with custom composite partition keys"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Timestream for LiveAnalytics schema validation with custom composite partition keys

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/customer-defined-partition-keys-schema-validation
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Timestream for LiveAnalytics schema validation with custom composite partition keys
<a name="customer-defined-partition-keys-schema-validation"></a>

Schema validation in Timestream for LiveAnalytics helps ensure that data ingested into the database complies with the specified schema, minimizing ingestion errors and improving data quality. In particular, schema validation is especially useful when adopting customer-defined partition key with the goal of optimizing your query performance.

## What is Timestream for LiveAnalytics schema validation with customer-defined partition keys?
<a name="customer-defined-partition-keys-schema-validation-what-is"></a>

Timestream for LiveAnalytics schema validation is a feature that validates data being ingested into a Timestream for LiveAnalytics table based on a predefined schema. This schema defines the data model, including partition key, data types, and constraints for the records being inserted.

When using a customer-defined partition key, schema validation becomes even more crucial. Partition keys allow you to specify a partition key, which determines how your data is stored in Timestream for LiveAnalytics. By validating the incoming data against the schema with a custom partition key, you can enforce data consistency, detect errors early, and improve the overall quality of the data stored in Timestream for LiveAnalytics.

## How to Use Timestream for LiveAnalytics schema validation with custom composite partition keys
<a name="customer-defined-partition-keys-schema-validation-using"></a>

To use Timestream for LiveAnalytics schema validation with custom composite partition keys, follow these steps:

**Think about what your query patterns will look like: **To properly choose and define the schema for your Timestream for LiveAnalytics table you should start with your query requirements.

**Specify custom composite partition keys: **When creating the table, specify a custom partition key. This key determines the attribute that will be used to partition the table data. You can choose between dimension keys and measure keys for partitioning. A dimension key partitions data based on a dimension name, while a measure key partitions data based on the measure name.

**Set enforcement levels: **To ensure proper data partitioning and the benefits that come with it, Amazon Timestream for LiveAnalytics allows you to set enforcement levels for each partition key in your schema. The enforcement level determines whether the partition key dimension is required or optional when ingesting records. You can choose between two options: `REQUIRED`, which means the partition key must be present in the ingested record, and `OPTIONAL`, which means the partition key doesn't have to be present. It is recommended that you use the `REQUIRED` enforcement level when using a customer-defined partition to ensure that your data is properly partitioned and you get the full benefits of this feature. Additionally, you can change the enforcement level configuration at any time after the schema creation to adjust to your data ingestion requirements.

**Ingest data: **When ingesting data into the Timestream for LiveAnalytics table, the schema validation process will check the records against the defined schema with custom composite partition keys. If the records do not adhere to the schema, Timestream for LiveAnalytics will return a validation error.

**Handle validation errors:** In case of validation errors, Timestream for LiveAnalytics will return a `ValidationException` or a `RejectedRecordsException`, depending on the type of error. Make sure to handle these exceptions in your application and take appropriate action, such as fixing the incorrect records and retrying the ingestion.

**Update enforcement levels: **If necessary, you can update the enforcement level of partition keys after table creation using the `UpdateTable` action. However, it's important to note that some aspects of the partition key configuration, such as the name, and type, cannot be changed after table creation. If you change the enforcement level from `REQUIRED` to `OPTIONAL`, all records will be accepted regardless of the presence of the attribute selected as the customer-defined partition key. Conversely, if you change the enforcement level from `OPTIONAL` to `REQUIRED`, you may start seeing 4xx write errors for records that don't meet this condition. Therefore, it's essential to choose the appropriate enforcement level for your use case when creating your table, based on your data's partitioning requirements.

## When to use Timestream for LiveAnalytics schema validation with custom composite partition keys
<a name="customer-defined-partition-keys-schema-validation-when-to-use"></a>

Timestream for LiveAnalytics schema validation with custom composite partition keys should be used in scenarios where data consistency, quality, and optimized partitioning are crucial. By enforcing a schema during data ingestion, you can prevent errors and inconsistencies that might lead to incorrect analysis or loss of valuable insights.

## Interaction with batch load jobs
<a name="customer-defined-partition-keys-schema-validation-when-to-use-batch-load"></a>

When setting up a batch load job to import data into a table with a customer-defined partition key, there are a few scenarios that could affect the process:

1. If the enforcement level is set to `OPTIONAL`, an alert will be displayed on the console during the creation flow if the partition key is not mapped during job configuration. This alert will not appear when using the API or CLI.

1. If the enforcement level is set to `REQUIRED`, the job creation will be rejected unless the partition key is mapped to a source data column.

1. If the enforcement level is changed to `REQUIRED` after the job is created, the job will continue to execute, but any records that do not have the proper mapping for the partition key will be rejected with a 4xx error.

## Interaction with scheduled query
<a name="customer-defined-partition-keys-schema-validation-when-to-use-scheduled-query"></a>

When setting up a scheduled query job for calculating and storing aggregates, rollups, and other forms of preprocessed data into a table with a customer-defined partition key, there are a few scenarios that could affect the process:

1. If the enforcement level is set to `OPTIONAL`, an alert will be displayed if the partition key is not mapped during job configuration. This alert will not appear when using the API or CLI.

1. If the enforcement level is set to `REQUIRED`, the job creation will be rejected unless the partition key is mapped to a source data column.

1. If the enforcement level is changed to `REQUIRED` after the job is created and the scheduled query results does not contain the partition key dimension, all the next iterations of the job will fail.