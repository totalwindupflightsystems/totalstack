---
id: "@specs/aws/amp/docs/API_CreateQueryLoggingConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateQueryLoggingConfiguration"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# CreateQueryLoggingConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_CreateQueryLoggingConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateQueryLoggingConfiguration
<a name="API_CreateQueryLoggingConfiguration"></a>

Creates a query logging configuration for the specified workspace. This operation enables logging of queries that exceed the specified QSP threshold.

## Request Syntax
<a name="API_CreateQueryLoggingConfiguration_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/logging/query HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "destinations": [ 
      { 
         "cloudWatchLogs": { 
            "logGroupArn": "{{string}}"
         },
         "filters": { 
            "qspThreshold": {{number}}
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateQueryLoggingConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_CreateQueryLoggingConfiguration_RequestSyntax) **   <a name="prometheus-CreateQueryLoggingConfiguration-request-uri-workspaceId"></a>
The ID of the workspace for which to create the query logging configuration.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## Request Body
<a name="API_CreateQueryLoggingConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateQueryLoggingConfiguration_RequestSyntax) **   <a name="prometheus-CreateQueryLoggingConfiguration-request-clientToken"></a>
(Optional) A unique, case-sensitive identifier that you can provide to ensure the idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+`   
Required: No

 ** [destinations](#API_CreateQueryLoggingConfiguration_RequestSyntax) **   <a name="prometheus-CreateQueryLoggingConfiguration-request-destinations"></a>
The destinations where query logs will be sent. Only CloudWatch Logs destination is supported. The list must contain exactly one element.  
Type: Array of [LoggingDestination](API_LoggingDestination.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

## Response Syntax
<a name="API_CreateQueryLoggingConfiguration_ResponseSyntax"></a>

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
<a name="API_CreateQueryLoggingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [status](#API_CreateQueryLoggingConfiguration_ResponseSyntax) **   <a name="prometheus-CreateQueryLoggingConfiguration-response-status"></a>
The current status of the query logging configuration.  
Type: [QueryLoggingConfigurationStatus](API_QueryLoggingConfigurationStatus.md) object

## Errors
<a name="API_CreateQueryLoggingConfiguration_Errors"></a>

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
<a name="API_CreateQueryLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/CreateQueryLoggingConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/CreateQueryLoggingConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/CreateQueryLoggingConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/CreateQueryLoggingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/CreateQueryLoggingConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/CreateQueryLoggingConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/CreateQueryLoggingConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/CreateQueryLoggingConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/CreateQueryLoggingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/CreateQueryLoggingConfiguration) 