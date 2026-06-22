---
id: "@specs/aws/bedrock-agent/docs/API_ListPromptRouters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListPromptRouters"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListPromptRouters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_ListPromptRouters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListPromptRouters
<a name="API_ListPromptRouters"></a>

Retrieves a list of prompt routers.

## Request Syntax
<a name="API_ListPromptRouters_RequestSyntax"></a>

```
GET /prompt-routers?maxResults={{maxResults}}&nextToken={{nextToken}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPromptRouters_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListPromptRouters_RequestSyntax) **   <a name="bedrock-ListPromptRouters-request-uri-maxResults"></a>
The maximum number of prompt routers to return in one page of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListPromptRouters_RequestSyntax) **   <a name="bedrock-ListPromptRouters-request-uri-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [type](#API_ListPromptRouters_RequestSyntax) **   <a name="bedrock-ListPromptRouters-request-uri-type"></a>
The type of the prompt routers, such as whether it's default or custom.  
Valid Values: `custom | default` 

## Request Body
<a name="API_ListPromptRouters_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPromptRouters_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "promptRouterSummaries": [ 
      { 
         "createdAt": "string",
         "description": "string",
         "fallbackModel": { 
            "modelArn": "string"
         },
         "models": [ 
            { 
               "modelArn": "string"
            }
         ],
         "promptRouterArn": "string",
         "promptRouterName": "string",
         "routingCriteria": { 
            "responseQualityDifference": number
         },
         "status": "string",
         "type": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPromptRouters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPromptRouters_ResponseSyntax) **   <a name="bedrock-ListPromptRouters-response-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [promptRouterSummaries](#API_ListPromptRouters_ResponseSyntax) **   <a name="bedrock-ListPromptRouters-response-promptRouterSummaries"></a>
A list of prompt router summaries.  
Type: Array of [PromptRouterSummary](API_PromptRouterSummary.md) objects

## Errors
<a name="API_ListPromptRouters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_ListPromptRouters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListPromptRouters) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListPromptRouters) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListPromptRouters) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListPromptRouters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListPromptRouters) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListPromptRouters) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListPromptRouters) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListPromptRouters) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListPromptRouters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListPromptRouters) 