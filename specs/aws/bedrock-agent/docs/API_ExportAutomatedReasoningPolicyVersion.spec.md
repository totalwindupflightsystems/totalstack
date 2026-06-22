---
id: "@specs/aws/bedrock-agent/docs/API_ExportAutomatedReasoningPolicyVersion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExportAutomatedReasoningPolicyVersion"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ExportAutomatedReasoningPolicyVersion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_ExportAutomatedReasoningPolicyVersion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExportAutomatedReasoningPolicyVersion
<a name="API_ExportAutomatedReasoningPolicyVersion"></a>

Exports the policy definition for an Automated Reasoning policy version. Returns the complete policy definition including rules, variables, and custom variable types in a structured format.

## Request Syntax
<a name="API_ExportAutomatedReasoningPolicyVersion_RequestSyntax"></a>

```
GET /automated-reasoning-policies/{{policyArn}}/export HTTP/1.1
```

## URI Request Parameters
<a name="API_ExportAutomatedReasoningPolicyVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyArn](#API_ExportAutomatedReasoningPolicyVersion_RequestSyntax) **   <a name="bedrock-ExportAutomatedReasoningPolicyVersion-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy to export. Can be either the unversioned ARN for the draft policy or a versioned ARN for a specific policy version.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_ExportAutomatedReasoningPolicyVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ExportAutomatedReasoningPolicyVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "rules": [ 
      { 
         "alternateExpression": "string",
         "expression": "string",
         "id": "string"
      }
   ],
   "types": [ 
      { 
         "description": "string",
         "name": "string",
         "values": [ 
            { 
               "description": "string",
               "value": "string"
            }
         ]
      }
   ],
   "variables": [ 
      { 
         "description": "string",
         "name": "string",
         "type": "string"
      }
   ],
   "version": "string"
}
```

## Response Elements
<a name="API_ExportAutomatedReasoningPolicyVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [rules](#API_ExportAutomatedReasoningPolicyVersion_ResponseSyntax) **   <a name="bedrock-ExportAutomatedReasoningPolicyVersion-response-rules"></a>
The formal logic rules extracted from the source document. Rules define the logical constraints that determine whether model responses are valid, invalid, or satisfiable.  
Type: Array of [AutomatedReasoningPolicyDefinitionRule](API_AutomatedReasoningPolicyDefinitionRule.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1500 items.

 ** [types](#API_ExportAutomatedReasoningPolicyVersion_ResponseSyntax) **   <a name="bedrock-ExportAutomatedReasoningPolicyVersion-response-types"></a>
The custom user-defined vairable types used in the policy. Types are enum-based variable types that provide additional context beyond the predefined variable types.  
Type: Array of [AutomatedReasoningPolicyDefinitionType](API_AutomatedReasoningPolicyDefinitionType.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 150 items.

 ** [variables](#API_ExportAutomatedReasoningPolicyVersion_ResponseSyntax) **   <a name="bedrock-ExportAutomatedReasoningPolicyVersion-response-variables"></a>
The variables that represent concepts in the policy. Variables can have values assigned when translating natural language into formal logic. Their descriptions are crucial for accurate translation.  
Type: Array of [AutomatedReasoningPolicyDefinitionVariable](API_AutomatedReasoningPolicyDefinitionVariable.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 600 items.

 ** [version](#API_ExportAutomatedReasoningPolicyVersion_ResponseSyntax) **   <a name="bedrock-ExportAutomatedReasoningPolicyVersion-response-version"></a>
The version of the policy definition format.  
Type: String

## Errors
<a name="API_ExportAutomatedReasoningPolicyVersion_Errors"></a>

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
HTTP Status Code: 400

## See Also
<a name="API_ExportAutomatedReasoningPolicyVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ExportAutomatedReasoningPolicyVersion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ExportAutomatedReasoningPolicyVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ExportAutomatedReasoningPolicyVersion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ExportAutomatedReasoningPolicyVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ExportAutomatedReasoningPolicyVersion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ExportAutomatedReasoningPolicyVersion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ExportAutomatedReasoningPolicyVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ExportAutomatedReasoningPolicyVersion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ExportAutomatedReasoningPolicyVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ExportAutomatedReasoningPolicyVersion) 