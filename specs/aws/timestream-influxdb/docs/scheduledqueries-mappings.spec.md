---
id: "@specs/aws/timestream-influxdb/docs/scheduledqueries-mappings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Data model mappings"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Data model mappings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/scheduledqueries-mappings
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Data model mappings for scheduled queries
<a name="scheduledqueries-mappings"></a>

Timestream for LiveAnalytics supports flexible modeling of data in its tables and this same flexibility applies to results of scheduled queries that are materialized into another Timestream for LiveAnalytics table. With scheduled queries, you can query any table, whether it has data in multi-measure records or single-measure records and write the query results using either multi-measure or single-measure records. 

You use the TargetConfiguration in the specification of a scheduled query to map the query results to the appropriate columns in the destination derived table. The following sections describe the different ways of specifying this TargetConfiguration to achieve different data models in the derived table. Specifically, you will see:
+ How to write to multi-measure records when the query result does not have a measure name and you specify the target measure name in the TargetConfiguration.
+ How you use measure name in the query result to write multi-measure records. 
+ How you can define a model to write multiple records with different multi-measure attributes.
+ How you can define a model to write to single-measure records in the derived table.
+ How you can query single-measure records and/or multi-measure records in a scheduled query and have the results materialized to either a single-measure record or a multi-measure record, which allows you to choose the flexibility of data models.

## Example: Target measure name for multi-measure records
<a name="scheduledqueries-mappings-targetmeasurename"></a>

In this example, you will see that the query is reading data from a table with multi-measure data and is writing the results into another table using multi-measure records. The scheduled query result does not have a natural measure name column. Here, you specify the measure name in the derived table using the TargetMultiMeasureName property in the TargetConfiguration.TimestreamConfiguration. 

```
{
    "Name" : "CustomMultiMeasureName",
    "QueryString" : "SELECT region, bin(time, 1h) as hour, AVG(memory_cached) as avg_mem_cached_1h, MIN(memory_free) as min_mem_free_1h, MAX(memory_used) as max_mem_used_1h, SUM(disk_io_writes) as sum_1h, AVG(disk_used) as avg_disk_used_1h, AVG(disk_free) as avg_disk_free_1h, MAX(cpu_user) as max_cpu_user_1h, MIN(cpu_idle) as min_cpu_idle_1h, MAX(cpu_system) as max_cpu_system_1h FROM raw_data.devops_multi WHERE time BETWEEN bin(@scheduled_runtime, 1h) - 14h AND bin(@scheduled_runtime, 1h) - 2h AND measure_name = 'metrics' GROUP BY region, bin(time, 1h)",
    "ScheduleConfiguration" : {
        "ScheduleExpression" : "cron(0 0/1 * * ? *)"
    },
    "NotificationConfiguration" : {
        "SnsConfiguration" : {
            "TopicArn" : "******"
        }
    },
    "ScheduledQueryExecutionRoleArn": "******",
    "TargetConfiguration": {
        "TimestreamConfiguration": {
            "DatabaseName" : "derived",
            "TableName" : "dashboard_metrics_1h_agg_1",
            "TimeColumn" : "hour",
            "DimensionMappings" : [
                {
                    "Name": "region",
                    "DimensionValueType" : "VARCHAR"
                }
            ],
            "MultiMeasureMappings" : {
                "TargetMultiMeasureName": "dashboard-metrics",
                "MultiMeasureAttributeMappings" : [
                    {
                        "SourceColumn" : "avg_mem_cached_1h",
                        "MeasureValueType" : "DOUBLE",
                        "TargetMultiMeasureAttributeName" : "avgMemCached"
                    },
                    {
                        "SourceColumn" : "min_mem_free_1h",
                        "MeasureValueType" : "DOUBLE"
                    },
                    {
                        "SourceColumn" : "max_mem_used_1h",
                        "MeasureValueType" : "DOUBLE"
                    },
                    {
                        "SourceColumn" : "sum_1h",
                        "MeasureValueType" : "DOUBLE",
                        "TargetMultiMeasureAttributeName" : "totalDiskWrites"
                    },
                    {
                        "SourceColumn" : "avg_disk_used_1h",
                        "MeasureValueType" : "DOUBLE"
                    },
                    {
                        "SourceColumn" : "avg_disk_free_1h",
                        "MeasureValueType" : "DOUBLE"
                    },
                    {
                        "SourceColumn" : "max_cpu_user_1h",
                        "MeasureValueType" : "DOUBLE",
                        "TargetMultiMeasureAttributeName" : "CpuUserP100"
                    },
                    {
                        "SourceColumn" : "min_cpu_idle_1h",
                        "MeasureValueType" : "DOUBLE"
                    },
                    {
                        "SourceColumn" : "max_cpu_system_1h",
                        "MeasureValueType" : "DOUBLE",
                        "TargetMultiMeasureAttributeName" : "CpuSystemP100"
                    }  
                ]
            }
        }
    },
    "ErrorReportConfiguration": {
        "S3Configuration" : {
            "BucketName" : "******",
            "ObjectKeyPrefix": "errors",
            "EncryptionOption": "SSE_S3"
        }
    }
}
```

