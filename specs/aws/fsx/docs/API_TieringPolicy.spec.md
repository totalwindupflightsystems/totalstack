---
id: "@specs/aws/fsx/docs/API_TieringPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TieringPolicy"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# TieringPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_TieringPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TieringPolicy
<a name="API_TieringPolicy"></a>

Describes the data tiering policy for an ONTAP volume. When enabled, Amazon FSx for ONTAP's intelligent tiering automatically transitions a volume's data between the file system's primary storage and capacity pool storage based on your access patterns.

Valid tiering policies are the following:
+  `SNAPSHOT_ONLY` - (Default value) moves cold snapshots to the capacity pool storage tier.
+  `AUTO` - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns.
+  `ALL` - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier.
+  `NONE` - keeps a volume's data in the primary storage tier, preventing it from being moved to the capacity pool tier.

## Contents
<a name="API_TieringPolicy_Contents"></a>

 ** CoolingPeriod **   <a name="FSx-Type-TieringPolicy-CoolingPeriod"></a>
Specifies the number of days that user data in a volume must remain inactive before it is considered "cold" and moved to the capacity pool. Used with the `AUTO` and `SNAPSHOT_ONLY` tiering policies. Enter a whole number between 2 and 183. Default values are 31 days for `AUTO` and 2 days for `SNAPSHOT_ONLY`.  
Type: Integer  
Valid Range: Minimum value of 2. Maximum value of 183.  
Required: No

 ** Name **   <a name="FSx-Type-TieringPolicy-Name"></a>
Specifies the tiering policy used to transition data. Default value is `SNAPSHOT_ONLY`.  
+  `SNAPSHOT_ONLY` - moves cold snapshots to the capacity pool storage tier.
+  `AUTO` - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns.
+  `ALL` - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier.
+  `NONE` - keeps a volume's data in the primary storage tier, preventing it from being moved to the capacity pool tier.
Type: String  
Valid Values: `SNAPSHOT_ONLY | AUTO | ALL | NONE`   
Required: No

## See Also
<a name="API_TieringPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/TieringPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/TieringPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/TieringPolicy) 