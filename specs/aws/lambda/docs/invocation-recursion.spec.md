---
id: "@specs/aws/lambda/docs/invocation-recursion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Recursive loop detection"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Recursive loop detection

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/invocation-recursion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Use Lambda recursive loop detection to prevent infinite loops
<a name="invocation-recursion"></a>

When you configure a Lambda function to output to the same service or resource that invokes the function, it's possible to create an infinite recursive loop. For example, a Lambda function might write a message to an Amazon Simple Queue Service (Amazon SQS) queue, which then invokes the same function. This invocation causes the function to write another message to the queue, which in turn invokes the function again.

Unintentional recursive loops can result in unexpected charges being billed to your AWS account. Loops can also cause Lambda to [scale](lambda-concurrency.md) and use all of your account's available concurrency. To help reduce the impact of unintentional loops, Lambda detects certain types of recursive loops shortly after they occur. By default, when Lambda detects a recursive loop, it stops your function being invoked and notifies you. If your design intentionally uses recursive patterns, you can a change a function's default configuration to allow it to be invoked recursively. See [Allowing a Lambda function to run in a recursive loop](#invocation-recursion-disable) for more information.

**Topics**
+ [Understanding recursive loop detection](#invocation-recursion-concepts)
+ [Supported AWS services and SDKs](#invocation-recursion-supported)
+ [Recursive loop notifications](#invocation-recursion-monitoring)
+ [Responding to recursive loop detection notifications](#invocation-recursion-responding)
+ [Allowing a Lambda function to run in a recursive loop](#invocation-recursion-disable)
+ [Supported Regions for Lambda recursive loop detection](#invocation-recursion-regions)

## Understanding recursive loop detection
<a name="invocation-recursion-concepts"></a>

Recursive loop detection in Lambda works by tracking events. Lambda is an event-driven compute service that runs your function code when certain events occur. For example, when an item is added to an Amazon SQS queue or Amazon Simple Notification Service (Amazon SNS) topic. Lambda passes events to your function as JSON objects, which contain information about the change in the system state. When an event causes your function to run, this is called an *invocation*.

To detect recursive loops, Lambda uses [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) tracing headers. When [AWS services that support recursive loop detection](#invocation-recursion-supportedservices) send events to Lambda, those events are automatically annotated with metadata. When your Lambda function writes one of these events to another supported AWS service using a [supported version of an AWS SDK](#invocation-recursion-supportedsdks), it updates this metadata. The updated metadata includes a count of the number of times that the event has invoked the function.

**Note**  
You don't need to enable X-Ray active tracing for this feature to work. Recursive loop detection is turned on by default for all AWS customers. There is no charge to use the feature.

A *chain of requests* is a sequence of Lambda invocations caused by the same triggering event. For example, imagine that an Amazon SQS queue invokes your Lambda function. Your Lambda function then sends the processed event back to the same Amazon SQS queue, which invokes your function again. In this example, each invocation of your function falls in the same chain of requests.

If your function is invoked approximately 16 times in the same chain of requests, then Lambda automatically stops the next function invocation in that request chain and notifies you. If your function is configured with multiple triggers, then invocations from other triggers aren't affected.

**Note**  
Even when the `maxReceiveCount` setting on the source queue's redrive policy is higher than 16, Lambda recursion protection does not prevent Amazon SQS from retrying the message after a recursive loop is detected and terminated. When Lambda detects a recursive loop and drops subsequent invocations, it returns a `RecursiveInvocationException` to the event source mapping. This increments the `receiveCount` value on the message. Lambda continues to retry the message, and continues to block function invocations, until Amazon SQS determines that the `maxReceiveCount` is exceeded and sends the message to the configured dead-letter queue.

If you have an [on-failure destination](invocation-async-retain-records.md#invocation-async-destinations) or [dead-letter queue](invocation-async-retain-records.md#invocation-dlq) configured for your function, then Lambda also sends the event from the stopped invocation to your destination or dead-letter queue. When configuring a destination or dead-letter queue for your function, be sure not to use an event trigger or event source mapping that your function also uses. If you send events to the same resource that invokes your function, then you can create another recursive loop and this loop will also be terminated. If you opt out of recursion loop detection, this loop will not be terminated.

## Supported AWS services and SDKs
<a name="invocation-recursion-supported"></a>

Lambda can detect only recursive loops that include certain supported AWS services. For recursive loops to be detected, your function must also use one of the supported AWS SDKs.

### Supported AWS services
<a name="invocation-recursion-supportedservices"></a>

Lambda currently detects recursive loops between your functions, Amazon SQS, Amazon S3, and Amazon SNS. Lambda also detects loops comprised only of Lambda functions, which may invoke each other synchronously or asynchronously. The following diagrams show some examples of loops that Lambda can detect:

![Diagrams of recursive loops between a Lambda function, Amazon SNS, Amazon S3, and an Amazon SQS queue.](http://docs.aws.amazon.com/lambda/latest/dg/images/RunawayWorkloadDetected_v3.png)


When another AWS service such as Amazon DynamoDB forms part of the loop, Lambda can't currently detect and stop it.

Because Lambda currently detects only recursive loops involving Amazon SQS, Amazon S3, and Amazon SNS, it's still possible that loops involving other AWS services can result in unintended usage of your Lambda functions.

To guard against unexpected charges being billed to your AWS account, we recommend that you configure [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) to alert you to unusual usage patterns. For example, you can configure CloudWatch to notify you about spikes in Lambda function concurrency or invocations. You can also configure a [billing alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html) to notify you when spending in your account exceeds a threshold that you specify. Or, you can use [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) to alert you to unusual billing patterns.

### Supported AWS SDKs
<a name="invocation-recursion-supportedsdks"></a>

For Lambda to detect recursive loops, your function must use one of the following SDK versions or higher:


| Runtime | Minimum required AWS SDK version | 
| --- | --- | 
| Node.js | 2.1147.0 (SDK version 2)<br />3.105.0 (SDK version 3) | 
| Python | 1.24.46 (boto3)<br />1.27.46 (botocore) | 
| Java 8 and Java 11 | 2.17.135 | 
| Java 17 | 2.20.81 | 
| Java 21 | 2.21.24 | 
| .NET | 3.7.293.0 | 
| Ruby | 3.134.0 | 
| PHP | 3.232.0 | 
| Go | V2 SDK 1.57.0 | 

Some Lambda runtimes such as Python and Node.js include a version of the AWS SDK. If the SDK version included in your function's runtime is lower than the minimum required, then you can add a supported version of the SDK to your function's deployment package. You can also add a supported SDK version to your function using a [Lambda layer](chapter-layers.md). For a list of the SDKs included with each Lambda runtime, see [Lambda runtimes](lambda-runtimes.md).

## Recursive loop notifications
<a name="invocation-recursion-monitoring"></a>

When Lambda stops a recursive loop, you receive notifications through the [Health Dashboard](https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/) and through email. You can also use CloudWatch metrics to monitor the number of recursive invocations that Lambda has stopped.

### Health Dashboard notifications
<a name="invocation-recursion-phd"></a>

When Lambda stops a recursive invocation, the Health Dashboard displays a notification on the **Your account health** page, under [Open and recent issues](https://health.aws.amazon.com/health/home#/account/dashboard/open-issues). Note that it can take up to 3.5 hours after Lambda stops a recursive invocation before this notification is displayed. For more information about viewing account events in the Health Dashboard, see [Getting started with your AWS Health Dashboard – Your account health](https://docs.aws.amazon.com/health/latest/ug/getting-started-health-dashboard.html) in the *AWS Health User Guide*.

### Email alerts
<a name="invocation-recursion-email"></a>

When Lambda first stops a recursive invocation of your function, it sends you an email alert. Lambda sends a maximum of one email every 24 hours for each function in your AWS account. After Lambda sends an email notification, you won't receive any more emails for that function for another 24 hours, even if Lambda stops further recursive invocations of the function. Note that it can take up to 3.5 hours after Lambda stops a recursive invocation before you receive this email alert.

Lambda sends recursive loop email alerts to your AWS account's primary account contact and alternate operations contact. For information about viewing or updating the email addresses in your account, see [Updating contact information](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html) in the *AWS General Reference*.

### Amazon CloudWatch metrics
<a name="invocation-recursion-cloudwatch"></a>

The [CloudWatch metric](monitoring-metrics-types.md) `RecursiveInvocationsDropped` records the number of function invocations that Lambda has stopped because your function has been invoked more than approximately 16 times in a single chain of requests. Lambda emits this metric as soon as it stops a recursive invocation. To view this metric, follow the instructions for [Viewing metrics on the CloudWatch console](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html#monitoring-metrics-console) and choose the metric `RecursiveInvocationsDropped`.

## Responding to recursive loop detection notifications
<a name="invocation-recursion-responding"></a>

When your function is invoked more than approximately 16 times by the same triggering event, Lambda stops the next function invocation for that event to break the recursive loop. To prevent a reoccurrence of a recursive loop that Lambda has broken, do the following: 
+ Reduce your function's available [concurrency](lambda-concurrency.md) to zero, which throttles all future invocations.
+ Remove or disable the trigger or event source mapping that's invoking your function.
+ Identify and fix code defects that write events back to the AWS resource that's invoking your function. A common source of defects occurs when you use variables to define a function's event source and target. Check that you're not using the same value for both variables.

Additionally, if the event source for your Lambda function is an Amazon SQS queue, then consider [configuring a dead-letter queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-dead-letter-queue.html) on the source queue.

**Note**  
Make sure that you configure the dead-letter queue on the source queue, not on the Lambda function. The dead-letter queue that you configure on a function is used for the function's [asynchronous invocation queue](invocation-async.md), not for event source queues.

If the event source is an Amazon SNS topic, then consider adding an [on-failure destination](invocation-async-retain-records.md#invocation-async-destinations) for your function.

**To reduce your function's available concurrency to zero (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of your function.

1. Choose **Throttle**.

1. In the **Throttle your function** dialog box, choose **Confirm**.

**To remove a trigger or event source mapping for your function (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of your function.

1. Choose the **Configuration** tab, then choose **Triggers**.

1. Under **Triggers**, select the trigger or event source mapping that you want to delete, then choose **Delete**.

1. In the **Delete triggers** dialog box, choose **Delete**.

**To disable an event source mapping for your function (AWS CLI)**

1. To find the UUID for the event source mapping that you want to disable, run the AWS Command Line Interface (AWS CLI) [list-event-source-mappings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-event-source-mappings.html) command.

   ```
   aws lambda list-event-source-mappings
   ```

1. To disable the event source mapping, run the following AWS CLI [update-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-event-source-mapping.html) command.

   ```
   aws lambda update-event-source-mapping --function-name {{MyFunction}} \
   --uuid {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} --no-enabled
   ```

## Allowing a Lambda function to run in a recursive loop
<a name="invocation-recursion-disable"></a>

If your design intentionally uses a recursive loop, you can configure a Lambda function to allow it to be invoked recursively. We recommend that you avoid using recursive loops in your design. Implementation errors can lead to recursive invocations using all of your AWS account's available concurrency and to unexpected charges being billed to your account.

**Important**  
If you use recursive loops, treat them with caution. Implement best practice guard rails to minimize the risks of implementation errors. To learn more about best practices for using recursive patterns, see [Recursive patterns that cause run-away Lambda functions](https://serverlessland.com/content/service/lambda/guides/aws-lambda-operator-guide/recursive-runaway) in Serverless Land.

You can configure functions to allow recursive loops using the Lambda console, the AWS Command Line Interface (AWS CLI), and the [PutFunctionRecursionConfig](https://docs.aws.amazon.com//lambda/latest/api/API_PutFunctionRecursionConfig.html) API. You can also configure a function's recursive loop detection setting in AWS SAM and CloudFormation. 

By default, Lambda detects and terminates recursive loops. Unless your design intentionally uses a recursive loop, we recommend that you don't change your functions' default configuration.

Note that when you configure a function to allow recursive loops, the [CloudWatch metric](monitoring-metrics-types.md#invocation-metrics) `RecursiveInvocationsDropped` isn't emitted.

------
#### [ Console ]

**To allow a function to run in a recursive loop (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of your function to open the function detail page.

1. Choose the **Configuration** tab, then choose **Concurrency and recursion detection**.

1. Beside **Recursive loop detection**, choose **Edit**.

1. Select **Allow recursive loops**.

1. Choose **Save**.

------
#### [ AWS CLI ]

You can use the [PutFunctionRecursionConfig](https://docs.aws.amazon.com/lambda/latest/api/API_PutFunctionRecursionConfig.html) API to allow your function to be invoked in a recursive loop. Specify `Allow` for the recursive loop parameter. For example, you can call this API with the `put-function-recursion-config` AWS CLI command:

```
aws lambda put-function-recursion-config --function-name {{yourFunctionName}} --recursive-loop Allow
```

------

You can change your function's configuration back to the default setting so that Lambda terminates recursive loops when it detects them. Edit your function's configuration using the Lambda console or the AWS CLI.

------
#### [ Console ]

**To configure a function so that recursive loops are terminated (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of your function to open the function detail page.

1. Choose the **Configuration** tab, then choose **Concurrency and recursion detection**.

1. Beside **Recursive loop detection**, choose **Edit**.

1. Select **Terminate recursive loops**.

1. Choose **Save**.

------
#### [ AWS CLI ]

You can use the [PutFunctionRecursionConfig](https://docs.aws.amazon.com/lambda/latest/api/API_PutFunctionRecursionConfig.html) API to configure your function so that Lambda terminates recursive loops when it detects them. Specify `Terminate` for the recursive loop parameter. For example, you can call this API with the `put-function-recursion-config` AWS CLI command:

```
aws lambda put-function-recursion-config --function-name {{yourFunctionName}} --recursive-loop Terminate
```

------

## Supported Regions for Lambda recursive loop detection
<a name="invocation-recursion-regions"></a>

Lambda recursive loop detection is supported in all [commercial Regions](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#region) except Mexico (Central) and Asia Pacific (New Zealand).