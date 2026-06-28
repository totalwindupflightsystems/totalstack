---
id: "@specs/aws/amp/docs/API_CreateAnomalyDetector"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAnomalyDetector"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# CreateAnomalyDetector

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_CreateAnomalyDetector
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAnomalyDetector
<a name="API_CreateAnomalyDetector"></a>

Creates an anomaly detector within a workspace using the Random Cut Forest algorithm for time-series analysis. The anomaly detector analyzes Amazon Managed Service for Prometheus metrics to identify unusual patterns and behaviors.

## Request Syntax
<a name="API_CreateAnomalyDetector_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/anomalydetectors HTTP/1.1
Content-type: application/json

{
   "alias": "{{string}}",
   "clientToken": "{{string}}",
   "configuration": { ... },
   "evaluationIntervalInSeconds": {{number}},
   "labels": { 
      "{{string}}" : "{{string}}" 
   },
   "missingDataAction": { ... },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateAnomalyDetector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_CreateAnomalyDetector_RequestSyntax) **   <a name="prometheus-CreateAnomalyDetector-request-uri-workspaceId"></a>
The identifier of the workspace where the anomaly detector will be created.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## Request Body
<a name="API_CreateAnomalyDetector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [alias](#API_CreateAnomalyDetector_RequestSyntax) **   <a name="prometheus-CreateAnomalyDetector-request-alias"></a>
A user-friendly name for the anomaly detector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[0-9A-Za-z][-.0-9A-Z_a-z]*`   
Required: Yes

 ** [clientToken](#API_CreateAnomalyDetector_RequestSyntax) **   <a name="prometheus-CreateAnomalyDetector-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+`   
Required: No

 ** [configuration](#API_CreateAnomalyDetector_RequestSyntax) **   <a name="prometheus-CreateAnomalyDetector-request-configuration"></a>
The algorithm configuration for the anomaly detector.  
Type: [AnomalyDetectorConfiguration](API_AnomalyDetectorConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [evaluationIntervalInSeconds](#API_CreateAnomalyDetector_RequestSyntax) **   <a name="prometheus-CreateAnomalyDetector-request-evaluationIntervalInSeconds"></a>
The frequency, in seconds, at which the anomaly detector evaluates metrics. The default value is 60 seconds.  
Type: Integer  
Valid Range: Minimum value of 30. Maximum value of 86400.  
Required: No

 ** [labels](#API_CreateAnomalyDetector_RequestSyntax) **   <a name="prometheus-CreateAnomalyDetector-request-labels"></a>
The Amazon Managed Service for Prometheus metric labels to associate with the anomaly detector.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 140 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 7168.  
Key Pattern: `(?!__)[a-zA-Z_][a-zA-Z0-9_]*`   
Value Length Constraints: Minimum length of 1. Maximum length of 7168.  
Required: No

 ** [missingDataAction](#API_CreateAnomalyDetector_RequestSyntax) **   <a name="prometheus-CreateAnomalyDetector-request-missingDataAction"></a>
Specifies the action to take when data is missing during evaluation.  
Type: [AnomalyDetectorMissingDataAction](API_AnomalyDetectorMissingDataAction.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [tags](#API_CreateAnomalyDetector_RequestSyntax) **   <a name="prometheus-CreateAnomalyDetector-request-tags"></a>
The metadata to apply to the anomaly detector to assist with categorization and organization.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Required: No

## Response Syntax
<a name="API_CreateAnomalyDetector_ResponseSyntax"></a>

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
<a name="API_CreateAnomalyDetector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [anomalyDetectorId](#API_CreateAnomalyDetector_ResponseSyntax) **   <a name="prometheus-CreateAnomalyDetector-response-anomalyDetectorId"></a>
The unique identifier of the created anomaly detector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `ad-[0-9A-Za-z][-.0-9A-Z_a-z]*` 

 ** [arn](#API_CreateAnomalyDetector_ResponseSyntax) **   <a name="prometheus-CreateAnomalyDetector-response-arn"></a>
The Amazon Resource Name (ARN) of the created anomaly detector.  
Type: String  
Pattern: `arn:aws[-a-z]*:aps:[-a-z0-9]+:[0-9]{12}:anomalydetector/ws-.+/ad-.+` 

 ** [status](#API_CreateAnomalyDetector_ResponseSyntax) **   <a name="prometheus-CreateAnomalyDetector-response-status"></a>
The status information of the created anomaly detector.  
Type: [AnomalyDetectorStatus](API_AnomalyDetectorStatus.md) object

 ** [tags](#API_CreateAnomalyDetector_ResponseSyntax) **   <a name="prometheus-CreateAnomalyDetector-response-tags"></a>
The tags applied to the created anomaly detector.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)` 

## Errors
<a name="API_CreateAnomalyDetector_Errors"></a>

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
<a name="API_CreateAnomalyDetector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/CreateAnomalyDetector) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/CreateAnomalyDetector) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/CreateAnomalyDetector) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/CreateAnomalyDetector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/CreateAnomalyDetector) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/CreateAnomalyDetector) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/CreateAnomalyDetector) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/CreateAnomalyDetector) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/CreateAnomalyDetector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/CreateAnomalyDetector) 