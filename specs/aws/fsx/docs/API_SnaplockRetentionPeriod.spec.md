---
id: "@specs/aws/fsx/docs/API_SnaplockRetentionPeriod"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SnaplockRetentionPeriod"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# SnaplockRetentionPeriod

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_SnaplockRetentionPeriod
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SnaplockRetentionPeriod
<a name="API_SnaplockRetentionPeriod"></a>

The configuration to set the retention period of an FSx for ONTAP SnapLock volume. The retention period includes default, maximum, and minimum settings. For more information, see [Working with the retention period in SnapLock](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-retention.html). 

## Contents
<a name="API_SnaplockRetentionPeriod_Contents"></a>

 ** DefaultRetention **   <a name="FSx-Type-SnaplockRetentionPeriod-DefaultRetention"></a>
The retention period assigned to a write once, read many (WORM) file by default if an explicit retention period is not set for an FSx for ONTAP SnapLock volume. The default retention period must be greater than or equal to the minimum retention period and less than or equal to the maximum retention period.   
Type: [RetentionPeriod](API_RetentionPeriod.md) object  
Required: Yes

 ** MaximumRetention **   <a name="FSx-Type-SnaplockRetentionPeriod-MaximumRetention"></a>
The longest retention period that can be assigned to a WORM file on an FSx for ONTAP SnapLock volume.   
Type: [RetentionPeriod](API_RetentionPeriod.md) object  
Required: Yes

 ** MinimumRetention **   <a name="FSx-Type-SnaplockRetentionPeriod-MinimumRetention"></a>
The shortest retention period that can be assigned to a WORM file on an FSx for ONTAP SnapLock volume.   
Type: [RetentionPeriod](API_RetentionPeriod.md) object  
Required: Yes

## See Also
<a name="API_SnaplockRetentionPeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SnaplockRetentionPeriod) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SnaplockRetentionPeriod) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SnaplockRetentionPeriod) 