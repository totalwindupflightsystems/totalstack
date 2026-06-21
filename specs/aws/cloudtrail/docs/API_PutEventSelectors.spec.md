---
id: "@specs/aws/cloudtrail/docs/API_PutEventSelectors"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutEventSelectors"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# PutEventSelectors

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_PutEventSelectors
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutEventSelectors
<a name="API_PutEventSelectors"></a>

Configures event selectors (also referred to as *basic event selectors*) or advanced event selectors for your trail. You can use either `AdvancedEventSelectors` or `EventSelectors`, but not both. If you apply `AdvancedEventSelectors` to a trail, any existing `EventSelectors` are overwritten.

You can use `AdvancedEventSelectors` to log management events, data events for all resource types, and network activity events.

You can use `EventSelectors` to log management events and data events for the following resource types:
+  `AWS::DynamoDB::Table` 
+  `AWS::Lambda::Function` 
+  `AWS::S3::Object` 

You can't use `EventSelectors` to log network activity events.

If you want your trail to log Insights events, be sure the event selector or advanced event selector enables logging of the Insights event types you want configured for your trail. For more information about logging Insights events, see [Working with CloudTrail Insights](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html) in the *CloudTrail User Guide*. By default, trails created without specific event selectors are configured to log all read and write management events, and no data events or network activity events.

When an event occurs in your account, CloudTrail evaluates the event selectors or advanced event selectors in all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn't match any event selector, the trail doesn't log the event.

Example

1. You create an event selector for a trail and specify that you want to log write-only events.

1. The EC2 `GetConsoleOutput` and `RunInstances` API operations occur in your account.

1. CloudTrail evaluates whether the events match your event selectors.

1. The `RunInstances` is a write-only event and it matches your event selector. The trail logs the event.

1. The `GetConsoleOutput` is a read-only event that doesn't match your event selector. The trail doesn't log the event. 

The `PutEventSelectors` operation must be called from the Region in which the trail was created; otherwise, an `InvalidHomeRegionException` exception is thrown.

You can configure up to five event selectors for each trail.

You can add advanced event selectors, and conditions for your advanced event selectors, up to a maximum of 500 values for all conditions and selectors on a trail. For more information, see [Logging management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html), [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html), [Logging network activity events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html), and [Quotas in AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html) in the * AWS CloudTrail User Guide*.

## Request Syntax
<a name="API_PutEventSelectors_RequestSyntax"></a>

