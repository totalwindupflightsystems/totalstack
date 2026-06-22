---
id: "@specs/aws/timestream-influxdb/docs/batch-load-data-model-mappings"
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
> **spec:id:** @specs/aws/timestream-influxdb/docs/batch-load-data-model-mappings
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Data model mappings for batch load
<a name="batch-load-data-model-mappings"></a>

The following discusses the schema for data model mappings and gives and example.

## Data model mappings schema
<a name="batch-load-data-model-mappings-schema"></a>

The `CreateBatchLoadTask` request syntax and a `BatchLoadTaskDescription` object returned by a call to `DescribeBatchLoadTask` include a `DataModelConfiguration` object that includes the `DataModel` for batch loading. The `DataModel` defines mappings from source data that's stored in CSV format in an S3 location to a target Timestream for LiveAnalytics database and table. 

The `TimeColumn` field indicates the source data's location for the value to be mapped to the destination table's `time` column in Timestream for LiveAnalytics. The `TimeUnit` specifies the unit for the `TimeColumn`, and can be one of `MILLISECONDS`, `SECONDS`, `MICROSECONDS`, or `NANOSECONDS`. There are also mappings for dimensions and measures. Dimension mappings are composed of source columns and target fields. 

For more information, see [DimensionMapping](https://docs.aws.amazon.com/timestream/latest/developerguide/API_DimensionMapping). The mappings for measures have two options, `MixedMeasureMappings` and `MultiMeasureMappings`.

To summarize, a `DataModel` contains mappings from a data source in an S3 location to a target Timestream for LiveAnalytics table for the following.
+ Time
+ Dimensions
+ Measures

If possible, we recommend that you map measure data to multi-measure records in Timestream for LiveAnalytics. For information about the benefits of multi-measure records, see [Multi-measure records](writes.md#writes.writing-data-multi-measure). 

If multiple measures in the source data are stored in one row, you can map those multiple measures to multi-measure records in Timestream for LiveAnalytics using `MultiMeasureMappings`. If there are values that must map to a single-measure record, you can use `MixedMeasureMappings`. 

`MixedMeasureMappings` and `MultiMeasureMappings` both include `MultiMeasureAttributeMappings`. Multi-measure records are supported regardless of whether single-measure records are needed.

If only multi-measure target records are needed in Timestream for LiveAnalytics, you can define measure mappings in the following structure.

```
CreateBatchLoadTask
    MeasureNameColumn
    MultiMeasureMappings
        TargetMultiMeasureName
        MultiMeasureAttributeMappings array
```

**Note**  
We recommend using `MultiMeasureMappings` whenever possible.

If single-measure target records are needed in Timestream for LiveAnalytics, you can define measure mappings in the following structure.

```
CreateBatchLoadTask
    MeasureNameColumn
    MixedMeasureMappings array
        MixedMeasureMapping
            MeasureName
            MeasureValueType
            SourceColumn
            TargetMeasureName
            MultiMeasureAttributeMappings array
```

When you use `MultiMeasureMappings`, the `MultiMeasureAttributeMappings` array is always required. When you use the `MixedMeasureMappings` array, if the `MeasureValueType` is `MULTI` for a given `MixedMeasureMapping`, `MultiMeasureAttributeMappings` is required for that `MixedMeasureMapping`. Otherwise, `MeasureValueType` indicates the measure type for the single-measure record.

Either way, there is an array of `MultiMeasureAttributeMapping` available. You define the mappings to multi-measure records in each `MultiMeasureAttributeMapping` as follows:

`SourceColumn`  
The column in the source data that is located in Amazon S3.

`TargetMultiMeasureAttributeName`  
The name of the target multi-measure name in the destination table. This input is required when `MeasureNameColumn` is not provided. If `MeasureNameColumn` is provided, the value from that column is used as the multi-measure name.

`MeasureValueType`  
One of `DOUBLE`, `BIGINT` `BOOLEAN`, `VARCHAR`, or `TIMESTAMP`.

## Data model mappings with `MultiMeasureMappings` example
<a name="batch-load-data-model-mappings-example-multi"></a>

This example demonstrates mapping to multi-measure records, the preferred approach, which store each measure value in a dedicated column. You can download a sample CSV at [sample CSV](samples/batch-load-sample-file.csv.zip). The sample has the following headings to map to a target column in a Timestream for LiveAnalytics table.
+ `time`
+ `measure_name`
+ `region`
+ `location`
+ `hostname`
+ `memory_utilization`
+ `cpu_utilization`

Identify the `time` and `measure_name` columns in the CSV file. In this case these map directly to the Timestream for LiveAnalytics table columns of the same names.
+ `time` maps to `time`
+ `measure_name` maps to `measure_name` (or your chosen value)

When using the API, you specify `time` in the `TimeColumn` field and a supported time unit value such as `MILLISECONDS` in the `TimeUnit` field. These correspond to **Source columnn name** and **Timestamp time input** in the console. You can group or partition records using `measure_name` which is defined with the `MeasureNameColumn` key.

In the sample, `region`, `location`, and `hostname` are dimensions. Dimensions are mapped in an array of `DimensionMapping` objects.

For measures, the value `TargetMultiMeasureAttributeName` will become a column in the Timestream for LiveAnalytics table. You can keep the same name such as in this example. Or you can specify a new one. `MeasureValueType` is one of `DOUBLE`, `BIGINT`, `BOOLEAN`, `VARCHAR`, or `TIMESTAMP`. 

```
{
  "TimeColumn": "time",
  "TimeUnit": "MILLISECONDS",
  "DimensionMappings": [
    {
      "SourceColumn": "region",
      "DestinationColumn": "region"
    },
    {
      "SourceColumn": "location",
      "DestinationColumn": "location"
    },
    {
      "SourceColumn": "hostname",
      "DestinationColumn": "hostname"
    }
  ],
  "MeasureNameColumn": "measure_name",
  "MultiMeasureMappings": {
    "MultiMeasureAttributeMappings": [
      {
        "SourceColumn": "memory_utilization",
        "TargetMultiMeasureAttributeName": "memory_utilization",
        "MeasureValueType": "DOUBLE"
      },
      {
        "SourceColumn": "cpu_utilization",
        "TargetMultiMeasureAttributeName": "cpu_utilization",
        "MeasureValueType": "DOUBLE"
      }
    ]
  }
}
```

![Visual builder table showing seven column mappings with source names, target names, attribute types, and data types.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/column-mapping.jpg)


## Data model mappings with `MixedMeasureMappings` example
<a name="batch-load-data-model-mappings-example-mixed"></a>

We recommend that you only use this approach when you need to map to single-measure records in Timestream for LiveAnalytics.