The mapping in this example creates one multi-measure record with measure name dashboard-metrics and attribute names avgMemCached, min\_mem\_free\_1h, max\_mem\_used\_1h, totalDiskWrites, avg\_disk\_used\_1h, avg\_disk\_free\_1h, CpuUserP100, min\_cpu\_idle\_1h, CpuSystemP100. Notice the optional use of TargetMultiMeasureAttributeName to rename the query output columns to a different attribute name used for result materialization.

The following is the schema for the destination table once this scheduled query is materialized. As you can see from the Timestream for LiveAnalytics attribute type in the following result, the results are materialized into a multi-measure record with a single-measure name `dashboard-metrics`, as shown in the measure schema.


| Column | Type | Timestream for LiveAnalytics attribute type | 
| --- | --- | --- | 
| region | varchar | DIMENSION | 
| measure\_name | varchar | MEASURE\_NAME | 
| time | timestamp | TIMESTAMP | 
| CpuSystemP100 | double | MULTI | 
| avgMemCached | double | MULTI | 
| min\_cpu\_idle\_1h | double | MULTI | 
| avg\_disk\_free\_1h | double | MULTI | 
| avg\_disk\_used\_1h | double | MULTI | 
| totalDiskWrites | double | MULTI | 
| max\_mem\_used\_1h | double | MULTI | 
| min\_mem\_free\_1h | double | MULTI | 
| CpuUserP100 | double | MULTI | 

The following are the corresponding measures obtained with a SHOW MEASURES query.


| measure\_name | data\_type | Dimensions | 
| --- | --- | --- | 
| dashboard-metrics | multi | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 

## Example: Using measure name from scheduled query in multi-measure records
<a name="scheduledqueries-mappings-usingmeasurename"></a>

In this example, you will see a query reading from a table with single-measure records and materializing the results into multi-measure records. In this case, the scheduled query result has a column whose values can be used as measure names in the target table where the results of the scheduled query is materialized. Then you can specify the measure name for the multi-measure record in the derived table using the MeasureNameColumn property in TargetConfiguration.TimestreamConfiguration. 

