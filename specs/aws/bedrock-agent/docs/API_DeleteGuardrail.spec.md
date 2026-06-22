---
id: "@specs/aws/bedrock-agent/docs/API_DeleteGuardrail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteGuardrail"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# DeleteGuardrail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_DeleteGuardrail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteGuardrail
<a name="API_DeleteGuardrail"></a>

Deletes a guardrail.
+ To delete a guardrail, only specify the ARN of the guardrail in the `guardrailIdentifier` field. If you delete a guardrail, all of its versions will be deleted.
+ To delete a version of a guardrail, specify the ARN of the guardrail in the `guardrailIdentifier` field and the version in the `guardrailVersion` field.

## Request Syntax
<a name="API_DeleteGuardrail_RequestSyntax"></a>

```
DELETE /guardrails/{{guardrailIdentifier}}?guardrailVersion={{guardrailVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteGuardrail_RequestParameters"></a>

The request uses the following URI parameters.

 ** [guardrailIdentifier](#API_DeleteGuardrail_RequestSyntax) **   <a name="bedrock-DeleteGuardrail-request-uri-guardrailIdentifier"></a>
The unique identifier of the guardrail. This can be an ID or the ARN.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))`   
Required: Yes

 ** [guardrailVersion](#API_DeleteGuardrail_RequestSyntax) **   <a name="bedrock-DeleteGuardrail-request-uri-guardrailVersion"></a>
The version of the guardrail.  
Pattern: `[1-9][0-9]{0,7}` 

## Request Body
<a name="API_DeleteGuardrail_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteGuardrail_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_DeleteGuardrail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_DeleteGuardrail_Errors"></a>

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

 ** ResourceInUseException **   
Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.  
HTTP Status Code: 400

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
<a name="API_DeleteGuardrail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/DeleteGuardrail) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/DeleteGuardrail) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/DeleteGuardrail) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/DeleteGuardrail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/DeleteGuardrail) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/DeleteGuardrail) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/DeleteGuardrail) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/DeleteGuardrail) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/DeleteGuardrail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/DeleteGuardrail) 