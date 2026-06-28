---
id: "@specs/aws/amp/docs/API_PutAnomalyDetector"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutAnomalyDetector"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# PutAnomalyDetector

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_PutAnomalyDetector
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutAnomalyDetector
<a name="API_PutAnomalyDetector"></a>

When you call `PutAnomalyDetector`, the operation creates a new anomaly detector if one doesn't exist, or updates an existing one. Each call to this operation triggers a complete retraining of the detector, which includes querying the minimum required samples and backfilling the detector with historical data. This process occurs regardless of whether you're making a minor change like updating the evaluation interval or making more substantial modifications. The operation serves as the single method for creating, updating, and retraining anomaly detectors.

## Request Syntax
<a name="API_PutAnomalyDetector_RequestSyntax"></a>

```
PUT /workspaces/{{workspaceId}}/anomalydetectors/{{anomalyDetectorId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "configuration": { ... },
   "evaluationIntervalInSeconds": {{number}},
   "labels": { 
      "{{string}}" : "{{string}}" 
   },
   "missingDataAction": { ... }
}
```

## URI Request Parameters
<a name="API_PutAnomalyDetector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [anomalyDetectorId](#API_PutAnomalyDetector_RequestSyntax) **   <a name="prometheus-PutAnomalyDetector-request-uri-anomalyDetectorId"></a>
The identifier of the anomaly detector to update.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `ad-[0-9A-Za-z][-.0-9A-Z_a-z]*`   
Required: Yes

 ** [workspaceId](#API_PutAnomalyDetector_RequestSyntax) **   <a name="prometheus-PutAnomalyDetector-request-uri-workspaceId"></a>
The identifier of the workspace containing the anomaly detector to update.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## Request Body
<a name="API_PutAnomalyDetector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_PutAnomalyDetector_RequestSyntax) **   <a name="prometheus-PutAnomalyDetector-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+`   
Required: No

 ** [configuration](#API_PutAnomalyDetector_RequestSyntax) **   <a name="prometheus-PutAnomalyDetector-request-configuration"></a>
The algorithm configuration for the anomaly detector.  
Type: [AnomalyDetectorConfiguration](API_AnomalyDetectorConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [evaluationIntervalInSeconds](#API_PutAnomalyDetector_RequestSyntax) **   <a name="prometheus-PutAnomalyDetector-request-evaluationIntervalInSeconds"></a>
The frequency, in seconds, at which the anomaly detector evaluates metrics.  
Type: Integer  
Valid Range: Minimum value of 30. Maximum value of 86400.  
Required: No

 ** [labels](#API_PutAnomalyDetector_RequestSyntax) **   <a name="prometheus-PutAnomalyDetector-request-labels"></a>
The Amazon Managed Service for Prometheus metric labels to associate with the anomaly detector.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 7168.  
Key Pattern: `(?!__)[a-zA-Z_][a-zA-Z0-9_]*`   
Value Length Constraints: Minimum length of 1. Maximum length of 7168.  
Required: No

 ** [missingDataAction](#API_PutAnomalyDetector_RequestSyntax) **   <a name="prometheus-PutAnomalyDetector-request-missingDataAction"></a>
Specifies the action to take when data is missing during evaluation.  
Type: [AnomalyDetectorMissingDataAction](API_AnomalyDetectorMissingDataAction.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## Response Syntax
<a name="API_PutAnomalyDetector_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "anomalyDetectorId": "string",
   "arn": "string",
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
<a name="API_PutAnomalyDetector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [anomalyDetectorId](#API_PutAnomalyDetector_ResponseSyntax) **   <a name="prometheus-PutAnomalyDetector-response-anomalyDetectorId"></a>
The unique identifier of the updated anomaly detector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `ad-[0-9A-Za-z][-.0-9A-Z_a-z]*` 

 ** [arn](#API_PutAnomalyDetector_ResponseSyntax) **   <a name="prometheus-PutAnomalyDetector-response-arn"></a>
The Amazon Resource Name (ARN) of the updated anomaly detector.  
Type: String  
Pattern: `arn:aws[-a-z]*:aps:[-a-z0-9]+:[0-9]{12}:anomalydetector/ws-.+/ad-.+` 

 ** [status](#API_PutAnomalyDetector_ResponseSyntax) **   <a name="prometheus-PutAnomalyDetector-response-status"></a>
The status information of the updated anomaly detector.  
Type: [AnomalyDetectorStatus](API_AnomalyDetectorStatus.md) object

 ** [tags](#API_PutAnomalyDetector_ResponseSyntax) **   <a name="prometheus-PutAnomalyDetector-response-tags"></a>
The tags applied to the updated anomaly detector.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)` 

## Errors
<a name="API_PutAnomalyDetector_Errors"></a>

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
<a name="API_PutAnomalyDetector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/PutAnomalyDetector) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/PutAnomalyDetector) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/PutAnomalyDetector) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/PutAnomalyDetector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/PutAnomalyDetector) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/PutAnomalyDetector) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/PutAnomalyDetector) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/PutAnomalyDetector) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/PutAnomalyDetector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/PutAnomalyDetector) 