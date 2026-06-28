---
id: "@specs/aws/fsx/docs/API_AutocommitPeriod"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AutocommitPeriod"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# AutocommitPeriod

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_AutocommitPeriod
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AutocommitPeriod
<a name="API_AutocommitPeriod"></a>

Sets the autocommit period of files in an FSx for ONTAP SnapLock volume, which determines how long the files must remain unmodified before they're automatically transitioned to the write once, read many (WORM) state. 

For more information, see [Autocommit](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/worm-state.html#worm-state-autocommit). 

## Contents
<a name="API_AutocommitPeriod_Contents"></a>

 ** Type **   <a name="FSx-Type-AutocommitPeriod-Type"></a>
Defines the type of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. Setting this value to `NONE` disables autocommit. The default value is `NONE`.   
Type: String  
Valid Values: `MINUTES | HOURS | DAYS | MONTHS | YEARS | NONE`   
Required: Yes

 ** Value **   <a name="FSx-Type-AutocommitPeriod-Value"></a>
Defines the amount of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. The following ranges are valid:   
+  `Minutes`: 5 - 65,535
+  `Hours`: 1 - 65,535
+  `Days`: 1 - 3,650
+  `Months`: 1 - 120
+  `Years`: 1 - 10
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

## See Also
<a name="API_AutocommitPeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/AutocommitPeriod) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/AutocommitPeriod) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/AutocommitPeriod) 