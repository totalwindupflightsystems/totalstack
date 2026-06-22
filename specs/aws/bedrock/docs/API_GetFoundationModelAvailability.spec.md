---
id: "@specs/aws/bedrock/docs/API_GetFoundationModelAvailability"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetFoundationModelAvailability"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetFoundationModelAvailability

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_GetFoundationModelAvailability
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetFoundationModelAvailability
<a name="API_GetFoundationModelAvailability"></a>

Get information about the Foundation model availability.

## Request Syntax
<a name="API_GetFoundationModelAvailability_RequestSyntax"></a>

```
GET /foundation-model-availability/{{modelId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFoundationModelAvailability_RequestParameters"></a>

The request uses the following URI parameters.

 ** [modelId](#API_GetFoundationModelAvailability_RequestSyntax) **   <a name="bedrock-GetFoundationModelAvailability-request-uri-modelId"></a>
The model Id of the foundation model.  
Length Constraints: Minimum length of 0. Maximum length of 140.  
Pattern: `[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}|)`   
Required: Yes

## Request Body
<a name="API_GetFoundationModelAvailability_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFoundationModelAvailability_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agreementAvailability": { 
      "errorMessage": "string",
      "status": "string"
   },
   "authorizationStatus": "string",
   "entitlementAvailability": "string",
   "modelId": "string",
   "regionAvailability": "string"
}
```

## Response Elements
<a name="API_GetFoundationModelAvailability_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementAvailability](#API_GetFoundationModelAvailability_ResponseSyntax) **   <a name="bedrock-GetFoundationModelAvailability-response-agreementAvailability"></a>
Agreement availability.   
Type: [AgreementAvailability](API_AgreementAvailability.md) object

 ** [authorizationStatus](#API_GetFoundationModelAvailability_ResponseSyntax) **   <a name="bedrock-GetFoundationModelAvailability-response-authorizationStatus"></a>
Authorization status.  
Type: String  
Valid Values: `AUTHORIZED | NOT_AUTHORIZED` 

 ** [entitlementAvailability](#API_GetFoundationModelAvailability_ResponseSyntax) **   <a name="bedrock-GetFoundationModelAvailability-response-entitlementAvailability"></a>
Entitlement availability.   
Type: String  
Valid Values: `AVAILABLE | NOT_AVAILABLE` 

 ** [modelId](#API_GetFoundationModelAvailability_ResponseSyntax) **   <a name="bedrock-GetFoundationModelAvailability-response-modelId"></a>
The model Id of the foundation model.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 140.  
Pattern: `[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}|)` 

 ** [regionAvailability](#API_GetFoundationModelAvailability_ResponseSyntax) **   <a name="bedrock-GetFoundationModelAvailability-response-regionAvailability"></a>
Region availability.   
Type: String  
Valid Values: `AVAILABLE | NOT_AVAILABLE` 

## Errors
<a name="API_GetFoundationModelAvailability_Errors"></a>

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
<a name="API_GetFoundationModelAvailability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetFoundationModelAvailability) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetFoundationModelAvailability) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetFoundationModelAvailability) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetFoundationModelAvailability) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetFoundationModelAvailability) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetFoundationModelAvailability) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetFoundationModelAvailability) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetFoundationModelAvailability) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetFoundationModelAvailability) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetFoundationModelAvailability) 