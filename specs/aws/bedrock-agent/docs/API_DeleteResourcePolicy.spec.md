---
id: "@specs/aws/bedrock-agent/docs/API_DeleteResourcePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteResourcePolicy"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# DeleteResourcePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_DeleteResourcePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteResourcePolicy
<a name="API_DeleteResourcePolicy"></a>

Deletes a previously created Bedrock resource policy.

## Request Syntax
<a name="API_DeleteResourcePolicy_RequestSyntax"></a>

```
DELETE /resource-policy/{{resourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteResourcePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="bedrock-DeleteResourcePolicy-request-uri-resourceArn"></a>
The ARN of the Bedrock resource to which this resource policy applies.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## Request Body
<a name="API_DeleteResourcePolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/DeleteResourcePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/DeleteResourcePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/DeleteResourcePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/DeleteResourcePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/DeleteResourcePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/DeleteResourcePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/DeleteResourcePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/DeleteResourcePolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/DeleteResourcePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/DeleteResourcePolicy) 