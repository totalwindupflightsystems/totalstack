---
id: "@specs/aws/storagegateway/docs/API_TapeRecoveryPointInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TapeRecoveryPointInfo"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# TapeRecoveryPointInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_TapeRecoveryPointInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TapeRecoveryPointInfo
<a name="API_TapeRecoveryPointInfo"></a>

Describes a recovery point.

## Contents
<a name="API_TapeRecoveryPointInfo_Contents"></a>

 ** TapeARN **   <a name="StorageGateway-Type-TapeRecoveryPointInfo-TapeARN"></a>
The Amazon Resource Name (ARN) of the virtual tape.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$`   
Required: No

 ** TapeRecoveryPointTime **   <a name="StorageGateway-Type-TapeRecoveryPointInfo-TapeRecoveryPointTime"></a>
The time when the point-in-time view of the virtual tape was replicated for later recovery.  
The default timestamp format of the tape recovery point time is in the ISO8601 extended YYYY-MM-DD'T'HH:MM:SS'Z' format.  
Type: Timestamp  
Required: No

 ** TapeSizeInBytes **   <a name="StorageGateway-Type-TapeRecoveryPointInfo-TapeSizeInBytes"></a>
The size, in bytes, of the virtual tapes to recover.  
Type: Long  
Required: No

 ** TapeStatus **   <a name="StorageGateway-Type-TapeRecoveryPointInfo-TapeStatus"></a>
The status of the virtual tapes.  
Type: String  
Required: No

## See Also
<a name="API_TapeRecoveryPointInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/TapeRecoveryPointInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/TapeRecoveryPointInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/TapeRecoveryPointInfo) 