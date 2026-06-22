---
id: "@specs/aws/bedrock/docs/API_agent_GetFlowAlias"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetFlowAlias"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetFlowAlias

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_GetFlowAlias
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetFlowAlias
<a name="API_agent_GetFlowAlias"></a>

Retrieves information about a flow. For more information, see [Deploy a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-deploy.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_GetFlowAlias_RequestSyntax"></a>

```
GET /flows/{{flowIdentifier}}/aliases/{{aliasIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_GetFlowAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [aliasIdentifier](#API_agent_GetFlowAlias_RequestSyntax) **   <a name="bedrock-agent_GetFlowAlias-request-uri-aliasIdentifier"></a>
The unique identifier of the alias for which to retrieve information.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10})|(TSTALIASID|[0-9a-zA-Z]{10})`   
Required: Yes

 ** [flowIdentifier](#API_agent_GetFlowAlias_RequestSyntax) **   <a name="bedrock-agent_GetFlowAlias-request-uri-flowIdentifier"></a>
The unique identifier of the flow that the alias belongs to.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

## Request Body
<a name="API_agent_GetFlowAlias_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_GetFlowAlias_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "concurrencyConfiguration": { 
      "maxConcurrency": number,
      "type": "string"
   },
   "createdAt": "string",
   "description": "string",
   "flowId": "string",
   "id": "string",
   "name": "string",
   "routingConfiguration": [ 
      { 
         "flowVersion": "string"
      }
   ],
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_agent_GetFlowAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_agent_GetFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_GetFlowAlias-response-arn"></a>
The Amazon Resource Name (ARN) of the flow.  
Type: String  
Pattern: `arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/(TSTALIASID|[0-9a-zA-Z]{10})` 

 ** [concurrencyConfiguration](#API_agent_GetFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_GetFlowAlias-response-concurrencyConfiguration"></a>
The configuration that specifies how nodes in the flow are executed in parallel.  
Type: [FlowAliasConcurrencyConfiguration](API_agent_FlowAliasConcurrencyConfiguration.md) object

 ** [createdAt](#API_agent_GetFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_GetFlowAlias-response-createdAt"></a>
The time at which the flow was created.  
Type: Timestamp

 ** [description](#API_agent_GetFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_GetFlowAlias-response-description"></a>
The description of the flow.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [flowId](#API_agent_GetFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_GetFlowAlias-response-flowId"></a>
The unique identifier of the flow that the alias belongs to.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [id](#API_agent_GetFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_GetFlowAlias-response-id"></a>
The unique identifier of the alias of the flow.  
Type: String  
Pattern: `(TSTALIASID|[0-9a-zA-Z]{10})` 

 ** [name](#API_agent_GetFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_GetFlowAlias-response-name"></a>
The name of the alias.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}` 

 ** [routingConfiguration](#API_agent_GetFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_GetFlowAlias-response-routingConfiguration"></a>
Contains information about the version that the alias is mapped to.  
Type: Array of [FlowAliasRoutingConfigurationListItem](API_agent_FlowAliasRoutingConfigurationListItem.md) objects  
Array Members: Fixed number of 1 item.

 ** [updatedAt](#API_agent_GetFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_GetFlowAlias-response-updatedAt"></a>
The time at which the alias was last updated.  
Type: Timestamp

## Errors
<a name="API_agent_GetFlowAlias_Errors"></a>

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
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_GetFlowAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/GetFlowAlias) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/GetFlowAlias) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/GetFlowAlias) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/GetFlowAlias) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/GetFlowAlias) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/GetFlowAlias) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/GetFlowAlias) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/GetFlowAlias) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/GetFlowAlias) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/GetFlowAlias) 