---
id: "@specs/aws/bedrock-agent/docs/API_agent_ListAgentActionGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAgentActionGroups"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListAgentActionGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_ListAgentActionGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAgentActionGroups
<a name="API_agent_ListAgentActionGroups"></a>

Lists the action groups for an agent and information about each one.

## Request Syntax
<a name="API_agent_ListAgentActionGroups_RequestSyntax"></a>

```
POST /agents/{{agentId}}/agentversions/{{agentVersion}}/actiongroups/ HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent_ListAgentActionGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_agent_ListAgentActionGroups_RequestSyntax) **   <a name="bedrock-agent_ListAgentActionGroups-request-uri-agentId"></a>
The unique identifier of the agent.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [agentVersion](#API_agent_ListAgentActionGroups_RequestSyntax) **   <a name="bedrock-agent_ListAgentActionGroups-request-uri-agentVersion"></a>
The version of the agent.  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})`   
Required: Yes

## Request Body
<a name="API_agent_ListAgentActionGroups_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_agent_ListAgentActionGroups_RequestSyntax) **   <a name="bedrock-agent_ListAgentActionGroups-request-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [nextToken](#API_agent_ListAgentActionGroups_RequestSyntax) **   <a name="bedrock-agent_ListAgentActionGroups-request-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

## Response Syntax
<a name="API_agent_ListAgentActionGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionGroupSummaries": [ 
      { 
         "actionGroupId": "string",
         "actionGroupName": "string",
         "actionGroupState": "string",
         "description": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_agent_ListAgentActionGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionGroupSummaries](#API_agent_ListAgentActionGroups_ResponseSyntax) **   <a name="bedrock-agent_ListAgentActionGroups-response-actionGroupSummaries"></a>
A list of objects, each of which contains information about an action group.  
Type: Array of [ActionGroupSummary](API_agent_ActionGroupSummary.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [nextToken](#API_agent_ListAgentActionGroups_ResponseSyntax) **   <a name="bedrock-agent_ListAgentActionGroups-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_agent_ListAgentActionGroups_Errors"></a>

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

## Examples
<a name="API_agent_ListAgentActionGroups_Examples"></a>

### Example request
<a name="API_agent_ListAgentActionGroups_Example_1"></a>

This example illustrates one usage of ListAgentActionGroups.

```
POST /agents/AGENT12345/agentversions/1/actiongroups/ HTTP/1.1
Content-type: application/json

{
   "maxResults": 10
}
```

## See Also
<a name="API_agent_ListAgentActionGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/ListAgentActionGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/ListAgentActionGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ListAgentActionGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/ListAgentActionGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ListAgentActionGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/ListAgentActionGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/ListAgentActionGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/ListAgentActionGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/ListAgentActionGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ListAgentActionGroups) 