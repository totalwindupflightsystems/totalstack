---
id: "@specs/aws/amp/docs/API_ScraperComponent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ScraperComponent"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# ScraperComponent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_ScraperComponent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ScraperComponent
<a name="API_ScraperComponent"></a>

A component of a Amazon Managed Service for Prometheus scraper that can be configured for logging.

## Contents
<a name="API_ScraperComponent_Contents"></a>

 ** type **   <a name="prometheus-Type-ScraperComponent-type"></a>
The type of the scraper component.  
Type: String  
Valid Values: `SERVICE_DISCOVERY | COLLECTOR | EXPORTER`   
Required: Yes

 ** config **   <a name="prometheus-Type-ScraperComponent-config"></a>
The configuration settings for the scraper component.  
Type: [ComponentConfig](API_ComponentConfig.md) object  
Required: No

## See Also
<a name="API_ScraperComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/ScraperComponent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/ScraperComponent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/ScraperComponent) 