---
id: "@specs/aws/amp/docs/API_CreateScraper"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateScraper"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# CreateScraper

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_CreateScraper
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateScraper
<a name="API_CreateScraper"></a>

The `CreateScraper` operation creates a scraper to collect metrics. A scraper pulls metrics from Prometheus-compatible sources and sends them to your Amazon Managed Service for Prometheus workspace. You can configure scrapers to collect metrics from Amazon EKS clusters, Amazon MSK clusters, or from VPC-based sources that support DNS-based service discovery. Scrapers are flexible, and can be configured to control what metrics are collected, the frequency of collection, what transformations are applied to the metrics, and more.

An IAM role will be created for you that Amazon Managed Service for Prometheus uses to access the metrics in your source. You must configure this role with a policy that allows it to scrape metrics from your source. For Amazon EKS sources, see [Configuring your Amazon EKS cluster](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-eks-setup) in the *Amazon Managed Service for Prometheus User Guide*.

The `scrapeConfiguration` parameter contains the base-64 encoded YAML configuration for the scraper.

When creating a scraper, the service creates a `Network Interface` in each **Availability Zone** that are passed into `CreateScraper` through subnets. These network interfaces are used to connect to your source within the VPC for scraping metrics.

**Note**  
For more information about collectors, including what metrics are collected, and how to configure the scraper, see [Using an AWS managed collector](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html) in the *Amazon Managed Service for Prometheus User Guide*.

## Request Syntax
<a name="API_CreateScraper_RequestSyntax"></a>

```
POST /scrapers HTTP/1.1
Content-type: application/json

{
   "alias": "{{string}}",
   "clientToken": "{{string}}",
   "destination": { ... },
   "roleConfiguration": { 
      "sourceRoleArn": "{{string}}",
      "targetRoleArn": "{{string}}"
   },
   "scrapeConfiguration": { ... },
   "source": { ... },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateScraper_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateScraper_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [alias](#API_CreateScraper_RequestSyntax) **   <a name="prometheus-CreateScraper-request-alias"></a>
(optional) An alias to associate with the scraper. This is for your use, and does not need to be unique.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[0-9A-Za-z][-.0-9A-Z_a-z]*`   
Required: No

 ** [clientToken](#API_CreateScraper_RequestSyntax) **   <a name="prometheus-CreateScraper-request-clientToken"></a>
(Optional) A unique, case-sensitive identifier that you can provide to ensure the idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+`   
Required: No

 ** [destination](#API_CreateScraper_RequestSyntax) **   <a name="prometheus-CreateScraper-request-destination"></a>
The Amazon Managed Service for Prometheus workspace to send metrics to.  
Type: [Destination](API_Destination.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [roleConfiguration](#API_CreateScraper_RequestSyntax) **   <a name="prometheus-CreateScraper-request-roleConfiguration"></a>
Use this structure to enable cross-account access, so that you can use a target account to access Prometheus metrics from source accounts.  
Type: [RoleConfiguration](API_RoleConfiguration.md) object  
Required: No

 ** [scrapeConfiguration](#API_CreateScraper_RequestSyntax) **   <a name="prometheus-CreateScraper-request-scrapeConfiguration"></a>
The configuration file to use in the new scraper. For more information, see [Scraper configuration](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-configuration) in the *Amazon Managed Service for Prometheus User Guide*.  
Type: [ScrapeConfiguration](API_ScrapeConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [source](#API_CreateScraper_RequestSyntax) **   <a name="prometheus-CreateScraper-request-source"></a>
The Amazon EKS or AWS cluster from which the scraper will collect metrics.  
Type: [Source](API_Source.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [tags](#API_CreateScraper_RequestSyntax) **   <a name="prometheus-CreateScraper-request-tags"></a>
(Optional) The list of tag keys and values to associate with the scraper.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Required: No

## Response Syntax
<a name="API_CreateScraper_ResponseSyntax"></a>

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
<a name="API_CreateScraper_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateScraper_ResponseSyntax) **   <a name="prometheus-CreateScraper-response-arn"></a>
The Amazon Resource Name (ARN) of the new scraper.  
Type: String

 ** [scraperId](#API_CreateScraper_ResponseSyntax) **   <a name="prometheus-CreateScraper-response-scraperId"></a>
The ID of the new scraper.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[0-9A-Za-z][-.0-9A-Z_a-z]*` 

 ** [status](#API_CreateScraper_ResponseSyntax) **   <a name="prometheus-CreateScraper-response-status"></a>
A structure that displays the current status of the scraper.  
Type: [ScraperStatus](API_ScraperStatus.md) object

 ** [tags](#API_CreateScraper_ResponseSyntax) **   <a name="prometheus-CreateScraper-response-tags"></a>
The list of tag keys and values that are associated with the scraper.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)` 

## Errors
<a name="API_CreateScraper_Errors"></a>

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
<a name="API_CreateScraper_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/CreateScraper) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/CreateScraper) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/CreateScraper) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/CreateScraper) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/CreateScraper) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/CreateScraper) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/CreateScraper) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/CreateScraper) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/CreateScraper) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/CreateScraper) 