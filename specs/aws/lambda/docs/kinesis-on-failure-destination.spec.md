---
id: "@specs/aws/lambda/docs/kinesis-on-failure-destination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Error handling"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Error handling

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/kinesis-on-failure-destination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Retain discarded batch records for a Kinesis Data Streams event source in Lambda
<a name="kinesis-on-failure-destination"></a>

Error handling for Kinesis event source mappings depends on whether the error occurs before the function is invoked or during function invocation:
+ **Before invocation:** If a Lambda event source mapping is unable to invoke the function due to throttling or other issues, it retries until the records expire or exceed the maximum age configured on the event source mapping ([MaximumRecordAgeInSeconds](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-MaximumRecordAgeInSeconds)).
+ **During invocation:** If the function is invoked but returns an error, Lambda retries until the records expire, exceed the maximum age ([MaximumRecordAgeInSeconds](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-MaximumRecordAgeInSeconds)), or reach the configured retry quota ([MaximumRetryAttempts](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-MaximumRetryAttempts)). For function errors, you can also configure [BisectBatchOnFunctionError](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-response-BisectBatchOnFunctionError), which splits a failed batch into two smaller batches, isolating bad records and avoiding timeouts. Splitting batches doesn't consume the retry quota.

If the error handling measures fail, Lambda discards the records and continues processing batches from the stream. With the default settings, this means that a bad record can block processing on the affected shard for up to one week. To avoid this, configure your function's event source mapping with a reasonable number of retries and a maximum record age that fits your use case.

## Configuring destinations for failed invocations
<a name="kinesis-on-failure-destination-console"></a>

To retain records of failed event source mapping invocations, add a destination to your function's event source mapping. Each record sent to the destination is a JSON document containing metadata about the failed invocation. For Amazon S3 destinations, Lambda also sends the entire invocation record along with the metadata. You can configure any Amazon SNS topic, Amazon SQS queue, Amazon S3 bucket, or Kafka as a destination.

