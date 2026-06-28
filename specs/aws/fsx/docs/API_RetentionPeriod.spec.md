---
id: "@specs/aws/fsx/docs/API_RetentionPeriod"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RetentionPeriod"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# RetentionPeriod

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_RetentionPeriod
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RetentionPeriod
<a name="API_RetentionPeriod"></a>

Specifies the retention period of an FSx for ONTAP SnapLock volume. After it is set, it can't be changed. Files can't be deleted or modified during the retention period. 

For more information, see [Working with the retention period in SnapLock](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-retention.html). 

## Contents
<a name="API_RetentionPeriod_Contents"></a>

 ** Type **   <a name="FSx-Type-RetentionPeriod-Type"></a>
Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE`, the files are retained forever. If you set it to `UNSPECIFIED`, the files are retained until you set an explicit retention period.   
Type: String  
Valid Values: `SECONDS | MINUTES | HOURS | DAYS | MONTHS | YEARS | INFINITE | UNSPECIFIED`   
Required: Yes

 ** Value **   <a name="FSx-Type-RetentionPeriod-Value"></a>
Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You can't set a value for `INFINITE` or `UNSPECIFIED`. For all other options, the following ranges are valid:   
+  `Seconds`: 0 - 65,535
+  `Minutes`: 0 - 65,535
+  `Hours`: 0 - 24
+  `Days`: 0 - 365
+  `Months`: 0 - 12
+  `Years`: 0 - 100
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 65535.  
Required: No

## See Also
<a name="API_RetentionPeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/RetentionPeriod) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/RetentionPeriod) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/RetentionPeriod) 