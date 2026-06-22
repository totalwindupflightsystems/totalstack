---
id: "@specs/aws/bedrock-agent/docs/API_agent-runtime_GenerateQuery"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GenerateQuery"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GenerateQuery

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent-runtime_GenerateQuery
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GenerateQuery
<a name="API_agent-runtime_GenerateQuery"></a>

Generates an SQL query from a natural language query. For more information, see [Generate a query for structured data](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-generate-query.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent-runtime_GenerateQuery_RequestSyntax"></a>

```
POST /generateQuery HTTP/1.1
Content-type: application/json

{
   "queryGenerationInput": { 
      "text": "{{string}}",
      "type": "{{string}}"
   },
   "transformationConfiguration": { 
      "mode": "{{string}}",
      "textToSqlConfiguration": { 
         "knowledgeBaseConfiguration": { 
            "knowledgeBaseArn": "{{string}}"
         },
         "type": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_agent-runtime_GenerateQuery_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_agent-runtime_GenerateQuery_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [queryGenerationInput](#API_agent-runtime_GenerateQuery_RequestSyntax) **   <a name="bedrock-agent-runtime_GenerateQuery-request-queryGenerationInput"></a>
Specifies information about a natural language query to transform into SQL.  
Type: [QueryGenerationInput](API_agent-runtime_QueryGenerationInput.md) object  
Required: Yes

 ** [transformationConfiguration](#API_agent-runtime_GenerateQuery_RequestSyntax) **   <a name="bedrock-agent-runtime_GenerateQuery-request-transformationConfiguration"></a>
Specifies configurations for transforming the natural language query into SQL.  
Type: [TransformationConfiguration](API_agent-runtime_TransformationConfiguration.md) object  
Required: Yes

## Response Syntax
<a name="API_agent-runtime_GenerateQuery_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "queries": [ 
      { 
         "sql": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_agent-runtime_GenerateQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [queries](#API_agent-runtime_GenerateQuery_ResponseSyntax) **   <a name="bedrock-agent-runtime_GenerateQuery-response-queries"></a>
A list of objects, each of which defines a generated query that can correspond to the natural language queries.  
Type: Array of [GeneratedQuery](API_agent-runtime_GeneratedQuery.md) objects  
Array Members: Minimum number of 0 items.

## Errors
<a name="API_agent-runtime_GenerateQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions. Check your permissions and retry your request.  
HTTP Status Code: 403

 ** BadGatewayException **   
There was an issue with a dependency due to a server issue. Retry your request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 502

 ** ConflictException **   
There was a conflict performing an operation. Resolve the conflict and retry your request.  
HTTP Status Code: 409

 ** DependencyFailedException **   
There was an issue with a dependency. Check the resource configurations and retry the request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 424

 ** InternalServerException **   
An internal server error occurred. Retry your request.    
 ** reason **   
The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.
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
<a name="API_agent-runtime_GenerateQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/GenerateQuery) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/GenerateQuery) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/GenerateQuery) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/GenerateQuery) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/GenerateQuery) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/GenerateQuery) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/GenerateQuery) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/GenerateQuery) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/GenerateQuery) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/GenerateQuery) 