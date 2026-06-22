---
id: "@specs/aws/bedrock/docs/API_CreateGuardrailVersion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateGuardrailVersion"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreateGuardrailVersion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_CreateGuardrailVersion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateGuardrailVersion
<a name="API_CreateGuardrailVersion"></a>

Creates a version of the guardrail. Use this API to create a snapshot of the guardrail when you are satisfied with a configuration, or to compare the configuration with another version.

## Request Syntax
<a name="API_CreateGuardrailVersion_RequestSyntax"></a>

```
POST /guardrails/{{guardrailIdentifier}} HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateGuardrailVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [guardrailIdentifier](#API_CreateGuardrailVersion_RequestSyntax) **   <a name="bedrock-CreateGuardrailVersion-request-uri-guardrailIdentifier"></a>
The unique identifier of the guardrail. This can be an ID or the ARN.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))`   
Required: Yes

## Request Body
<a name="API_CreateGuardrailVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateGuardrailVersion_RequestSyntax) **   <a name="bedrock-CreateGuardrailVersion-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon S3 User Guide*.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [description](#API_CreateGuardrailVersion_RequestSyntax) **   <a name="bedrock-CreateGuardrailVersion-request-description"></a>
A description of the guardrail version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

## Response Syntax
<a name="API_CreateGuardrailVersion_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "guardrailId": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_CreateGuardrailVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [guardrailId](#API_CreateGuardrailVersion_ResponseSyntax) **   <a name="bedrock-CreateGuardrailVersion-response-guardrailId"></a>
The unique identifier of the guardrail.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 64.  
Pattern: `[a-z0-9]+` 

 ** [version](#API_CreateGuardrailVersion_ResponseSyntax) **   <a name="bedrock-CreateGuardrailVersion-response-version"></a>
The number of the version of the guardrail.  
Type: String  
Pattern: `[1-9][0-9]{0,7}` 

## Errors
<a name="API_CreateGuardrailVersion_Errors"></a>

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

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 400

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_CreateGuardrailVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateGuardrailVersion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateGuardrailVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateGuardrailVersion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateGuardrailVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateGuardrailVersion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateGuardrailVersion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateGuardrailVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateGuardrailVersion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateGuardrailVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateGuardrailVersion) 