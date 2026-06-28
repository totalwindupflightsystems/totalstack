---
id: "@specs/aws/amp/docs/API_DeleteAnomalyDetector"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteAnomalyDetector"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# DeleteAnomalyDetector

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_DeleteAnomalyDetector
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteAnomalyDetector
<a name="API_DeleteAnomalyDetector"></a>

Removes an anomaly detector from a workspace. This operation is idempotent.

## Request Syntax
<a name="API_DeleteAnomalyDetector_RequestSyntax"></a>

```
DELETE /workspaces/{{workspaceId}}/anomalydetectors/{{anomalyDetectorId}}?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAnomalyDetector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [anomalyDetectorId](#API_DeleteAnomalyDetector_RequestSyntax) **   <a name="prometheus-DeleteAnomalyDetector-request-uri-anomalyDetectorId"></a>
The identifier of the anomaly detector to delete.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `ad-[0-9A-Za-z][-.0-9A-Z_a-z]*`   
Required: Yes

 ** [clientToken](#API_DeleteAnomalyDetector_RequestSyntax) **   <a name="prometheus-DeleteAnomalyDetector-request-uri-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+` 

 ** [workspaceId](#API_DeleteAnomalyDetector_RequestSyntax) **   <a name="prometheus-DeleteAnomalyDetector-request-uri-workspaceId"></a>
The identifier of the workspace containing the anomaly detector to delete.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## Request Body
<a name="API_DeleteAnomalyDetector_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAnomalyDetector_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_DeleteAnomalyDetector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_DeleteAnomalyDetector_Errors"></a>

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
<a name="API_DeleteAnomalyDetector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/DeleteAnomalyDetector) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/DeleteAnomalyDetector) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/DeleteAnomalyDetector) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/DeleteAnomalyDetector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/DeleteAnomalyDetector) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/DeleteAnomalyDetector) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/DeleteAnomalyDetector) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/DeleteAnomalyDetector) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/DeleteAnomalyDetector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/DeleteAnomalyDetector) 