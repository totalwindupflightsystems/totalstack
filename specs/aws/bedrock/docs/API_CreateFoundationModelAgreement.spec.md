---
id: "@specs/aws/bedrock/docs/API_CreateFoundationModelAgreement"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFoundationModelAgreement"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreateFoundationModelAgreement

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_CreateFoundationModelAgreement
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFoundationModelAgreement
<a name="API_CreateFoundationModelAgreement"></a>

Request a model access agreement for the specified model.

## Request Syntax
<a name="API_CreateFoundationModelAgreement_RequestSyntax"></a>

```
POST /create-foundation-model-agreement HTTP/1.1
Content-type: application/json

{
   "modelId": "{{string}}",
   "offerToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateFoundationModelAgreement_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateFoundationModelAgreement_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [modelId](#API_CreateFoundationModelAgreement_RequestSyntax) **   <a name="bedrock-CreateFoundationModelAgreement-request-modelId"></a>
Model Id of the model for the access request.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 140.  
Pattern: `[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}|)`   
Required: Yes

 ** [offerToken](#API_CreateFoundationModelAgreement_RequestSyntax) **   <a name="bedrock-CreateFoundationModelAgreement-request-offerToken"></a>
An offer token encapsulates the information for an offer.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_CreateFoundationModelAgreement_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "modelId": "string"
}
```

## Response Elements
<a name="API_CreateFoundationModelAgreement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [modelId](#API_CreateFoundationModelAgreement_ResponseSyntax) **   <a name="bedrock-CreateFoundationModelAgreement-response-modelId"></a>
Model Id of the model for the access request.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 140.  
Pattern: `[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}|)` 

## Errors
<a name="API_CreateFoundationModelAgreement_Errors"></a>

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

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_CreateFoundationModelAgreement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateFoundationModelAgreement) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateFoundationModelAgreement) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateFoundationModelAgreement) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateFoundationModelAgreement) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateFoundationModelAgreement) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateFoundationModelAgreement) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateFoundationModelAgreement) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateFoundationModelAgreement) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateFoundationModelAgreement) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateFoundationModelAgreement) 