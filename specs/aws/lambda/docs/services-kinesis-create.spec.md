---
id: "@specs/aws/lambda/docs/services-kinesis-create"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create mapping"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Create mapping

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/services-kinesis-create
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Process Amazon Kinesis Data Streams records with Lambda
<a name="services-kinesis-create"></a>

To process Amazon Kinesis Data Streams records with Lambda, create a Lambda event source mapping. You can map a Lambda function to a standard iterator or enhanced fan-out consumer. For more information, see [Polling and batching streams](with-kinesis.md#kinesis-polling-and-batching).

## Create an Kinesis event source mapping
<a name="services-kinesis-eventsourcemapping"></a>

To invoke your Lambda function with records from your data stream, create an [event source mapping](invocation-eventsourcemapping.md). You can create multiple event source mappings to process the same data with multiple Lambda functions, or to process items from multiple data streams with a single function. When processing items from multiple streams, each batch contains records from only a single shard or stream.

You can configure event source mappings to process records from a stream in a different AWS account. To learn more, see [Creating a cross-account event source mapping](#services-kinesis-eventsourcemapping-cross-account).

Before you create an event source mapping, you need to give your Lambda function permission to read from a Kinesis data stream. Lambda needs the following permissions to manage resources related to your Kinesis data stream:
+ [kinesis:DescribeStream](https://docs.aws.amazon.com/lambda/latest/api/API_DescribeStream.html)
+ [kinesis:DescribeStreamSummary](https://docs.aws.amazon.com/lambda/latest/api/API_DescribeStreamSummary.html)
+ [kinesis:GetRecords](https://docs.aws.amazon.com/lambda/latest/api/API_GetRecords.html)
+ [kinesis:GetShardIterator](https://docs.aws.amazon.com/lambda/latest/api/API_GetShardIterator.html)
+ [kinesis:ListShards](https://docs.aws.amazon.com/lambda/latest/api/API_ListShards.html)
+ [kinesis:SubscribeToShard](https://docs.aws.amazon.com/lambda/latest/api/API_SubscribeToShard.html)

The AWS managed policy [AWSLambdaKinesisExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaKinesisExecutionRole.html) includes these permissions. Add this managed policy to your function as described in the following procedure.

**Note**  
You don't need the `kinesis:ListStreams` permission to create and manage event source mappings for Kinesis. However, if you create an event source mapping in the console and you don't have this permission, you won't be able to select a Kinesis stream from a dropdown list and the console will display an error. To create the event source mapping, you'll need to manually enter the Amazon Resource Name (ARN) of your stream.
Lambda makes `kinesis:GetRecords` and `kinesis:GetShardIterator` API calls when retrying failed invocations.

------
#### [ AWS Management Console ]

**To add Kinesis permissions to your function**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console and select your function.

1. In the **Configuration** tab, select **Permissions**.

1. In the **Execution role** pane, under **Role name**, choose the link to your function’s execution role. This link opens the page for that role in the IAM console.

1. In the **Permissions policies** pane, choose **Add permissions**, then select **Attach policies**.

1. In the search field, enter **AWSLambdaKinesisExecutionRole**.

1. Select the checkbox next to the policy and choose **Add permission**.

------
#### [ AWS CLI ]

**To add Kinesis permissions to your function**
+ Run the following CLI command to add the `AWSLambdaKinesisExecutionRole` policy to your function’s execution role:

  ```
  aws iam attach-role-policy \
  --role-name {{MyFunctionRole}} \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaKinesisExecutionRole
  ```

------
#### [ AWS SAM ]

**To add Kinesis permissions to your function**
+ In your function’s definition, add the `Policies` property as shown in the following example:

  ```
  Resources:
    MyFunction:
      Type: AWS::Serverless::Function
      Properties:
        CodeUri: ./my-function/
        Handler: index.handler
        Runtime: nodejs24.x
        Policies:
          - AWSLambdaKinesisExecutionRole
  ```

------

After configuring the required permissions, create the event source mapping.

------
#### [ AWS Management Console ]

**To create the Kinesis event source mapping**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console and select your function.

1. In the **Function overview** pane, choose **Add trigger**.

1. Under **Trigger configuration**, for the source, select **Kinesis**.

1. Select the Kinesis stream you want to create the event source mapping for and, optionally, a consumer of your stream.

1. (Optional) edit the **Batch size**, **Starting position**, and **Batch window** for your event source mapping.

1. Choose **Add**.

When creating your event source mapping from the console, your IAM role must have the [kinesis:ListStreams](https://docs.aws.amazon.com/lambda/latest/api/API_ListStreams.html) and [kinesis:ListStreamConsumers](https://docs.aws.amazon.com/lambda/latest/api/API_ListStreamConsumers.html) permissions.

------
#### [ AWS CLI ]

**To create the Kinesis event source mapping**
+ Run the following CLI command to create a Kinesis event source mapping. Choose your own batch size and starting position according to your use case.

  ```
  aws lambda create-event-source-mapping \
  --function-name {{MyFunction}} \
  --event-source-arn {{arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream}} \
  --starting-position {{LATEST}} \
  --batch-size {{100}}
  ```

To specify a batching window, add the `--maximum-batching-window-in-seconds` option. For more information about using this and other parameters, see [create-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html) in the *AWS CLI Command Reference*.

------
#### [ AWS SAM ]

**To create the Kinesis event source mapping**
+ In your function’s definition, add the `KinesisEvent` property as shown in the following example:

  ```
  Resources:
    MyFunction:
      Type: AWS::Serverless::Function
      Properties:
        CodeUri: ./my-function/
        Handler: index.handler
        Runtime: nodejs24.x
        Policies:
          - AWSLambdaKinesisExecutionRole
        Events:
          KinesisEvent:
            Type: Kinesis
            Properties:
              Stream: !GetAtt MyKinesisStream.Arn
              StartingPosition: LATEST
              BatchSize: 100
  
    MyKinesisStream:
      Type: AWS::Kinesis::Stream
      Properties:
        ShardCount: 1
  ```

To learn more about creating an event source mapping for Kinesis Data Streams in AWS SAM, see [Kinesis](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-kinesis.html) in the *AWS Serverless Application Model Developer Guide*.

------

## Polling and stream starting position
<a name="services-kinesis-stream-start-pos"></a>

Be aware that stream polling during event source mapping creation and updates is eventually consistent.
+ During event source mapping creation, it may take several minutes to start polling events from the stream.
+ During event source mapping updates, it may take several minutes to stop and restart polling events from the stream.

This behavior means that if you specify `LATEST` as the starting position for the stream, the event source mapping could miss events during creation or updates. To ensure that no events are missed, specify the stream starting position as `TRIM_HORIZON` or `AT_TIMESTAMP`.

## Creating a cross-account event source mapping
<a name="services-kinesis-eventsourcemapping-cross-account"></a>

Amazon Kinesis Data Streams supports [resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html). Because of this, you can process data ingested into a stream in one AWS account with a Lambda function in another account.

To create an event source mapping for your Lambda function using a Kinesis stream in a different AWS account, you must configure the stream using a resource-based policy to give your Lambda function permission to read items. To learn how to configure your stream to allow cross-account access, see [Sharing access with cross-account AWS Lambda functions](https://docs.aws.amazon.com/streams/latest/dev/resource-based-policy-examples.html#Resource-based-policy-examples-lambda) in the *Amazon Kinesis Streams Developer guide*.

Once you’ve configured your stream with a resource-based policy that gives your Lambda function the required permissions, create the event source mapping using any of the methods described in the previous section.

If you choose to create your event source mapping using the Lambda console, paste the ARN of your stream directly into the input field. If you want to specify a consumer for your stream, pasting the ARN of the consumer automatically populates the stream field.