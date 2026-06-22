---
id: "@specs/aws/bedrock-agent/docs/API_CreateAutomatedReasoningPolicyVersion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAutomatedReasoningPolicyVersion"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# CreateAutomatedReasoningPolicyVersion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_CreateAutomatedReasoningPolicyVersion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAutomatedReasoningPolicyVersion
<a name="API_CreateAutomatedReasoningPolicyVersion"></a>

Creates a new version of an existing Automated Reasoning policy. This allows you to iterate on your policy rules while maintaining previous versions for rollback or comparison purposes.

## Request Syntax
<a name="API_CreateAutomatedReasoningPolicyVersion_RequestSyntax"></a>

```
POST /automated-reasoning-policies/{{policyArn}}/versions HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "lastUpdatedDefinitionHash": "{{string}}",
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateAutomatedReasoningPolicyVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyArn](#API_CreateAutomatedReasoningPolicyVersion_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyVersion-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to create a version.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_CreateAutomatedReasoningPolicyVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateAutomatedReasoningPolicyVersion_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyVersion-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [lastUpdatedDefinitionHash](#API_CreateAutomatedReasoningPolicyVersion_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyVersion-request-lastUpdatedDefinitionHash"></a>
The hash of the current policy definition used as a concurrency token to ensure the policy hasn't been modified since you last retrieved it.  
Type: String  
Length Constraints: Fixed length of 128.  
Pattern: `[0-9a-z]{128}`   
Required: Yes

 ** [tags](#API_CreateAutomatedReasoningPolicyVersion_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyVersion-request-tags"></a>
A list of tags to associate with the policy version.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateAutomatedReasoningPolicyVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "definitionHash": "string",
   "description": "string",
   "name": "string",
   "policyArn": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_CreateAutomatedReasoningPolicyVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateAutomatedReasoningPolicyVersion_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyVersion-response-createdAt"></a>
The timestamp when the policy version was created.  
Type: Timestamp

 ** [definitionHash](#API_CreateAutomatedReasoningPolicyVersion_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyVersion-response-definitionHash"></a>
The hash of the policy definition for this version.  
Type: String  
Length Constraints: Fixed length of 128.  
Pattern: `[0-9a-z]{128}` 

 ** [description](#API_CreateAutomatedReasoningPolicyVersion_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyVersion-response-description"></a>
The description of the policy version.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+` 

 ** [name](#API_CreateAutomatedReasoningPolicyVersion_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyVersion-response-name"></a>
The name of the policy version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_ ]+` 

 ** [policyArn](#API_CreateAutomatedReasoningPolicyVersion_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyVersion-response-policyArn"></a>
The versioned Amazon Resource Name (ARN) of the policy version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?` 

 ** [version](#API_CreateAutomatedReasoningPolicyVersion_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyVersion-response-version"></a>
The version number of the policy version.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 12.  
Pattern: `([1-9][0-9]{0,11})` 

## Errors
<a name="API_CreateAutomatedReasoningPolicyVersion_Errors"></a>

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
<a name="API_CreateAutomatedReasoningPolicyVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateAutomatedReasoningPolicyVersion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateAutomatedReasoningPolicyVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateAutomatedReasoningPolicyVersion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateAutomatedReasoningPolicyVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateAutomatedReasoningPolicyVersion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateAutomatedReasoningPolicyVersion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateAutomatedReasoningPolicyVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateAutomatedReasoningPolicyVersion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateAutomatedReasoningPolicyVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateAutomatedReasoningPolicyVersion) 