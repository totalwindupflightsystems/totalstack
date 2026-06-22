---
id: "@specs/aws/bedrock/docs/API_DeleteMarketplaceModelEndpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteMarketplaceModelEndpoint"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# DeleteMarketplaceModelEndpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_DeleteMarketplaceModelEndpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteMarketplaceModelEndpoint
<a name="API_DeleteMarketplaceModelEndpoint"></a>

Deletes an endpoint for a model from Amazon Bedrock Marketplace.

## Request Syntax
<a name="API_DeleteMarketplaceModelEndpoint_RequestSyntax"></a>

```
DELETE /marketplace-model/endpoints/{{endpointArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteMarketplaceModelEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endpointArn](#API_DeleteMarketplaceModelEndpoint_RequestSyntax) **   <a name="bedrock-DeleteMarketplaceModelEndpoint-request-uri-endpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint you want to delete.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: Yes

## Request Body
<a name="API_DeleteMarketplaceModelEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteMarketplaceModelEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteMarketplaceModelEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteMarketplaceModelEndpoint_Errors"></a>

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
<a name="API_DeleteMarketplaceModelEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/DeleteMarketplaceModelEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/DeleteMarketplaceModelEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/DeleteMarketplaceModelEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/DeleteMarketplaceModelEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/DeleteMarketplaceModelEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/DeleteMarketplaceModelEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/DeleteMarketplaceModelEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/DeleteMarketplaceModelEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/DeleteMarketplaceModelEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/DeleteMarketplaceModelEndpoint) 