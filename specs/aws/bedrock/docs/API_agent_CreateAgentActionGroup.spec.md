---
id: "@specs/aws/bedrock/docs/API_agent_CreateAgentActionGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAgentActionGroup"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreateAgentActionGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_CreateAgentActionGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAgentActionGroup
<a name="API_agent_CreateAgentActionGroup"></a>

Creates an action group for an agent. An action group represents the actions that an agent can carry out for the customer by defining the APIs that an agent can call and the logic for calling them.

To allow your agent to request the user for additional information when trying to complete a task, add an action group with the `parentActionGroupSignature` field set to `AMAZON.UserInput`. 

To allow your agent to generate, run, and troubleshoot code when trying to complete a task, add an action group with the `parentActionGroupSignature` field set to `AMAZON.CodeInterpreter`. 

You must leave the `description`, `apiSchema`, and `actionGroupExecutor` fields blank for this action group. During orchestration, if your agent determines that it needs to invoke an API in an action group, but doesn't have enough information to complete the API request, it will invoke this action group instead and return an [Observation](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Observation.html) reprompting the user for more information.

## Request Syntax
<a name="API_agent_CreateAgentActionGroup_RequestSyntax"></a>

```
PUT /agents/{{agentId}}/agentversions/{{agentVersion}}/actiongroups/ HTTP/1.1
Content-type: application/json

{
   "actionGroupExecutor": { ... },
   "actionGroupName": "{{string}}",
   "actionGroupState": "{{string}}",
   "apiSchema": { ... },
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "functionSchema": { ... },
   "parentActionGroupSignature": "{{string}}",
   "parentActionGroupSignatureParams": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_agent_CreateAgentActionGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_agent_CreateAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_CreateAgentActionGroup-request-uri-agentId"></a>
The unique identifier of the agent for which to create the action group.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [agentVersion](#API_agent_CreateAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_CreateAgentActionGroup-request-uri-agentVersion"></a>
The version of the agent for which to create the action group.  
Length Constraints: Fixed length of 5.  
Pattern: `DRAFT`   
Required: Yes

## Request Body
<a name="API_agent_CreateAgentActionGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionGroupExecutor](#API_agent_CreateAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_CreateAgentActionGroup-request-actionGroupExecutor"></a>
The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action or the custom control method for handling the information elicited from the user.  
Type: [ActionGroupExecutor](API_agent_ActionGroupExecutor.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [actionGroupName](#API_agent_CreateAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_CreateAgentActionGroup-request-actionGroupName"></a>
The name to give the action group.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** [actionGroupState](#API_agent_CreateAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_CreateAgentActionGroup-request-actionGroupState"></a>
Specifies whether the action group is available for the agent to invoke or not when sending an [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html) request.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** [apiSchema](#API_agent_CreateAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_CreateAgentActionGroup-request-apiSchema"></a>
Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema. For more information, see [Action group OpenAPI schemas](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html).  
Type: [APISchema](API_agent_APISchema.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [clientToken](#API_agent_CreateAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_CreateAgentActionGroup-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_agent_CreateAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_CreateAgentActionGroup-request-description"></a>
A description of the action group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [functionSchema](#API_agent_CreateAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_CreateAgentActionGroup-request-functionSchema"></a>
Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.  
Type: [FunctionSchema](API_agent_FunctionSchema.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [parentActionGroupSignature](#API_agent_CreateAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_CreateAgentActionGroup-request-parentActionGroupSignature"></a>
Specify a built-in or computer use action for this action group. If you specify a value, you must leave the `description`, `apiSchema`, and `actionGroupExecutor` fields empty for this action group.   
+ To allow your agent to request the user for additional information when trying to complete a task, set this field to `AMAZON.UserInput`. 
+ To allow your agent to generate, run, and troubleshoot code when trying to complete a task, set this field to `AMAZON.CodeInterpreter`.
+ To allow your agent to use an Anthropic computer use tool, specify one of the following values. 
**Important**  
 Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. When operating computer use functionality, we recommend taking additional security precautions, such as executing computer actions in virtual environments with restricted data access and limited internet connectivity. For more information, see [Configure an Amazon Bedrock Agent to complete tasks with computer use tools](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html). 
  +  `ANTHROPIC.Computer` - Gives the agent permission to use the mouse and keyboard and take screenshots.
  +  `ANTHROPIC.TextEditor` - Gives the agent permission to view, create and edit files.
  +  `ANTHROPIC.Bash` - Gives the agent permission to run commands in a bash shell.
Type: String  
Valid Values: `AMAZON.UserInput | AMAZON.CodeInterpreter | ANTHROPIC.Computer | ANTHROPIC.Bash | ANTHROPIC.TextEditor`   
Required: No

 ** [parentActionGroupSignatureParams](#API_agent_CreateAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_CreateAgentActionGroup-request-parentActionGroupSignatureParams"></a>
The configuration settings for a computer use action.  
 Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. For more information, see [Configure an Amazon Bedrock Agent to complete tasks with computer use tools](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html). 
Type: String to string map  
Key Length Constraints: Minimum length of 0. Maximum length of 100.  
Value Length Constraints: Minimum length of 0. Maximum length of 100.  
Required: No

## Response Syntax
<a name="API_agent_CreateAgentActionGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentActionGroup": { 
      "actionGroupExecutor": { ... },
      "actionGroupId": "string",
      "actionGroupName": "string",
      "actionGroupState": "string",
      "agentId": "string",
      "agentVersion": "string",
      "apiSchema": { ... },
      "clientToken": "string",
      "createdAt": "string",
      "description": "string",
      "functionSchema": { ... },
      "parentActionGroupSignatureParams": { 
         "string" : "string" 
      },
      "parentActionSignature": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_agent_CreateAgentActionGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentActionGroup](#API_agent_CreateAgentActionGroup_ResponseSyntax) **   <a name="bedrock-agent_CreateAgentActionGroup-response-agentActionGroup"></a>
Contains details about the action group that was created.  
Type: [AgentActionGroup](API_agent_AgentActionGroup.md) object

## Errors
<a name="API_agent_CreateAgentActionGroup_Errors"></a>

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

## Examples
<a name="API_agent_CreateAgentActionGroup_Examples"></a>

### Create an action group using an OpenAPI schema and a Lambda function
<a name="API_agent_CreateAgentActionGroup_Example_1"></a>

The following example creates an action group using an OpenAPI schema uploaded to an Amazon S3 bucket and sends the information elicited from the user to a Lambda function.

```
PUT /agents/AGENT12345/agentversions/DRAFT/actiongroups/ HTTP/1.1
Content-type: application/json

