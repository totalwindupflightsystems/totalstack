---
id: "@specs/aws/amp/docs/API_UpdateLoggingConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateLoggingConfiguration"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# UpdateLoggingConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_UpdateLoggingConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateLoggingConfiguration
<a name="API_UpdateLoggingConfiguration"></a>

Updates the log group ARN or the workspace ID of the current rules and alerting logging configuration.

**Note**  
These logging configurations are only for rules and alerting logs.

## Request Syntax
<a name="API_UpdateLoggingConfiguration_RequestSyntax"></a>

```
PUT /workspaces/{{workspaceId}}/logging HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "logGroupArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateLoggingConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_UpdateLoggingConfiguration_RequestSyntax) **   <a name="prometheus-UpdateLoggingConfiguration-request-uri-workspaceId"></a>
The ID of the workspace to update the logging configuration for.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## Request Body
<a name="API_UpdateLoggingConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateLoggingConfiguration_RequestSyntax) **   <a name="prometheus-UpdateLoggingConfiguration-request-clientToken"></a>
A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+`   
Required: No

 ** [logGroupArn](#API_UpdateLoggingConfiguration_RequestSyntax) **   <a name="prometheus-UpdateLoggingConfiguration-request-logGroupArn"></a>
The ARN of the CloudWatch log group to which the vended log data will be published.  
Type: String  
Pattern: `arn:aws[a-z0-9-]*:logs:[a-z0-9-]+:[0-9]{12}:log-group:[A-Za-z0-9\.\-\_\#/]{1,512}\:\*`   
Required: Yes

## Response Syntax
<a name="API_UpdateLoggingConfiguration_ResponseSyntax"></a>

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
<a name="API_UpdateLoggingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [status](#API_UpdateLoggingConfiguration_ResponseSyntax) **   <a name="prometheus-UpdateLoggingConfiguration-response-status"></a>
A structure that contains the current status of the logging configuration.  
Type: [LoggingConfigurationStatus](API_LoggingConfigurationStatus.md) object

## Errors
<a name="API_UpdateLoggingConfiguration_Errors"></a>

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
<a name="API_UpdateLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/UpdateLoggingConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/UpdateLoggingConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/UpdateLoggingConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/UpdateLoggingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/UpdateLoggingConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/UpdateLoggingConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/UpdateLoggingConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/UpdateLoggingConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/UpdateLoggingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/UpdateLoggingConfiguration) 