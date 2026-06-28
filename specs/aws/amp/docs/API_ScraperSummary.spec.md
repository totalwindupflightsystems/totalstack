---
id: "@specs/aws/amp/docs/API_ScraperSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ScraperSummary"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# ScraperSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_ScraperSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ScraperSummary
<a name="API_ScraperSummary"></a>

The `ScraperSummary` structure contains a summary of the details about one scraper in your account.

## Contents
<a name="API_ScraperSummary_Contents"></a>

 ** arn **   <a name="prometheus-Type-ScraperSummary-arn"></a>
The Amazon Resource Name (ARN) of the scraper.  
Type: String  
Required: Yes

 ** createdAt **   <a name="prometheus-Type-ScraperSummary-createdAt"></a>
The date and time that the scraper was created.  
Type: Timestamp  
Required: Yes

 ** destination **   <a name="prometheus-Type-ScraperSummary-destination"></a>
The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.  
Type: [Destination](API_Destination.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** lastModifiedAt **   <a name="prometheus-Type-ScraperSummary-lastModifiedAt"></a>
The date and time that the scraper was last modified.  
Type: Timestamp  
Required: Yes

 ** roleArn **   <a name="prometheus-Type-ScraperSummary-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that provides permissions for the scraper to discover and collect metrics on your behalf.  
Type: String  
Pattern: `arn:aws[-a-z]*:iam::[0-9]{12}:role/.+`   
Required: Yes

 ** scraperId **   <a name="prometheus-Type-ScraperSummary-scraperId"></a>
The ID of the scraper.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[0-9A-Za-z][-.0-9A-Z_a-z]*`   
Required: Yes

 ** source **   <a name="prometheus-Type-ScraperSummary-source"></a>
The Amazon EKS cluster from which the scraper collects metrics.  
Type: [Source](API_Source.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** status **   <a name="prometheus-Type-ScraperSummary-status"></a>
A structure that contains the current status of the scraper.  
Type: [ScraperStatus](API_ScraperStatus.md) object  
Required: Yes

 ** alias **   <a name="prometheus-Type-ScraperSummary-alias"></a>
(Optional) A name associated with the scraper.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[0-9A-Za-z][-.0-9A-Z_a-z]*`   
Required: No

 ** roleConfiguration **   <a name="prometheus-Type-ScraperSummary-roleConfiguration"></a>
This structure displays information about the IAM roles used for cross-account scraping configuration.  
Type: [RoleConfiguration](API_RoleConfiguration.md) object  
Required: No

 ** statusReason **   <a name="prometheus-Type-ScraperSummary-statusReason"></a>
If there is a failure, the reason for the failure.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

 ** tags **   <a name="prometheus-Type-ScraperSummary-tags"></a>
(Optional) The list of tag keys and values associated with the scraper.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Required: No

## See Also
<a name="API_ScraperSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/ScraperSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/ScraperSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/ScraperSummary) 