---
id: "@specs/aws/storagegateway/docs/API_Tape"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tape"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# Tape

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_Tape
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tape
<a name="API_Tape"></a>

Describes a virtual tape object.

## Contents
<a name="API_Tape_Contents"></a>

 ** KMSKey **   <a name="StorageGateway-Type-Tape-KMSKey"></a>
Optional. The Amazon Resource Name (ARN) of a symmetric AWS KMS key used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric KMS keys. This value must be set if `KMSEncrypted` is `true`, or if `EncryptionType` is `SseKms` or `DsseKms`.  
Type: String  
Length Constraints: Minimum length of 7. Maximum length of 2048.  
Pattern: `(^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`   
Required: No

 ** PoolEntryDate **   <a name="StorageGateway-Type-Tape-PoolEntryDate"></a>
The date that the tape enters a custom tape pool.  
Type: Timestamp  
Required: No

 ** PoolId **   <a name="StorageGateway-Type-Tape-PoolId"></a>
The ID of the pool that contains tapes that will be archived. The tapes in this pool are archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** Progress **   <a name="StorageGateway-Type-Tape-Progress"></a>
For archiving virtual tapes, indicates how much data remains to be uploaded before archiving is complete.  
Range: 0 (not started) to 100 (complete).  
Type: Double  
Required: No

 ** RetentionStartDate **   <a name="StorageGateway-Type-Tape-RetentionStartDate"></a>
The date that the tape is first archived with tape retention lock enabled.  
Type: Timestamp  
Required: No

 ** TapeARN **   <a name="StorageGateway-Type-Tape-TapeARN"></a>
The Amazon Resource Name (ARN) of the virtual tape.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$`   
Required: No

 ** TapeBarcode **   <a name="StorageGateway-Type-Tape-TapeBarcode"></a>
The barcode that identifies a specific virtual tape.  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 16.  
Pattern: `^[A-Z0-9]*$`   
Required: No

 ** TapeCreatedDate **   <a name="StorageGateway-Type-Tape-TapeCreatedDate"></a>
The date the virtual tape was created.  
Type: Timestamp  
Required: No

 ** TapeSizeInBytes **   <a name="StorageGateway-Type-Tape-TapeSizeInBytes"></a>
The size, in bytes, of the virtual tape capacity.  
Type: Long  
Required: No

 ** TapeStatus **   <a name="StorageGateway-Type-Tape-TapeStatus"></a>
The current state of the virtual tape.  
Type: String  
Required: No

 ** TapeUsedInBytes **   <a name="StorageGateway-Type-Tape-TapeUsedInBytes"></a>
The size, in bytes, of data stored on the virtual tape.  
This value is not available for tapes created prior to May 13, 2015.
Type: Long  
Required: No

 ** VTLDevice **   <a name="StorageGateway-Type-Tape-VTLDevice"></a>
The virtual tape library (VTL) device that the virtual tape is associated with.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** Worm **   <a name="StorageGateway-Type-Tape-Worm"></a>
If the tape is archived as write-once-read-many (WORM), this value is `true`.  
Type: Boolean  
Required: No

## See Also
<a name="API_Tape_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/Tape) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/Tape) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/Tape) 