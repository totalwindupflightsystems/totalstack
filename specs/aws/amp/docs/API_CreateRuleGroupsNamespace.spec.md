---
id: "@specs/aws/amp/docs/API_CreateRuleGroupsNamespace"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateRuleGroupsNamespace"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# CreateRuleGroupsNamespace

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_CreateRuleGroupsNamespace
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateRuleGroupsNamespace
<a name="API_CreateRuleGroupsNamespace"></a>

The `CreateRuleGroupsNamespace` operation creates a rule groups namespace within a workspace. A rule groups namespace is associated with exactly one rules file. A workspace can have multiple rule groups namespaces.

**Important**  
The combined length of a rule group namespace and a rule group name cannot exceed 721 UTF-8 bytes.

Use this operation only to create new rule groups namespaces. To update an existing rule groups namespace, use `PutRuleGroupsNamespace`.

## Request Syntax
<a name="API_CreateRuleGroupsNamespace_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/rulegroupsnamespaces HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "data": {{blob}},
   "name": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateRuleGroupsNamespace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_CreateRuleGroupsNamespace_RequestSyntax) **   <a name="prometheus-CreateRuleGroupsNamespace-request-uri-workspaceId"></a>
The ID of the workspace to add the rule groups namespace.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## Request Body
<a name="API_CreateRuleGroupsNamespace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateRuleGroupsNamespace_RequestSyntax) **   <a name="prometheus-CreateRuleGroupsNamespace-request-clientToken"></a>
A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+`   
Required: No

 ** [data](#API_CreateRuleGroupsNamespace_RequestSyntax) **   <a name="prometheus-CreateRuleGroupsNamespace-request-data"></a>
The rules file to use in the new namespace.  
Contains the base64-encoded version of the YAML rules file.  
For details about the rule groups namespace structure, see [RuleGroupsNamespaceData](https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-RuleGroupsNamespaceData.html).  
Type: Base64-encoded binary data object  
Required: Yes

 ** [name](#API_CreateRuleGroupsNamespace_RequestSyntax) **   <a name="prometheus-CreateRuleGroupsNamespace-request-name"></a>
The name for the new rule groups namespace.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

 ** [tags](#API_CreateRuleGroupsNamespace_RequestSyntax) **   <a name="prometheus-CreateRuleGroupsNamespace-request-tags"></a>
The list of tag keys and values to associate with the rule groups namespace.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Required: No

## Response Syntax
<a name="API_CreateRuleGroupsNamespace_ResponseSyntax"></a>

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
<a name="API_CreateRuleGroupsNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateRuleGroupsNamespace_ResponseSyntax) **   <a name="prometheus-CreateRuleGroupsNamespace-response-arn"></a>
The Amazon Resource Name (ARN) of the new rule groups namespace.  
Type: String

 ** [name](#API_CreateRuleGroupsNamespace_ResponseSyntax) **   <a name="prometheus-CreateRuleGroupsNamespace-response-name"></a>
The name of the new rule groups namespace.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*` 

 ** [status](#API_CreateRuleGroupsNamespace_ResponseSyntax) **   <a name="prometheus-CreateRuleGroupsNamespace-response-status"></a>
A structure that returns the current status of the rule groups namespace.  
Type: [RuleGroupsNamespaceStatus](API_RuleGroupsNamespaceStatus.md) object

 ** [tags](#API_CreateRuleGroupsNamespace_ResponseSyntax) **   <a name="prometheus-CreateRuleGroupsNamespace-response-tags"></a>
The list of tag keys and values that are associated with the namespace.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)` 

## Errors
<a name="API_CreateRuleGroupsNamespace_Errors"></a>

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
<a name="API_CreateRuleGroupsNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/CreateRuleGroupsNamespace) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/CreateRuleGroupsNamespace) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/CreateRuleGroupsNamespace) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/CreateRuleGroupsNamespace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/CreateRuleGroupsNamespace) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/CreateRuleGroupsNamespace) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/CreateRuleGroupsNamespace) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/CreateRuleGroupsNamespace) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/CreateRuleGroupsNamespace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/CreateRuleGroupsNamespace) 