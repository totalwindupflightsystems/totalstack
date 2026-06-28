---
id: "@specs/aws/amp/docs/API_GetDefaultScraperConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetDefaultScraperConfiguration"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# GetDefaultScraperConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_GetDefaultScraperConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetDefaultScraperConfiguration
<a name="API_GetDefaultScraperConfiguration"></a>

The `GetDefaultScraperConfiguration` operation returns the default scraper configuration used when Amazon EKS creates a scraper for you.

## Request Syntax
<a name="API_GetDefaultScraperConfiguration_RequestSyntax"></a>

```
GET /scraperconfiguration HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDefaultScraperConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetDefaultScraperConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDefaultScraperConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuration": blob
}
```

## Response Elements
<a name="API_GetDefaultScraperConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_GetDefaultScraperConfiguration_ResponseSyntax) **   <a name="prometheus-GetDefaultScraperConfiguration-response-configuration"></a>
The configuration file. Base 64 encoded. For more information, see [Scraper configuration](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-configuration)in the *Amazon Managed Service for Prometheus User Guide*.  
Type: Base64-encoded binary data object

## Errors
<a name="API_GetDefaultScraperConfiguration_Errors"></a>

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

## See Also
<a name="API_GetDefaultScraperConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/GetDefaultScraperConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/GetDefaultScraperConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/GetDefaultScraperConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/GetDefaultScraperConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/GetDefaultScraperConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/GetDefaultScraperConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/GetDefaultScraperConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/GetDefaultScraperConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/GetDefaultScraperConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/GetDefaultScraperConfiguration) 