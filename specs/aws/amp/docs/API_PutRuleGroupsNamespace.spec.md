---
id: "@specs/aws/amp/docs/API_PutRuleGroupsNamespace"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutRuleGroupsNamespace"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# PutRuleGroupsNamespace

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_PutRuleGroupsNamespace
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutRuleGroupsNamespace
<a name="API_PutRuleGroupsNamespace"></a>

Updates an existing rule groups namespace within a workspace. A rule groups namespace is associated with exactly one rules file. A workspace can have multiple rule groups namespaces.

**Important**  
The combined length of a rule group namespace and a rule group name cannot exceed 721 UTF-8 bytes.

Use this operation only to update existing rule groups namespaces. To create a new rule groups namespace, use `CreateRuleGroupsNamespace`.

You can't use this operation to add tags to an existing rule groups namespace. Instead, use `TagResource`.

## Request Syntax
<a name="API_PutRuleGroupsNamespace_RequestSyntax"></a>

```
PUT /workspaces/{{workspaceId}}/rulegroupsnamespaces/{{name}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "data": {{blob}}
}
```

## URI Request Parameters
<a name="API_PutRuleGroupsNamespace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_PutRuleGroupsNamespace_RequestSyntax) **   <a name="prometheus-PutRuleGroupsNamespace-request-uri-name"></a>
The name of the rule groups namespace that you are updating.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

 ** [workspaceId](#API_PutRuleGroupsNamespace_RequestSyntax) **   <a name="prometheus-PutRuleGroupsNamespace-request-uri-workspaceId"></a>
The ID of the workspace where you are updating the rule groups namespace.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## Request Body
<a name="API_PutRuleGroupsNamespace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_PutRuleGroupsNamespace_RequestSyntax) **   <a name="prometheus-PutRuleGroupsNamespace-request-clientToken"></a>
A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+`   
Required: No

 ** [data](#API_PutRuleGroupsNamespace_RequestSyntax) **   <a name="prometheus-PutRuleGroupsNamespace-request-data"></a>
The new rules file to use in the namespace. A base64-encoded version of the YAML rule groups file.  
For details about the rule groups namespace structure, see [RuleGroupsNamespaceData](https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-RuleGroupsNamespaceData.html).  
Type: Base64-encoded binary data object  
Required: Yes

## Response Syntax
<a name="API_PutRuleGroupsNamespace_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "arn": "string",
   "name": "string",
   "status": { 
      "statusCode": "string",
      "statusReason": "string"
   },
   "tags": { 
      "string" : "string" 
   }
}
```

## Response Elements
<a name="API_PutRuleGroupsNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_PutRuleGroupsNamespace_ResponseSyntax) **   <a name="prometheus-PutRuleGroupsNamespace-response-arn"></a>
The ARN of the rule groups namespace.  
Type: String

 ** [name](#API_PutRuleGroupsNamespace_ResponseSyntax) **   <a name="prometheus-PutRuleGroupsNamespace-response-name"></a>
The name of the rule groups namespace that was updated.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*` 

 ** [status](#API_PutRuleGroupsNamespace_ResponseSyntax) **   <a name="prometheus-PutRuleGroupsNamespace-response-status"></a>
A structure that includes the current status of the rule groups namespace.  
Type: [RuleGroupsNamespaceStatus](API_RuleGroupsNamespaceStatus.md) object

 ** [tags](#API_PutRuleGroupsNamespace_ResponseSyntax) **   <a name="prometheus-PutRuleGroupsNamespace-response-tags"></a>
The list of tag keys and values that are associated with the namespace.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)` 

## Errors
<a name="API_PutRuleGroupsNamespace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.    
 ** message **   
Description of the error.
HTTP Status Code: 403

 ** ConflictException **   
The request would cause an inconsistent state.    
 ** message **   
Description of the error.  
 ** resourceId **   
Identifier of the resource affected.  
 ** resourceType **   
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **   
An unexpected error occurred during the processing of the request.    
 ** message **   
Description of the error.  
 ** retryAfterSeconds **   
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The request references a resources that doesn't exist.    
 ** message **   
Description of the error.  
 ** resourceId **   
Identifier of the resource affected.  
 ** resourceType **   
Type of the resource affected.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
Completing the request would cause a service quota to be exceeded.    
 ** message **   
Description of the error.  
 ** quotaCode **   
Service quotas code of the originating quota.  
 ** resourceId **   
Identifier of the resource affected.  
 ** resourceType **   
Type of the resource affected.  
 ** serviceCode **   
Service quotas code for the originating service.
HTTP Status Code: 402

 ** ThrottlingException **   
The request was denied due to request throttling.    
 ** message **   
Description of the error.  
 ** quotaCode **   
Service quotas code for the originating quota.  
 ** retryAfterSeconds **   
Advice to clients on when the call can be safely retried.  
 ** serviceCode **   
Service quotas code for the originating service.
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by an AWS service.    
 ** fieldList **   
The field that caused the error, if applicable.  
 ** message **   
Description of the error.  
 ** reason **   
Reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_PutRuleGroupsNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/PutRuleGroupsNamespace) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/PutRuleGroupsNamespace) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/PutRuleGroupsNamespace) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/PutRuleGroupsNamespace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/PutRuleGroupsNamespace) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/PutRuleGroupsNamespace) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/PutRuleGroupsNamespace) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/PutRuleGroupsNamespace) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/PutRuleGroupsNamespace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/PutRuleGroupsNamespace) 