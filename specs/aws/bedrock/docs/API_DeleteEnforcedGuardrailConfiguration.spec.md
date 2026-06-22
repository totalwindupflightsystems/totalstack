---
id: "@specs/aws/bedrock/docs/API_DeleteEnforcedGuardrailConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteEnforcedGuardrailConfiguration"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# DeleteEnforcedGuardrailConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_DeleteEnforcedGuardrailConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteEnforcedGuardrailConfiguration
<a name="API_DeleteEnforcedGuardrailConfiguration"></a>

Deletes the account-level enforced guardrail configuration.

## Request Syntax
<a name="API_DeleteEnforcedGuardrailConfiguration_RequestSyntax"></a>

```
DELETE /enforcedGuardrailsConfiguration/{{configId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteEnforcedGuardrailConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [configId](#API_DeleteEnforcedGuardrailConfiguration_RequestSyntax) **   <a name="bedrock-DeleteEnforcedGuardrailConfiguration-request-uri-configId"></a>
Unique ID for the account enforced configuration.  
Pattern: `[a-z0-9]+`   
Required: Yes

## Request Body
<a name="API_DeleteEnforcedGuardrailConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteEnforcedGuardrailConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteEnforcedGuardrailConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteEnforcedGuardrailConfiguration_Errors"></a>

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
<a name="API_DeleteEnforcedGuardrailConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/DeleteEnforcedGuardrailConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/DeleteEnforcedGuardrailConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/DeleteEnforcedGuardrailConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/DeleteEnforcedGuardrailConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/DeleteEnforcedGuardrailConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/DeleteEnforcedGuardrailConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/DeleteEnforcedGuardrailConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/DeleteEnforcedGuardrailConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/DeleteEnforcedGuardrailConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/DeleteEnforcedGuardrailConfiguration) 