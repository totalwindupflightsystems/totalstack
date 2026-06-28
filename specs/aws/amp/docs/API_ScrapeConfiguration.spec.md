---
id: "@specs/aws/amp/docs/API_ScrapeConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ScrapeConfiguration"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# ScrapeConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_ScrapeConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ScrapeConfiguration
<a name="API_ScrapeConfiguration"></a>

A scrape configuration for a scraper, base 64 encoded. For more information, see [Scraper configuration](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-configuration) in the *Amazon Managed Service for Prometheus User Guide*.

## Contents
<a name="API_ScrapeConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** configurationBlob **   <a name="prometheus-Type-ScrapeConfiguration-configurationBlob"></a>
The base 64 encoded scrape configuration file.  
Type: Base64-encoded binary data object  
Required: No

## See Also
<a name="API_ScrapeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/ScrapeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/ScrapeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/ScrapeConfiguration) 