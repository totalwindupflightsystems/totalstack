---
id: "@specs/aws/lambda/docs/kafka-on-failure-destination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Kafka on-failure destination"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Kafka on-failure destination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/kafka-on-failure-destination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using a Kafka topic as an on-failure destination
<a name="kafka-on-failure-destination"></a>

You can configure a Kafka topic as an on-failure destination for your Kafka event source mappings. When Lambda can't process records after exhausting retry attempts or when records exceed the maximum age, Lambda sends the failed records to the specified Kafka topic for later processing. When you configure both [infinite retries](kafka-retry-configurations.md) and an on-failure destination, Lambda automatically applies a maximum of 10 retry attempts.

## How a Kafka on-failure destination works
<a name="kafka-ofd-overview"></a>

When you configure a Kafka topic as an on-failure destination, Lambda acts as a Kafka producer and writes failed records to the destination topic. This creates a dead letter topic (DLT) pattern within your Kafka infrastructure.
+ **Same cluster requirement** – The destination topic must exist in the same Kafka cluster as your source topics.
+ **Actual record content** – Kafka destinations receive the actual failed records along with failure metadata.
+ **Recursion prevention** – Lambda prevents infinite loops by blocking configurations where the source and destination topics are the same.

## Configuring a Kafka on-failure destination
<a name="kafka-ofd-configure"></a>

You can configure a Kafka topic as an on-failure destination when creating or updating a Kafka event source mapping.

### Configuring a Kafka destination (console)
<a name="kafka-ofd-console"></a>