```
{
   "AdvancedEventSelectors": [ 
      { 
         "FieldSelectors": [ 
            { 
               "EndsWith": [ "{{string}}" ],
               "Equals": [ "{{string}}" ],
               "Field": "{{string}}",
               "NotEndsWith": [ "{{string}}" ],
               "NotEquals": [ "{{string}}" ],
               "NotStartsWith": [ "{{string}}" ],
               "StartsWith": [ "{{string}}" ]
            }
         ],
         "Name": "{{string}}"
      }
   ],
   "EventSelectors": [ 
      { 
         "DataResources": [ 
            { 
               "Type": "{{string}}",
               "Values": [ "{{string}}" ]
            }
         ],
         "ExcludeManagementEventSources": [ "{{string}}" ],
         "IncludeManagementEvents": {{boolean}},
         "ReadWriteType": "{{string}}"
      }
   ],
   "TrailName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutEventSelectors_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AdvancedEventSelectors](#API_PutEventSelectors_RequestSyntax) **   <a name="awscloudtrail-PutEventSelectors-request-AdvancedEventSelectors"></a>
 Specifies the settings for advanced event selectors. You can use advanced event selectors to log management events, data events for all resource types, and network activity events.  
You can add advanced event selectors, and conditions for your advanced event selectors, up to a maximum of 500 values for all conditions and selectors on a trail. You can use either `AdvancedEventSelectors` or `EventSelectors`, but not both. If you apply `AdvancedEventSelectors` to a trail, any existing `EventSelectors` are overwritten. For more information about advanced event selectors, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) and [Logging network activity events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html) in the * AWS CloudTrail User Guide*.   
Type: Array of [AdvancedEventSelector](API_AdvancedEventSelector.md) objects  
Required: No

 ** [EventSelectors](#API_PutEventSelectors_RequestSyntax) **   <a name="awscloudtrail-PutEventSelectors-request-EventSelectors"></a>
Specifies the settings for your event selectors. You can use event selectors to log management events and data events for the following resource types:  
+  `AWS::DynamoDB::Table` 
+  `AWS::Lambda::Function` 
+  `AWS::S3::Object` 
You can't use event selectors to log network activity events.  
You can configure up to five event selectors for a trail. You can use either `EventSelectors` or `AdvancedEventSelectors` in a `PutEventSelectors` request, but not both. If you apply `EventSelectors` to a trail, any existing `AdvancedEventSelectors` are overwritten.  
Type: Array of [EventSelector](API_EventSelector.md) objects  
Required: No

 ** [TrailName](#API_PutEventSelectors_RequestSyntax) **   <a name="awscloudtrail-PutEventSelectors-request-TrailName"></a>
Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:  
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (\_), or dashes (-)
+ Start with a letter or number, and end with a letter or number
+ Be between 3 and 128 characters
+ Have no adjacent periods, underscores or dashes. Names like `my-_namespace` and `my--namespace` are not valid.
+ Not be in IP address format (for example, 192.168.5.4)
If you specify a trail ARN, it must be in the following format.  
 `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`   
Type: String  
Required: Yes

## Response Syntax
<a name="API_PutEventSelectors_ResponseSyntax"></a>

```
{
   "AdvancedEventSelectors": [ 
      { 
         "FieldSelectors": [ 
            { 
               "EndsWith": [ "string" ],
               "Equals": [ "string" ],
               "Field": "string",
               "NotEndsWith": [ "string" ],
               "NotEquals": [ "string" ],
               "NotStartsWith": [ "string" ],
               "StartsWith": [ "string" ]
            }
         ],
         "Name": "string"
      }
   ],
   "EventSelectors": [ 
      { 
         "DataResources": [ 
            { 
               "Type": "string",
               "Values": [ "string" ]
            }
         ],
         "ExcludeManagementEventSources": [ "string" ],
         "IncludeManagementEvents": boolean,
         "ReadWriteType": "string"
      }
   ],
   "TrailARN": "string"
}
```

## Response Elements
<a name="API_PutEventSelectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdvancedEventSelectors](#API_PutEventSelectors_ResponseSyntax) **   <a name="awscloudtrail-PutEventSelectors-response-AdvancedEventSelectors"></a>
Specifies the advanced event selectors configured for your trail.  
Type: Array of [AdvancedEventSelector](API_AdvancedEventSelector.md) objects

 ** [EventSelectors](#API_PutEventSelectors_ResponseSyntax) **   <a name="awscloudtrail-PutEventSelectors-response-EventSelectors"></a>
Specifies the event selectors configured for your trail.  
Type: Array of [EventSelector](API_EventSelector.md) objects

 ** [TrailARN](#API_PutEventSelectors_ResponseSyntax) **   <a name="awscloudtrail-PutEventSelectors-response-TrailARN"></a>
Specifies the ARN of the trail that was updated with event selectors. The following is the format of a trail ARN.  
 `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`   
Type: String

## Errors
<a name="API_PutEventSelectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CloudTrailARNInvalidException **   
This exception is thrown when an operation is called with an ARN that is not valid.  
The following is the format of a trail ARN: `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`   
The following is the format of an event data store ARN: `arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`   
The following is the format of a dashboard ARN: `arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash`   
The following is the format of a channel ARN: `arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890`   
HTTP Status Code: 400

 ** ConflictException **   
This exception is thrown when the specified resource is not ready for an operation. This can occur when you try to run an operation on a resource before CloudTrail has time to fully load the resource, or because another operation is modifying the resource. If this exception occurs, wait a few minutes, and then try the operation again.  
HTTP Status Code: 400

 ** InsufficientDependencyServiceAccessPermissionException **   
This exception is thrown when the IAM identity that is used to create the organization resource lacks one or more required permissions for creating an organization resource in a required service.  
HTTP Status Code: 400

 ** InvalidEventSelectorsException **   
This exception is thrown when the `PutEventSelectors` operation is called with a number of event selectors, advanced event selectors, or data resources that is not valid. The combination of event selectors or advanced event selectors and data resources is not valid. A trail can have up to 5 event selectors. If a trail uses advanced event selectors, a maximum of 500 total values for all conditions in all advanced event selectors is allowed. A trail is limited to 250 data resources. These data resources can be distributed across event selectors, but the overall total cannot exceed 250.  
You can:  
+ Specify a valid number of event selectors (1 to 5) for a trail.
+ Specify a valid number of data resources (1 to 250) for an event selector. The limit of number of resources on an individual event selector is configurable up to 250. However, this upper limit is allowed only if the total number of data resources does not exceed 250 across all event selectors for a trail.
+ Specify up to 500 values for all conditions in all advanced event selectors for a trail.
+ Specify a valid value for a parameter. For example, specifying the `ReadWriteType` parameter with a value of `read-only` is not valid.
HTTP Status Code: 400

 ** InvalidHomeRegionException **   
This exception is thrown when an operation is called on a trail from a Region other than the Region in which the trail was created.  
HTTP Status Code: 400

 ** InvalidTrailNameException **   
This exception is thrown when the provided trail name is not valid. Trail names must meet the following requirements:  
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (\_), or dashes (-)
+ Start with a letter or number, and end with a letter or number
+ Be between 3 and 128 characters
+ Have no adjacent periods, underscores or dashes. Names like `my-_namespace` and `my--namespace` are not valid.
+ Not be in IP address format (for example, 192.168.5.4)
HTTP Status Code: 400

 ** NoManagementAccountSLRExistsException **   
 This exception is thrown when the management account does not have a service-linked role.   
HTTP Status Code: 400

 ** NotOrganizationMasterAccountException **   
This exception is thrown when the AWS account making the request to create or update an organization trail or event data store is not the management account for an organization in AWS Organizations. For more information, see [Prepare For Creating a Trail For Your Organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.html) or [Organization event data stores](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-organizations.html).  
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** ThrottlingException **   
 This exception is thrown when the request rate exceeds the limit.   
HTTP Status Code: 400

 ** TrailNotFoundException **   
This exception is thrown when the trail with the given name is not found.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## Examples
<a name="API_PutEventSelectors_Examples"></a>

### Example
<a name="API_PutEventSelectors_Example_1"></a>

The following example shows how to use advanced event selectors to log all management events (both readOnly and writeOnly), include `PutObject` and `DeleteObject` data events for the S3 objects in two S3 bucket prefixes, and log network activity events for AWS KMS. As shown here, you can use advanced event selectors to select not only the S3 prefix names by ARN, but the names of the specific events that you want to log.

```
{
   "AdvancedEventSelectors": [ 
      {
         "Name": "Log all management events",
         "FieldSelectors": [
            { "Field": "eventCategory", "Equals": ["Management"] }
          ]
      },
      {
         "Name": "Log PutObject and DeleteObject data events for two S3 prefixes",
         "FieldSelectors": [
            { "Field": "eventCategory", "Equals": ["Data"] },
            { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
            { "Field": "eventName", "Equals": ["PutObject","DeleteObject"] },
            { "Field": "resources.ARN", "StartsWith": ["arn:aws:s3:::amzn-s3-demo-bucket/prefix","arn:aws:s3:::amzn-s3-demo-bucket2/prefix2"] }
         ]
         
      },
      {
         "Name": "Log network activity events for AWS KMS",
         "FieldSelectors": [
            {"Field": "eventCategory", "Equals": ["NetworkActivity"]},
            {"Field": "eventSource", "Equals": ["kms.amazonaws.com"]}
         ]
      }
   ],
   "TrailName": "myTrail"
}
```

### Example
<a name="API_PutEventSelectors_Example_2"></a>

The following example shows how to use advanced event selectors to log all data events for Amazon SNS topics and platform endpoints, and to log only `SendMessage` data events for Amazon SQS.

```
{
   "AdvancedEventSelectors": [ 
      {
         "Name": "Log all data events for Amazon SNS topics",
         "FieldSelectors": [
            { "Field": "eventCategory", "Equals": ["Data"] },
            { "Field": "resources.type", "Equals": ["AWS::SNS::Topic"] }
         ]
      },
      {
         "Name": "Log all data events for Amazon SNS platform endpoints",
         "FieldSelectors": [
            { "Field": "eventCategory", "Equals": ["Data"] },
            { "Field": "resources.type", "Equals": ["AWS::SNS::PlatformEndpoint"] }
         ]  
      },
      {
         "Name": "Log SendMessage data events for SQS",
         "FieldSelectors": [
            { "Field": "eventCategory", "Equals": ["Data"] },
            { "Field": "resources.type", "Equals": ["AWS::SQS::Queue"] },
            { "Field": "eventName", "Equals": ["SendMessage"] }
         ]  
      }
   ],
   "TrailName": "myTrail"
}
```

## See Also
<a name="API_PutEventSelectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/PutEventSelectors) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/PutEventSelectors) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/PutEventSelectors) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/PutEventSelectors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/PutEventSelectors) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/PutEventSelectors) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/PutEventSelectors) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/PutEventSelectors) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/PutEventSelectors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/PutEventSelectors) 