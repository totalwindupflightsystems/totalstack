---
id: "@specs/aws/timestream-influxdb/docs/ts-limits"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Quotas"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Quotas

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/ts-limits
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Quotas
<a name="ts-limits"></a>

This topic describes current quotas, also referred to as limits, within Amazon Timestream for LiveAnalytics. Each quota applies on a per-Region basis unless otherwise specified.

**Topics**
+ [Default quotas](#ts-limits.default)
+ [Service limits](#system-limits)
+ [Supported data types](#limits.datatypes)
+ [Batch load](#limits.batch-load)
+ [Naming constraints](#limits.naming)
+ [Reserved keywords](#limits.reserved)
+ [System identifiers](#limits.system_identifier)
+ [UNLOAD](#limits.export-unload)

## Default quotas
<a name="ts-limits.default"></a>

The following table contains the Timestream for LiveAnalytics quotas and the default values.


| displayName | Description | defaultValue | 
| --- | --- | --- | 
| Databases per account | The maximum number of databases you can create per AWS account. | 500 | 
| Tables per account | The maximum number of tables you can create per AWS account. | 50000 | 
| Request rate for CRUD APIs | The maximum number of Create/Update/Delete requests allowed per second per account, in the current Region. | 1 | 
| Request rate for other APIs | The maximum number of List/Describe/Prepare/ExecuteScheduledQueryAPI requests allowed per second per account, in the current Region. | 5 | 
| Scheduled queries per account | The maximum number of scheduled queries you can create per AWS account. | 10000 | 
| Maximum count of active magnetic store partitions | The maximum number of active magnetic store partitions per database. A partition might remain active for up to six hours after receiving ingestion. | 250 | 

## Service limits
<a name="system-limits"></a>

The following table contains the Timestream for LiveAnalytics service limits and the default values. To edit data retention for a table from the console, see [Edit a table](https://docs.aws.amazon.com/timestream/latest/developerguide/console_timestream.html#console_timestream.edit-table.using-console).


| displayName | Description | defaultValue | 
| --- | --- | --- | 
| Future ingestion period in minutes | The maximum lead time (in minutes) for your time series data compared to the current system time. For example, if the future ingestion period is 15 minutes, then Timestream for LiveAnalytics will accept data that is up to 15 minutes ahead of the current system time. | 15 | 
| Minimum retention period for memory store in hours | The minimum duration (in hours) for which data must be retained in the memory store per table. | 1 | 
| Maximum retention period for memory store in hours | The maximum duration (in hours) for which data can be retained in the memory store per table. | 8766 | 
| Minimum retention period for magnetic store in days | The minimum duration (in days) for which data must be retained in the magnetic store per table. | 1 | 
| Maximum retention period for magnetic store in days | The maximum duration (in days) for which data can be retained in the magnetic store. This value is equivalent to 200 years. | 73000 | 
| Default retention period for magnetic store in days | The default value (in days) for which data is retained in the magnetic store per table. This value is equivalent to 200 years. | 73000 | 
| Default retention period for memory store in hours | The default duration (in hours) for which data is retained in the memory store. | 6 | 
| Dimensions per table | The maximum number of dimensions per table. | 128 | 
| Measure names per table | The maximum number of unique measure names per table. | 8192 | 
| Dimension name dimension value pair size per series | The maximum size of dimension name and dimension value pair per series. | 2 Kilobytes | 
| Maximum record size | The maximum size of a record. | 2 Kilobytes | 
| Records per WriteRecords API request | The maximum number of records in a WriteRecords API request. | 100 | 
| Dimension name length | The maximum number of bytes for a Dimension name. | 60 bytes | 
| Measure name length | The maximum number of bytes for a Measure name. | 256 bytes | 
| Database name length | The maximum number of bytes for a Database name. | 256 bytes | 
| Table name length | The maximum number of bytes for a Table name. | 256 bytes | 
| QueryString length in KiB | The maximum length (in KiB) of a query string in UTF-8 encoded characters for a query. | 256 | 
| Execution duration for queries in hours | The maximum execution duration (in hours) for a query. Queries that take longer will timeout. | 1 | 
| Query Insights | The maximum number of Query API requests allowed with query insights enabled per second per account, in the current Region. | 1 | 
| Metadata size for query result | The maximum metadata size for a query result. | 100 Kilobytes | 
| Data size for query result | The maximum data size for a query result. | 5 Gigabytes | 
| Measures per multi-measure record | The maximum number of measures per multi-measure record. | 256 | 
| Measure value size per multi-measure record | The maximum size of measure values per multi-measure record. | 2048 | 
| Unique measures across multi-measure records per table | The unique measures in all the multi-measure records defined in a single table. | 1024 | 
| Timestream Compute Units (TCUs) per account | The default maximum TCUs per account. | 200 | 
| Maximum Provisioned Timestream Compute Units (TCUs) per account. Provisioned TCU is available only in the Asia Pacific (Mumbai) region.  | The maximum number of TCUs you can provision in your account. | 1000 | 
| maxQueryTCU | The maximum query TCUs you can set for your account. | 1000 | 

## Supported data types
<a name="limits.datatypes"></a>

The following table describes the supported data types for measure and dimension values.


| Description | Timestream for LiveAnalytics value | 
| --- | --- | 
| Supported data types for measure values. |  Big int, double, string, boolean, MULTI, Timestamp  | 
| Supported data types for dimension values. |  String  | 

## Batch load
<a name="limits.batch-load"></a>

The current quotas, also referred to as limits, within batch load are as follows.


| Description | Timestream for LiveAnalytics value | 
| --- | --- | 
| Max batch load task size | Max batch load task size cannot exceed 100 GB. | 
| Files quantity | A batch load task cannot have more than 100 files. | 
| Maximum file size | Maximum file size in a batch load task cannot exceed 5 GB. | 
| CSV file row size | A row in a CSV file cannot exceed 16 MB. This is a hard limit which cannot be increased. | 
| Active batch load tasks | A table cannot have more than 5 active batch load tasks and an account cannot have more than 10 active batch load tasks. Timestream for LiveAnalytics will throttle new batch load tasks until more resources are available. | 

## Naming constraints
<a name="limits.naming"></a>

The following table describes naming constraints.


| Description | Timestream for LiveAnalytics value | 
| --- | --- | 
| The maximum length of a dimension name. |  60 bytes  | 
| The maximum length of a measure name. |  256 bytes  | 
| The maximum length of a table name or database name. |  256 bytes  | 
| Table and Database Name |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html)  Table and database names are compared using UTF-8 binary representation. This means that comparison for ASCII characters is case sensitive.   | 
| Measure Name |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html)  Table and database names are compared using UTF-8 binary representation. This means that comparison for ASCII characters is case sensitive.   | 
| Dimension Name |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html)  Dimension and measure names are compared using UTF-8 binary representation. This means that comparison for ASCII characters is case sensitive.   | 
| All Column Names | Column names can not be duplicated. Since multi-measure records represent dimensions and measures as columns, the name for a dimension can not be the same as the name for a measure. Names are case sensitive. | 

## Reserved keywords
<a name="limits.reserved"></a>

 All of the following are reserved keywords: 
+ ALTER 
+ AND 
+ AS 
+ BETWEEN 
+ BY 
+ CASE 
+ CAST 
+ CONSTRAINT 
+ CREATE 
+ CROSS 
+ CUBE 
+ CURRENT\_DATE
+ CURRENT\_TIME 
+ CURRENT\_TIMESTAMP 
+ CURRENT\_USER 
+ DEALLOCATE 
+ DELETE 
+ DESCRIBE 
+ DISTINCT 
+ DROP
+ ELSE 
+ END 
+ ESCAPE 
+ EXCEPT 
+ EXECUTE 
+ EXISTS 
+ EXTRACT 
+ FALSE 
+ FOR 
+ FROM 
+ FULL 
+ GROUP
+ GROUPING 
+ HAVING 
+ IN 
+ INNER 
+ INSERT 
+ INTERSECT 
+ INTO 
+ IS 
+ JOIN 
+ LEFT 
+ LIKE
+ LOCALTIME 
+ LOCALTIMESTAMP 
+ NATURAL 
+ NORMALIZE 
+ NOT 
+ NULL 
+ ON 
+ OR 
+ ORDER 
+ OUTER 
+ PREPARE
+ RECURSIVE 
+ RIGHT 
+ ROLLUP 
+ SELECT 
+ TABLE 
+ THEN 
+ TRUE 
+ UESCAPE 
+ UNION 
+ UNNEST 
+ USING 
+ VALUES
+ WHEN 
+ WHERE 
+ WITH

## System identifiers
<a name="limits.system_identifier"></a>

 We reserve column names "measure\_value", "ts\_non\_existent\_col" and "time" to be Timestream for LiveAnalytics system identifiers. Additionally, column names may not start with "ts\_" or "measure\_name". System identifiers are case sensitive. Identifiers compared using UTF-8 binary representation. This means that comparison for identifiers is case sensitive. 

**Note**  
System identifiers may not be used for dimension or measure names. We recommend you do not use system identifiers for database or table names.

## UNLOAD
<a name="limits.export-unload"></a>

For limits related to the `UNLOAD` command, see [Using UNLOAD to export query results to S3 from Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/export-unload.html).