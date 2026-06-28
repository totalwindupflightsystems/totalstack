---
id: "@specs/aws/storagegateway/docs/API_AutomaticTapeCreationRule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AutomaticTapeCreationRule"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# AutomaticTapeCreationRule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_AutomaticTapeCreationRule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AutomaticTapeCreationRule
<a name="API_AutomaticTapeCreationRule"></a>

An automatic tape creation policy consists of automatic tape creation rules where each rule defines when and how to create new tapes. For more information about automatic tape creation, see [Creating Tapes Automatically](https://docs.aws.amazon.com/storagegateway/latest/userguide/GettingStartedCreateTapes.html#CreateTapesAutomatically).

## Contents
<a name="API_AutomaticTapeCreationRule_Contents"></a>

 ** MinimumNumTapes **   <a name="StorageGateway-Type-AutomaticTapeCreationRule-MinimumNumTapes"></a>
The minimum number of available virtual tapes that the gateway maintains at all times. If the number of tapes on the gateway goes below this value, the gateway creates as many new tapes as are needed to have `MinimumNumTapes` on the gateway. For more information about automatic tape creation, see [Creating Tapes Automatically](https://docs.aws.amazon.com/storagegateway/latest/userguide/GettingStartedCreateTapes.html#CreateTapesAutomatically).  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10.  
Required: Yes

 ** PoolId **   <a name="StorageGateway-Type-AutomaticTapeCreationRule-PoolId"></a>
The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the Amazon S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: Yes

 ** TapeBarcodePrefix **   <a name="StorageGateway-Type-AutomaticTapeCreationRule-TapeBarcodePrefix"></a>
A prefix that you append to the barcode of the virtual tape that you are creating. This prefix makes the barcode unique.  
The prefix must be 1-4 characters in length and must be one of the uppercase letters from A to Z.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4.  
Pattern: `^[A-Z]*$`   
Required: Yes

 ** TapeSizeInBytes **   <a name="StorageGateway-Type-AutomaticTapeCreationRule-TapeSizeInBytes"></a>
The size, in bytes, of the virtual tape capacity.  
Type: Long  
Required: Yes

 ** Worm **   <a name="StorageGateway-Type-AutomaticTapeCreationRule-Worm"></a>
Set to `true` to indicate that tapes are to be archived as write-once-read-many (WORM). Set to `false` when WORM is not enabled for tapes.  
Type: Boolean  
Required: No

## See Also
<a name="API_AutomaticTapeCreationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/AutomaticTapeCreationRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/AutomaticTapeCreationRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/AutomaticTapeCreationRule) 