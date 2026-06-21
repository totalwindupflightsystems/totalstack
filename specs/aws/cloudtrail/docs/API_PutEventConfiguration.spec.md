---
id: "@specs/aws/cloudtrail/docs/API_PutEventConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutEventConfiguration"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# PutEventConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_PutEventConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutEventConfiguration
<a name="API_PutEventConfiguration"></a>

Updates the event configuration settings for the specified event data store or trail. This operation supports updating the maximum event size, adding or modifying context key selectors for event data store, and configuring aggregation settings for the trail.

## Request Syntax
<a name="API_PutEventConfiguration_RequestSyntax"></a>

```
{
   "AggregationConfigurations": [ 
      { 
         "EventCategory": "{{string}}",
         "Templates": [ "{{string}}" ]
      }
   ],
   "ContextKeySelectors": [ 
      { 
         "Equals": [ "{{string}}" ],
         "Type": "{{string}}"
      }
   ],
   "EventDataStore": "{{string}}",
   "MaxEventSize": "{{string}}",
   "TrailName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutEventConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AggregationConfigurations](#API_PutEventConfiguration_RequestSyntax) **   <a name="awscloudtrail-PutEventConfiguration-request-AggregationConfigurations"></a>
The list of aggregation configurations that you want to configure for the trail.  
Type: Array of [AggregationConfiguration](API_AggregationConfiguration.md) objects  
Array Members: Maximum number of 1 item.  
Required: No

 ** [ContextKeySelectors](#API_PutEventConfiguration_RequestSyntax) **   <a name="awscloudtrail-PutEventConfiguration-request-ContextKeySelectors"></a>
A list of context key selectors that will be included to provide enriched event data.  
Type: Array of [ContextKeySelector](API_ContextKeySelector.md) objects  
Array Members: Maximum number of 2 items.  
Required: No

 ** [EventDataStore](#API_PutEventConfiguration_RequestSyntax) **   <a name="awscloudtrail-PutEventConfiguration-request-EventDataStore"></a>
The Amazon Resource Name (ARN) or ID suffix of the ARN of the event data store for which event configuration settings are updated.  
Type: String  
Required: No

 ** [MaxEventSize](#API_PutEventConfiguration_RequestSyntax) **   <a name="awscloudtrail-PutEventConfiguration-request-MaxEventSize"></a>
The maximum allowed size for events to be stored in the specified event data store. If you are using context key selectors, MaxEventSize must be set to Large.  
Type: String  
Valid Values: `Standard | Large`   
Required: No

 ** [TrailName](#API_PutEventConfiguration_RequestSyntax) **   <a name="awscloudtrail-PutEventConfiguration-request-TrailName"></a>
The name of the trail for which you want to update event configuration settings.  
Type: String  
Required: No

## Response Syntax
<a name="API_PutEventConfiguration_ResponseSyntax"></a>

```
{
   "AggregationConfigurations": [ 
      { 
         "EventCategory": "string",
         "Templates": [ "string" ]
      }
   ],
   "ContextKeySelectors": [ 
      { 
         "Equals": [ "string" ],
         "Type": "string"
      }
   ],
   "EventDataStoreArn": "string",
   "MaxEventSize": "string",
   "TrailARN": "string"
}
```

## Response Elements
<a name="API_PutEventConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AggregationConfigurations](#API_PutEventConfiguration_ResponseSyntax) **   <a name="awscloudtrail-PutEventConfiguration-response-AggregationConfigurations"></a>
A list of aggregation configurations that are configured for the trail.  
Type: Array of [AggregationConfiguration](API_AggregationConfiguration.md) objects  
Array Members: Maximum number of 1 item.

 ** [ContextKeySelectors](#API_PutEventConfiguration_ResponseSyntax) **   <a name="awscloudtrail-PutEventConfiguration-response-ContextKeySelectors"></a>
The list of context key selectors that are configured for the event data store.  
Type: Array of [ContextKeySelector](API_ContextKeySelector.md) objects  
Array Members: Maximum number of 2 items.

 ** [EventDataStoreArn](#API_PutEventConfiguration_ResponseSyntax) **   <a name="awscloudtrail-PutEventConfiguration-response-EventDataStoreArn"></a>
The Amazon Resource Name (ARN) or ID suffix of the ARN of the event data store for which the event configuration settings were updated.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$` 

 ** [MaxEventSize](#API_PutEventConfiguration_ResponseSyntax) **   <a name="awscloudtrail-PutEventConfiguration-response-MaxEventSize"></a>
The maximum allowed size for events stored in the specified event data store.  
Type: String  
Valid Values: `Standard | Large` 

 ** [TrailARN](#API_PutEventConfiguration_ResponseSyntax) **   <a name="awscloudtrail-PutEventConfiguration-response-TrailARN"></a>
The Amazon Resource Name (ARN) of the trail that has aggregation enabled.  
Type: String

## Errors
<a name="API_PutEventConfiguration_Errors"></a>

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

 ** EventDataStoreARNInvalidException **   
The specified event data store ARN is not valid or does not map to an event data store in your account.  
HTTP Status Code: 400

 ** EventDataStoreNotFoundException **   
The specified event data store was not found.  
HTTP Status Code: 400

 ** InactiveEventDataStoreException **   
The event data store is inactive.  
HTTP Status Code: 400

 ** InsufficientDependencyServiceAccessPermissionException **   
This exception is thrown when the IAM identity that is used to create the organization resource lacks one or more required permissions for creating an organization resource in a required service.  
HTTP Status Code: 400

 ** InsufficientIAMAccessPermissionException **   
The task can't be completed because you are signed in with an account that lacks permissions to view or create a service-linked role. Sign in with an account that has the required permissions and then try again.  
HTTP Status Code: 400

 ** InvalidEventDataStoreCategoryException **   
This exception is thrown when event categories of specified event data stores are not valid.  
HTTP Status Code: 400

 ** InvalidEventDataStoreStatusException **   
The event data store is not in a status that supports the operation.  
HTTP Status Code: 400

 ** InvalidHomeRegionException **   
This exception is thrown when an operation is called on a trail from a Region other than the Region in which the trail was created.  
HTTP Status Code: 400

 ** InvalidParameterCombinationException **   
This exception is thrown when the combination of parameters provided is not valid.  
HTTP Status Code: 400

 ** InvalidParameterException **   
The request includes a parameter that is not valid.  
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

## See Also
<a name="API_PutEventConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/PutEventConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/PutEventConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/PutEventConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/PutEventConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/PutEventConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/PutEventConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/PutEventConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/PutEventConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/PutEventConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/PutEventConfiguration) 