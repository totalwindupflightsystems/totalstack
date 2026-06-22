---
id: "@specs/aws/bedrock-agent/docs/API_agent_CreateFlowAlias"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFlowAlias"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# CreateFlowAlias

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_CreateFlowAlias
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFlowAlias
<a name="API_agent_CreateFlowAlias"></a>

Creates an alias of a flow for deployment. For more information, see [Deploy a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-deploy.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_CreateFlowAlias_RequestSyntax"></a>

```
POST /flows/{{flowIdentifier}}/aliases HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "concurrencyConfiguration": { 
      "maxConcurrency": {{number}},
      "type": "{{string}}"
   },
   "description": "{{string}}",
   "name": "{{string}}",
   "routingConfiguration": [ 
      { 
         "flowVersion": "{{string}}"
      }
   ],
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_agent_CreateFlowAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowIdentifier](#API_agent_CreateFlowAlias_RequestSyntax) **   <a name="bedrock-agent_CreateFlowAlias-request-uri-flowIdentifier"></a>
The unique identifier of the flow for which to create an alias.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

## Request Body
<a name="API_agent_CreateFlowAlias_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_agent_CreateFlowAlias_RequestSyntax) **   <a name="bedrock-agent_CreateFlowAlias-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [concurrencyConfiguration](#API_agent_CreateFlowAlias_RequestSyntax) **   <a name="bedrock-agent_CreateFlowAlias-request-concurrencyConfiguration"></a>
The configuration that specifies how nodes in the flow are executed in parallel.  
Type: [FlowAliasConcurrencyConfiguration](API_agent_FlowAliasConcurrencyConfiguration.md) object  
Required: No

 ** [description](#API_agent_CreateFlowAlias_RequestSyntax) **   <a name="bedrock-agent_CreateFlowAlias-request-description"></a>
A description for the alias.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [name](#API_agent_CreateFlowAlias_RequestSyntax) **   <a name="bedrock-agent_CreateFlowAlias-request-name"></a>
A name for the alias.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** [routingConfiguration](#API_agent_CreateFlowAlias_RequestSyntax) **   <a name="bedrock-agent_CreateFlowAlias-request-routingConfiguration"></a>
Contains information about the version to which to map the alias.  
Type: Array of [FlowAliasRoutingConfigurationListItem](API_agent_FlowAliasRoutingConfigurationListItem.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** [tags](#API_agent_CreateFlowAlias_RequestSyntax) **   <a name="bedrock-agent_CreateFlowAlias-request-tags"></a>
Any tags that you want to attach to the alias of the flow. For more information, see [Tagging resources in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html).  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_agent_CreateFlowAlias_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_agent_CreateFlowAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_agent_CreateFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowAlias-response-arn"></a>
The Amazon Resource Name (ARN) of the alias.  
Type: String  
Pattern: `arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/(TSTALIASID|[0-9a-zA-Z]{10})` 

 ** [concurrencyConfiguration](#API_agent_CreateFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowAlias-response-concurrencyConfiguration"></a>
The configuration that specifies how nodes in the flow are executed in parallel.  
Type: [FlowAliasConcurrencyConfiguration](API_agent_FlowAliasConcurrencyConfiguration.md) object

 ** [createdAt](#API_agent_CreateFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowAlias-response-createdAt"></a>
The time at which the alias was created.  
Type: Timestamp

 ** [description](#API_agent_CreateFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowAlias-response-description"></a>
The description of the alias.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [flowId](#API_agent_CreateFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowAlias-response-flowId"></a>
The unique identifier of the flow that the alias belongs to.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [id](#API_agent_CreateFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowAlias-response-id"></a>
The unique identifier of the alias.  
Type: String  
Pattern: `(TSTALIASID|[0-9a-zA-Z]{10})` 

 ** [name](#API_agent_CreateFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowAlias-response-name"></a>
The name of the alias.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}` 

 ** [routingConfiguration](#API_agent_CreateFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowAlias-response-routingConfiguration"></a>
Contains information about the version that the alias is mapped to.  
Type: Array of [FlowAliasRoutingConfigurationListItem](API_agent_FlowAliasRoutingConfigurationListItem.md) objects  
Array Members: Fixed number of 1 item.

 ** [updatedAt](#API_agent_CreateFlowAlias_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowAlias-response-updatedAt"></a>
The time at which the alias of the flow was last updated.  
Type: Timestamp

## Errors
<a name="API_agent_CreateFlowAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
There was a conflict performing an operation.  
HTTP Status Code: 409

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 402

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.    
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_CreateFlowAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/CreateFlowAlias) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/CreateFlowAlias) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CreateFlowAlias) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/CreateFlowAlias) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CreateFlowAlias) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/CreateFlowAlias) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/CreateFlowAlias) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/CreateFlowAlias) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/CreateFlowAlias) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CreateFlowAlias) 