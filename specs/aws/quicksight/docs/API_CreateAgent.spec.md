---
id: "@specs/aws/quicksight/docs/API_CreateAgent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAgent"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateAgent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateAgent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAgent
<a name="API_CreateAgent"></a>

Creates an agent in Amazon QuickSight.

## Request Syntax
<a name="API_CreateAgent_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/agents HTTP/1.1
Content-type: application/json

{
   "ActionConnectors": [ "{{string}}" ],
   "AgentId": "{{string}}",
   "AgentLifecycle": "{{string}}",
   "CustomPromptInput": { ... },
   "Description": "{{string}}",
   "IconId": "{{string}}",
   "Name": "{{string}}",
   "Spaces": [ "{{string}}" ],
   "StarterPrompts": [ "{{string}}" ],
   "WelcomeMessage": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAgent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateAgent_RequestSyntax) **   <a name="QS-CreateAgent-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the agent.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_CreateAgent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AgentId](#API_CreateAgent_RequestSyntax) **   <a name="QS-CreateAgent-request-AgentId"></a>
A unique identifier for the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_.+]+`   
Required: Yes

 ** [Name](#API_CreateAgent_RequestSyntax) **   <a name="QS-CreateAgent-request-Name"></a>
The name of the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `(?!\s*$).+`   
Required: Yes

 ** [ActionConnectors](#API_CreateAgent_RequestSyntax) **   <a name="QS-CreateAgent-request-ActionConnectors"></a>
The Amazon Resource Names (ARNs) of the action connectors to attach to the agent.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [AgentLifecycle](#API_CreateAgent_RequestSyntax) **   <a name="QS-CreateAgent-request-AgentLifecycle"></a>
The lifecycle state of the agent. Valid values are `PREVIEW` and `PUBLISHED`.  
Type: String  
Valid Values: `PREVIEW | PUBLISHED`   
Required: No

 ** [CustomPromptInput](#API_CreateAgent_RequestSyntax) **   <a name="QS-CreateAgent-request-CustomPromptInput"></a>
The custom prompt configuration for the agent.  
Type: [CustomPromptInput](API_CustomPromptInput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [Description](#API_CreateAgent_RequestSyntax) **   <a name="QS-CreateAgent-request-Description"></a>
A description of the agent.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `\P{C}*`   
Required: No

 ** [IconId](#API_CreateAgent_RequestSyntax) **   <a name="QS-CreateAgent-request-IconId"></a>
The icon identifier for the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [Spaces](#API_CreateAgent_RequestSyntax) **   <a name="QS-CreateAgent-request-Spaces"></a>
The Amazon Resource Names (ARNs) of the spaces to attach to the agent.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [StarterPrompts](#API_CreateAgent_RequestSyntax) **   <a name="QS-CreateAgent-request-StarterPrompts"></a>
A list of starter prompts that are displayed to users when they begin interacting with the agent.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 3 items.  
Length Constraints: Minimum length of 0. Maximum length of 100.  
Required: No

 ** [WelcomeMessage](#API_CreateAgent_RequestSyntax) **   <a name="QS-CreateAgent-request-WelcomeMessage"></a>
The welcome message that is displayed when a user starts a conversation with the agent.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 300.  
Required: No

## Response Syntax
<a name="API_CreateAgent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AgentId": "string",
   "AgentName": "string",
   "AgentStatus": "string",
   "Arn": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_CreateAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AgentId](#API_CreateAgent_ResponseSyntax) **   <a name="QS-CreateAgent-response-AgentId"></a>
The unique identifier for the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_.+]+` 

 ** [AgentName](#API_CreateAgent_ResponseSyntax) **   <a name="QS-CreateAgent-response-AgentName"></a>
The name of the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `(?!\s*$).+` 

 ** [AgentStatus](#API_CreateAgent_ResponseSyntax) **   <a name="QS-CreateAgent-response-AgentStatus"></a>
The status of the agent.  
Type: String  
Valid Values: `ACTIVE | UPDATING | FAILED | CREATING` 

 ** [Arn](#API_CreateAgent_ResponseSyntax) **   <a name="QS-CreateAgent-response-Arn"></a>
The Amazon Resource Name (ARN) of the agent.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1284.  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}` 

 ** [RequestId](#API_CreateAgent_ResponseSyntax) **   <a name="QS-CreateAgent-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_CreateAgent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **   
Updating or deleting a resource can cause an inconsistent state.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **   
One or more preconditions aren't met.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceExistsException **   
The resource specified already exists.     
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 409

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_CreateAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateAgent) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateAgent) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateAgent) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateAgent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateAgent) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateAgent) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateAgent) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateAgent) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateAgent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateAgent) 