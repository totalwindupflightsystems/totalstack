---
id: "@specs/aws/storagegateway/docs/API_TapeArchive"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TapeArchive"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# TapeArchive

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_TapeArchive
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TapeArchive
<a name="API_TapeArchive"></a>

Represents a virtual tape that is archived in the virtual tape shelf (VTS).

## Contents
<a name="API_TapeArchive_Contents"></a>

 ** CompletionTime **   <a name="StorageGateway-Type-TapeArchive-CompletionTime"></a>
The time that the archiving of the virtual tape was completed.  
The default timestamp format is in the ISO8601 extended YYYY-MM-DD'T'HH:MM:SS'Z' format.  
Type: Timestamp  
Required: No

 ** KMSKey **   <a name="StorageGateway-Type-TapeArchive-KMSKey"></a>
Optional. The Amazon Resource Name (ARN) of a symmetric AWS KMS key used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric KMS keys. This value must be set if `KMSEncrypted` is `true`, or if `EncryptionType` is `SseKms` or `DsseKms`.  
Type: String  
Length Constraints: Minimum length of 7. Maximum length of 2048.  
Pattern: `(^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`   
Required: No

 ** PoolEntryDate **   <a name="StorageGateway-Type-TapeArchive-PoolEntryDate"></a>
The time that the tape entered the custom tape pool.  
The default timestamp format is in the ISO8601 extended YYYY-MM-DD'T'HH:MM:SS'Z' format.  
Type: Timestamp  
Required: No

 ** PoolId **   <a name="StorageGateway-Type-TapeArchive-PoolId"></a>
The ID of the pool that was used to archive the tape. The tapes in this pool are archived in the S3 storage class that is associated with the pool.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** RetentionStartDate **   <a name="StorageGateway-Type-TapeArchive-RetentionStartDate"></a>
If the archived tape is subject to tape retention lock, the date that the archived tape started being retained.  
Type: Timestamp  
Required: No

 ** RetrievedTo **   <a name="StorageGateway-Type-TapeArchive-RetrievedTo"></a>
The Amazon Resource Name (ARN) of the tape gateway that the virtual tape is being retrieved to.  
The virtual tape is retrieved from the virtual tape shelf (VTS).  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** TapeARN **   <a name="StorageGateway-Type-TapeArchive-TapeARN"></a>
The Amazon Resource Name (ARN) of an archived virtual tape.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$`   
Required: No

 ** TapeBarcode **   <a name="StorageGateway-Type-TapeArchive-TapeBarcode"></a>
The barcode that identifies the archived virtual tape.  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 16.  
Pattern: `^[A-Z0-9]*$`   
Required: No

 ** TapeCreatedDate **   <a name="StorageGateway-Type-TapeArchive-TapeCreatedDate"></a>
The date the virtual tape was created.  
Type: Timestamp  
Required: No

 ** TapeSizeInBytes **   <a name="StorageGateway-Type-TapeArchive-TapeSizeInBytes"></a>
The size, in bytes, of the archived virtual tape.  
Type: Long  
Required: No

 ** TapeStatus **   <a name="StorageGateway-Type-TapeArchive-TapeStatus"></a>
The current state of the archived virtual tape.  
Type: String  
Required: No

 ** TapeUsedInBytes **   <a name="StorageGateway-Type-TapeArchive-TapeUsedInBytes"></a>
The size, in bytes, of data stored on the virtual tape.  
This value is not available for tapes created prior to May 13, 2015.
Type: Long  
Required: No

 ** Worm **   <a name="StorageGateway-Type-TapeArchive-Worm"></a>
Set to `true` if the archived tape is stored as write-once-read-many (WORM).  
Type: Boolean  
Required: No

## See Also
<a name="API_TapeArchive_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/TapeArchive) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/TapeArchive) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/TapeArchive) 