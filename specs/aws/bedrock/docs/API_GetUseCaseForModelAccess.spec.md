---
id: "@specs/aws/bedrock/docs/API_GetUseCaseForModelAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetUseCaseForModelAccess"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetUseCaseForModelAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_GetUseCaseForModelAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetUseCaseForModelAccess
<a name="API_GetUseCaseForModelAccess"></a>

 Returns the use case for requesting access to Anthropic models. 

## Request Syntax
<a name="API_GetUseCaseForModelAccess_RequestSyntax"></a>

```
GET /use-case-for-model-access HTTP/1.1
```

## URI Request Parameters
<a name="API_GetUseCaseForModelAccess_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetUseCaseForModelAccess_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetUseCaseForModelAccess_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "formData": blob
}
```

## Response Elements
<a name="API_GetUseCaseForModelAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [formData](#API_GetUseCaseForModelAccess_ResponseSyntax) **   <a name="bedrock-GetUseCaseForModelAccess-response-formData"></a>
 Returns form data from the Anthropic first time user request.   
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 10. Maximum length of 16384.

## Errors
<a name="API_GetUseCaseForModelAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetUseCaseForModelAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetUseCaseForModelAccess) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetUseCaseForModelAccess) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetUseCaseForModelAccess) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetUseCaseForModelAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetUseCaseForModelAccess) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetUseCaseForModelAccess) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetUseCaseForModelAccess) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetUseCaseForModelAccess) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetUseCaseForModelAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetUseCaseForModelAccess) 