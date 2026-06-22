---
id: "@specs/aws/bedrock-agent/docs/API_agent_ListPrompts"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListPrompts"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListPrompts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_ListPrompts
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListPrompts
<a name="API_agent_ListPrompts"></a>

Returns either information about the working draft (`DRAFT` version) of each prompt in an account, or information about of all versions of a prompt, depending on whether you include the `promptIdentifier` field or not. For more information, see [View information about prompts using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-view.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_ListPrompts_RequestSyntax"></a>

```
GET /prompts/?maxResults={{maxResults}}&nextToken={{nextToken}}&promptIdentifier={{promptIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_ListPrompts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_agent_ListPrompts_RequestSyntax) **   <a name="bedrock-agent_ListPrompts-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_agent_ListPrompts_RequestSyntax) **   <a name="bedrock-agent_ListPrompts-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [promptIdentifier](#API_agent_ListPrompts_RequestSyntax) **   <a name="bedrock-agent_ListPrompts-request-uri-promptIdentifier"></a>
The unique identifier of the prompt for whose versions you want to return information. Omit this field to list information about all prompts in an account.  
Pattern: `([0-9a-zA-Z]{10})|(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10})(?::[0-9]{1,5})?` 

## Request Body
<a name="API_agent_ListPrompts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_ListPrompts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "promptSummaries": [ 
      { 
         "arn": "string",
         "createdAt": "string",
         "description": "string",
         "id": "string",
         "name": "string",
         "updatedAt": "string",
         "version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_agent_ListPrompts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_agent_ListPrompts_ResponseSyntax) **   <a name="bedrock-agent_ListPrompts-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [promptSummaries](#API_agent_ListPrompts_ResponseSyntax) **   <a name="bedrock-agent_ListPrompts-response-promptSummaries"></a>
A list, each member of which contains information about a prompt using Prompt management.  
Type: Array of [PromptSummary](API_agent_PromptSummary.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

## Errors
<a name="API_agent_ListPrompts_Errors"></a>

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
<a name="API_agent_ListPrompts_Examples"></a>

### List information about all prompts in an account
<a name="API_agent_ListPrompts_Example_1"></a>

The following request returns information about the working draft of each prompt in the account:

```
GET /prompts/ HTTP/1.1
```

### List information about all the versions of a prompt
<a name="API_agent_ListPrompts_Example_2"></a>

The following request returns information about all versions of the prompt in the account with the identifier `PROMPT12345`:

```
GET /prompts?promptIdentifier=PROMPT12345 HTTP/1.1
```

## See Also
<a name="API_agent_ListPrompts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/ListPrompts) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/ListPrompts) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ListPrompts) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/ListPrompts) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ListPrompts) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/ListPrompts) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/ListPrompts) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/ListPrompts) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/ListPrompts) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ListPrompts) 