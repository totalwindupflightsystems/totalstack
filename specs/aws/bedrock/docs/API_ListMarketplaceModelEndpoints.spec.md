---
id: "@specs/aws/bedrock/docs/API_ListMarketplaceModelEndpoints"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListMarketplaceModelEndpoints"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# ListMarketplaceModelEndpoints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_ListMarketplaceModelEndpoints
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListMarketplaceModelEndpoints
<a name="API_ListMarketplaceModelEndpoints"></a>

Lists the endpoints for models from Amazon Bedrock Marketplace in your AWS account.

## Request Syntax
<a name="API_ListMarketplaceModelEndpoints_RequestSyntax"></a>

```
GET /marketplace-model/endpoints?maxResults={{maxResults}}&modelSourceIdentifier={{modelSourceEquals}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMarketplaceModelEndpoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListMarketplaceModelEndpoints_RequestSyntax) **   <a name="bedrock-ListMarketplaceModelEndpoints-request-uri-maxResults"></a>
The maximum number of results to return in a single call. If more results are available, the operation returns a `NextToken` value.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [modelSourceEquals](#API_ListMarketplaceModelEndpoints_RequestSyntax) **   <a name="bedrock-ListMarketplaceModelEndpoints-request-uri-modelSourceEquals"></a>
If specified, only endpoints for the given model source identifier are returned.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*arn:aws:sagemaker:.*:hub-content/SageMakerPublicHub/Model/.*` 

 ** [nextToken](#API_ListMarketplaceModelEndpoints_RequestSyntax) **   <a name="bedrock-ListMarketplaceModelEndpoints-request-uri-nextToken"></a>
The token for the next set of results. You receive this token from a previous `ListMarketplaceModelEndpoints` call.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Request Body
<a name="API_ListMarketplaceModelEndpoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMarketplaceModelEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "marketplaceModelEndpoints": [ 
      { 
         "createdAt": "string",
         "endpointArn": "string",
         "modelSourceIdentifier": "string",
         "status": "string",
         "statusMessage": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMarketplaceModelEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [marketplaceModelEndpoints](#API_ListMarketplaceModelEndpoints_ResponseSyntax) **   <a name="bedrock-ListMarketplaceModelEndpoints-response-marketplaceModelEndpoints"></a>
An array of endpoint summaries.  
Type: Array of [MarketplaceModelEndpointSummary](API_MarketplaceModelEndpointSummary.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

 ** [nextToken](#API_ListMarketplaceModelEndpoints_ResponseSyntax) **   <a name="bedrock-ListMarketplaceModelEndpoints-response-nextToken"></a>
The token for the next set of results. Use this token to get the next set of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListMarketplaceModelEndpoints_Errors"></a>

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
<a name="API_ListMarketplaceModelEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListMarketplaceModelEndpoints) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListMarketplaceModelEndpoints) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListMarketplaceModelEndpoints) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListMarketplaceModelEndpoints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListMarketplaceModelEndpoints) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListMarketplaceModelEndpoints) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListMarketplaceModelEndpoints) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListMarketplaceModelEndpoints) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListMarketplaceModelEndpoints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListMarketplaceModelEndpoints) 