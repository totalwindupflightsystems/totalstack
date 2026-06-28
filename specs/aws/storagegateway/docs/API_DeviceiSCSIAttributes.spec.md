---
id: "@specs/aws/storagegateway/docs/API_DeviceiSCSIAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeviceiSCSIAttributes"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DeviceiSCSIAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DeviceiSCSIAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeviceiSCSIAttributes
<a name="API_DeviceiSCSIAttributes"></a>

Lists iSCSI information about a VTL device.

## Contents
<a name="API_DeviceiSCSIAttributes_Contents"></a>

 ** ChapEnabled **   <a name="StorageGateway-Type-DeviceiSCSIAttributes-ChapEnabled"></a>
Indicates whether mutual CHAP is enabled for the iSCSI target.  
Type: Boolean  
Required: No

 ** NetworkInterfaceId **   <a name="StorageGateway-Type-DeviceiSCSIAttributes-NetworkInterfaceId"></a>
The network interface identifier of the VTL device.  
Type: String  
Required: No

 ** NetworkInterfacePort **   <a name="StorageGateway-Type-DeviceiSCSIAttributes-NetworkInterfacePort"></a>
The port used to communicate with iSCSI VTL device targets.  
Type: Integer  
Required: No

 ** TargetARN **   <a name="StorageGateway-Type-DeviceiSCSIAttributes-TargetARN"></a>
Specifies the unique Amazon Resource Name (ARN) that encodes the iSCSI qualified name(iqn) of a tape drive or media changer target.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 800.  
Required: No

## See Also
<a name="API_DeviceiSCSIAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DeviceiSCSIAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DeviceiSCSIAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DeviceiSCSIAttributes) 