---
id: "@specs/aws/storagegateway/docs/API_PoolInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PoolInfo"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# PoolInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_PoolInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PoolInfo
<a name="API_PoolInfo"></a>

Describes a custom tape pool.

## Contents
<a name="API_PoolInfo_Contents"></a>

 ** PoolARN **   <a name="StorageGateway-Type-PoolInfo-PoolARN"></a>
The Amazon Resource Name (ARN) of the custom tape pool. Use the [ListTapePools](API_ListTapePools.md) operation to return a list of custom tape pools for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** PoolName **   <a name="StorageGateway-Type-PoolInfo-PoolName"></a>
The name of the custom tape pool. `PoolName` can use all ASCII characters, except '/' and '\\'.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `^[ -\.0-\[\]-~]*[!-\.0-\[\]-~][ -\.0-\[\]-~]*$`   
Required: No

 ** PoolStatus **   <a name="StorageGateway-Type-PoolInfo-PoolStatus"></a>
Status of the custom tape pool. Pool can be `ACTIVE` or `DELETED`.  
Type: String  
Valid Values: `ACTIVE | DELETED`   
Required: No

 ** RetentionLockTimeInDays **   <a name="StorageGateway-Type-PoolInfo-RetentionLockTimeInDays"></a>
Tape retention lock time is set in days. Tape retention lock can be enabled for up to 100 years (36,500 days).  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 36500.  
Required: No

 ** RetentionLockType **   <a name="StorageGateway-Type-PoolInfo-RetentionLockType"></a>
Tape retention lock type, which can be configured in two modes. When configured in governance mode, AWS accounts with specific IAM permissions are authorized to remove the tape retention lock from archived virtual tapes. When configured in compliance mode, the tape retention lock cannot be removed by any user, including the root AWS account.  
Type: String  
Valid Values: `COMPLIANCE | GOVERNANCE | NONE`   
Required: No

 ** StorageClass **   <a name="StorageGateway-Type-PoolInfo-StorageClass"></a>
The storage class that is associated with the custom pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.  
Type: String  
Valid Values: `DEEP_ARCHIVE | GLACIER`   
Required: No

## See Also
<a name="API_PoolInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/PoolInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/PoolInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/PoolInfo) 