---
id: "@specs/aws/lambda/docs/logging-using-cloudtrail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CloudTrail logs"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# CloudTrail logs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/logging-using-cloudtrail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Logging AWS Lambda API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS Lambda is integrated with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures API calls for Lambda as events. The calls captured include calls from the Lambda console and code calls to the Lambda API operations. Using the information collected by CloudTrail, you can determine the request that was made to Lambda, the IP address from which the request was made, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root user or user credentials.
+ Whether the request was made on behalf of an IAM Identity Center user.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

CloudTrail is active in your AWS account when you create the account and you automatically have access to the CloudTrail **Event history**. The CloudTrail **Event history** provides a viewable, searchable, downloadable, and immutable record of the past 90 days of recorded management events in an AWS Region. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*. There are no CloudTrail charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a [CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) event data store.

**CloudTrail trails**  
A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) and [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) in the *AWS CloudTrail User Guide*.  
You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/).

**CloudTrail Lake event data stores**  
*CloudTrail Lake* lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [ Apache ORC](https://orc.apache.org/) format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into *event data stores*, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-concepts.html#adv-event-selectors). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) in the *AWS CloudTrail User Guide*.  
CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html#cloudtrail-lake-manage-costs-pricing-option) you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

## Lambda data events in CloudTrail
<a name="cloudtrail-data-events"></a>

[Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) provide information about the resource operations performed on or in a resource (for example, reading or writing to an Amazon S3 object). These are also known as data plane operations. Data events are often high-volume activities. By default, CloudTrail doesn’t log most data events, and the CloudTrail **Event history** doesn't record them.

One CloudTrail data event that is logged by default for supported services is `LambdaESMDisabled`. To learn more about using this event to help troubleshoot issues with Lambda event source mappings, see [Using CloudTrail to troubleshoot disabled Lambda event sources](#cloudtrail-ESM-troubleshooting).

Additional charges apply for data events. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

You can log data events for the `AWS::Lambda::Function` resource type by using the CloudTrail console, AWS CLI, or CloudTrail API operations. For more information about how to log data events, see [Logging data events with the AWS Management Console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-console) and [Logging data events with the AWS Command Line Interface](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-with-the-AWS-CLI) in the *AWS CloudTrail User Guide*.

The following table lists the Lambda resource type for which you can log data events. The **Data event type (console)** column shows the value to choose from the **Data event type** list on the CloudTrail console. The **resources.type value** column shows the `resources.type` value, which you would specify when configuring advanced event selectors using the AWS CLI or CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API calls logged to CloudTrail for the resource type. 


| Data event type (console) | resources.type value | Data APIs logged to CloudTrail | 
| --- | --- | --- | 
| Lambda |  AWS::Lambda::Function  | [Invoke](https://docs.aws.amazon.com/lambda/latest/api/API_Invoke.html) | 

You can configure advanced event selectors to filter on the `eventName`, `readOnly`, and `resources.ARN` fields to log only those events that are important to you. The following example is the JSON view of a data event configuration that logs events for a specific function only. For more information about these fields, see [https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html) in the *AWS CloudTrail API Reference*.

```
[
  {
    "name": "function-invokes",
    "fieldSelectors": [
      {
        "field": "eventCategory",
        "equals": [
          "Data"
        ]
      },
      {
        "field": "resources.type",
        "equals": [
          "AWS::Lambda::Function"
        ]
      },
      {
        "field": "resources.ARN",
        "equals": [
          "{{arn:aws:lambda:us-east-1:111122223333:function:hello-world}}"
        ]
      }
    ]
  }
]
```

## Lambda management events in CloudTrail
<a name="cloudtrail-management-events"></a>

[Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

Lambda supports logging the following actions as management events in CloudTrail log files.

**Note**  
In the CloudTrail log file, the `eventName` might include date and version information, but it is still referring to the same public API action. For example the, `GetFunction` action appears as `GetFunction20150331v2`. The following list specifies when the event name differs from the API action name.
+ [AddLayerVersionPermission](https://docs.aws.amazon.com/lambda/latest/api/API_AddLayerVersionPermission.html)
+ [AddPermission](https://docs.aws.amazon.com/lambda/latest/api/API_AddPermission.html) (event name: `AddPermission20150331v2`)
+ [CreateAlias](https://docs.aws.amazon.com/lambda/latest/api/API_CreateAlias.html) (event name: `CreateAlias20150331`)
+ [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html) (event name: `CreateEventSourceMapping20150331`)
+ [CreateFunction](https://docs.aws.amazon.com/lambda/latest/api/API_CreateFunction.html) (event name: `CreateFunction20150331`)

  (The `Environment` and `ZipFile` parameters are omitted from the CloudTrail logs for `CreateFunction`.)
+ [CreateFunctionUrlConfig](https://docs.aws.amazon.com/lambda/latest/api/API_CreateFunctionUrlConfig.html)
+ [DeleteAlias](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteAlias.html) (event name: `DeleteAlias20150331`)
+ [DeleteCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteCodeSigningConfig.html)
+ [DeleteEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteEventSourceMapping.html) (event name: `DeleteEventSourceMapping20150331`)
+ [DeleteFunction](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteFunction.html) (event name: `DeleteFunction20150331`)
+ [DeleteFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteFunctionConcurrency.html) (event name: `DeleteFunctionConcurrency20171031`)
+ [DeleteFunctionUrlConfig](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteFunctionUrlConfig.html)
+ [DeleteProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteProvisionedConcurrencyConfig.html)
+ [GetAlias](https://docs.aws.amazon.com/lambda/latest/api/API_GetAlias.html) (event name: `GetAlias20150331`)
+ [GetEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_GetEventSourceMapping.html)
+ [GetFunction](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunction.html)
+ [GetFunctionUrlConfig](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunctionUrlConfig.html)
+ [GetFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunctionConfiguration.html)
+ [GetLayerVersionPolicy](https://docs.aws.amazon.com/lambda/latest/api/API_GetLayerVersionPolicy.html)
+ [GetPolicy](https://docs.aws.amazon.com/lambda/latest/api/API_GetPolicy.html)
+ [ListEventSourceMappings](https://docs.aws.amazon.com/lambda/latest/api/API_ListEventSourceMappings.html)
+ [ListFunctions](https://docs.aws.amazon.com/lambda/latest/api/API_ListFunctions.html)
+ [ListFunctionUrlConfigs](https://docs.aws.amazon.com/lambda/latest/api/API_ListFunctionUrlConfigs.html)
+ [PublishLayerVersion](https://docs.aws.amazon.com/lambda/latest/api/API_PublishLayerVersion.html) (event name: `PublishLayerVersion20181031`)

  (The `ZipFile` parameter is omitted from the CloudTrail logs for `PublishLayerVersion`.)
+ [PublishVersion](https://docs.aws.amazon.com/lambda/latest/api/API_PublishVersion.html) (event name: `PublishVersion20150331`)
+ [PutFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/api/API_PutFunctionConcurrency.html) (event name: `PutFunctionConcurrency20171031`)
+ [PutFunctionCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/api/API_PutFunctionCodeSigningConfig.html)
+ [PutFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/api/API_PutFunctionEventInvokeConfig.html)
+ [PutProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/api/API_PutProvisionedConcurrencyConfig.html)
+ [PutRuntimeManagementConfig](https://docs.aws.amazon.com/lambda/latest/api/API_PutRuntimeManagementConfig.html)
+ [RemovePermission](https://docs.aws.amazon.com/lambda/latest/api/API_RemovePermission.html) (event name: `RemovePermission20150331v2`)
+ [TagResource](https://docs.aws.amazon.com/lambda/latest/api/API_TagResource.html) (event name: `TagResource20170331v2`)
+ [UntagResource](https://docs.aws.amazon.com/lambda/latest/api/API_UntagResource.html) (event name: `UntagResource20170331v2`)
+ [UpdateAlias](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateAlias.html) (event name: `UpdateAlias20150331`)
+ [UpdateCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateCodeSigningConfig.html) 
+ [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html) (event name: `UpdateEventSourceMapping20150331`)
+ [UpdateFunctionCode](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionCode.html) (event name: `UpdateFunctionCode20150331v2`)

  (The `ZipFile` parameter is omitted from the CloudTrail logs for `UpdateFunctionCode`.)
+ [UpdateFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionConfiguration.html) (event name: `UpdateFunctionConfiguration20150331v2`)

  (The `Environment` parameter is omitted from the CloudTrail logs for `UpdateFunctionConfiguration`.)
+ [UpdateFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionEventInvokeConfig.html)
+ [UpdateFunctionUrlConfig](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionUrlConfig.html)

## Using CloudTrail to troubleshoot disabled Lambda event sources
<a name="cloudtrail-ESM-troubleshooting"></a>

When you change the state of an event source mapping using the [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html) API action, the API call is logged as a management event in CloudTrail. Event source mappings can also transition directly to the `Disabled` state due to errors.

For the following services, Lambda publishes the `LambdaESMDisabled` data event to CloudTrail when your event source transitions to the Disabled state:
+ Amazon Simple Queue Service (Amazon SQS)
+ Amazon DynamoDB
+ Amazon Kinesis

Lambda doesn't support this event for any other event source mapping types.

To receive alerts when event source mappings for supported services transition to the `Disabled` state, set up an alarm in Amazon CloudWatch using the `LambdaESMDisabled` CloudTrail event. To learn more about setting up a CloudWatch alarm, see [Creating CloudWatch alarms for CloudTrail events: examples](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html).

The `serviceEventDetails` entity in the `LambdaESMDisabled` event message contains one of the following error codes.

**`RESOURCE_NOT_FOUND`**  
The resource specified in the request does not exist.

**`FUNCTION_NOT_FOUND`**  
The function attached to the event source does not exist.

**`REGION_NAME_NOT_VALID`**  
A Region name provided to the event source or function is invalid.

**`AUTHORIZATION_ERROR`**  
Permissions have not been set, or are misconfigured.

**`FUNCTION_IN_FAILED_STATE`**  
The function code does not compile, has encountered an unrecoverable exception, or a bad deployment has occurred.

## Lambda event examples
<a name="cloudtrail-event-examples"></a>

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows CloudTrail log entries for the `GetFunction` and `DeleteFunction` actions.

**Note**  
The `eventName` might include date and version information, such as `"GetFunction20150331"`, but it is still referring to the same public API. 

```
{
  "Records": [
    {
      "eventVersion": "1.03",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "A1B2C3D4E5F6G7EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/myUserName",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "myUserName"
      },
      "eventTime": "2015-03-18T19:03:36Z",
      "eventSource": "lambda.amazonaws.com",
      "eventName": "GetFunction",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "127.0.0.1",
      "userAgent": "Python-httplib2/0.8 (gzip)",
      "errorCode": "AccessDenied",
      "errorMessage": "User: arn:aws:iam::111122223333:user/myUserName is not authorized to perform: lambda:GetFunction on resource: arn:aws:lambda:us-west-2:111122223333:function:other-acct-function",
      "requestParameters": null,
      "responseElements": null,
      "requestID": "7aebcd0f-cda1-11e4-aaa2-e356da31e4ff",
      "eventID": "e92a3e85-8ecd-4d23-8074-843aabfe89bf",
      "eventType": "AwsApiCall",
      "recipientAccountId": "111122223333"
    },
    {
      "eventVersion": "1.03",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "A1B2C3D4E5F6G7EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/myUserName",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "myUserName"
      },
      "eventTime": "2015-03-18T19:04:42Z",
      "eventSource": "lambda.amazonaws.com",
      "eventName": "DeleteFunction20150331",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "127.0.0.1",
      "userAgent": "Python-httplib2/0.8 (gzip)",
      "requestParameters": {
        "functionName": "basic-node-task"
      },
      "responseElements": null,
      "requestID": "a2198ecc-cda1-11e4-aaa2-e356da31e4ff",
      "eventID": "20b84ce5-730f-482e-b2b2-e8fcc87ceb22",
      "eventType": "AwsApiCall",
      "recipientAccountId": "111122223333"
    }
  ]
}
```

For information about CloudTrail record contents, see [CloudTrail record contents](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html) in the *AWS CloudTrail User Guide*.