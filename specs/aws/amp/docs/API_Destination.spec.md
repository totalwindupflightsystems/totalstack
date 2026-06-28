---
id: "@specs/aws/amp/docs/API_Destination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Destination"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# Destination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_Destination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Destination
<a name="API_Destination"></a>

Where to send the metrics from a scraper.

## Contents
<a name="API_Destination_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ampConfiguration **   <a name="prometheus-Type-Destination-ampConfiguration"></a>
The Amazon Managed Service for Prometheus workspace to send metrics to.  
Type: [AmpConfiguration](API_AmpConfiguration.md) object  
Required: No

## See Also
<a name="API_Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/Destination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/Destination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/Destination) 