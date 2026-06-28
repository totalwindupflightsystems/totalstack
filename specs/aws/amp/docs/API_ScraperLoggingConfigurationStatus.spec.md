---
id: "@specs/aws/amp/docs/API_ScraperLoggingConfigurationStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ScraperLoggingConfigurationStatus"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# ScraperLoggingConfigurationStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_ScraperLoggingConfigurationStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ScraperLoggingConfigurationStatus
<a name="API_ScraperLoggingConfigurationStatus"></a>

The status of a scraper logging configuration.

## Contents
<a name="API_ScraperLoggingConfigurationStatus_Contents"></a>

 ** statusCode **   <a name="prometheus-Type-ScraperLoggingConfigurationStatus-statusCode"></a>
The status code of the scraper logging configuration.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATION_FAILED | UPDATE_FAILED`   
Required: Yes

 ** statusReason **   <a name="prometheus-Type-ScraperLoggingConfigurationStatus-statusReason"></a>
The reason for the current status of the scraper logging configuration.  
Type: String  
Required: No

## See Also
<a name="API_ScraperLoggingConfigurationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/ScraperLoggingConfigurationStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/ScraperLoggingConfigurationStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/ScraperLoggingConfigurationStatus) 