```
{
    "Name" : "UsingMeasureNameFromQueryResult",
    "QueryString" : "SELECT region, bin(time, 1h) as hour, measure_name, AVG(CASE WHEN measure_name IN ('memory_cached', 'disk_used', 'disk_free') THEN measure_value::double ELSE NULL END) as avg_1h, MIN(CASE WHEN measure_name IN ('memory_free', 'cpu_idle') THEN measure_value::double ELSE NULL END) as min_1h, SUM(CASE WHEN measure_name IN ('disk_io_writes') THEN measure_value::double ELSE NULL END) as sum_1h, MAX(CASE WHEN measure_name IN ('memory_used', 'cpu_user', 'cpu_system') THEN measure_value::double ELSE NULL END) as max_1h FROM raw_data.devops WHERE time BETWEEN bin(@scheduled_runtime, 1h) - 14h AND bin(@scheduled_runtime, 1h) - 2h AND measure_name IN ('memory_free', 'memory_used', 'memory_cached', 'disk_io_writes', 'disk_used', 'disk_free', 'cpu_user', 'cpu_system', 'cpu_idle') GROUP BY region, measure_name, bin(time, 1h)",
    "ScheduleConfiguration" : {
        "ScheduleExpression" : "cron(0 0/1 * * ? *)"
    },
    "NotificationConfiguration" : {
        "SnsConfiguration" : {
            "TopicArn" : "******"
        }
    },
    "ScheduledQueryExecutionRoleArn": "******",
    "TargetConfiguration": {
        "TimestreamConfiguration": {
            "DatabaseName" : "derived",
            "TableName" : "dashboard_metrics_1h_agg_2",
            "TimeColumn" : "hour",
            "DimensionMappings" : [
                {
                    "Name": "region",
                    "DimensionValueType" : "VARCHAR"
                }
            ],
            "MeasureNameColumn" : "measure_name",
            "MultiMeasureMappings" : {
                "MultiMeasureAttributeMappings" : [
                    {
                        "SourceColumn" : "avg_1h",
                        "MeasureValueType" : "DOUBLE"
                    },
                    {
                        "SourceColumn" : "min_1h",
                        "MeasureValueType" : "DOUBLE",
                        "TargetMultiMeasureAttributeName": "p0_1h"
                    },
                    {
                        "SourceColumn" : "sum_1h",
                        "MeasureValueType" : "DOUBLE"
                    },
                    {
                        "SourceColumn" : "max_1h",
                        "MeasureValueType" : "DOUBLE",
                        "TargetMultiMeasureAttributeName": "p100_1h"
                    } 
                ]
            }
        }
    },
    "ErrorReportConfiguration": {
        "S3Configuration" : {
            "BucketName" : "******",
            "ObjectKeyPrefix": "errors",
            "EncryptionOption": "SSE_S3"
        }
    }
}
```

The mapping in this example will create multi-measure records with attributes avg\_1h, p0\_1h, sum\_1h, p100\_1h and will use the values of the measure\_name column in the query result as the measure name for the multi-measure records in the destination table. Additionally note that the previous examples optionally use the TargetMultiMeasureAttributeName with a subset of the mappings to rename the attributes. For instance, min\_1h was renamed to p0\_1h and max\_1h is renamed to p100\_1h.

The following is the schema for the destination table once this scheduled query is materialized. As you can see from the Timestream for LiveAnalytics attribute type in the following result, the results are materialized into a multi-measure record. If you look at the measure schema, there were nine different measure names that were ingested which correspond to the values seen in the query results.


| Column | Type | Timestream for LiveAnalytics attribute type | 
| --- | --- | --- | 
| region | varchar | DIMENSION | 
| measure\_name | varchar | MEASURE\_NAME | 
| time | timestamp | TIMESTAMP | 
| sum\_1h | double | MULTI | 
| p100\_1h | double | MULTI | 
| p0\_1h | double | MULTI | 
| avg\_1h | double | MULTI | 

The following are corresponding measures obtained with a SHOW MEASURES query.


| measure\_name | data\_type | Dimensions | 
| --- | --- | --- | 
| cpu\_idle | multi | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| cpu\_system | multi | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| cpu\_user | multi | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| disk\_free | multi | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| disk\_io\_writes | multi | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| disk\_used | multi | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| memory\_cached | multi | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| memory\_free | multi | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| memory\_free | multi | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 

## Example: Mapping results to different multi-measure records with different attributes
<a name="scheduledqueries-mappings-mappintresultstodiffrentmultimeasure"></a>

The following example shows how you can map different columns in your query result into different multi-measure records with different measure names. If you see the following scheduled query definition, the result of the query has the following columns: region, hour, avg\_mem\_cached\_1h, min\_mem\_free\_1h, max\_mem\_used\_1h, total\_disk\_io\_writes\_1h, avg\_disk\_used\_1h, avg\_disk\_free\_1h, max\_cpu\_user\_1h, max\_cpu\_system\_1h, min\_cpu\_system\_1h. `region` is mapped to dimension, and `hour` is mapped to the time column. 

The MixedMeasureMappings property in TargetConfiguration.TimestreamConfiguration specifies how to map the measures to multi-measure records in the derived table. 

In this specific example, avg\_mem\_cached\_1h, min\_mem\_free\_1h, max\_mem\_used\_1h are used in one multi-measure record with measure name of mem\_aggregates, total\_disk\_io\_writes\_1h, avg\_disk\_used\_1h, avg\_disk\_free\_1h are used in another multi-measure record with measure name of disk\_aggregates, and finally max\_cpu\_user\_1h, max\_cpu\_system\_1h, min\_cpu\_system\_1h are used in another multi-measure record with measure name cpu\_aggregates. 

