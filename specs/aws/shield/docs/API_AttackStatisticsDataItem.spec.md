---
id: "@specs/aws/shield/docs/API_AttackStatisticsDataItem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttackStatisticsDataItem"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# AttackStatisticsDataItem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_AttackStatisticsDataItem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttackStatisticsDataItem
<a name="API_AttackStatisticsDataItem"></a>

A single attack statistics data record. This is returned by [DescribeAttackStatistics](API_DescribeAttackStatistics.md) along with a time range indicating the time period that the attack statistics apply to. 

## Contents
<a name="API_AttackStatisticsDataItem_Contents"></a>

 ** AttackCount **   <a name="AWSShield-Type-AttackStatisticsDataItem-AttackCount"></a>
The number of attacks detected during the time period. This is always present, but might be zero.   
Type: Long  
Required: Yes

 ** AttackVolume **   <a name="AWSShield-Type-AttackStatisticsDataItem-AttackVolume"></a>
Information about the volume of attacks during the time period. If the accompanying `AttackCount` is zero, this setting might be empty.  
Type: [AttackVolume](API_AttackVolume.md) object  
Required: No

## See Also
<a name="API_AttackStatisticsDataItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/AttackStatisticsDataItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/AttackStatisticsDataItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/AttackStatisticsDataItem) 