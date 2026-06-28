---
id: "@specs/aws/amp/docs/API_PutResourcePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutResourcePolicy"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# PutResourcePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_PutResourcePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

Creates or updates a resource-based policy for an Amazon Managed Service for Prometheus workspace. Use resource-based policies to grant permissions to other AWS accounts or services to access your workspace.

Only Prometheus-compatible APIs can be used for workspace sharing. You can add non-Prometheus-compatible APIs to the policy, but they will be ignored. For more information, see [Prometheus-compatible APIs](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-Prometheus-Compatible-Apis.html) in the *Amazon Managed Service for Prometheus User Guide*.

If your workspace uses customer-managed KMS keys for encryption, you must grant the principals in your resource-based policy access to those KMS keys. You can do this by creating KMS grants. For more information, see [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) in the *AWS Key Management Service API Reference* and [Encryption at rest](https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html) in the *Amazon Managed Service for Prometheus User Guide*.

For more information about working with IAM, see [Using Amazon Managed Service for Prometheus with IAM](https://docs.aws.amazon.com/prometheus/latest/userguide/security_iam_service-with-iam.html) in the *Amazon Managed Service for Prometheus User Guide*.

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
PUT /workspaces/{{workspaceId}}/policy HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "policyDocument": "{{string}}",
   "revisionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_PutResourcePolicy_RequestSyntax) **   <a name="prometheus-PutResourcePolicy-request-uri-workspaceId"></a>
The ID of the workspace to attach the resource-based policy to.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## Request Body
<a name="API_PutResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_PutResourcePolicy_RequestSyntax) **   <a name="prometheus-PutResourcePolicy-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the request is safe to retry (idempotent).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+`   
Required: No

 ** [policyDocument](#API_PutResourcePolicy_RequestSyntax) **   <a name="prometheus-PutResourcePolicy-request-policyDocument"></a>
The JSON policy document to use as the resource-based policy. This policy defines the permissions that other AWS accounts or services have to access your workspace.  
Type: String  
Required: Yes

 ** [revisionId](#API_PutResourcePolicy_RequestSyntax) **   <a name="prometheus-PutResourcePolicy-request-revisionId"></a>
The revision ID of the policy to update. Use this parameter to ensure that you are updating the correct version of the policy. If you don't specify a revision ID, the policy is updated regardless of its current revision.  
For the first **PUT** request on a workspace that doesn't have an existing resource policy, you can specify `NO_POLICY` as the revision ID.  
Type: String  
Required: No

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "policyStatus": "string",
   "revisionId": "string"
}
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [policyStatus](#API_PutResourcePolicy_ResponseSyntax) **   <a name="prometheus-PutResourcePolicy-response-policyStatus"></a>
The current status of the resource-based policy.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING` 

 ** [revisionId](#API_PutResourcePolicy_ResponseSyntax) **   <a name="prometheus-PutResourcePolicy-response-revisionId"></a>
The revision ID of the newly created or updated resource-based policy.  
Type: String

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

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
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/PutResourcePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/PutResourcePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/PutResourcePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/PutResourcePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/PutResourcePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/PutResourcePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/PutResourcePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/PutResourcePolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/PutResourcePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/PutResourcePolicy) 