In these mappings, you can also optionally use TargetMultiMeasureAttributeName to rename the query result column to have a different attribute name in the destination table. For instance, the result column avg\_mem\_cached\_1h gets renamed to avgMemCached, total\_disk\_io\_writes\_1h gets renamed to totalIOWrites, etc. 

When you're defining the mappings for multi-measure records, Timestream for LiveAnalytics inspects every row in the query results and automatically ignores the column values that have NULL values. As a result, in the case of mappings with multiple measures names, if all the column values for that group in the mapping are NULL for a given row, then no value for that measure name is ingested for that row. 

For example, in the following mapping, avg\_mem\_cached\_1h, min\_mem\_free\_1h, and max\_mem\_used\_1h are mapped to measure name mem\_aggregates. If for a given row of the query result, all these of the column values are NULL, Timestream for LiveAnalytics won't ingest the measure mem\_aggregates for that row. If all nine columns for a given row are NULL, then you will see an user error reported in your error report. 

```
{
    "Name" : "AggsInDifferentMultiMeasureRecords",
    "QueryString" : "SELECT region, bin(time, 1h) as hour, AVG(CASE WHEN measure_name = 'memory_cached' THEN measure_value::double ELSE NULL END) as avg_mem_cached_1h, MIN(CASE WHEN measure_name = 'memory_free' THEN measure_value::double ELSE NULL END) as min_mem_free_1h, MAX(CASE WHEN measure_name = 'memory_used' THEN measure_value::double ELSE NULL END) as max_mem_used_1h, SUM(CASE WHEN measure_name = 'disk_io_writes' THEN measure_value::double ELSE NULL END) as total_disk_io_writes_1h, AVG(CASE WHEN measure_name = 'disk_used' THEN measure_value::double ELSE NULL END) as avg_disk_used_1h, AVG(CASE WHEN measure_name = 'disk_free' THEN measure_value::double ELSE NULL END) as avg_disk_free_1h, MAX(CASE WHEN measure_name = 'cpu_user' THEN measure_value::double ELSE NULL END) as max_cpu_user_1h, MAX(CASE WHEN measure_name = 'cpu_system' THEN measure_value::double ELSE NULL END) as max_cpu_system_1h, MIN(CASE WHEN measure_name = 'cpu_idle' THEN measure_value::double ELSE NULL END) as min_cpu_system_1h FROM raw_data.devops WHERE time BETWEEN bin(@scheduled_runtime, 1h) - 14h AND bin(@scheduled_runtime, 1h) - 2h AND measure_name IN ('memory_cached', 'memory_free', 'memory_used', 'disk_io_writes', 'disk_used', 'disk_free', 'cpu_user', 'cpu_system', 'cpu_idle') GROUP BY region, bin(time, 1h)",
    "ScheduleConfiguration" : {
        "ScheduleExpression" : "cron(0 0/1 * * ? *)"
    },
    "NotificationConfiguration" : {
        "SnsConfiguration" : {
            "TopicArn" : "******"
        }
    },
    "ScheduledQueryExecutionRoleArn": "******",
    "TargetConfiguration": {
        "TimestreamConfiguration": {
            "DatabaseName" : "derived",
            "TableName" : "dashboard_metrics_1h_agg_3",
            "TimeColumn" : "hour",
            "DimensionMappings" : [
                {
                    "Name": "region",
                    "DimensionValueType" : "VARCHAR"
                }
            ],
            "MixedMeasureMappings" : [
                {
                    "MeasureValueType" : "MULTI",
                    "TargetMeasureName" : "mem_aggregates",
                    "MultiMeasureAttributeMappings" : [
                        {
                            "SourceColumn" : "avg_mem_cached_1h",
                            "MeasureValueType" : "DOUBLE",
                            "TargetMultiMeasureAttributeName": "avgMemCached"
                        },
                        {
                            "SourceColumn" : "min_mem_free_1h",
                            "MeasureValueType" : "DOUBLE"
                        },
                        {
                            "SourceColumn" : "max_mem_used_1h",
                            "MeasureValueType" : "DOUBLE",
                            "TargetMultiMeasureAttributeName": "maxMemUsed"
                        }
                    ]
                },
                {
                    "MeasureValueType" : "MULTI",
                    "TargetMeasureName" : "disk_aggregates",
                    "MultiMeasureAttributeMappings" : [
                        {
                            "SourceColumn" : "total_disk_io_writes_1h",
                            "MeasureValueType" : "DOUBLE",
                            "TargetMultiMeasureAttributeName": "totalIOWrites"
                        },
                        {
                            "SourceColumn" : "avg_disk_used_1h",
                            "MeasureValueType" : "DOUBLE"
                        },
                        {
                            "SourceColumn" : "avg_disk_free_1h",
                            "MeasureValueType" : "DOUBLE"
                        }
                    ]
                },
                {
                    "MeasureValueType" : "MULTI",
                    "TargetMeasureName" : "cpu_aggregates",
                    "MultiMeasureAttributeMappings" : [
                        {
                            "SourceColumn" : "max_cpu_user_1h",
                            "MeasureValueType" : "DOUBLE"
                        },
                        {
                            "SourceColumn" : "max_cpu_system_1h",
                            "MeasureValueType" : "DOUBLE"
                        },
                        {
                            "SourceColumn" : "min_cpu_idle_1h",
                            "MeasureValueType" : "DOUBLE",
                            "TargetMultiMeasureAttributeName": "minCpuIdle"
                        }
                    ]
                }
            ]
        }
    },
    "ErrorReportConfiguration": {
        "S3Configuration" : {
            "BucketName" : "******",
            "ObjectKeyPrefix": "errors",
            "EncryptionOption": "SSE_S3"
        }
    }
}
```

