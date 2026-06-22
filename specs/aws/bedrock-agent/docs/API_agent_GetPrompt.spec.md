---
id: "@specs/aws/bedrock-agent/docs/API_agent_GetPrompt"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetPrompt"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetPrompt

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_GetPrompt
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetPrompt
<a name="API_agent_GetPrompt"></a>

Retrieves information about the working draft (`DRAFT` version) of a prompt or a version of it, depending on whether you include the `promptVersion` field or not. For more information, see [View information about prompts using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-view.html) and [View information about a version of your prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html#prompt-management-versions-view.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_GetPrompt_RequestSyntax"></a>

```
GET /prompts/{{promptIdentifier}}/?promptVersion={{promptVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_GetPrompt_RequestParameters"></a>

The request uses the following URI parameters.

 ** [promptIdentifier](#API_agent_GetPrompt_RequestSyntax) **   <a name="bedrock-agent_GetPrompt-request-uri-promptIdentifier"></a>
The unique identifier of the prompt.  
Pattern: `([0-9a-zA-Z]{10})|(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10})(?::[0-9]{1,5})?`   
Required: Yes

 ** [promptVersion](#API_agent_GetPrompt_RequestSyntax) **   <a name="bedrock-agent_GetPrompt-request-uri-promptVersion"></a>
The version of the prompt about which you want to retrieve information. Omit this field to return information about the working draft of the prompt.  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})` 

## Request Body
<a name="API_agent_GetPrompt_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_GetPrompt_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": "string",
   "customerEncryptionKeyArn": "string",
   "defaultVariant": "string",
   "description": "string",
   "id": "string",
   "name": "string",
   "updatedAt": "string",
   "variants": [ 
      { 
         "additionalModelRequestFields": JSON value,
         "genAiResource": { ... },
         "inferenceConfiguration": { ... },
         "metadata": [ 
            { 
               "key": "string",
               "value": "string"
            }
         ],
         "modelId": "string",
         "name": "string",
         "templateConfiguration": { ... },
         "templateType": "string"
      }
   ],
   "version": "string"
}
```

## Response Elements
<a name="API_agent_GetPrompt_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_agent_GetPrompt_ResponseSyntax) **   <a name="bedrock-agent_GetPrompt-response-arn"></a>
The Amazon Resource Name (ARN) of the prompt or the prompt version (if you specified a version in the request).  
Type: String  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10}(?::[0-9]{1,5})?)` 

 ** [createdAt](#API_agent_GetPrompt_ResponseSyntax) **   <a name="bedrock-agent_GetPrompt-response-createdAt"></a>
The time at which the prompt was created.  
Type: Timestamp

 ** [customerEncryptionKeyArn](#API_agent_GetPrompt_ResponseSyntax) **   <a name="bedrock-agent_GetPrompt-response-customerEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key that the prompt is encrypted with.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [defaultVariant](#API_agent_GetPrompt_ResponseSyntax) **   <a name="bedrock-agent_GetPrompt-response-defaultVariant"></a>
The name of the default variant for the prompt. This value must match the `name` field in the relevant [PromptVariant](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html) object.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}` 

 ** [description](#API_agent_GetPrompt_ResponseSyntax) **   <a name="bedrock-agent_GetPrompt-response-description"></a>
The descriptino of the prompt.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [id](#API_agent_GetPrompt_ResponseSyntax) **   <a name="bedrock-agent_GetPrompt-response-id"></a>
The unique identifier of the prompt.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [name](#API_agent_GetPrompt_ResponseSyntax) **   <a name="bedrock-agent_GetPrompt-response-name"></a>
The name of the prompt.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}` 

 ** [updatedAt](#API_agent_GetPrompt_ResponseSyntax) **   <a name="bedrock-agent_GetPrompt-response-updatedAt"></a>
The time at which the prompt was last updated.  
Type: Timestamp

 ** [variants](#API_agent_GetPrompt_ResponseSyntax) **   <a name="bedrock-agent_GetPrompt-response-variants"></a>
A list of objects, each containing details about a variant of the prompt.  
Type: Array of [PromptVariant](API_agent_PromptVariant.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [version](#API_agent_GetPrompt_ResponseSyntax) **   <a name="bedrock-agent_GetPrompt-response-version"></a>
The version of the prompt.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})` 

## Errors
<a name="API_agent_GetPrompt_Errors"></a>

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
<a name="API_agent_GetPrompt_Examples"></a>

### Get information about the working draft of a prompt
<a name="API_agent_GetPrompt_Example_1"></a>

The following request returns information about the working draft of the prompt in the account with the identifier `PROMPT12345`:

```
GET /prompts/PROMPT12345 HTTP/1.1
```

### List information about all the versions of a prompt
<a name="API_agent_GetPrompt_Example_2"></a>

The following request returns information about version `2` of the prompt in the account with the identifier `PROMPT12345`:

```
GET /prompts/PROMPT12345?promptVersion=2 HTTP/1.1
```

## See Also
<a name="API_agent_GetPrompt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/GetPrompt) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/GetPrompt) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/GetPrompt) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/GetPrompt) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/GetPrompt) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/GetPrompt) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/GetPrompt) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/GetPrompt) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/GetPrompt) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/GetPrompt) 