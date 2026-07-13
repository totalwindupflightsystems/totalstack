---
id: "@specs/aws/lambda/docs/services-dynamodb-eventsourcemapping"
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
> **spec:id:** @specs/aws/lambda/docs/services-dynamodb-eventsourcemapping
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Process DynamoDB records with Lambda
<a name="services-dynamodb-eventsourcemapping"></a>

Create an event source mapping to tell Lambda to send records from your stream to a Lambda function. You can create multiple event source mappings to process the same data with multiple Lambda functions, or to process items from multiple streams with a single function.

You can configure event source mappings to process records from a stream in a different AWS account. To learn more, see [Creating a cross-account event source mapping](#services-dynamodb-eventsourcemapping-cross-account).

To configure your function to read from DynamoDB Streams, attach the [AWSLambdaDynamoDBExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaDynamoDBExecutionRole.html) AWS managed policy to your execution role and then create a **DynamoDB** trigger.

**To add permissions and create a trigger**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of a function.

1. Choose the **Configuration** tab, and then choose **Permissions**.

1. Under **Role name**, choose the link to your execution role. This link opens the role in the IAM console.  
![Link to execution role](http://docs.aws.amazon.com/lambda/latest/dg/images/execution-role.png)

1. Choose **Add permissions**, and then choose **Attach policies**.  
![Attach policies in IAM console](http://docs.aws.amazon.com/lambda/latest/dg/images/attach-policies.png)

1. In the search field, enter `AWSLambdaDynamoDBExecutionRole`. Add this policy to your execution role. This is an AWS managed policy that contains the permissions your function needs to read from the DynamoDB stream. For more information about this policy, see [AWSLambdaDynamoDBExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaDynamoDBExecutionRole.html) in the *AWS Managed Policy Reference*.

1. Go back to your function in the Lambda console. Under **Function overview**, choose **Add trigger**.  
![Function overview section of the Lambda console](http://docs.aws.amazon.com/lambda/latest/dg/images/add-trigger.png)

1. Choose a trigger type.

1. Configure the required options, and then choose **Add**.

Lambda supports the following options for DynamoDB event sources:

**Event source options**
+ **DynamoDB table** – The DynamoDB table to read records from.
+ **Batch size** – The number of records to send to the function in each batch, up to 10,000. Lambda passes all of the records in the batch to the function in a single call, as long as the total size of the events doesn't exceed the [payload limit](gettingstarted-limits.md) for synchronous invocation (6 MB).
+ **Batch window** – Specify the maximum amount of time to gather records before invoking the function, in seconds.
+ **Starting position** – Process only new records, or all existing records.
  + **Latest** – Process new records that are added to the stream.
  + **Trim horizon** – Process all records in the stream.

  After processing any existing records, the function is caught up and continues to process new records.
+ **On-failure destination** – A standard SQS queue or standard SNS topic for records that can't be processed. When Lambda discards a batch of records that's too old or has exhausted all retries, Lambda sends details about the batch to the queue or topic.
+ **Retry attempts** – The maximum number of times that Lambda retries when the function returns an error. This doesn't apply to service errors or throttles where the batch didn't reach the function.
+ **Maximum age of record** – The maximum age of a record that Lambda sends to your function.
+ **Split batch on error** – When the function returns an error, split the batch into two before retrying. Your original batch size setting remains unchanged.
+ **Concurrent batches per shard** – Concurrently process multiple batches from the same shard.
+ **Enabled** – Set to true to enable the event source mapping. Set to false to stop processing records. Lambda keeps track of the last record processed and resumes processing from that point when the mapping is reenabled.

**Note**  
You are not charged for GetRecords API calls invoked by Lambda as part of DynamoDB triggers.

To manage the event source configuration later, choose the trigger in the designer.

## Creating a cross-account event source mapping
<a name="services-dynamodb-eventsourcemapping-cross-account"></a>

Amazon DynamoDB now supports [resource-based policies](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-resource-based.html). With this capability, you can process data from a DynamoDB stream in one AWS account with a Lambda function in another account.

To create an event source mapping for your Lambda function using a DynamoDB stream in a different AWS account, you must configure the stream using a resource-based policy to give your Lambda function permission to read records. To learn how to configure your stream for cross-account access, see [Share access with cross-account Lambda functions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-cross-account-access.html#rbac-analyze-cross-account-lambda-access) in the *Amazon DynamoDB Developer Guide*.

Once you have configured your stream with a resource-based policy that gives your Lambda function the required permissions, create the event source mapping with your cross-account stream ARN. You can find the stream ARN under the table's **Exports and streams** tab in the cross-account DynamoDB console. 

When using the Lambda console, paste the stream ARN directly into the DynamoDB table input field in the event source mapping creation page.

 **Note:** Cross-region triggers are not supported. 