The following is the schema for the destination table once this scheduled query is materialized.


| Column | Type | Timestream for LiveAnalytics attribute type | 
| --- | --- | --- | 
| region | varchar | DIMENSION | 
| measure\_name | varchar | MEASURE\_NAME | 
| time | timestamp | TIMESTAMP | 
| minCpuIdle | double | MULTI | 
| max\_cpu\_system\_1h | double | MULTI | 
| max\_cpu\_user\_1h | double | MULTI | 
| avgMemCached | double | MULTI | 
| maxMemUsed | double | MULTI | 
| min\_mem\_free\_1h | double | MULTI | 
| avg\_disk\_free\_1h | double | MULTI | 
| avg\_disk\_used\_1h | double | MULTI | 
| totalIOWrites | double | MULTI | 

The following are the corresponding measures obtained with a SHOW MEASURES query.


| measure\_name | data\_type | Dimensions | 
| --- | --- | --- | 
| cpu\_aggregates | multi | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| disk\_aggregates | multi | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| mem\_aggregates | multi | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 

## Example: Mapping results to single-measure records with measure name from query results
<a name="scheduledqueries-mappings-mappintresultstosinglemeasurerecords"></a>

The following is an example of a scheduled query whose results are materialized into single-measure records. In this example, the query result has the measure\_name column whose values will be used as measure names in the target table. You use the MixedMeasureMappings attribute in the TargetConfiguration.TimestreamConfiguration to specify the mapping of the query result column to the scalar measure in the target table. 

In the following example definition, the query result is expected to nine distinct measure\_name values. You list out all these measure names in the mapping and specify which column to use for the single-measure value for that measure name. For example, in this mapping, if measure name of memory\_cached is seen for a given result row, then the value in the avg\_1h column is used as the value for the measure when the data is written to the target table. You can optionally use TargetMeasureName to provide a new measure name for this value. 

