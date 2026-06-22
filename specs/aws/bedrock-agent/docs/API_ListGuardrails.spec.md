---
id: "@specs/aws/bedrock-agent/docs/API_ListGuardrails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListGuardrails"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListGuardrails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_ListGuardrails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListGuardrails
<a name="API_ListGuardrails"></a>

Lists details about all the guardrails in an account. To list the `DRAFT` version of all your guardrails, don't specify the `guardrailIdentifier` field. To list all versions of a guardrail, specify the ARN of the guardrail in the `guardrailIdentifier` field.

You can set the maximum number of results to return in a response in the `maxResults` field. If there are more results than the number you set, the response returns a `nextToken` that you can send in another `ListGuardrails` request to see the next batch of results.

## Request Syntax
<a name="API_ListGuardrails_RequestSyntax"></a>

```
GET /guardrails?guardrailIdentifier={{guardrailIdentifier}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListGuardrails_RequestParameters"></a>

The request uses the following URI parameters.

 ** [guardrailIdentifier](#API_ListGuardrails_RequestSyntax) **   <a name="bedrock-ListGuardrails-request-uri-guardrailIdentifier"></a>
The unique identifier of the guardrail. This can be an ID or the ARN.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))` 

 ** [maxResults](#API_ListGuardrails_RequestSyntax) **   <a name="bedrock-ListGuardrails-request-uri-maxResults"></a>
The maximum number of results to return in the response.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListGuardrails_RequestSyntax) **   <a name="bedrock-ListGuardrails-request-uri-nextToken"></a>
If there are more results than were returned in the response, the response returns a `nextToken` that you can send in another `ListGuardrails` request to see the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Request Body
<a name="API_ListGuardrails_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListGuardrails_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "guardrails": [ 
      { 
         "arn": "string",
         "createdAt": "string",
         "crossRegionDetails": { 
            "guardrailProfileArn": "string",
            "guardrailProfileId": "string"
         },
         "description": "string",
         "id": "string",
         "name": "string",
         "status": "string",
         "updatedAt": "string",
         "version": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListGuardrails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [guardrails](#API_ListGuardrails_ResponseSyntax) **   <a name="bedrock-ListGuardrails-response-guardrails"></a>
A list of objects, each of which contains details about a guardrail.  
Type: Array of [GuardrailSummary](API_GuardrailSummary.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

 ** [nextToken](#API_ListGuardrails_ResponseSyntax) **   <a name="bedrock-ListGuardrails-response-nextToken"></a>
If there are more results than were returned in the response, the response returns a `nextToken` that you can send in another `ListGuardrails` request to see the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListGuardrails_Errors"></a>

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
<a name="API_ListGuardrails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListGuardrails) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListGuardrails) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListGuardrails) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListGuardrails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListGuardrails) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListGuardrails) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListGuardrails) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListGuardrails) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListGuardrails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListGuardrails) 