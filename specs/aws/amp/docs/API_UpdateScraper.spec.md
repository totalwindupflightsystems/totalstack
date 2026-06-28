---
id: "@specs/aws/amp/docs/API_UpdateScraper"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateScraper"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# UpdateScraper

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_UpdateScraper
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateScraper
<a name="API_UpdateScraper"></a>

Updates an existing scraper.

You can't use this function to update the source from which the scraper is collecting metrics. To change the source, delete the scraper and create a new one.

## Request Syntax
<a name="API_UpdateScraper_RequestSyntax"></a>

```
PUT /scrapers/{{scraperId}} HTTP/1.1
Content-type: application/json

{
   "alias": "{{string}}",
   "clientToken": "{{string}}",
   "destination": { ... },
   "roleConfiguration": { 
      "sourceRoleArn": "{{string}}",
      "targetRoleArn": "{{string}}"
   },
   "scrapeConfiguration": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateScraper_RequestParameters"></a>

The request uses the following URI parameters.

 ** [scraperId](#API_UpdateScraper_RequestSyntax) **   <a name="prometheus-UpdateScraper-request-uri-scraperId"></a>
The ID of the scraper to update.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[0-9A-Za-z][-.0-9A-Z_a-z]*`   
Required: Yes

## Request Body
<a name="API_UpdateScraper_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [alias](#API_UpdateScraper_RequestSyntax) **   <a name="prometheus-UpdateScraper-request-alias"></a>
The new alias of the scraper.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[0-9A-Za-z][-.0-9A-Z_a-z]*`   
Required: No

 ** [clientToken](#API_UpdateScraper_RequestSyntax) **   <a name="prometheus-UpdateScraper-request-clientToken"></a>
A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+`   
Required: No

 ** [destination](#API_UpdateScraper_RequestSyntax) **   <a name="prometheus-UpdateScraper-request-destination"></a>
The new Amazon Managed Service for Prometheus workspace to send metrics to.  
Type: [Destination](API_Destination.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [roleConfiguration](#API_UpdateScraper_RequestSyntax) **   <a name="prometheus-UpdateScraper-request-roleConfiguration"></a>
Use this structure to enable cross-account access, so that you can use a target account to access Prometheus metrics from source accounts.  
Type: [RoleConfiguration](API_RoleConfiguration.md) object  
Required: No

 ** [scrapeConfiguration](#API_UpdateScraper_RequestSyntax) **   <a name="prometheus-UpdateScraper-request-scrapeConfiguration"></a>
Contains the base-64 encoded YAML configuration for the scraper.  
For more information about configuring a scraper, see [Using an AWS managed collector](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html) in the *Amazon Managed Service for Prometheus User Guide*.
Type: [ScrapeConfiguration](API_ScrapeConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## Response Syntax
<a name="API_UpdateScraper_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "arn": "string",
   "scraperId": "string",
   "status": { 
      "statusCode": "string"
   },
   "tags": { 
      "string" : "string" 
   }
}
```

## Response Elements
<a name="API_UpdateScraper_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateScraper_ResponseSyntax) **   <a name="prometheus-UpdateScraper-response-arn"></a>
The Amazon Resource Name (ARN) of the updated scraper.  
Type: String

 ** [scraperId](#API_UpdateScraper_ResponseSyntax) **   <a name="prometheus-UpdateScraper-response-scraperId"></a>
The ID of the updated scraper.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[0-9A-Za-z][-.0-9A-Z_a-z]*` 

 ** [status](#API_UpdateScraper_ResponseSyntax) **   <a name="prometheus-UpdateScraper-response-status"></a>
A structure that displays the current status of the scraper.  
Type: [ScraperStatus](API_ScraperStatus.md) object

 ** [tags](#API_UpdateScraper_ResponseSyntax) **   <a name="prometheus-UpdateScraper-response-tags"></a>
The list of tag keys and values that are associated with the scraper.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)` 

## Errors
<a name="API_UpdateScraper_Errors"></a>

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
<a name="API_UpdateScraper_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/UpdateScraper) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/UpdateScraper) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/UpdateScraper) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/UpdateScraper) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/UpdateScraper) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/UpdateScraper) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/UpdateScraper) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/UpdateScraper) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/UpdateScraper) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/UpdateScraper) 