```
{
    "Name" : "UsingMeasureNameColumnForSingleMeasureMapping",
    "QueryString" : "SELECT region, bin(time, 1h) as hour, measure_name, AVG(CASE WHEN measure_name IN ('memory_cached', 'disk_used', 'disk_free') THEN measure_value::double ELSE NULL END) as avg_1h, MIN(CASE WHEN measure_name IN ('memory_free', 'cpu_idle') THEN measure_value::double ELSE NULL END) as min_1h, SUM(CASE WHEN measure_name IN ('disk_io_writes') THEN measure_value::double ELSE NULL END) as sum_1h, MAX(CASE WHEN measure_name IN ('memory_used', 'cpu_user', 'cpu_system') THEN measure_value::double ELSE NULL END) as max_1h FROM raw_data.devops WHERE time BETWEEN bin(@scheduled_runtime, 1h) - 14h AND bin(@scheduled_runtime, 1h) - 2h AND measure_name IN ('memory_free', 'memory_used', 'memory_cached', 'disk_io_writes', 'disk_used', 'disk_free', 'cpu_user', 'cpu_system', 'cpu_idle') GROUP BY region, bin(time, 1h), measure_name",
    "ScheduleConfiguration" : {
        "ScheduleExpression" : "cron(0 0/1 * * ? *)"
    },
    "NotificationConfiguration" : {
        "SnsConfiguration" : {
            "TopicArn" : "******"
        }
    },
    "ScheduledQueryExecutionRoleArn": "******",
    "TargetConfiguration": {
        "TimestreamConfiguration": {
            "DatabaseName" : "derived",
            "TableName" : "dashboard_metrics_1h_agg_4",
            "TimeColumn" : "hour",
            "DimensionMappings" : [
                {
                    "Name": "region",
                    "DimensionValueType" : "VARCHAR"
                }
            ],
            "MeasureNameColumn" : "measure_name",
            "MixedMeasureMappings" : [
                {
                    "MeasureName" : "memory_cached",
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "avg_1h",
                    "TargetMeasureName" : "AvgMemCached"
                },
                {
                    "MeasureName" : "disk_used",
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "avg_1h"
                },
                {
                    "MeasureName" : "disk_free",
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "avg_1h"
                },
                {
                    "MeasureName" : "memory_free",
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "min_1h",
                    "TargetMeasureName" : "MinMemFree"
                },
                {
                    "MeasureName" : "cpu_idle",
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "min_1h"
                },
                {
                    "MeasureName" : "disk_io_writes",
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "sum_1h",
                    "TargetMeasureName" : "total-disk-io-writes"
                },
                {
                    "MeasureName" : "memory_used",
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "max_1h",
                    "TargetMeasureName" : "maxMemUsed"
                },
                {
                    "MeasureName" : "cpu_user",
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "max_1h"
                },
                {
                    "MeasureName" : "cpu_system",
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "max_1h"
                }
            ]
        }
    },
    "ErrorReportConfiguration": {
        "S3Configuration" : {
            "BucketName" : "******",
            "ObjectKeyPrefix": "errors",
            "EncryptionOption": "SSE_S3"
        }
    }
}
```

The following is the schema for the destination table once this scheduled query is materialized. As you can see from the schema, the table is using single-measure records. If you list the measure schema for the table, you will see the nine measures written to based on the mapping provided in the specification.


| Column | Type | Timestream for LiveAnalytics attribute type | 
| --- | --- | --- | 
| region | varchar | DIMENSION | 
| measure\_name | varchar | MEASURE\_NAME | 
| time | timestamp | TIMESTAMP | 
| measure\_value::double | double | MEASURE\_VALUE | 

The following are the corresponding measures obtained with a SHOW MEASURES query.


| measure\_name | data\_type | Dimensions | 
| --- | --- | --- | 
| AvgMemCached | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| MinMemFree | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| cpu\_idle | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| cpu\_system | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| cpu\_user | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| disk\_free | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| disk\_used | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| maxMemUsed | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| total-disk-io-writes | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 

## Example: Mapping results to single-measure records with query result columns as measure names
<a name="scheduledqueries-mappings-mappintresultstsolumnsasmeasurename"></a>

In this example, you have a query whose results do not have a measure name column. Instead, you want the query result column name as the measure name when mapping the output to single-measure records. Earlier there was an example where a similar result was written to a multi-measure record. In this example, you will see how to map it to single-measure records if that fits your application scenario. 

Again, you specify this mapping using the MixedMeasureMappings property in TargetConfiguration.TimestreamConfiguration. In the following example, you see that the query result has nine columns. You use the result columns as measure names and the values as the single-measure values. 

For example, for a given row in the query result, the column name avg\_mem\_cached\_1h is used as the column name and value associated with column, and avg\_mem\_cached\_1h is used as the measure value for the single-measure record. You can also use TargetMeasureName to use a different measure name in the target table. For instance, for values in column sum\_1h, the mapping specifies to use total\_disk\_io\_writes\_1h as the measure name in the target table. If any column's value is NULL, then the corresponding measure is ignored. 

