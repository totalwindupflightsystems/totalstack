---
id: "@specs/aws/cloudtrail/docs/API_SourceConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SourceConfig"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# SourceConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_SourceConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SourceConfig
<a name="API_SourceConfig"></a>

 Contains configuration information about the channel. 

## Contents
<a name="API_SourceConfig_Contents"></a>

 ** AdvancedEventSelectors **   <a name="awscloudtrail-Type-SourceConfig-AdvancedEventSelectors"></a>
 The advanced event selectors that are configured for the channel.  
Type: Array of [AdvancedEventSelector](API_AdvancedEventSelector.md) objects  
Required: No

 ** ApplyToAllRegions **   <a name="awscloudtrail-Type-SourceConfig-ApplyToAllRegions"></a>
 Specifies whether the channel applies to a single Region or to all Regions.  
Type: Boolean  
Required: No

## See Also
<a name="API_SourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/SourceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/SourceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/SourceConfig) 