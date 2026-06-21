---
id: "@specs/aws/cloudtrail/docs/API_StartLogging"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartLogging"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# StartLogging

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_StartLogging
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartLogging
<a name="API_StartLogging"></a>

Starts the recording of AWS API calls and log file delivery for a trail. For a trail that is enabled in all Regions, this operation must be called from the Region in which the trail was created. This operation cannot be called on the shadow trails (replicated trails in other Regions) of a trail that is enabled in all Regions.

## Request Syntax
<a name="API_StartLogging_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_StartLogging_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_StartLogging_RequestSyntax) **   <a name="awscloudtrail-StartLogging-request-Name"></a>
Specifies the name or the CloudTrail ARN of the trail for which CloudTrail logs AWS API calls. The following is the format of a trail ARN.  
 `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`   
Type: String  
Required: Yes

## Response Elements
<a name="API_StartLogging_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartLogging_Errors"></a>

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

## See Also
<a name="API_StartLogging_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/StartLogging) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/StartLogging) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/StartLogging) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/StartLogging) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/StartLogging) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/StartLogging) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/StartLogging) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/StartLogging) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/StartLogging) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/StartLogging) 