```
{
    "Name" : "SingleMeasureMappingWithoutMeasureNameColumnInQueryResult",
    "QueryString" : "SELECT region, bin(time, 1h) as hour, AVG(CASE WHEN measure_name = 'memory_cached' THEN measure_value::double ELSE NULL END) as avg_mem_cached_1h, AVG(CASE WHEN measure_name = 'disk_used' THEN measure_value::double ELSE NULL END) as avg_disk_used_1h, AVG(CASE WHEN measure_name = 'disk_free' THEN measure_value::double ELSE NULL END) as avg_disk_free_1h, MIN(CASE WHEN measure_name = 'memory_free' THEN measure_value::double ELSE NULL END) as min_mem_free_1h, MIN(CASE WHEN measure_name = 'cpu_idle' THEN measure_value::double ELSE NULL END) as min_cpu_idle_1h, SUM(CASE WHEN measure_name = 'disk_io_writes' THEN measure_value::double ELSE NULL END) as sum_1h, MAX(CASE WHEN measure_name = 'memory_used' THEN measure_value::double ELSE NULL END) as max_mem_used_1h, MAX(CASE WHEN measure_name = 'cpu_user' THEN measure_value::double ELSE NULL END) as max_cpu_user_1h, MAX(CASE WHEN measure_name = 'cpu_system' THEN measure_value::double ELSE NULL END) as max_cpu_system_1h FROM raw_data.devops WHERE time BETWEEN bin(@scheduled_runtime, 1h) - 14h AND bin(@scheduled_runtime, 1h) - 2h AND measure_name IN ('memory_free', 'memory_used', 'memory_cached', 'disk_io_writes', 'disk_used', 'disk_free', 'cpu_user', 'cpu_system', 'cpu_idle') GROUP BY region, bin(time, 1h)",
    "ScheduleConfiguration" : {
        "ScheduleExpression" : "cron(0 0/1 * * ? *)"
    },
    "NotificationConfiguration" : {
        "SnsConfiguration" : {
            "TopicArn" : "******"
        }
    },
    "ScheduledQueryExecutionRoleArn": "******",
    "TargetConfiguration": {
        "TimestreamConfiguration": {
            "DatabaseName" : "derived",
            "TableName" : "dashboard_metrics_1h_agg_5",
            "TimeColumn" : "hour",
            "DimensionMappings" : [
                {
                    "Name": "region",
                    "DimensionValueType" : "VARCHAR"
                }
            ],
            "MixedMeasureMappings" : [
                {
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "avg_mem_cached_1h"
                },
                {
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "avg_disk_used_1h"
                },
                {
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "avg_disk_free_1h"
                },
                {
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "min_mem_free_1h"
                },
                {
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "min_cpu_idle_1h"
                },
                {
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "sum_1h",
                    "TargetMeasureName" : "total_disk_io_writes_1h"
                },
                {
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "max_mem_used_1h"
                },
                {
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "max_cpu_user_1h"
                },
                {
                    "MeasureValueType" : "DOUBLE",
                    "SourceColumn" : "max_cpu_system_1h"
                }
            ]
        }
    },
    "ErrorReportConfiguration": {
        "S3Configuration" : {
            "BucketName" : "******",
            "ObjectKeyPrefix": "errors",
            "EncryptionOption": "SSE_S3"
        }
    }
}
```

The following is the schema for the destination table once this scheduled query is materialized. As you can see that the target table is storing records with single-measure values of type double. Similarly, the measure schema for the table shows the nine measure names. Also notice that the measure name total\_disk\_io\_writes\_1h is present since the mapping renamed sum\_1h to total\_disk\_io\_writes\_1h.


| Column | Type | Timestream for LiveAnalytics attribute type | 
| --- | --- | --- | 
| region | varchar | DIMENSION | 
| measure\_name | varchar | MEASURE\_NAME | 
| time | timestamp | TIMESTAMP | 
| measure\_value::double | double | MEASURE\_VALUE | 

The following are the corresponding measures obtained with a SHOW MEASURES query.


| measure\_name | data\_type | Dimensions | 
| --- | --- | --- | 
| avg\_disk\_free\_1h | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| avg\_disk\_used\_1h | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| avg\_mem\_cached\_1h | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| max\_cpu\_system\_1h | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| max\_cpu\_user\_1h | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| max\_mem\_used\_1h | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| min\_cpu\_idle\_1h | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| min\_mem\_free\_1h | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 
| total-disk-io-writes | double | [{'dimension\_name': 'region', 'data\_type': 'varchar'}] | 