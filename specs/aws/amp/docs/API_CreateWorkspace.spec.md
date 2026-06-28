---
id: "@specs/aws/amp/docs/API_CreateWorkspace"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateWorkspace"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# CreateWorkspace

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_CreateWorkspace
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateWorkspace
<a name="API_CreateWorkspace"></a>

Creates a Prometheus workspace. A workspace is a logical space dedicated to the storage and querying of Prometheus metrics. You can have one or more workspaces in each Region in your account.

## Request Syntax
<a name="API_CreateWorkspace_RequestSyntax"></a>

```
POST /workspaces HTTP/1.1
Content-type: application/json

{
   "alias": "{{string}}",
   "clientToken": "{{string}}",
   "kmsKeyArn": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateWorkspace_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWorkspace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [alias](#API_CreateWorkspace_RequestSyntax) **   <a name="prometheus-CreateWorkspace-request-alias"></a>
An alias that you assign to this workspace to help you identify it. It does not need to be unique.  
Blank spaces at the beginning or end of the alias that you specify will be trimmed from the value used.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** [clientToken](#API_CreateWorkspace_RequestSyntax) **   <a name="prometheus-CreateWorkspace-request-clientToken"></a>
A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+`   
Required: No

 ** [kmsKeyArn](#API_CreateWorkspace_RequestSyntax) **   <a name="prometheus-CreateWorkspace-request-kmsKeyArn"></a>
(optional) The ARN for a customer managed AWS KMS key to use for encrypting data within your workspace. For more information about using your own key in your workspace, see [Encryption at rest](https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html) in the *Amazon Managed Service for Prometheus User Guide*.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws[-a-z]*:kms:[-a-z0-9]+:[0-9]{12}:key/[-a-f0-9]+`   
Required: No

 ** [tags](#API_CreateWorkspace_RequestSyntax) **   <a name="prometheus-CreateWorkspace-request-tags"></a>
The list of tag keys and values to associate with the workspace.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Required: No

## Response Syntax
<a name="API_CreateWorkspace_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "arn": "string",
   "kmsKeyArn": "string",
   "status": { 
      "statusCode": "string"
   },
   "tags": { 
      "string" : "string" 
   },
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_CreateWorkspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateWorkspace_ResponseSyntax) **   <a name="prometheus-CreateWorkspace-response-arn"></a>
The ARN for the new workspace.  
Type: String  
Pattern: `arn:aws[-a-z]*:aps:[-a-z0-9]+:[0-9]{12}:workspace/.+` 

 ** [kmsKeyArn](#API_CreateWorkspace_ResponseSyntax) **   <a name="prometheus-CreateWorkspace-response-kmsKeyArn"></a>
(optional) If the workspace was created with a customer managed AWS KMS key, the ARN for the key used.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws[-a-z]*:kms:[-a-z0-9]+:[0-9]{12}:key/[-a-f0-9]+` 

 ** [status](#API_CreateWorkspace_ResponseSyntax) **   <a name="prometheus-CreateWorkspace-response-status"></a>
The current status of the new workspace. Immediately after you create the workspace, the status is usually `CREATING`.  
Type: [WorkspaceStatus](API_WorkspaceStatus.md) object

 ** [tags](#API_CreateWorkspace_ResponseSyntax) **   <a name="prometheus-CreateWorkspace-response-tags"></a>
The list of tag keys and values that are associated with the workspace.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)` 

 ** [workspaceId](#API_CreateWorkspace_ResponseSyntax) **   <a name="prometheus-CreateWorkspace-response-workspaceId"></a>
The unique ID for the new workspace.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*` 

## Errors
<a name="API_CreateWorkspace_Errors"></a>

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
<a name="API_CreateWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/CreateWorkspace) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/CreateWorkspace) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/CreateWorkspace) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/CreateWorkspace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/CreateWorkspace) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/CreateWorkspace) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/CreateWorkspace) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/CreateWorkspace) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/CreateWorkspace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/CreateWorkspace) 