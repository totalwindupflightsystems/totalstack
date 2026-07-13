---
id: "@specs/aws/lambda/docs/esm-logging"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Kafka ESM logging"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Kafka ESM logging

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/esm-logging
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Kafka event source mapping logging
<a name="esm-logging"></a>

You can configure the system-level logging for your Kafka event source mappings to enable and filter the system logs that Lambda event pollers send to CloudWatch. 

This feature is only available for Kafka event source mappings, and with [Provisioned mode](https://docs.aws.amazon.com/lambda/latest/dg/kafka-scaling-modes.html#kafka-provisioned-mode).

For event source mapping with logging config, you can also check the system logs from pre-built log queries in the **Monitor** tab from the page Console **Lambda** > **Additional resources** > **event source mappings** now.

## How the logging works
<a name="esm-logging-overview"></a>

When you set the logging config with log level in your event source mapping, the Lambda event poller sends out corresponding logs (event source mapping system logs).

The event source mapping reuses the same [log destination](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-logs.html#configuring-log-destinations) with your Lambda function. Make sure the execution role of your Lambda function has the necessary logging permissions.

The event source mapping will have its own log stream, with date and event source mapping UUID as the log stream name, like `2020/01/01/12345678-1234-1234-1234-12345678901`.

For event source mapping system logs, you can choose between the following log levels.


| Log level | Usage | 
| --- | --- | 
| DEBUG (most detail) | Detailed information for event source processing progress | 
| INFO | Messages about the normal operation of your event source mapping | 
| WARN (least detail) | Messages about potential warns and errors that may lead to unexpected behavior | 

When you select a log level, Lambda event poller sends logs at that level and lower. For example, if you set the event source mapping system log level to INFO, event poller doesn’t send log outputs at the DEBUG level.

## Configuring logging
<a name="esm-logging-configure"></a>

You can set the logging configure when creating or updating a Kafka event source mapping.

### Configuring logging (console)
<a name="esm-logging-console"></a>

**To configure the logging (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose your function name.

1. Do one of the following:
   + To add a new Kafka trigger, under **Function overview**, choose **Add trigger**.
   + To modify an existing Kafka trigger, choose the trigger and then choose **Edit**.

1. Under **Event poller configuration**, for **Provisioned mode**, enable the **Configure** checkbox. And the **Log level** setting would show up.

1.  Click **Log level** dropdown list and select a level for the event source mapping.

1. Choose **Add** or **Save** at the bottom to create or update the event source mapping.

### Configuring logging (AWS CLI)
<a name="esm-logging-cli"></a>

#### Creating an event source mapping with logging
<a name="esm-logging-cli-create"></a>

The following example creates a Amazon MSK event source mapping with logging config:

```
aws lambda create-event-source-mapping \
  --function-name my-kafka-function \
  --topics AWSKafkaTopic \
  --event-source-arn arn:aws:kafka:us-east-1:123456789012:cluster/my-cluster/abc123 \
  --starting-position LATEST \
  --provisioned-poller-config MinimumPollers=1,MaximumPollers=3 \
  --logging-config '{"SystemLogLevel":"DEBUG"}'
```

For self-managed Kafka, use the same syntax:

```
aws lambda create-event-source-mapping \
  --function-name my-kafka-function \
  --topics AWSKafkaTopic \
  --self-managed-event-source '{"Endpoints":{"KAFKA_BOOTSTRAP_SERVERS":["abc.xyz.com:9092"]}}' \
  --starting-position LATEST \
  --provisioned-poller-config MinimumPollers=1,MaximumPollers=3 \
  --logging-config '{"SystemLogLevel":"DEBUG"}'
```

#### Updating logging config
<a name="esm-logging-cli-update"></a>

Use the `update-event-source-mapping` command to add or modify logging config:

```
aws lambda update-event-source-mapping \
  --uuid 12345678-1234-1234-1234-123456789012 \
  --logging-config '{"SystemLogLevel":"WARN"}'
```

## Record format for a Kafka event source mapping system log
<a name="esm-logging-record-format"></a>

When Lambda event poller sends the log, each log entry contains general event source mapping metadata and also event specific content.

### WARN log record
<a name="esm-logging-warn-record"></a>

WARN record contains errors or warnings from the event poller, and it's emitted when the event happened. For example:

```
{
    "eventType": "ESM_PROCESSING_EVENT",
    "timestamp": 1546347650000,
    "resourceArn": "arn:aws:lambda:us-east-1:123456789012:event-source-mapping:12345678-1234-1234-1234-123456789012",
    "eventSourceArn": "arn:aws:kafka:us-east-1:123456789012:cluster/tests-cluster/87654321-4321-4321-4321-876543221-s1",
    "eventProcessorId": "12345678-1234-1234-1234-123456789012/0",
    "logLevel": "WARN",
    "error": {
        "errorMessage": "Timeout expired while fetching topic metadata",
        "errorCode": "org.apache.kafka.common.errors.TimeoutException"
    }
}
```

### INFO log record
<a name="esm-logging-info-record"></a>

INFO record contains Kafka consumer client configurations in each event poller, and it's emitted on the event of a consumer being built or changed. For example:

```
{
    "eventType": "POLLER_STATUS_EVENT",
    "timestamp": 1546347660000,
    "resourceArn": "arn:aws:lambda:us-east-1:123456789012:event-source-mapping:12345678-1234-1234-1234-123456789012",
    "eventSourceArn": "arn:aws:kafka:us-east-1:123456789012:cluster/tests-cluster/87654321-4321-4321-4321-876543221-s1",
    "eventProcessorId": "12345678-1234-1234-1234-123456789012/0",
    "logLevel": "INFO",
    "kafkaEventSourceConnection": {
        "brokerEndpoints": "boot-abcd1234.c2.kafka-serverless.us-east-1.amazonaws.com:9098",
        "consumerId": "12345678-1234-1234-1234-123456789012-0",
        "topics": [
            "test"
        ],
        "consumerGroupId": "12345678-1234-1234-1234-123456789012",
        "securityProtocol": "SASL_SSL",
        "saslMechanism": "AWS_MSK_IAM",
        "totalPartitionCount": 2,
        "assignedPartitionCount": 2,
        "partitionsAssignmentGeneration": 5,
        "assignedPartitions": [
            "test-0",
            "test-1"
        ],
        "networkConfig": {
            "ipAddresses": [
                "10.100.141.1"
            ],
            "subnetCidrBlock": "10.100.128.0/20",
            "securityGroups": [
                "sg-abcdefabcdefabcdef"
            ]
        }
    }
}
```

### DEBUG log record
<a name="esm-logging-debug-record"></a>

DEBUG log contains the Kafka offsets related info in event source mapping processing, and the offset info is emitted per minute. For example:

```
{
    "eventType": "KAFKA_STATUS_EVENT",
    "timestamp": 1546347670000,
    "resourceArn": "arn:aws:lambda:us-east-1:123456789012:event-source-mapping:12345678-1234-1234-1234-123456789012",
    "eventSourceArn": "arn:aws:kafka:us-east-1:123456789012:cluster/tests-cluster/87654321-4321-4321-4321-876543221-s1",
    "eventProcessorId": "12345678-1234-1234-1234-123456789012/0",
    "logLevel": "DEBUG",
    "kafkaPartitionOffsets": {
        "partition": "test-1",
        "endOffset": 5004,
        "consumedOffset": 5003,
        "processedOffset": 5003,
        "committedOffset": 5004
    }
}
```