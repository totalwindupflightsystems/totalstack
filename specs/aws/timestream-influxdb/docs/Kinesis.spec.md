---
id: "@specs/aws/timestream-influxdb/docs/Kinesis"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon Kinesis"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Amazon Kinesis

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/Kinesis
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Amazon Kinesis
<a name="Kinesis"></a>

## Using Amazon Managed Service for Apache Flink
<a name="kinesis-via-flink"></a>

You can send data from Kinesis Data Streams to Timestream for LiveAnalytics using the sample Timestream data connector for Managed Service for Apache Flink. Refer to [Amazon Managed Service for Apache Flink](ApacheFlink.md) for Apache Flink for more information.

## Using EventBridge Pipes to send Kinesis data to Timestream
<a name="Kinesis-via-pipes"></a>

You can use EventBridge Pipes to send data from a Kinesis stream to a Amazon Timestream for LiveAnalytics table.

Pipes are intended for point-to-point integrations between supported sources and targets, with support for advanced transformations and enrichment. Pipes reduce the need for specialized knowledge and integration code when developing event-driven architectures. To set up a pipe, you choose the source, add optional filtering, define optional enrichment, and choose the target for the event data.

![A source sends events to an EventBridge pipe, which filters and routes matching events to the target.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/pipes-overview_shared_architecture.png)


This integration enables you to leverage the power of Timestream's time-series data analysis capabilities, while simplifying your data ingestion pipeline.

Using EventBridge Pipes with Timestream offers the following benefits:
+ Real-time Data Ingestion: Stream data from Kinesis directly to Timestream for LiveAnalytics, enabling real-time analytics and monitoring.
+ Seamless Integration: Utilize EventBridge Pipes to manage the flow of data without the need for complex custom integrations.
+ Enhanced Filtering and Transformation: Filter or transform Kinesis records before they are stored in Timestream to meet your specific data processing requirements.
+ Scalability: Handle high-throughput data streams and ensure efficient data processing with built-in parallelism and batching capabilities.

### Configuration
<a name="Kinesis-via-pipes-config"></a>

To set up an EventBridge Pipe to stream data from Kinesis to Timestream, follow these steps:

1. Create a Kinesis stream

   Ensure you have an active Kinesis data stream from which you want to ingest data.

1. Create a Timestream database and table

   Set up your Timestream database and table where the data will be stored.

1. Configure the EventBridge Pipe:
   + Source: Select your Kinesis stream as the source.
   + Target: Choose Timestream as the target.
   + Batching Settings: Define batching window and batch size to optimize data processing and reduce latency.

**Important**  
When setting up a pipe, we recommend testing the correctness of all configurations by ingesting a few records. Please note that successful creation of a pipe does not guarantee that the pipeline is correct and data will flow without errors. There may be runtime errors, such as incorrect table, incorrect dynamic path parameter, or invalid Timestream record after applying mapping, that will be discovered when actual data flows through the pipe.

