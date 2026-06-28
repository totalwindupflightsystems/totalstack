---
id: "@specs/aws/amp/docs/API_ListAnomalyDetectors"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAnomalyDetectors"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# ListAnomalyDetectors

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_ListAnomalyDetectors
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAnomalyDetectors
<a name="API_ListAnomalyDetectors"></a>

Returns a paginated list of anomaly detectors for a workspace with optional filtering by alias.

## Request Syntax
<a name="API_ListAnomalyDetectors_RequestSyntax"></a>

```
GET /workspaces/{{workspaceId}}/anomalydetectors?alias={{alias}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAnomalyDetectors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [alias](#API_ListAnomalyDetectors_RequestSyntax) **   <a name="prometheus-ListAnomalyDetectors-request-uri-alias"></a>
Filters the results to anomaly detectors with the specified alias.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[0-9A-Za-z][-.0-9A-Z_a-z]*` 

 ** [maxResults](#API_ListAnomalyDetectors_RequestSyntax) **   <a name="prometheus-ListAnomalyDetectors-request-uri-maxResults"></a>
The maximum number of results to return in a single call. Valid range is 1 to 1000.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListAnomalyDetectors_RequestSyntax) **   <a name="prometheus-ListAnomalyDetectors-request-uri-nextToken"></a>
The pagination token to continue retrieving results.  
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [workspaceId](#API_ListAnomalyDetectors_RequestSyntax) **   <a name="prometheus-ListAnomalyDetectors-request-uri-workspaceId"></a>
The identifier of the workspace containing the anomaly detectors to list.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## Request Body
<a name="API_ListAnomalyDetectors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAnomalyDetectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "anomalyDetectors": [ 
      { 
         "alias": "string",
         "anomalyDetectorId": "string",
         "arn": "string",
         "createdAt": number,
         "modifiedAt": number,
         "status": { 
            "statusCode": "string",
            "statusReason": "string"
         },
         "tags": { 
            "string" : "string" 
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAnomalyDetectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [anomalyDetectors](#API_ListAnomalyDetectors_ResponseSyntax) **   <a name="prometheus-ListAnomalyDetectors-response-anomalyDetectors"></a>
The list of anomaly detectors in the workspace.  
Type: Array of [AnomalyDetectorSummary](API_AnomalyDetectorSummary.md) objects

 ** [nextToken](#API_ListAnomalyDetectors_ResponseSyntax) **   <a name="prometheus-ListAnomalyDetectors-response-nextToken"></a>
The pagination token to retrieve the next set of results.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Errors
<a name="API_ListAnomalyDetectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.    
 ** message **   
Description of the error.
HTTP Status Code: 403

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
<a name="API_ListAnomalyDetectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/ListAnomalyDetectors) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/ListAnomalyDetectors) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/ListAnomalyDetectors) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/ListAnomalyDetectors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/ListAnomalyDetectors) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/ListAnomalyDetectors) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/ListAnomalyDetectors) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/ListAnomalyDetectors) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/ListAnomalyDetectors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/ListAnomalyDetectors) 