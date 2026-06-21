---
id: "@specs/aws/cloudtrail/docs/API_PutResourcePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutResourcePolicy"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# PutResourcePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_PutResourcePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

 Attaches a resource-based permission policy to a CloudTrail event data store, dashboard, or channel. For more information about resource-based policies, see [CloudTrail resource-based policy examples](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html) in the *CloudTrail User Guide*. 

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}",
   "ResourcePolicy": "{{string}}"
}
```

## Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_PutResourcePolicy_RequestSyntax) **   <a name="awscloudtrail-PutResourcePolicy-request-ResourceArn"></a>
 The Amazon Resource Name (ARN) of the CloudTrail event data store, dashboard, or channel attached to the resource-based policy.  
Example event data store ARN format: `arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`   
Example dashboard ARN format: `arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash`   
Example channel ARN format: `arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890`   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: Yes

 ** [ResourcePolicy](#API_PutResourcePolicy_RequestSyntax) **   <a name="awscloudtrail-PutResourcePolicy-request-ResourcePolicy"></a>
 A JSON-formatted string for an AWS resource-based policy.   
 For example resource-based policies, see [CloudTrail resource-based policy examples](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html) in the *CloudTrail User Guide*.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.  
Required: Yes

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
{
   "DelegatedAdminResourcePolicy": "string",
   "ResourceArn": "string",
   "ResourcePolicy": "string"
}
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DelegatedAdminResourcePolicy](#API_PutResourcePolicy_ResponseSyntax) **   <a name="awscloudtrail-PutResourcePolicy-response-DelegatedAdminResourcePolicy"></a>
 The default resource-based policy that is automatically generated for the delegated administrator of an AWS Organizations organization. This policy will be evaluated in tandem with any policy you submit for the resource. For more information about this policy, see [Default resource policy for delegated administrators](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-organizations.html#cloudtrail-lake-organizations-eds-rbp).   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [ResourceArn](#API_PutResourcePolicy_ResponseSyntax) **   <a name="awscloudtrail-PutResourcePolicy-response-ResourceArn"></a>
 The Amazon Resource Name (ARN) of the CloudTrail event data store, dashboard, or channel attached to the resource-based policy.   
Example event data store ARN format: `arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`   
Example dashboard ARN format: `arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash`   
Example channel ARN format: `arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890`   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$` 

 ** [ResourcePolicy](#API_PutResourcePolicy_ResponseSyntax) **   <a name="awscloudtrail-PutResourcePolicy-response-ResourcePolicy"></a>
 The JSON-formatted string of the AWS resource-based policy attached to the CloudTrail event data store, dashboard, or channel.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **   
This exception is thrown when the specified resource is not ready for an operation. This can occur when you try to run an operation on a resource before CloudTrail has time to fully load the resource, or because another operation is modifying the resource. If this exception occurs, wait a few minutes, and then try the operation again.  
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** ResourceARNNotValidException **   
 This exception is thrown when the provided resource does not exist, or the ARN format of the resource is not valid.   
The following is the format of an event data store ARN: `arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`   
The following is the format of a dashboard ARN: `arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash`   
The following is the format of a channel ARN: `arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890`   
HTTP Status Code: 400

 ** ResourceNotFoundException **   
This exception is thrown when the specified resource is not found.  
HTTP Status Code: 400

 ** ResourcePolicyNotValidException **   
 This exception is thrown when the resouce-based policy has syntax errors, or contains a principal that is not valid.   
HTTP Status Code: 400

 ** ResourceTypeNotSupportedException **   
This exception is thrown when the specified resource type is not supported by CloudTrail.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/PutResourcePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/PutResourcePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/PutResourcePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/PutResourcePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/PutResourcePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/PutResourcePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/PutResourcePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/PutResourcePolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/PutResourcePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/PutResourcePolicy) 