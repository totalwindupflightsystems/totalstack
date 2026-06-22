---
id: "@specs/aws/bedrock-agent/docs/API_RegisterMarketplaceModelEndpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RegisterMarketplaceModelEndpoint"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# RegisterMarketplaceModelEndpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_RegisterMarketplaceModelEndpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RegisterMarketplaceModelEndpoint
<a name="API_RegisterMarketplaceModelEndpoint"></a>

Registers an existing Amazon SageMaker endpoint with Amazon Bedrock Marketplace, allowing it to be used with Amazon Bedrock APIs.

## Request Syntax
<a name="API_RegisterMarketplaceModelEndpoint_RequestSyntax"></a>

```
POST /marketplace-model/endpoints/{{endpointIdentifier}}/registration HTTP/1.1
Content-type: application/json

{
   "modelSourceIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterMarketplaceModelEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endpointIdentifier](#API_RegisterMarketplaceModelEndpoint_RequestSyntax) **   <a name="bedrock-RegisterMarketplaceModelEndpoint-request-uri-endpointIdentifier"></a>
The ARN of the Amazon SageMaker endpoint you want to register with Amazon Bedrock Marketplace.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: Yes

## Request Body
<a name="API_RegisterMarketplaceModelEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [modelSourceIdentifier](#API_RegisterMarketplaceModelEndpoint_RequestSyntax) **   <a name="bedrock-RegisterMarketplaceModelEndpoint-request-modelSourceIdentifier"></a>
The ARN of the model from Amazon Bedrock Marketplace that is deployed on the endpoint.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*arn:aws:sagemaker:.*:hub-content/SageMakerPublicHub/Model/.*`   
Required: Yes

## Response Syntax
<a name="API_RegisterMarketplaceModelEndpoint_ResponseSyntax"></a>

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
<a name="API_RegisterMarketplaceModelEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [marketplaceModelEndpoint](#API_RegisterMarketplaceModelEndpoint_ResponseSyntax) **   <a name="bedrock-RegisterMarketplaceModelEndpoint-response-marketplaceModelEndpoint"></a>
Details about the registered endpoint.  
Type: [MarketplaceModelEndpoint](API_MarketplaceModelEndpoint.md) object

## Errors
<a name="API_RegisterMarketplaceModelEndpoint_Errors"></a>

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

 ** ServiceUnavailableException **   
Returned if the service cannot complete the request.  
HTTP Status Code: 503

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_RegisterMarketplaceModelEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/RegisterMarketplaceModelEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/RegisterMarketplaceModelEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/RegisterMarketplaceModelEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/RegisterMarketplaceModelEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/RegisterMarketplaceModelEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/RegisterMarketplaceModelEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/RegisterMarketplaceModelEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/RegisterMarketplaceModelEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/RegisterMarketplaceModelEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/RegisterMarketplaceModelEndpoint) 