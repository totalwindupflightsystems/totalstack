---
id: "@specs/aws/amp/docs/API_PutAlertManagerDefinition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutAlertManagerDefinition"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# PutAlertManagerDefinition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_PutAlertManagerDefinition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutAlertManagerDefinition
<a name="API_PutAlertManagerDefinition"></a>

Updates an existing alert manager definition in a workspace. If the workspace does not already have an alert manager definition, don't use this operation to create it. Instead, use `CreateAlertManagerDefinition`.

## Request Syntax
<a name="API_PutAlertManagerDefinition_RequestSyntax"></a>

```
PUT /workspaces/{{workspaceId}}/alertmanager/definition HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "data": {{blob}}
}
```

## URI Request Parameters
<a name="API_PutAlertManagerDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_PutAlertManagerDefinition_RequestSyntax) **   <a name="prometheus-PutAlertManagerDefinition-request-uri-workspaceId"></a>
The ID of the workspace to update the alert manager definition in.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## Request Body
<a name="API_PutAlertManagerDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_PutAlertManagerDefinition_RequestSyntax) **   <a name="prometheus-PutAlertManagerDefinition-request-clientToken"></a>
A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+`   
Required: No

 ** [data](#API_PutAlertManagerDefinition_RequestSyntax) **   <a name="prometheus-PutAlertManagerDefinition-request-data"></a>
The alert manager definition to use. A base64-encoded version of the YAML alert manager definition file.  
For details about the alert manager definition, see [AlertManagedDefinitionData](https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-AlertManagerDefinitionData.html).  
Type: Base64-encoded binary data object  
Required: Yes

## Response Syntax
<a name="API_PutAlertManagerDefinition_ResponseSyntax"></a>

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
<a name="API_PutAlertManagerDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [status](#API_PutAlertManagerDefinition_ResponseSyntax) **   <a name="prometheus-PutAlertManagerDefinition-response-status"></a>
A structure that returns the current status of the alert manager definition.  
Type: [AlertManagerDefinitionStatus](API_AlertManagerDefinitionStatus.md) object

## Errors
<a name="API_PutAlertManagerDefinition_Errors"></a>

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
<a name="API_PutAlertManagerDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/PutAlertManagerDefinition) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/PutAlertManagerDefinition) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/PutAlertManagerDefinition) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/PutAlertManagerDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/PutAlertManagerDefinition) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/PutAlertManagerDefinition) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/PutAlertManagerDefinition) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/PutAlertManagerDefinition) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/PutAlertManagerDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/PutAlertManagerDefinition) 