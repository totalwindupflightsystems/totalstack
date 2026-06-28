---
id: "@specs/aws/amp/docs/API_DeleteScraperLoggingConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteScraperLoggingConfiguration"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# DeleteScraperLoggingConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_DeleteScraperLoggingConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteScraperLoggingConfiguration
<a name="API_DeleteScraperLoggingConfiguration"></a>

Deletes the logging configuration for a Amazon Managed Service for Prometheus scraper.

## Request Syntax
<a name="API_DeleteScraperLoggingConfiguration_RequestSyntax"></a>

```
DELETE /scrapers/{{scraperId}}/logging-configuration?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteScraperLoggingConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeleteScraperLoggingConfiguration_RequestSyntax) **   <a name="prometheus-DeleteScraperLoggingConfiguration-request-uri-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the request is processed exactly once.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+` 

 ** [scraperId](#API_DeleteScraperLoggingConfiguration_RequestSyntax) **   <a name="prometheus-DeleteScraperLoggingConfiguration-request-uri-scraperId"></a>
The ID of the scraper whose logging configuration will be deleted.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[0-9A-Za-z][-.0-9A-Z_a-z]*`   
Required: Yes

## Request Body
<a name="API_DeleteScraperLoggingConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteScraperLoggingConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_DeleteScraperLoggingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_DeleteScraperLoggingConfiguration_Errors"></a>

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
<a name="API_DeleteScraperLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/DeleteScraperLoggingConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/DeleteScraperLoggingConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/DeleteScraperLoggingConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/DeleteScraperLoggingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/DeleteScraperLoggingConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/DeleteScraperLoggingConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/DeleteScraperLoggingConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/DeleteScraperLoggingConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/DeleteScraperLoggingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/DeleteScraperLoggingConfiguration) 