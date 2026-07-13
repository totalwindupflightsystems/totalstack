---
id: "@specs/aws/lambda/docs/services-sqs-configure"
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
> **spec:id:** @specs/aws/lambda/docs/services-sqs-configure
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating and configuring an Amazon SQS event source mapping
<a name="services-sqs-configure"></a>

To process Amazon SQS messages with Lambda, configure your queue with the appropriate settings, then create a Lambda event source mapping.

**Topics**
+ [Configuring a queue to use with Lambda](#events-sqs-queueconfig)
+ [Setting up Lambda execution role permissions](#events-sqs-permissions)
+ [Creating an SQS event source mapping](#events-sqs-eventsource)

## Configuring a queue to use with Lambda
<a name="events-sqs-queueconfig"></a>

If you don't already have an existing Amazon SQS queue, [create one](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.html) to serve as an event source for your Lambda function. The Lambda function and the Amazon SQS queue must be in the same AWS Region, although they can be in [different AWS accounts](with-sqs-cross-account-example.md).

To allow your function time to process each batch of records, set the source queue's [ visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) to at least six times the [configuration timeout](configuration-timeout.md) on your function. The extra time allows Lambda to retry if your function is throttled while processing a previous batch.

**Note**  
Your function's timeout must be less than or equal to the queue's visibility timeout. Lambda validates this requirement when you create or update an event source mapping and will return an error if the function timeout exceeds the queue's visibility timeout.

By default, if Lambda encounters an error at any point while processing a batch, all messages in that batch return to the queue. After the [ visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html), the messages become visible to Lambda again. You can configure your event source mapping to use [ partial batch responses](services-sqs-errorhandling.md#services-sqs-batchfailurereporting) to return only the failed messages back to the queue. In addition, if your function fails to process a message multiple times, Amazon SQS can send it to a [ dead-letter queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html). We recommend setting the `maxReceiveCount` on your source queue's [ redrive policy](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html#policies-for-dead-letter-queues) to at least 5. This gives Lambda a few chances to retry before sending failed messages directly to the dead-letter queue.

## Setting up Lambda execution role permissions
<a name="events-sqs-permissions"></a>

The [ AWSLambdaSQSQueueExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaSQSQueueExecutionRole.html) AWS managed policy includes the permissions that Lambda needs to read from your Amazon SQS queue. You can add this managed policy to your function's [execution role](lambda-intro-execution-role.md).

Optionally, if you're using an encrypted queue, you also need to add the following permission to your execution role:
+ [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html)

## Creating an SQS event source mapping
<a name="events-sqs-eventsource"></a>

Create an event source mapping to tell Lambda to send items from your queue to a Lambda function. You can create multiple event source mappings to process items from multiple queues with a single function. When Lambda invokes the target function, the event can contain multiple items, up to a configurable maximum *batch size*.

To configure your function to read from Amazon SQS, attach the [ AWSLambdaSQSQueueExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaSQSQueueExecutionRole.html) AWS managed policy to your execution role. Then, create an **SQS** event source mapping from the console using the following steps.

**To add permissions and create a trigger**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of a function.

1. Choose the **Configuration** tab, and then choose **Permissions**.

1. Under **Role name**, choose the link to your execution role. This link opens the role in the IAM console.  
![Link to execution role](http://docs.aws.amazon.com/lambda/latest/dg/images/execution-role.png)

1. Choose **Add permissions**, and then choose **Attach policies**.  
![Attach policies in IAM console](http://docs.aws.amazon.com/lambda/latest/dg/images/attach-policies.png)

1. In the search field, enter `AWSLambdaSQSQueueExecutionRole`. Add this policy to your execution role. This is an AWS managed policy that contains the permissions your function needs to read from an Amazon SQS queue. For more information about this policy, see [ AWSLambdaSQSQueueExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaSQSQueueExecutionRole.html) in the *AWS Managed Policy Reference*.

1. Go back to your function in the Lambda console. Under **Function overview**, choose **Add trigger**.  
![Function overview section of the Lambda console](http://docs.aws.amazon.com/lambda/latest/dg/images/add-trigger.png)

1. Choose a trigger type.

1. Configure the required options, and then choose **Add**.

Lambda supports the following configuration options for Amazon SQS event sources:

**SQS queue**  
The Amazon SQS queue to read records from. The Lambda function and the Amazon SQS queue must be in the same AWS Region, although they can be in [different AWS accounts](with-sqs-cross-account-example.md).

**Enable trigger**  
The status of the event source mapping. **Enable trigger** is selected by default.

**Batch size**  
The maximum number of records to send to the function in each batch. For a standard queue, this can be up to 10,000 records. For a FIFO queue, the maximum is 10. For a batch size over 10, you must also set the batch window (`MaximumBatchingWindowInSeconds`) to at least 1 second.  
Configure your [ function timeout](https://serverlessland.com/content/service/lambda/guides/aws-lambda-operator-guide/configurations#timeouts) to allow enough time to process an entire batch of items. If items take a long time to process, choose a smaller batch size. A large batch size can improve efficiency for workloads that are very fast or have a lot of overhead. If you configure [reserved concurrency](configuration-concurrency.md) on your function, set a minimum of five concurrent executions to reduce the chance of throttling errors when Lambda invokes your function.  
Lambda passes all of the records in the batch to the function in a single call, as long as the total size of the events doesn't exceed the [ invocation payload size quota](gettingstarted-limits.md) for synchronous invocation (6 MB). Both Lambda and Amazon SQS generate metadata for each record. This additional metadata is counted towards the total payload size and can cause the total number of records sent in a batch to be lower than your configured batch size. The metadata fields that Amazon SQS sends can be variable in length. For more information about the Amazon SQS metadata fields, see the [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) API operation documentation in the *Amazon Simple Queue Service API Reference*.

**Batch window**  
The maximum amount of time to gather records before invoking the function, in seconds. This applies only to standard queues.  
If you're using a batch window greater than 0 seconds, you must account for the increased processing time in your queue's [ visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html). We recommend setting your queue's visibility timeout to six times your [function timeout](configuration-timeout.md), plus the value of `MaximumBatchingWindowInSeconds`. This allows time for your Lambda function to process each batch of events and to retry in the event of a throttling error.  
When messages become available, Lambda starts processing messages in batches. Lambda starts processing five batches at a time with five concurrent invocations of your function. If messages are still available, Lambda adds up to 300 concurrent invokes of your function a minute, up to a maximum of 1,250 concurrent invokes. When using provisioned mode, each event poller can handle up to 1 MB/s of throughput, up to 10 concurrent invokes, or up to 10 Amazon SQS polling API calls per second. Lambda scales the number of event pollers between your configured minimum and maximum, quickly adding up to 1,000 concurrent invokes per minute to provide low-latency processing of your Amazon SQS events. You control scaling and concurrency through these minimum and maximum event poller settings. To learn more about function scaling and concurrency, see [Understanding Lambda function scaling](lambda-concurrency.md).  
To process more messages, you can optimize your Lambda function for higher throughput. For more information, see [ Understanding how AWS Lambda scales with Amazon SQS standard queues](https://aws.amazon.com/blogs/compute/understanding-how-aws-lambda-scales-when-subscribed-to-amazon-sqs-queues/#:~:text=If there are more messages,messages from the SQS queue.).

**Filter criteria**  
Add filter criteria to control which events Lambda sends to your function for processing. For more information, see [Control which events Lambda sends to your function](invocation-eventfiltering.md).

**Maximum concurrency**  
The maximum number of concurrent functions that the event source can invoke. Cannot be used with Provisioned Mode enabled. For more information, see [Configuring maximum concurrency for Amazon SQS event sources](services-sqs-scaling.md#events-sqs-max-concurrency).

**Provisioned Mode**  
When enabled, allocates dedicated polling resources for your event source mapping. You can configure the minimum (2-200) and maximum (2-2000) number of event pollers. Each event poller can handle up to 1 MB/sec of throughput, up to 10 concurrent invokes, or up to 10 Amazon SQS polling API calls per second.  
Note: You cannot use Provisioned Mode and Maximum concurrency together. When Provisioned Mode is enabled, use the maximum pollers setting to control concurrency.