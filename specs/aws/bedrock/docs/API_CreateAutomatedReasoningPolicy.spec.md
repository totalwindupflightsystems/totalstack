---
id: "@specs/aws/bedrock/docs/API_CreateAutomatedReasoningPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAutomatedReasoningPolicy"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreateAutomatedReasoningPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_CreateAutomatedReasoningPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAutomatedReasoningPolicy
<a name="API_CreateAutomatedReasoningPolicy"></a>

Creates an Automated Reasoning policy for Amazon Bedrock Guardrails. Automated Reasoning policies use mathematical techniques to detect hallucinations, suggest corrections, and highlight unstated assumptions in the responses of your GenAI application.

To create a policy, you upload a source document that describes the rules that you're encoding. Automated Reasoning extracts important concepts from the source document that will become variables in the policy and infers policy rules.

## Request Syntax
<a name="API_CreateAutomatedReasoningPolicy_RequestSyntax"></a>

```
POST /automated-reasoning-policies HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "description": "{{string}}",
   "kmsKeyId": "{{string}}",
   "name": "{{string}}",
   "policyDefinition": { 
      "rules": [ 
         { 
            "alternateExpression": "{{string}}",
            "expression": "{{string}}",
            "id": "{{string}}"
         }
      ],
      "types": [ 
         { 
            "description": "{{string}}",
            "name": "{{string}}",
            "values": [ 
               { 
                  "description": "{{string}}",
                  "value": "{{string}}"
               }
            ]
         }
      ],
      "variables": [ 
         { 
            "description": "{{string}}",
            "name": "{{string}}",
            "type": "{{string}}"
         }
      ],
      "version": "{{string}}"
   },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateAutomatedReasoningPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAutomatedReasoningPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateAutomatedReasoningPolicy_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicy-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [description](#API_CreateAutomatedReasoningPolicy_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicy-request-description"></a>
A description of the Automated Reasoning policy. Use this to provide context about the policy's purpose and the types of validations it performs.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: No

 ** [kmsKeyId](#API_CreateAutomatedReasoningPolicy_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicy-request-kmsKeyId"></a>
The identifier of the AWS KMS key to use for encrypting the automated reasoning policy and its associated artifacts. If you don't specify a AWS KMS key, Amazon Bedrock uses an AWS KMS managed key for encryption. For enhanced security and control, you can specify a customer managed AWS KMS key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)`   
Required: No

 ** [name](#API_CreateAutomatedReasoningPolicy_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicy-request-name"></a>
A unique name for the Automated Reasoning policy. The name must be between 1 and 63 characters and can contain letters, numbers, hyphens, and underscores.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_ ]+`   
Required: Yes

 ** [policyDefinition](#API_CreateAutomatedReasoningPolicy_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicy-request-policyDefinition"></a>
The policy definition that contains the formal logic rules, variables, and custom variable types used to validate foundation model responses in your application.  
Type: [AutomatedReasoningPolicyDefinition](API_AutomatedReasoningPolicyDefinition.md) object  
Required: No

 ** [tags](#API_CreateAutomatedReasoningPolicy_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicy-request-tags"></a>
A list of tags to associate with the Automated Reasoning policy. Tags help you organize and manage your policies.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateAutomatedReasoningPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "definitionHash": "string",
   "description": "string",
   "name": "string",
   "policyArn": "string",
   "updatedAt": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_CreateAutomatedReasoningPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicy-response-createdAt"></a>
The timestamp when the policy was created.  
Type: Timestamp

 ** [definitionHash](#API_CreateAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicy-response-definitionHash"></a>
The hash of the policy definition. This is used as a concurrency token for creating policy versions that you can use in your application.  
Type: String  
Length Constraints: Fixed length of 128.  
Pattern: `[0-9a-z]{128}` 

 ** [description](#API_CreateAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicy-response-description"></a>
The description of the Automated Reasoning policy.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+` 

 ** [name](#API_CreateAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicy-response-name"></a>
The name of the Automated Reasoning policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_ ]+` 

 ** [policyArn](#API_CreateAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicy-response-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy that you created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?` 

 ** [updatedAt](#API_CreateAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicy-response-updatedAt"></a>
The timestamp when the policy was last updated.  
Type: Timestamp

 ** [version](#API_CreateAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicy-response-version"></a>
The version number of the newly created Automated Reasoning policy. The initial version is always DRAFT.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 12.  
Pattern: `([1-9][0-9]{0,11})` 

## Errors
<a name="API_CreateAutomatedReasoningPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
Error occurred because of a conflict while performing an operation.  
HTTP Status Code: 400

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 400

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** TooManyTagsException **   
The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request.     
 ** resourceName **   
The name of the resource with too many tags.
HTTP Status Code: 400

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_CreateAutomatedReasoningPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateAutomatedReasoningPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateAutomatedReasoningPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateAutomatedReasoningPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateAutomatedReasoningPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateAutomatedReasoningPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateAutomatedReasoningPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateAutomatedReasoningPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateAutomatedReasoningPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateAutomatedReasoningPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateAutomatedReasoningPolicy) 