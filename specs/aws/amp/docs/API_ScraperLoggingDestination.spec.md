---
id: "@specs/aws/amp/docs/API_ScraperLoggingDestination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ScraperLoggingDestination"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# ScraperLoggingDestination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_ScraperLoggingDestination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ScraperLoggingDestination
<a name="API_ScraperLoggingDestination"></a>

The destination where scraper logs are sent.

## Contents
<a name="API_ScraperLoggingDestination_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cloudWatchLogs **   <a name="prometheus-Type-ScraperLoggingDestination-cloudWatchLogs"></a>
The CloudWatch Logs configuration for the scraper logging destination.  
Type: [CloudWatchLogDestination](API_CloudWatchLogDestination.md) object  
Required: No

## See Also
<a name="API_ScraperLoggingDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/ScraperLoggingDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/ScraperLoggingDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/ScraperLoggingDestination) 