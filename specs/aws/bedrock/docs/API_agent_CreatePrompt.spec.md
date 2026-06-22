---
id: "@specs/aws/bedrock/docs/API_agent_CreatePrompt"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreatePrompt"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreatePrompt

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_CreatePrompt
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreatePrompt
<a name="API_agent_CreatePrompt"></a>

Creates a prompt in your prompt library that you can add to a flow. For more information, see [Prompt management in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html), [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) and [Prompt flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_CreatePrompt_RequestSyntax"></a>

```
POST /prompts/ HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "customerEncryptionKeyArn": "{{string}}",
   "defaultVariant": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "variants": [ 
      { 
         "additionalModelRequestFields": {{JSON value}},
         "genAiResource": { ... },
         "inferenceConfiguration": { ... },
         "metadata": [ 
            { 
               "key": "{{string}}",
               "value": "{{string}}"
            }
         ],
         "modelId": "{{string}}",
         "name": "{{string}}",
         "templateConfiguration": { ... },
         "templateType": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_agent_CreatePrompt_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_agent_CreatePrompt_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_agent_CreatePrompt_RequestSyntax) **   <a name="bedrock-agent_CreatePrompt-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [customerEncryptionKeyArn](#API_agent_CreatePrompt_RequestSyntax) **   <a name="bedrock-agent_CreatePrompt-request-customerEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key to encrypt the prompt.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [defaultVariant](#API_agent_CreatePrompt_RequestSyntax) **   <a name="bedrock-agent_CreatePrompt-request-defaultVariant"></a>
The name of the default variant for the prompt. This value must match the `name` field in the relevant [PromptVariant](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html) object.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: No

 ** [description](#API_agent_CreatePrompt_RequestSyntax) **   <a name="bedrock-agent_CreatePrompt-request-description"></a>
A description for the prompt.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [name](#API_agent_CreatePrompt_RequestSyntax) **   <a name="bedrock-agent_CreatePrompt-request-name"></a>
A name for the prompt.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** [tags](#API_agent_CreatePrompt_RequestSyntax) **   <a name="bedrock-agent_CreatePrompt-request-tags"></a>
Any tags that you want to attach to the prompt. For more information, see [Tagging resources in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html).  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** [variants](#API_agent_CreatePrompt_RequestSyntax) **   <a name="bedrock-agent_CreatePrompt-request-variants"></a>
A list of objects, each containing details about a variant of the prompt.  
Type: Array of [PromptVariant](API_agent_PromptVariant.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: No

## Response Syntax
<a name="API_agent_CreatePrompt_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_agent_CreatePrompt_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_agent_CreatePrompt_ResponseSyntax) **   <a name="bedrock-agent_CreatePrompt-response-arn"></a>
The Amazon Resource Name (ARN) of the prompt.  
Type: String  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10}(?::[0-9]{1,5})?)` 

 ** [createdAt](#API_agent_CreatePrompt_ResponseSyntax) **   <a name="bedrock-agent_CreatePrompt-response-createdAt"></a>
The time at which the prompt was created.  
Type: Timestamp

 ** [customerEncryptionKeyArn](#API_agent_CreatePrompt_ResponseSyntax) **   <a name="bedrock-agent_CreatePrompt-response-customerEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key that you encrypted the prompt with.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [defaultVariant](#API_agent_CreatePrompt_ResponseSyntax) **   <a name="bedrock-agent_CreatePrompt-response-defaultVariant"></a>
The name of the default variant for your prompt.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}` 

 ** [description](#API_agent_CreatePrompt_ResponseSyntax) **   <a name="bedrock-agent_CreatePrompt-response-description"></a>
The description of the prompt.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [id](#API_agent_CreatePrompt_ResponseSyntax) **   <a name="bedrock-agent_CreatePrompt-response-id"></a>
The unique identifier of the prompt.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [name](#API_agent_CreatePrompt_ResponseSyntax) **   <a name="bedrock-agent_CreatePrompt-response-name"></a>
The name of the prompt.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}` 

 ** [updatedAt](#API_agent_CreatePrompt_ResponseSyntax) **   <a name="bedrock-agent_CreatePrompt-response-updatedAt"></a>
The time at which the prompt was last updated.  
Type: Timestamp

 ** [variants](#API_agent_CreatePrompt_ResponseSyntax) **   <a name="bedrock-agent_CreatePrompt-response-variants"></a>
A list of objects, each containing details about a variant of the prompt.  
Type: Array of [PromptVariant](API_agent_PromptVariant.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [version](#API_agent_CreatePrompt_ResponseSyntax) **   <a name="bedrock-agent_CreatePrompt-response-version"></a>
The version of the prompt. When you create a prompt, the version created is the `DRAFT` version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})` 

## Errors
<a name="API_agent_CreatePrompt_Errors"></a>

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
<a name="API_agent_CreatePrompt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/CreatePrompt) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/CreatePrompt) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CreatePrompt) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/CreatePrompt) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CreatePrompt) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/CreatePrompt) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/CreatePrompt) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/CreatePrompt) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/CreatePrompt) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CreatePrompt) 