With Amazon S3 destinations, you can use the [Amazon S3 Event Notifications](https://docs.aws.amazon.com/) feature to receive notifications when objects are uploaded to your destination S3 bucket. You can also configure S3 Event Notifications to invoke another Lambda function to perform automated processing on failed batches.

Your execution role must have permissions for the destination:
+ **For an SQS destination:** [sqs:SendMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html)
+ **For an SNS destination:** [sns:Publish](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html)
+ **For an S3 destination:** [ s3:PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) and [s3:ListBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/ListObjectsV2.html)
+ **For a Kafka destination:** [kafka-cluster:WriteData](https://docs.aws.amazon.com/msk/latest/developerguide/kafka-actions.html)

You can configure a Kafka topic as an on-failure destination for your Kafka event source mappings. When Lambda can't process records after exhausting retry attempts or when records exceed the maximum age, Lambda sends the failed records to the specified Kafka topic for later processing. Refer to [Using a Kafka topic as an on-failure destination](kafka-on-failure-destination.md).

If you've enabled encryption with your own KMS key for an S3 destination, your function's execution role must also have permission to call [kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html). If the KMS key and S3 bucket destination are in a different account from your Lambda function and execution role, configure the KMS key to trust the execution role to allow kms:GenerateDataKey.

To configure an on-failure destination using the console, follow these steps:

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose a function.

1. Under **Function overview**, choose **Add destination**.

1. For **Source**, choose **Event source mapping invocation**.

1. For **Event source mapping**, choose an event source that's configured for this function.

1. For **Condition**, select **On failure**. For event source mapping invocations, this is the only accepted condition.

1. For **Destination type**, choose the destination type that Lambda sends invocation records to.

1. For **Destination**, choose a resource.

1. Choose **Save**.

You can also configure an on-failure destination using the AWS Command Line Interface (AWS CLI). For example, the following [create-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html) command adds an event source mapping with an SQS on-failure destination to `MyFunction`:

```
aws lambda create-event-source-mapping \
--function-name "MyFunction" \
--event-source-arn arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream \
--destination-config '{"OnFailure": {"Destination": "arn:aws:sqs:us-east-1:123456789012:dest-queue"}}'
```

The following [update-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-event-source-mapping.html) command updates an event source mapping to send failed invocation records to an SNS destination after two retry attempts, or if the records are more than an hour old.

```
aws lambda update-event-source-mapping \
--uuid f89f8514-cdd9-4602-9e1f-01a5b77d449b \
--maximum-retry-attempts 2 \
--maximum-record-age-in-seconds 3600 \
--destination-config '{"OnFailure": {"Destination": "arn:aws:sns:us-east-1:123456789012:dest-topic"}}'
```

Updated settings are applied asynchronously and aren't reflected in the output until the process completes. Use the [get-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-event-source-mapping.html) command to view the current status.

To remove a destination, supply an empty string as the argument to the `destination-config` parameter:

```
aws lambda update-event-source-mapping \
--uuid f89f8514-cdd9-4602-9e1f-01a5b77d449b \
--destination-config '{"OnFailure": {"Destination": ""}}'
```

### Security best practices for Amazon S3 destinations
<a name="kinesis-s3-destination-security"></a>

Deleting an S3 bucket that's configured as a destination without removing the destination from your function's configuration can create a security risk. If another user knows your destination bucket's name, they can recreate the bucket in their AWS account. Records of failed invocations will be sent to their bucket, potentially exposing data from your function.

**Warning**  
To ensure that invocation records from your function can't be sent to an S3 bucket in another AWS account, add a condition to your function's execution role that limits `s3:PutObject` permissions to buckets in your account. 

The following example shows an IAM policy that limits your function's `s3:PutObject` permissions to buckets in your account. This policy also gives Lambda the `s3:ListBucket` permission it needs to use an S3 bucket as a destination.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "S3BucketResourceAccountWrite",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::*/*",
                "arn:aws:s3:::*"
            ],
            "Condition": {
                "StringEquals": {
                    "s3:ResourceAccount": {{"111122223333"}}
                }
            }
        }
    ]
}
```

To add a permissions policy to your function's execution role using the AWS Management Console or AWS CLI, refer to the instructions in the following procedures:

------
#### [ Console ]

**To add a permissions policy to a function's execution role (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Select the Lambda function whose execution role you want to modify.

1. In the **Configuration** tab, select **Permissions**.

1. In the **Execution role** tab, select your function's **Role name** to open the role's IAM console page.

1. Add a permissions policy to the role by doing the following:

   1. In the **Permissions policies** pane, choose **Add permissions** and select **Create inline policy**.

   1. In **Policy editor**, select **JSON**.

   1. Paste the policy you want to add into the editor (replacing the existing JSON), and then choose **Next**.

   1. Under **Policy details**, enter a **Policy name**.

   1. Choose **Create policy**.

------
#### [ AWS CLI ]

**To add a permissions policy to a function's execution role (CLI)**

1. Create a JSON policy document with the required permissions and save it in a local directory.

1. Use the IAM `put-role-policy` CLI command to add the permissions to your function's execution role. Run the following command from the directory you saved your JSON policy document in and replace the role name, policy name, and policy document with your own values.

   ```
   aws iam put-role-policy \
   --role-name {{my_lambda_role}} \
   --policy-name LambdaS3DestinationPolicy \
   --policy-document file://{{my_policy.json}}
   ```

------

### Example Amazon SNS and Amazon SQS invocation record
<a name="kinesis-on-failure-destination-example-sns-sqs"></a>

The following example shows what Lambda sends to an SQS queue or SNS topic for a failed Kinesis event source invocation. Because Lambda sends only the metadata for these destination types, use the `streamArn`, `shardId`, `startSequenceNumber`, and `endSequenceNumber` fields to obtain the full original record. All of the fields shown in the `KinesisBatchInfo` property will always be present.

```
{
    "requestContext": {
        "requestId": "c9b8fa9f-5a7f-xmpl-af9c-0c604cde93a5",
        "functionArn": "arn:aws:lambda:us-east-2:123456789012:function:myfunction",
        "condition": "RetryAttemptsExhausted",
        "approximateInvokeCount": 1
    },
    "responseContext": {
        "statusCode": 200,
        "executedVersion": "$LATEST",
        "functionError": "Unhandled"
    },
    "version": "1.0",
    "timestamp": "2019-11-14T00:38:06.021Z",
    "KinesisBatchInfo": {
        "shardId": "shardId-000000000001",
        "startSequenceNumber": "49601189658422359378836298521827638475320189012309704722",
        "endSequenceNumber": "49601189658422359378836298522902373528957594348623495186",
        "approximateArrivalOfFirstRecord": "2019-11-14T00:38:04.835Z",
        "approximateArrivalOfLastRecord": "2019-11-14T00:38:05.580Z",
        "batchSize": 500,
        "streamArn": "arn:aws:kinesis:us-east-2:123456789012:stream/mystream"
    }
}
```

You can use this information to retrieve the affected records from the stream for troubleshooting. The actual records aren't included, so you must process this record and retrieve them from the stream before they expire and are lost.

### Example Amazon S3 invocation record
<a name="kinesis-on-failure-destination-example-sns-sqs-s3"></a>

The following example shows what Lambda sends to an Amazon S3 bucket for a failed Kinesis event source invocation. In addition to all of the fields from the previous example for SQS and SNS destinations, the `payload` field contains the original invocation record as an escaped JSON string.

```
{
    "requestContext": {
        "requestId": "c9b8fa9f-5a7f-xmpl-af9c-0c604cde93a5",
        "functionArn": "arn:aws:lambda:us-east-2:123456789012:function:myfunction",
        "condition": "RetryAttemptsExhausted",
        "approximateInvokeCount": 1
    },
    "responseContext": {
        "statusCode": 200,
        "executedVersion": "$LATEST",
        "functionError": "Unhandled"
    },
    "version": "1.0",
    "timestamp": "2019-11-14T00:38:06.021Z",
    "KinesisBatchInfo": {
        "shardId": "shardId-000000000001",
        "startSequenceNumber": "49601189658422359378836298521827638475320189012309704722",
        "endSequenceNumber": "49601189658422359378836298522902373528957594348623495186",
        "approximateArrivalOfFirstRecord": "2019-11-14T00:38:04.835Z",
        "approximateArrivalOfLastRecord": "2019-11-14T00:38:05.580Z",
        "batchSize": 500,
        "streamArn": "arn:aws:kinesis:us-east-2:123456789012:stream/mystream"
    },
    "payload": "<Whole Event>" // Only available in S3
}
```

The S3 object containing the invocation record uses the following naming convention:

```
aws/lambda/<ESM-UUID>/<shardID>/YYYY/MM/DD/YYYY-MM-DDTHH.MM.SS-<Random UUID>
```