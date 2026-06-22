---
id: "@specs/aws/bedrock/docs/API_PutResourcePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutResourcePolicy"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# PutResourcePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_PutResourcePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

Adds a resource policy for a Bedrock resource.

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
POST /resource-policy HTTP/1.1
Content-type: application/json

{
   "resourceArn": "{{string}}",
   "resourcePolicy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceArn](#API_PutResourcePolicy_RequestSyntax) **   <a name="bedrock-PutResourcePolicy-request-resourceArn"></a>
The ARN of the Bedrock resource to which this resource policy applies.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** [resourcePolicy](#API_PutResourcePolicy_RequestSyntax) **   <a name="bedrock-PutResourcePolicy-request-resourcePolicy"></a>
The JSON string representing the Bedrock resource policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20480.  
Pattern: `[ -ÿ]+`   
Required: Yes

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "resourceArn": "string"
}
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [resourceArn](#API_PutResourcePolicy_ResponseSyntax) **   <a name="bedrock-PutResourcePolicy-response-resourceArn"></a>
The ARN of the Bedrock resource to which this resource policy applies.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
Error occurred because of a conflict while performing an operation.  
HTTP Status Code: 400

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/PutResourcePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/PutResourcePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/PutResourcePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/PutResourcePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/PutResourcePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/PutResourcePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/PutResourcePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/PutResourcePolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/PutResourcePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/PutResourcePolicy) 