---
id: "@specs/aws/shield/docs/API_AttackVolume"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttackVolume"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# AttackVolume

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_AttackVolume
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttackVolume
<a name="API_AttackVolume"></a>

Information about the volume of attacks during the time period, included in an [AttackStatisticsDataItem](API_AttackStatisticsDataItem.md). If the accompanying `AttackCount` in the statistics object is zero, this setting might be empty.

## Contents
<a name="API_AttackVolume_Contents"></a>

 ** BitsPerSecond **   <a name="AWSShield-Type-AttackVolume-BitsPerSecond"></a>
A statistics object that uses bits per second as the unit. This is included for network level attacks.   
Type: [AttackVolumeStatistics](API_AttackVolumeStatistics.md) object  
Required: No

 ** PacketsPerSecond **   <a name="AWSShield-Type-AttackVolume-PacketsPerSecond"></a>
A statistics object that uses packets per second as the unit. This is included for network level attacks.   
Type: [AttackVolumeStatistics](API_AttackVolumeStatistics.md) object  
Required: No

 ** RequestsPerSecond **   <a name="AWSShield-Type-AttackVolume-RequestsPerSecond"></a>
A statistics object that uses requests per second as the unit. This is included for application level attacks, and is only available for accounts that are subscribed to Shield Advanced.  
Type: [AttackVolumeStatistics](API_AttackVolumeStatistics.md) object  
Required: No

## See Also
<a name="API_AttackVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/AttackVolume) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/AttackVolume) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/AttackVolume) 