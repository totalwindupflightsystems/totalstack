---
id: "@specs/aws/amp/docs/API_DescribeScraperLoggingConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeScraperLoggingConfiguration"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# DescribeScraperLoggingConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_DescribeScraperLoggingConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeScraperLoggingConfiguration
<a name="API_DescribeScraperLoggingConfiguration"></a>

Describes the logging configuration for a Amazon Managed Service for Prometheus scraper.

## Request Syntax
<a name="API_DescribeScraperLoggingConfiguration_RequestSyntax"></a>

```
GET /scrapers/{{scraperId}}/logging-configuration HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeScraperLoggingConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [scraperId](#API_DescribeScraperLoggingConfiguration_RequestSyntax) **   <a name="prometheus-DescribeScraperLoggingConfiguration-request-uri-scraperId"></a>
The ID of the scraper whose logging configuration will be described.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[0-9A-Za-z][-.0-9A-Z_a-z]*`   
Required: Yes

## Request Body
<a name="API_DescribeScraperLoggingConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeScraperLoggingConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "loggingDestination": { ... },
   "modifiedAt": number,
   "scraperComponents": [ 
      { 
         "config": { 
            "options": { 
               "string" : "string" 
            }
         },
         "type": "string"
      }
   ],
   "scraperId": "string",
   "status": { 
      "statusCode": "string",
      "statusReason": "string"
   }
}
```

## Response Elements
<a name="API_DescribeScraperLoggingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [loggingDestination](#API_DescribeScraperLoggingConfiguration_ResponseSyntax) **   <a name="prometheus-DescribeScraperLoggingConfiguration-response-loggingDestination"></a>
The destination where scraper logs are sent.  
Type: [ScraperLoggingDestination](API_ScraperLoggingDestination.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [modifiedAt](#API_DescribeScraperLoggingConfiguration_ResponseSyntax) **   <a name="prometheus-DescribeScraperLoggingConfiguration-response-modifiedAt"></a>
The date and time when the logging configuration was last modified.  
Type: Timestamp

 ** [scraperComponents](#API_DescribeScraperLoggingConfiguration_ResponseSyntax) **   <a name="prometheus-DescribeScraperLoggingConfiguration-response-scraperComponents"></a>
The list of scraper components configured for logging.  
Type: Array of [ScraperComponent](API_ScraperComponent.md) objects  
Array Members: Minimum number of 1 item.

 ** [scraperId](#API_DescribeScraperLoggingConfiguration_ResponseSyntax) **   <a name="prometheus-DescribeScraperLoggingConfiguration-response-scraperId"></a>
The ID of the scraper.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[0-9A-Za-z][-.0-9A-Z_a-z]*` 

 ** [status](#API_DescribeScraperLoggingConfiguration_ResponseSyntax) **   <a name="prometheus-DescribeScraperLoggingConfiguration-response-status"></a>
The status of the scraper logging configuration.  
Type: [ScraperLoggingConfigurationStatus](API_ScraperLoggingConfigurationStatus.md) object

## Errors
<a name="API_DescribeScraperLoggingConfiguration_Errors"></a>

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
<a name="API_DescribeScraperLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/DescribeScraperLoggingConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/DescribeScraperLoggingConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/DescribeScraperLoggingConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/DescribeScraperLoggingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/DescribeScraperLoggingConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/DescribeScraperLoggingConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/DescribeScraperLoggingConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/DescribeScraperLoggingConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/DescribeScraperLoggingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/DescribeScraperLoggingConfiguration) 