---
id: "@specs/aws/amp/docs/API_UpdateWorkspaceConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateWorkspaceConfiguration"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# UpdateWorkspaceConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_UpdateWorkspaceConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateWorkspaceConfiguration
<a name="API_UpdateWorkspaceConfiguration"></a>

Use this operation to create or update the label sets, label set limits, and retention period of a workspace.

You must specify at least one of `limitsPerLabelSet` or `retentionPeriodInDays` for the request to be valid.

## Request Syntax
<a name="API_UpdateWorkspaceConfiguration_RequestSyntax"></a>

```
PATCH /workspaces/{{workspaceId}}/configuration HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "limitsPerLabelSet": [ 
      { 
         "labelSet": { 
            "{{string}}" : "{{string}}" 
         },
         "limits": { 
            "maxSeries": {{number}}
         }
      }
   ],
   "retentionPeriodInDays": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateWorkspaceConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_UpdateWorkspaceConfiguration_RequestSyntax) **   <a name="prometheus-UpdateWorkspaceConfiguration-request-uri-workspaceId"></a>
The ID of the workspace that you want to update. To find the IDs of your workspaces, use the [ListWorkspaces](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListWorkspaces.htm) operation.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## Request Body
<a name="API_UpdateWorkspaceConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateWorkspaceConfiguration_RequestSyntax) **   <a name="prometheus-UpdateWorkspaceConfiguration-request-clientToken"></a>
You can include a token in your operation to make it an idempotent opeartion.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+`   
Required: No

 ** [limitsPerLabelSet](#API_UpdateWorkspaceConfiguration_RequestSyntax) **   <a name="prometheus-UpdateWorkspaceConfiguration-request-limitsPerLabelSet"></a>
This is an array of structures, where each structure defines a label set for the workspace, and defines the active time series limit for each of those label sets. Each label name in a label set must be unique.  
Type: Array of [LimitsPerLabelSet](API_LimitsPerLabelSet.md) objects  
Required: No

 ** [retentionPeriodInDays](#API_UpdateWorkspaceConfiguration_RequestSyntax) **   <a name="prometheus-UpdateWorkspaceConfiguration-request-retentionPeriodInDays"></a>
Specifies how many days that metrics will be retained in the workspace.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

## Response Syntax
<a name="API_UpdateWorkspaceConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "status": { 
      "statusCode": "string",
      "statusReason": "string"
   }
}
```

## Response Elements
<a name="API_UpdateWorkspaceConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [status](#API_UpdateWorkspaceConfiguration_ResponseSyntax) **   <a name="prometheus-UpdateWorkspaceConfiguration-response-status"></a>
The status of the workspace configuration.  
Type: [WorkspaceConfigurationStatus](API_WorkspaceConfigurationStatus.md) object

## Errors
<a name="API_UpdateWorkspaceConfiguration_Errors"></a>

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
<a name="API_UpdateWorkspaceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/UpdateWorkspaceConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/UpdateWorkspaceConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/UpdateWorkspaceConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/UpdateWorkspaceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/UpdateWorkspaceConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/UpdateWorkspaceConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/UpdateWorkspaceConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/UpdateWorkspaceConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/UpdateWorkspaceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/UpdateWorkspaceConfiguration) 