The following configurations determine the rate at which data is ingested:
+ BatchSize: The maximum size of the batch that will be sent to Timestream for LiveAnalytics. Range: 0 - 100. Recommendation is to keep this value as 100 to get maximum throughput.
+ MaximumBatchingWindowInSeconds: The maximum time to wait to fill the batchSize before the batch is sent to Timestream for LiveAnalytics target. Depending on the rate of incoming events, this configuration will decide the delay of ingestion, recommendation is to keep this value < 10s to keep sending the data to Timestream in near real-time.
+ ParallelizationFactor: The number of batches to process concurrently from each shard. Recommendation is to use the maximum value of 10 to get maximum throughput and near real-time ingestion.

  If your stream is read by multiple targets, use enhanced fan-out to provide a dedicated consumer to your pipe to achieve high throughput. For more information, see [Developing enhanced fan-out consumers with the Kinesis Data Streams API](https://docs.aws.amazon.com/streams/latest/dev/building-enhanced-consumers-api.html) in the *Kinesis Data Streams User Guide*.

**Note**  
The maximum throughput that can be achieved is bounded by [concurrent pipe executions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-quota.html#eb-pipes-limits) per account.

The following configuration ensures prevention of data loss:
+ DeadLetterConfig: Recommendation is to always configure DeadLetterConfig to avoid any data loss for cases when events could not be ingested to Timestream for LiveAnalytics due to user errors.

Optimize your pipe's performance with the following configuration settings, which helps prevent records from causing slowdowns or blockages.
+ MaximumRecordAgeInSeconds: Records older than this will not be processed and will directly get moved to DLQ. We recommend setting this value to be no higher than the configured Memory store retention period of the target Timestream table.
+ MaximumRetryAttempts: The number of retry attempts for a record before the record is sent to DeadLetterQueue. Recommendation is to configure this at 10. This should be able to help address any transient issues and for persistent issues, the record will be moved to DeadLetterQueue and unblock the rest of the stream.
+ OnPartialBatchItemFailure: For sources that support partial batch processing, we recommend you to enable this and configure it as AUTOMATIC\_BISECT for additional retry of failed records before dropping/sending to DLQ.

#### Configuration example
<a name="Kinesis-via-pipes-config-example"></a>

Here is an example of how to configure an EventBridge Pipe to stream data from a Kinesis stream to a Timestream table:

**Example IAM policy updates for Timestream**    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "timestream:WriteRecords"
            ],
            "Resource": [
                "arn:aws:timestream:us-east-1:123456789012:database/my-database/table/my-table"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "timestream:DescribeEndpoints"
            ],
            "Resource": "*"
        }
    ]
}
```

**Example Kinesis stream configuration**  <a name="kinesis-stream-config.example"></a>

```
{
  "Source": "arn:aws:kinesis:us-east-1:123456789012:stream/my-kinesis-stream",
  "SourceParameters": {
    "KinesisStreamParameters": {
        "BatchSize": 100,
        "DeadLetterConfig": {
            "Arn": "arn:aws:sqs:us-east-1:123456789012:my-sqs-queue"
        },
       "MaximumBatchingWindowInSeconds": 5,
        "MaximumRecordAgeInSeconds": 1800,
        "MaximumRetryAttempts": 10,
        "StartingPosition": "LATEST",
       "OnPartialBatchItemFailure": "AUTOMATIC_BISECT"
    }
  }
}
```

**Example Timestream target configuration**  <a name="kinesis-stream-config.example"></a>

```
{
    "Target": "arn:aws:timestream:us-east-1:123456789012:database/my-database/table/my-table",
    "TargetParameters": {
        "TimestreamParameters": {
            "DimensionMappings": [
                {
                    "DimensionName": "sensor_id",
                    "DimensionValue": "$.data.device_id",
                    "DimensionValueType": "VARCHAR"
                },
                {
                    "DimensionName": "sensor_type",
                    "DimensionValue": "$.data.sensor_type",
                    "DimensionValueType": "VARCHAR"
                },
                {
                    "DimensionName": "sensor_location",
                    "DimensionValue": "$.data.sensor_loc",
                    "DimensionValueType": "VARCHAR"
                }
            ],
            "MultiMeasureMappings": [
                {
                    "MultiMeasureName": "readings",
                    "MultiMeasureAttributeMappings": [
                        {
                            "MultiMeasureAttributeName": "temperature",
                            "MeasureValue": "$.data.temperature",
                            "MeasureValueType": "DOUBLE"
                        },
                        {
                            "MultiMeasureAttributeName": "humidity",
                            "MeasureValue": "$.data.humidity",
                            "MeasureValueType": "DOUBLE"
                        },
                        {
                            "MultiMeasureAttributeName": "pressure",
                            "MeasureValue": "$.data.pressure",
                            "MeasureValueType": "DOUBLE"
                        }
                    ]
                }
            ],
            "SingleMeasureMappings": [],
            "TimeFieldType": "TIMESTAMP_FORMAT",
            "TimestampFormat": "yyyy-MM-dd HH:mm:ss.SSS",
            "TimeValue": "$.data.time",
            "VersionValue": "$.approximateArrivalTimestamp"
        }
    }
}
```



### Event transformation
<a name="Kinesis-via-pipes-trans"></a>

EventBridge Pipes allow you to transform data before it reaches Timestream. You can define transformation rules to modify the incoming Kinesis records, such as changing field names.

Suppose your Kinesis stream contains temperature and humidity data. You can use an EventBridge transformation to rename these fields before inserting them into Timestream.

### Best practices
<a name="Kinesis-via-pipes-best"></a>

**Batching and Buffering**
+ Configure the batching window and size to balance between write latency and processing efficiency.
+ Use a batching window to accumulate enough data before processing, reducing the overhead of frequent small batches.

**Parallel Processing**

Utilize the **ParallelizationFactor** setting to increase concurrency, especially for high-throughput streams. This ensures that multiple batches from each shard can be processed simultaneously.

**Data Transformation**

Leverage the transformation capabilities of EventBridge Pipes to filter and enhance records before storing them in Timestream. This can help in aligning the data with your analytical requirements.

**Security**
+ Ensure that the IAM roles used for EventBridge Pipes have the necessary permissions to read from Kinesis and write to Timestream.
+ Use encryption and access control measures to secure data in transit and at rest.

### Debugging failures
<a name="Kinesis-via-pipes-debug"></a>
+ **Automatic Disabling of Pipes**

  Pipes will be automatically disabled in about 2 hours if the target does not exist or has permission issues
+ **Throttles**

  Pipes have the capability to automatically back off and retry until the throttles have reduced.
+ **Enabling Logs**

  We recommend you enable Logs at ERROR level and include execution data to get more insights into failed. Upon any failure, these logs will contain request/response sent/received from Timestream. This helps you understand the error associated and if needed reprocess the records after fixing it.

### Monitoring
<a name="Kinesis-via-pipes-monitor"></a>

We recommend you to set up alarms on the following to detect any issues with data flow:
+ Maximum Age of the Record in Source
  + `GetRecords.IteratorAgeMilliseconds`
+ Failure metrics in Pipes
  + `ExecutionFailed`
  + `TargetStageFailed`
+ Timestream Write API errors
  + `UserErrors`

For additional monitoring metrics, see [Monitoring EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-monitoring.html#eb-metrics) in the *EventBridge User Guide*.