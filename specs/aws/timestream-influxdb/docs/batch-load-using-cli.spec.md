---
id: "@specs/aws/timestream-influxdb/docs/batch-load-using-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Using batch load with the CLI"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Using batch load with the CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/batch-load-using-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Using batch load with the AWS CLI
<a name="batch-load-using-cli"></a>

**Setup**

To start using batch load, go through the following steps.

1. Install the AWS CLI using the instructions at [Accessing Amazon Timestream for LiveAnalytics using the AWS CLI](Tools.CLI.md).

1. Run the following command to verify that the Timestream CLI commands have been updated. Verify that create-batch-load-task is in the list.

   `aws timestream-write help`

1. Prepare a data source using the instructions at [Preparing a batch load data file](batch-load-preparing-data-file.md).

1. Create a database and table using the instructions at [Accessing Amazon Timestream for LiveAnalytics using the AWS CLI](Tools.CLI.md).

1. Create an S3 bucket for report output. The bucket must be in the same Region. For more information about buckets, see [Creating, configuring, and working with Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html).

1. Create a batch load task. For steps, see [Create a batch load task](#batch-load-using-cli-create-task).

1. Confirm the status of the task. For steps, see [Describe batch load task](#batch-load-using-cli-describe-task).

## Create a batch load task
<a name="batch-load-using-cli-create-task"></a>

You can create a batch load task with the `create-batch-load-task` command. When you create a batch load task using the CLI, you can use a JSON parameter, `cli-input-json`, which lets you aggregate the parameters into a single JSON fragment. You can also break those details apart using several other parameters including `data-model-configuration`, `data-source-configuration`, `report-configuration`, `target-database-name`, and `target-table-name`.

For an example, see [Create batch load task example](#batch-load-using-cli-example)

## Describe batch load task
<a name="batch-load-using-cli-describe-task"></a>

You can retrieve a batch load task description as follows.

```
aws timestream-write describe-batch-load-task --task-id {{<value>}}
```

Following is an example response.

```
{
    "BatchLoadTaskDescription": {
        "TaskId": "{{<TaskId>}}",
        "DataSourceConfiguration": {
            "DataSourceS3Configuration": {
                "BucketName": "test-batch-load-west-2",
                "ObjectKeyPrefix": "sample.csv"
            },
            "CsvConfiguration": {},
            "DataFormat": "CSV"
        },
        "ProgressReport": {
            "RecordsProcessed": 2,
            "RecordsIngested": 0,
            "FileParseFailures": 0,
            "RecordIngestionFailures": 2,
            "FileFailures": 0,
            "BytesIngested": 119
        },
        "ReportConfiguration": {
            "ReportS3Configuration": {
                "BucketName": "test-batch-load-west-2",
                "ObjectKeyPrefix": "{{<ObjectKeyPrefix>}}",
                "EncryptionOption": "SSE_S3"
            }
        },
        "DataModelConfiguration": {
            "DataModel": {
                "TimeColumn": "timestamp",
                "TimeUnit": "SECONDS",
                "DimensionMappings": [
                    {
                        "SourceColumn": "vehicle",
                        "DestinationColumn": "vehicle"
                    },
                    {
                        "SourceColumn": "registration",
                        "DestinationColumn": "license"
                    }
                ],
                "MultiMeasureMappings": {
                    "TargetMultiMeasureName": "test",
                    "MultiMeasureAttributeMappings": [
                        {
                            "SourceColumn": "wgt",
                            "TargetMultiMeasureAttributeName": "weight",
                            "MeasureValueType": "DOUBLE"
                        },
                        {
                            "SourceColumn": "spd",
                            "TargetMultiMeasureAttributeName": "speed",
                            "MeasureValueType": "DOUBLE"
                        },
                        {
                            "SourceColumn": "fuel",
                            "TargetMultiMeasureAttributeName": "fuel",
                            "MeasureValueType": "DOUBLE"
                        },
                        {
                            "SourceColumn": "miles",
                            "TargetMultiMeasureAttributeName": "miles",
                            "MeasureValueType": "DOUBLE"
                        }
                    ]
                }
            }
        },
        "TargetDatabaseName": "BatchLoadExampleDatabase",
        "TargetTableName": "BatchLoadExampleTable",
        "TaskStatus": "FAILED",
        "RecordVersion": 1,
        "CreationTime": 1677167593.266,
        "LastUpdatedTime": 1677167602.38
    }
}
```

## List batch load tasks
<a name="batch-load-using-cli-list-tasks"></a>

You can list batch load tasks as follows.

```
aws timestream-write list-batch-load-tasks
```

An output appears as follows.

```
{
    "BatchLoadTasks": [
        {
            "TaskId": "{{<TaskId>}}",
            "TaskStatus": "FAILED",
            "DatabaseName": "BatchLoadExampleDatabase",
            "TableName": "BatchLoadExampleTable",
            "CreationTime": 1677167593.266,
            "LastUpdatedTime": 1677167602.38
        }
    ]
}
```

## Resume batch load task
<a name="batch-load-using-cli-resume-task"></a>

You can resume a batch load task as follows.

```
aws timestream-write resume-batch-load-task --task-id {{<value>}}
```

A response can indicate success or contain error information.

## Create batch load task example
<a name="batch-load-using-cli-example"></a>

**Example**  

1. Create a Timestream for LiveAnalytics database named `BatchLoad` and a table named `BatchLoadTest`. Verify and, if necessary, adjust the values for `MemoryStoreRetentionPeriodInHours` and `MagneticStoreRetentionPeriodInDays`.

   ```
   aws timestream-write create-database --database-name BatchLoad \
   
   aws timestream-write create-table --database-name BatchLoad \
   --table-name BatchLoadTest \
   --retention-properties "{\"MemoryStoreRetentionPeriodInHours\": 12, \"MagneticStoreRetentionPeriodInDays\": 100}"
   ```

1. Using the console, create an S3 bucket and copy the `sample.csv` file to that location. You can download a sample CSV at [sample CSV](samples/batch-load-sample-file.csv.zip).

1. Using the console create an S3 bucket for Timestream for LiveAnalytics to write a report if the batch load task completes with errors.

1. Create a batch load task. Make sure to replace {{$INPUT\_BUCKET}} and {{$REPORT\_BUCKET}} with the buckets that you created in the preceding steps.

   ```
   aws timestream-write create-batch-load-task \
   --data-model-configuration "{\
               \"DataModel\": {\
                 \"TimeColumn\": \"timestamp\",\
                 \"TimeUnit\": \"SECONDS\",\
                 \"DimensionMappings\": [\
                   {\
                     \"SourceColumn\": \"vehicle\"\
                   },\
                   {\
                     \"SourceColumn\": \"registration\",\
                     \"DestinationColumn\": \"license\"\
                   }\
                 ],
                 \"MultiMeasureMappings\": {\
                   \"TargetMultiMeasureName\": \"mva_measure_name\",\
                   \"MultiMeasureAttributeMappings\": [\
                     {\
                       \"SourceColumn\": \"wgt\",\
                       \"TargetMultiMeasureAttributeName\": \"weight\",\
                       \"MeasureValueType\": \"DOUBLE\"\
                     },\
                     {\
                       \"SourceColumn\": \"spd\",\
                       \"TargetMultiMeasureAttributeName\": \"speed\",\
                       \"MeasureValueType\": \"DOUBLE\"\
                     },\
                     {\
                       \"SourceColumn\": \"fuel_consumption\",\
                       \"TargetMultiMeasureAttributeName\": \"fuel\",\
                       \"MeasureValueType\": \"DOUBLE\"\
                     },\
                     {\
                       \"SourceColumn\": \"miles\",\
                       \"MeasureValueType\": \"BIGINT\"\
                     }\
                   ]\
                 }\
               }\
             }" \
   --data-source-configuration "{
               \"DataSourceS3Configuration\": {\
                 \"BucketName\": \"{{$INPUT_BUCKET}}\",\
                 \"ObjectKeyPrefix\": \"{{$INPUT_OBJECT_KEY_PREFIX}}\"
               },\
               \"DataFormat\": \"CSV\"\
             }" \
   --report-configuration "{\
               \"ReportS3Configuration\": {\
                 \"BucketName\": \"{{$REPORT_BUCKET}}\",\
                 \"EncryptionOption\": \"SSE_S3\"\
               }\
             }" \
   --target-database-name BatchLoad \
   --target-table-name BatchLoadTest
   ```

   The preceding command returns the following output.

   ```
   {
       "TaskId": "{{TaskId}} "
   }
   ```

1. Check on the progress of the task. Make sure you replace {{$TASK\_ID}} with the task id that was returned in the preceding step.

   ```
   aws timestream-write describe-batch-load-task --task-id {{$TASK_ID}} 
   ```
**Example output**  

```
{
    "BatchLoadTaskDescription": {
        "ProgressReport": {
            "BytesIngested": 1024,
            "RecordsIngested": 2,
            "FileFailures": 0,
            "RecordIngestionFailures": 0,
            "RecordsProcessed": 2,
            "FileParseFailures": 0
        },
        "DataModelConfiguration": {
            "DataModel": {
                "DimensionMappings": [
                    {
                        "SourceColumn": "vehicle",
                        "DestinationColumn": "vehicle"
                    },
                    {
                        "SourceColumn": "registration",
                        "DestinationColumn": "license"
                    }
                ],
                "TimeUnit": "SECONDS",
                "TimeColumn": "timestamp",
                "MultiMeasureMappings": {
                    "MultiMeasureAttributeMappings": [
                        {
                            "TargetMultiMeasureAttributeName": "weight",
                            "SourceColumn": "wgt",
                            "MeasureValueType": "DOUBLE"
                        },
                        {
                            "TargetMultiMeasureAttributeName": "speed",
                            "SourceColumn": "spd",
                            "MeasureValueType": "DOUBLE"
                        },
                        {
                            "TargetMultiMeasureAttributeName": "fuel",
                            "SourceColumn": "fuel_consumption",
                            "MeasureValueType": "DOUBLE"
                        },
                        {
                            "TargetMultiMeasureAttributeName": "miles",
                            "SourceColumn": "miles",
                            "MeasureValueType": "DOUBLE"
                        }
                    ],
                    "TargetMultiMeasureName": "mva_measure_name"
                }
            }
        },
        "TargetDatabaseName": "BatchLoad",
        "CreationTime": 1672960381.735,
        "TaskStatus": "SUCCEEDED",
        "RecordVersion": 1,
        "TaskId": "{{TaskId}} ",
        "TargetTableName": "BatchLoadTest",
        "ReportConfiguration": {
            "ReportS3Configuration": {
                "EncryptionOption": "SSE_S3",
                "ObjectKeyPrefix": "{{ObjectKeyPrefix}} ",
                "BucketName": "amzn-s3-demo-bucket"
            }
        },
        "DataSourceConfiguration": {
            "DataSourceS3Configuration": {
                "ObjectKeyPrefix": "sample.csv",
                "BucketName": "amzn-s3-demo-source-bucket"
            },
            "DataFormat": "CSV",
            "CsvConfiguration": {}
        },
        "LastUpdatedTime": 1672960387.334
    }
}
```