---
id: "@specs/aws/bedrock/docs/API_UpdateAutomatedReasoningPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateAutomatedReasoningPolicy"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# UpdateAutomatedReasoningPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_UpdateAutomatedReasoningPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateAutomatedReasoningPolicy
<a name="API_UpdateAutomatedReasoningPolicy"></a>

Updates an existing Automated Reasoning policy with new rules, variables, or configuration. This creates a new version of the policy while preserving the previous version.

## Request Syntax
<a name="API_UpdateAutomatedReasoningPolicy_RequestSyntax"></a>

```
PATCH /automated-reasoning-policies/{{policyArn}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
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
   }
}
```

## URI Request Parameters
<a name="API_UpdateAutomatedReasoningPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyArn](#API_UpdateAutomatedReasoningPolicy_RequestSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicy-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy to update. This must be the ARN of a draft policy.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_UpdateAutomatedReasoningPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateAutomatedReasoningPolicy_RequestSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicy-request-description"></a>
The updated description for the Automated Reasoning policy.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: No

 ** [name](#API_UpdateAutomatedReasoningPolicy_RequestSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicy-request-name"></a>
The updated name for the Automated Reasoning policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_ ]+`   
Required: No

 ** [policyDefinition](#API_UpdateAutomatedReasoningPolicy_RequestSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicy-request-policyDefinition"></a>
The updated policy definition containing the formal logic rules, variables, and types.  
Type: [AutomatedReasoningPolicyDefinition](API_AutomatedReasoningPolicyDefinition.md) object  
Required: Yes

## Response Syntax
<a name="API_UpdateAutomatedReasoningPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "definitionHash": "string",
   "name": "string",
   "policyArn": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateAutomatedReasoningPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [definitionHash](#API_UpdateAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicy-response-definitionHash"></a>
The hash of the updated policy definition.  
Type: String  
Length Constraints: Fixed length of 128.  
Pattern: `[0-9a-z]{128}` 

 ** [name](#API_UpdateAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicy-response-name"></a>
The updated name of the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_ ]+` 

 ** [policyArn](#API_UpdateAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicy-response-policyArn"></a>
The Amazon Resource Name (ARN) of the updated policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?` 

 ** [updatedAt](#API_UpdateAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicy-response-updatedAt"></a>
The timestamp when the policy was last updated.  
Type: Timestamp

## Errors
<a name="API_UpdateAutomatedReasoningPolicy_Errors"></a>

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
<a name="API_UpdateAutomatedReasoningPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/UpdateAutomatedReasoningPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/UpdateAutomatedReasoningPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/UpdateAutomatedReasoningPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/UpdateAutomatedReasoningPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/UpdateAutomatedReasoningPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/UpdateAutomatedReasoningPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/UpdateAutomatedReasoningPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/UpdateAutomatedReasoningPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/UpdateAutomatedReasoningPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/UpdateAutomatedReasoningPolicy) 