{
   "actionGroupName": "Test Action",
   "actionGroupState": "ENABLED",
   "apiSchema": {
        "s3": {
            "s3BucketName": "apischema-s3",
            "s3ObjectKey": "it_agent_openapi.json"
        }
    },
   "description": "Testing latest IT Management action",
   "actionGroupExecutor": {
        "lambda": "arn:aws:lambda:us-west-2:123456789012:function:ItAgentLambda"
    }
}
```

### Create an action group using an OpenAPI schema and return control
<a name="API_agent_CreateAgentActionGroup_Example_2"></a>

The following example creates an action group using an OpenAPI schema uploaded to an Amazon S3 bucket and returns control by sending the information in the `InvokeAgent` response.

```
{
    "actionGroupName": "WeatherAPIs",
    "description": "Actions to get current weather and historical trends for a location",
    "actionGroupState": "ENABLED",
    "apiSchema": {
        "s3": {
            "s3BucketName": "openapi-spec-iad",
            "s3ObjectKey": "get_weather_openapi.yaml"
        }
    },
    "actionGroupExecutor": {
        "customControl": "RETURN_CONTROL"
    }
}
```

### Create an action group using function details and return control
<a name="API_agent_CreateAgentActionGroup_Example_3"></a>

The following example creates an action group using function details and returns control by sending the information in the `InvokeAgent` response

```
PUT /agents/AGENT12345/agentversions/DRAFT/actiongroups/ HTTP/1.1
Content-type: application/json

{
    "actionGroupName": "OrderManagementAction",
    "description": "Action to get the order history, product details, product availability and to update the order",
    "actionGroupState": "ENABLED",
    "actionGroupExecutor": {
        "customControl": "RETURN_CONTROL"
    },
    "functionSchema": {
        "functions": [{
            "name": "GetOrderDetails",
            "description": "Retrieves the order history for a given OrderId and returns productId, color, productName, size, productType, quantity, and status."
            "parameters": {
                "orderId": {
                    "type": "string",
                    "required": true
                }
            }
        }]
    }
}
```

## See Also
<a name="API_agent_CreateAgentActionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/CreateAgentActionGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/CreateAgentActionGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CreateAgentActionGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/CreateAgentActionGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CreateAgentActionGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/CreateAgentActionGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/CreateAgentActionGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/CreateAgentActionGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/CreateAgentActionGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CreateAgentActionGroup) 