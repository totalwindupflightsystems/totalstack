---
id: "@specs/aws/storagegateway/docs/API_TapeInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TapeInfo"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# TapeInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_TapeInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TapeInfo
<a name="API_TapeInfo"></a>

Describes a virtual tape.

## Contents
<a name="API_TapeInfo_Contents"></a>

 ** GatewayARN **   <a name="StorageGateway-Type-TapeInfo-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** PoolEntryDate **   <a name="StorageGateway-Type-TapeInfo-PoolEntryDate"></a>
The date that the tape entered the custom tape pool with tape retention lock enabled.  
Type: Timestamp  
Required: No

 ** PoolId **   <a name="StorageGateway-Type-TapeInfo-PoolId"></a>
The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** RetentionStartDate **   <a name="StorageGateway-Type-TapeInfo-RetentionStartDate"></a>
The date that the tape became subject to tape retention lock.  
Type: Timestamp  
Required: No

 ** TapeARN **   <a name="StorageGateway-Type-TapeInfo-TapeARN"></a>
The Amazon Resource Name (ARN) of a virtual tape.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$`   
Required: No

 ** TapeBarcode **   <a name="StorageGateway-Type-TapeInfo-TapeBarcode"></a>
The barcode that identifies a specific virtual tape.  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 16.  
Pattern: `^[A-Z0-9]*$`   
Required: No

 ** TapeSizeInBytes **   <a name="StorageGateway-Type-TapeInfo-TapeSizeInBytes"></a>
The size, in bytes, of a virtual tape.  
Type: Long  
Required: No

 ** TapeStatus **   <a name="StorageGateway-Type-TapeInfo-TapeStatus"></a>
The status of the tape.  
Type: String  
Required: No

## See Also
<a name="API_TapeInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/TapeInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/TapeInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/TapeInfo) 