---
id: "@specs/aws/bedrock/docs/API_UpdateMarketplaceModelEndpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateMarketplaceModelEndpoint"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# UpdateMarketplaceModelEndpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_UpdateMarketplaceModelEndpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateMarketplaceModelEndpoint
<a name="API_UpdateMarketplaceModelEndpoint"></a>

Updates the configuration of an existing endpoint for a model from Amazon Bedrock Marketplace.

## Request Syntax
<a name="API_UpdateMarketplaceModelEndpoint_RequestSyntax"></a>

```
PATCH /marketplace-model/endpoints/{{endpointArn}} HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "endpointConfig": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateMarketplaceModelEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endpointArn](#API_UpdateMarketplaceModelEndpoint_RequestSyntax) **   <a name="bedrock-UpdateMarketplaceModelEndpoint-request-uri-endpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint you want to update.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: Yes

## Request Body
<a name="API_UpdateMarketplaceModelEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_UpdateMarketplaceModelEndpoint_RequestSyntax) **   <a name="bedrock-UpdateMarketplaceModelEndpoint-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because AWS SDKs automatically generate it for you and set this parameter. If you're not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [endpointConfig](#API_UpdateMarketplaceModelEndpoint_RequestSyntax) **   <a name="bedrock-UpdateMarketplaceModelEndpoint-request-endpointConfig"></a>
The new configuration for the endpoint, including the number and type of instances to use.  
Type: [EndpointConfig](API_EndpointConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_UpdateMarketplaceModelEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "marketplaceModelEndpoint": { 
      "createdAt": "string",
      "endpointArn": "string",
      "endpointConfig": { ... },
      "endpointStatus": "string",
      "endpointStatusMessage": "string",
      "modelSourceIdentifier": "string",
      "status": "string",
      "statusMessage": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_UpdateMarketplaceModelEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [marketplaceModelEndpoint](#API_UpdateMarketplaceModelEndpoint_ResponseSyntax) **   <a name="bedrock-UpdateMarketplaceModelEndpoint-response-marketplaceModelEndpoint"></a>
Details about the updated endpoint.  
Type: [MarketplaceModelEndpoint](API_MarketplaceModelEndpoint.md) object

## Errors
<a name="API_UpdateMarketplaceModelEndpoint_Errors"></a>

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
<a name="API_UpdateMarketplaceModelEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/UpdateMarketplaceModelEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/UpdateMarketplaceModelEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/UpdateMarketplaceModelEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/UpdateMarketplaceModelEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/UpdateMarketplaceModelEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/UpdateMarketplaceModelEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/UpdateMarketplaceModelEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/UpdateMarketplaceModelEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/UpdateMarketplaceModelEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/UpdateMarketplaceModelEndpoint) 