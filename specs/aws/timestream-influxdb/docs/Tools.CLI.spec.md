---
id: "@specs/aws/timestream-influxdb/docs/Tools.CLI"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Using the AWS CLI"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Using the AWS CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/Tools.CLI
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Accessing Amazon Timestream for LiveAnalytics using the AWS CLI
<a name="Tools.CLI"></a>

 You can use the AWS Command Line Interface (AWS CLI) to control multiple AWS services from the command line and automate them through scripts. You can use the AWS CLI for ad hoc operations. You can also use it to embed Amazon Timestream for LiveAnalytics operations within utility scripts.

 Before you can use the AWS CLI with Timestream for LiveAnalytics, you must get credentials that grant programmatic access. For more information, see [Provide Timestream for LiveAnalytics access](accessing.md#getting-started.prereqs.iam-user). 

For a complete listing of all the commands available for the Timestream for LiveAnalytics Query API in the AWS CLI, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/timestream-query/index.html).

For a complete listing of all the commands available for the Timestream for LiveAnalytics Write API in the AWS CLI, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/timestream-write/index.html).

**Topics**
+ [Downloading and configuring the AWS CLI](#Tools.CLI.DownloadingAndRunning)
+ [Using the AWS CLI with Timestream for LiveAnalytics](#Tools.CLI.UsingWithQLDB)

## Downloading and configuring the AWS CLI
<a name="Tools.CLI.DownloadingAndRunning"></a>

The AWS CLI runs on Windows, macOS, or Linux. To download, install, and configure it, follow these steps:

1. Download the AWS CLI at [http://aws.amazon.com/cli](https://aws.amazon.com/cli).

1. Follow the instructions for [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) and [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS Command Line Interface User Guide*.

## Using the AWS CLI with Timestream for LiveAnalytics
<a name="Tools.CLI.UsingWithQLDB"></a>

The command line format consists of an Amazon Timestream for LiveAnalytics operation name, followed by the parameters for that operation. The AWS CLI supports a shorthand syntax for the parameter values, in addition to JSON.

 Use `help` to list all available commands in Timestream for LiveAnalytics. For example: 

```
aws timestream-write help
```

```
aws timestream-query help
```

 You can also use `help` to describe a specific command and learn more about its usage: 

```
aws timestream-write create-database help
```

 For example, to create a database: 

```
aws timestream-write create-database --database-name myFirstDatabase
```

 To create a table with magnetic store writes enabled: 

```
aws timestream-write create-table \
--database-name metricsdb \
--table-name metrics \
--magnetic-store-write-properties "{\"EnableMagneticStoreWrites\": true}"
```

To write data using single-measure records:

```
aws timestream-write write-records \
--database-name metricsdb \
--table-name metrics \
--common-attributes "{\"Dimensions\":[{\"Name\":\"asset_id\", \"Value\":\"100\"}], \"Time\":\"1631051324000\",\"TimeUnit\":\"MILLISECONDS\"}" \
--records "[{\"MeasureName\":\"temperature\", \"MeasureValueType\":\"DOUBLE\",\"MeasureValue\":\"30\"},{\"MeasureName\":\"windspeed\", \"MeasureValueType\":\"DOUBLE\",\"MeasureValue\":\"7\"},{\"MeasureName\":\"humidity\", \"MeasureValueType\":\"DOUBLE\",\"MeasureValue\":\"15\"},{\"MeasureName\":\"brightness\", \"MeasureValueType\":\"DOUBLE\",\"MeasureValue\":\"17\"}]"
```

To write data using multi-measure records:

```
# wide model helper method to create Multi-measure records
function ingest_multi_measure_records {
  epoch=`date +%s`
  epoch+=$i

  # multi-measure records
  aws timestream-write write-records \
  --database-name $src_db_wide \
  --table-name $src_tbl_wide \
  --common-attributes "{\"Dimensions\":[{\"Name\":\"device_id\", \
              \"Value\":\"12345678\"},\
            {\"Name\":\"device_type\", \"Value\":\"iPhone\"}, \
            {\"Name\":\"os_version\", \"Value\":\"14.8\"}, \
            {\"Name\":\"region\", \"Value\":\"us-east-1\"} ], \
            \"Time\":\"$epoch\",\"TimeUnit\":\"MILLISECONDS\"}" \
--records "[{\"MeasureName\":\"video_metrics\", \"MeasureValueType\":\"MULTI\", \
  \"MeasureValues\": \
  [{\"Name\":\"video_startup_time\",\"Value\":\"0\",\"Type\":\"BIGINT\"}, \
  {\"Name\":\"rebuffering_ratio\",\"Value\":\"0.5\",\"Type\":\"DOUBLE\"}, \
  {\"Name\":\"video_playback_failures\",\"Value\":\"0\",\"Type\":\"BIGINT\"}, \
  {\"Name\":\"average_frame_rate\",\"Value\":\"0.5\",\"Type\":\"DOUBLE\"}]}]" \
--endpoint-url $ingest_endpoint \
  --region  $region
}

# create 5 records
for i in {100..105};
  do ingest_multi_measure_records $i;
done
```

To query a table: 

```
aws timestream-query query \
--query-string "SELECT time, device_id, device_type, os_version, 
region, video_startup_time, rebuffering_ratio, video_playback_failures, \
average_frame_rate \
FROM metricsdb.metrics \
where time >= ago (15m)"
```

To create a scheduled query: 

```
aws timestream-query create-scheduled-query \
  --name scheduled_query_name \
  --query-string "select bin(time, 1m) as time, \
          avg(measure_value::double) as avg_cpu, min(measure_value::double) as min_cpu, region \
          from $src_db.$src_tbl where measure_name = 'cpu' \
          and time BETWEEN @scheduled_runtime - (interval '5' minute)  AND @scheduled_runtime \
          group by region, bin(time, 1m)" \
  --schedule-configuration "{\"ScheduleExpression\":\"$cron_exp\"}" \
  --notification-configuration "{\"SnsConfiguration\":{\"TopicArn\":\"$sns_topic_arn\"}}" \
  --scheduled-query-execution-role-arn "arn:aws:iam::452360119086:role/TimestreamSQExecutionRole" \
  --target-configuration "{\"TimestreamConfiguration\":{\
          \"DatabaseName\": \"$dest_db\",\
          \"TableName\": \"$dest_tbl\",\
          \"TimeColumn\":\"time\",\
          \"DimensionMappings\":[{\
            \"Name\": \"region\", \"DimensionValueType\": \"VARCHAR\"
          }],\
          \"MultiMeasureMappings\":{\
            \"TargetMultiMeasureName\": \"mma_name\",
            \"MultiMeasureAttributeMappings\":[{\
              \"SourceColumn\": \"avg_cpu\", \"MeasureValueType\": \"DOUBLE\", \"TargetMultiMeasureAttributeName\": \"target_avg_cpu\"
            },\
            { \
              \"SourceColumn\": \"min_cpu\", \"MeasureValueType\": \"DOUBLE\", \"TargetMultiMeasureAttributeName\": \"target_min_cpu\"
            }] \
          }\
          }}" \
  --error-report-configuration "{\"S3Configuration\": {\
        \"BucketName\": \"$s3_err_bucket\",\
        \"ObjectKeyPrefix\": \"scherrors\",\
        \"EncryptionOption\": \"SSE_S3\"\
        }\
      }"
```