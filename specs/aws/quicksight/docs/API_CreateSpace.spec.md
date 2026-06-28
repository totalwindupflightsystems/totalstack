---
id: "@specs/aws/quicksight/docs/API_CreateSpace"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateSpace"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateSpace

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateSpace
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateSpace
<a name="API_CreateSpace"></a>

Creates a new Amazon QuickSight space. A space is a collection of resources that can be used to organize and manage QuickSight assets.

## Request Syntax
<a name="API_CreateSpace_RequestSyntax"></a>

```
POST /v1/accounts/{{AwsAccountId}}/spaces HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "SpaceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateSpace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateSpace_RequestSyntax) **   <a name="QS-CreateSpace-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the space.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_CreateSpace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_CreateSpace_RequestSyntax) **   <a name="QS-CreateSpace-request-Name"></a>
A display name for the space.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `[\P{C}\n\r\t\f\v\p{Cf}]*`   
Required: Yes

 ** [SpaceId](#API_CreateSpace_RequestSyntax) **   <a name="QS-CreateSpace-request-SpaceId"></a>
The ID of the space. This ID is unique per AWS Region for each AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_=.+]+`   
Required: Yes

 ** [Description](#API_CreateSpace_RequestSyntax) **   <a name="QS-CreateSpace-request-Description"></a>
A description of the space.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `[\P{C}\n\r\t\f\v\p{Cf}]*`   
Required: No

## Response Syntax
<a name="API_CreateSpace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RequestId": "string",
   "spaceArn": "string",
   "spaceId": "string"
}
```

## Response Elements
<a name="API_CreateSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [spaceId](#API_CreateSpace_ResponseSyntax) **   <a name="QS-CreateSpace-response-spaceId"></a>
The ID of the space.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_=.+]+` 

 ** [RequestId](#API_CreateSpace_ResponseSyntax) **   <a name="QS-CreateSpace-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [spaceArn](#API_CreateSpace_ResponseSyntax) **   <a name="QS-CreateSpace-response-spaceArn"></a>
The ARN of the space.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 512.  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}` 

## Errors
<a name="API_CreateSpace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **   
Updating or deleting a resource can cause an inconsistent state.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

 ** ResourceExistsException **   
The resource specified already exists.     
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 409

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_CreateSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateSpace) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateSpace) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateSpace) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateSpace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateSpace) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateSpace) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateSpace) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateSpace) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateSpace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateSpace) 