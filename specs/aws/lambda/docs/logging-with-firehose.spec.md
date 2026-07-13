---
id: "@specs/aws/lambda/docs/logging-with-firehose"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Log with Firehose"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Log with Firehose

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/logging-with-firehose
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Sending Lambda function logs to Firehose
<a name="logging-with-firehose"></a>

The Lambda console now offers the option to send function logs to Firehose. This enables real-time streaming of your logs to various destinations supported by Firehose, including third-party analytics tools and custom endpoints.

**Note**  
You can configure Lambda function logs to be sent to Firehose using the Lambda console, AWS CLI, AWS CloudFormation, and all AWS SDKs.

## Pricing
<a name="logging-firehose-pricing"></a>

For details on pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs).

## Required permissions for Firehose log destination
<a name="logging-firehose-permissions"></a>

When using the Lambda console to configure Firehose as your function's log destination, you need:

1. The [required IAM permissions](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-prereqs) to use CloudWatch Logs with Lambda.

1. To [set up subscription filters with Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html#FirehoseExample). This filter defines which log events are delivered to your Firehose stream.

## Sending Lambda function logs to Firehose
<a name="logging-firehose-setup"></a>

In the Lambda console, you can send function logs directly to Firehose after creating a new function. To do this, complete these steps:

1. Sign in to the AWS Management Console and open the Lambda console.

1. Choose your function's name.

1. Choose the **Configuration** tab.

1. Choose the **Monitoring and operations tools** tab.

1. In the "Logging configuration" section, choose **Edit**.

1. In the "Log content" section, select a log format.

1. In the "Log destination" section, complete the following steps:

   1. Select a destination service.

   1. Choose to **Create a new log group** or use an **Existing log group**.
**Note**  
If choosing an existing log group for a Firehose destination, ensure the log group you choose is a `Delivery` log group type.

   1. Choose a Firehose stream.

   1. The CloudWatch `Delivery` log group will appear.

1. Choose **Save**.

**Note**  
If the IAM role provided in the console doesn't have the required permission, then the destination setup will fail. To fix this, refer to Required permissions for Firehose log destination to provide the required permissions.

## Cross-Account Logging
<a name="cross-account-logging-firehose"></a>

You can configure Lambda to send logs to Firehose delivery stream in a different AWS account. This requires setting up a destination and configuring appropriate permissions in both accounts.

For detailed instructions on setting up cross-account logging, including required IAM roles and policies, see [Setting up a new cross-account subscription](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CrossAccountSubscriptions.html) in the CloudWatch Logs documentation.