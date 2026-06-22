---
id: "@specs/aws/bedrock-agent/docs/API_agent_CreatePromptVersion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreatePromptVersion"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# CreatePromptVersion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_CreatePromptVersion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreatePromptVersion
<a name="API_agent_CreatePromptVersion"></a>

Creates a static snapshot of your prompt that can be deployed to production. For more information, see [Deploy prompts using Prompt management by creating versions](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_CreatePromptVersion_RequestSyntax"></a>

```
POST /prompts/{{promptIdentifier}}/versions HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_agent_CreatePromptVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [promptIdentifier](#API_agent_CreatePromptVersion_RequestSyntax) **   <a name="bedrock-agent_CreatePromptVersion-request-uri-promptIdentifier"></a>
The unique identifier of the prompt that you want to create a version of.  
Pattern: `([0-9a-zA-Z]{10})|(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10})(?::[0-9]{1,5})?`   
Required: Yes

## Request Body
<a name="API_agent_CreatePromptVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_agent_CreatePromptVersion_RequestSyntax) **   <a name="bedrock-agent_CreatePromptVersion-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_agent_CreatePromptVersion_RequestSyntax) **   <a name="bedrock-agent_CreatePromptVersion-request-description"></a>
A description for the version of the prompt.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [tags](#API_agent_CreatePromptVersion_RequestSyntax) **   <a name="bedrock-agent_CreatePromptVersion-request-tags"></a>
Any tags that you want to attach to the version of the prompt. For more information, see [Tagging resources in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html).  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_agent_CreatePromptVersion_ResponseSyntax"></a>

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
<a name="API_agent_CreatePromptVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_agent_CreatePromptVersion_ResponseSyntax) **   <a name="bedrock-agent_CreatePromptVersion-response-arn"></a>
The Amazon Resource Name (ARN) of the version of the prompt.  
Type: String  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10}(?::[0-9]{1,5})?)` 

 ** [createdAt](#API_agent_CreatePromptVersion_ResponseSyntax) **   <a name="bedrock-agent_CreatePromptVersion-response-createdAt"></a>
The time at which the prompt was created.  
Type: Timestamp

 ** [customerEncryptionKeyArn](#API_agent_CreatePromptVersion_ResponseSyntax) **   <a name="bedrock-agent_CreatePromptVersion-response-customerEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key to encrypt the version of the prompt.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [defaultVariant](#API_agent_CreatePromptVersion_ResponseSyntax) **   <a name="bedrock-agent_CreatePromptVersion-response-defaultVariant"></a>
The name of the default variant for the prompt. This value must match the `name` field in the relevant [PromptVariant](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html) object.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}` 

 ** [description](#API_agent_CreatePromptVersion_ResponseSyntax) **   <a name="bedrock-agent_CreatePromptVersion-response-description"></a>
A description for the version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [id](#API_agent_CreatePromptVersion_ResponseSyntax) **   <a name="bedrock-agent_CreatePromptVersion-response-id"></a>
The unique identifier of the prompt.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [name](#API_agent_CreatePromptVersion_ResponseSyntax) **   <a name="bedrock-agent_CreatePromptVersion-response-name"></a>
The name of the prompt.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}` 

 ** [updatedAt](#API_agent_CreatePromptVersion_ResponseSyntax) **   <a name="bedrock-agent_CreatePromptVersion-response-updatedAt"></a>
The time at which the prompt was last updated.  
Type: Timestamp

 ** [variants](#API_agent_CreatePromptVersion_ResponseSyntax) **   <a name="bedrock-agent_CreatePromptVersion-response-variants"></a>
A list of objects, each containing details about a variant of the prompt.  
Type: Array of [PromptVariant](API_agent_PromptVariant.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [version](#API_agent_CreatePromptVersion_ResponseSyntax) **   <a name="bedrock-agent_CreatePromptVersion-response-version"></a>
The version of the prompt that was created. Versions are numbered incrementally, starting from 1.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})` 

## Errors
<a name="API_agent_CreatePromptVersion_Errors"></a>

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
<a name="API_agent_CreatePromptVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/CreatePromptVersion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/CreatePromptVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CreatePromptVersion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/CreatePromptVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CreatePromptVersion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/CreatePromptVersion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/CreatePromptVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/CreatePromptVersion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/CreatePromptVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CreatePromptVersion) 