**To configure a Kafka topic as an on-failure destination (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose your function name.

1. Do one of the following:
   + To add a new Kafka trigger, under **Function overview**, choose **Add trigger**.
   + To modify an existing Kafka trigger, choose the trigger and then choose **Edit**.

1. Under **Additional settings**, for **On-failure destination**, choose **Kafka topic**.

1. For **Topic name**, enter the name of the Kafka topic where you want to send failed records.

1. Choose **Add** or **Save**.

### Configuring a Kafka destination (AWS CLI)
<a name="kafka-ofd-cli"></a>

Use the `kafka://` prefix to specify a Kafka topic as an on-failure destination.

#### Creating an event source mapping with Kafka destination
<a name="kafka-ofd-cli-create"></a>

The following example creates a Amazon MSK event source mapping with a Kafka topic as the on-failure destination:

```
aws lambda create-event-source-mapping \
  --function-name my-kafka-function \
  --topics AWSKafkaTopic \
  --event-source-arn arn:aws:kafka:us-east-1:123456789012:cluster/my-cluster/abc123 \
  --starting-position LATEST \
  --provisioned-poller-config MinimumPollers=1,MaximumPollers=3 \
  --destination-config '{"OnFailure":{"Destination":"kafka://failed-records-topic"}}'
```

For self-managed Kafka, use the same syntax:

```
aws lambda create-event-source-mapping \
  --function-name my-kafka-function \
  --topics AWSKafkaTopic \
  --self-managed-event-source '{"Endpoints":{"KAFKA_BOOTSTRAP_SERVERS":["abc.xyz.com:9092"]}}' \
  --starting-position LATEST \
  --provisioned-poller-config MinimumPollers=1,MaximumPollers=3 \
  --destination-config '{"OnFailure":{"Destination":"kafka://failed-records-topic"}}'
```

#### Updating a Kafka destination
<a name="kafka-ofd-cli-update"></a>

Use the `update-event-source-mapping` command to add or modify a Kafka destination:

```
aws lambda update-event-source-mapping \
  --uuid 12345678-1234-1234-1234-123456789012 \
  --destination-config '{"OnFailure":{"Destination":"kafka://failed-records-topic"}}'
```

## Record format for a Kafka destination
<a name="kafka-ofd-record-format"></a>

When Lambda sends failed records to a Kafka topic, each message contains both metadata about the failure and the actual record content.

### Failure metadata
<a name="kafka-ofd-metadata"></a>

The metadata includes information about why the record failed and details about the original batch:

```
{
  "requestContext": {
    "requestId": "e4b46cbf-b738-xmpl-8880-a18cdf61200e",
    "functionArn": "arn:aws:lambda:us-east-1:123456789012:function:my-function:$LATEST",
    "condition": "RetriesExhausted",
    "approximateInvokeCount": 3
  },
  "responseContext": {
    "statusCode": 200,
    "executedVersion": "$LATEST",
    "functionError": "Unhandled"
  },
  "version": "1.0",
  "timestamp": "2019-11-14T18:16:05.568Z",
  "KafkaBatchInfo": {
    "batchSize": 1,
    "eventSourceArn": "arn:aws:kafka:us-east-1:123456789012:cluster/my-cluster/abc123",
    "bootstrapServers": "b-1.mycluster.abc123.kafka.us-east-1.amazonaws.com:9098",
    "payloadSize": 1162,
    "recordInfo": {
      "offset": "49601189658422359378836298521827638475320189012309704722",
      "timestamp": "2019-11-14T18:16:04.835Z"
    }
  },
  "payload": {
    "bootstrapServers": "b-1.mycluster.abc123.kafka.us-east-1.amazonaws.com:9098",
    "eventSource": "aws:kafka",
    "eventSourceArn": "arn:aws:kafka:us-east-1:123456789012:cluster/my-cluster/abc123",
    "records": {
      "my-topic-0": [
        {
          "headers": [],
          "key": "dGVzdC1rZXk=",
          "offset": 100,
          "partition": 0,
          "timestamp": 1749116692330,
          "timestampType": "CREATE_TIME",
          "topic": "my-topic",
          "value": "dGVzdC12YWx1ZQ=="
        }
      ]
    }
  }
}
```

### Partition key behavior
<a name="kafka-ofd-partitioning"></a>

Lambda uses the same partition key from the original record when producing to the destination topic. If the original record had no key, Lambda uses Kafka's default round-robin partitioning across all available partitions in the destination topic.

## Requirements and limitations
<a name="kafka-ofd-requirements"></a>
+ **Provisioned mode required** – A Kafka on-failure destination is only available for event source mappings with provisioned mode enabled.
+ **Same cluster only** – The destination topic must exist in the same Kafka cluster as your source topics.
+ **Topic permissions** – Your event source mapping must have write permissions to the destination topic. Example:

  ```
  {
      "Version": "2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "ClusterPermissions",
              "Effect": "Allow",
              "Action": [
                  "kafka-cluster:Connect",
                  "kafka-cluster:DescribeCluster",
                  "kafka-cluster:DescribeTopic",
                  "kafka-cluster:WriteData",
                  "kafka-cluster:ReadData"
              ],
              "Resource": [
                  "arn:aws:kafka:*:*:cluster/*"
              ]
          },
          {
              "Sid": "TopicPermissions",
              "Effect": "Allow",
              "Action": [
                  "kafka-cluster:DescribeTopic",
                  "kafka-cluster:WriteData",
                  "kafka-cluster:ReadData"
              ],
              "Resource": [
                  "arn:aws:kafka:*:*:topic/*/*"
              ]
          },
          {
              "Effect": "Allow",
              "Action": [
                  "kafka:DescribeCluster",
                  "kafka:GetBootstrapBrokers",
                  "kafka:Produce"
              ],
              "Resource": "arn:aws:kafka:*:*:cluster/*"
          },
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:CreateNetworkInterface",
                  "ec2:DescribeNetworkInterfaces",
                  "ec2:DeleteNetworkInterface",
                  "ec2:DescribeSubnets",
                  "ec2:DescribeSecurityGroups"
              ],
              "Resource": "*"
          }
      ]
  }
  ```
+ **No recursion** – The destination topic name cannot be the same as any of your source topic names.