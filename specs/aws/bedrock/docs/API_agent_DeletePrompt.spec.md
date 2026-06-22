---
id: "@specs/aws/bedrock/docs/API_agent_DeletePrompt"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeletePrompt"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# DeletePrompt

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_DeletePrompt
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeletePrompt
<a name="API_agent_DeletePrompt"></a>

Deletes a prompt or a version of it, depending on whether you include the `promptVersion` field or not. For more information, see [Delete prompts from the Prompt management tool](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-delete.html) and [Delete a version of a prompt from the Prompt management tool](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html#prompt-management-versions-delete.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_DeletePrompt_RequestSyntax"></a>

```
DELETE /prompts/{{promptIdentifier}}/?promptVersion={{promptVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_DeletePrompt_RequestParameters"></a>

The request uses the following URI parameters.

 ** [promptIdentifier](#API_agent_DeletePrompt_RequestSyntax) **   <a name="bedrock-agent_DeletePrompt-request-uri-promptIdentifier"></a>
The unique identifier of the prompt.  
Pattern: `([0-9a-zA-Z]{10})|(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10})(?::[0-9]{1,5})?`   
Required: Yes

 ** [promptVersion](#API_agent_DeletePrompt_RequestSyntax) **   <a name="bedrock-agent_DeletePrompt-request-uri-promptVersion"></a>
The version of the prompt to delete. To delete the prompt, omit this field.  
Pattern: `[0-9]{1,5}` 

## Request Body
<a name="API_agent_DeletePrompt_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_DeletePrompt_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_agent_DeletePrompt_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_agent_DeletePrompt_ResponseSyntax) **   <a name="bedrock-agent_DeletePrompt-response-id"></a>
The unique identifier of the prompt that was deleted.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [version](#API_agent_DeletePrompt_ResponseSyntax) **   <a name="bedrock-agent_DeletePrompt-response-version"></a>
The version of the prompt that was deleted.  
Type: String  
Pattern: `[0-9]{1,5}` 

## Errors
<a name="API_agent_DeletePrompt_Errors"></a>

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

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.    
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## Examples
<a name="API_agent_DeletePrompt_Examples"></a>

### Delete a prompt
<a name="API_agent_DeletePrompt_Example_1"></a>

The following request deletes the prompt in the account with the identifier `PROMPT12345`:

```
DELETE /prompts/PROMPT12345/ HTTP/1.1
```

### Delete a version of a prompt
<a name="API_agent_DeletePrompt_Example_2"></a>

The following request deletes version `1` of the prompt in the account with the identifier `PROMPT12345`:

```
GET /prompts/PROMPT12345?promptVersion=1 HTTP/1.1
```

## See Also
<a name="API_agent_DeletePrompt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/DeletePrompt) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/DeletePrompt) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DeletePrompt) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/DeletePrompt) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DeletePrompt) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/DeletePrompt) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/DeletePrompt) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/DeletePrompt) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/DeletePrompt) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DeletePrompt) 