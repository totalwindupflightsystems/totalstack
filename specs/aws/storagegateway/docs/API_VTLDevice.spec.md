---
id: "@specs/aws/storagegateway/docs/API_VTLDevice"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VTLDevice"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# VTLDevice

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_VTLDevice
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VTLDevice
<a name="API_VTLDevice"></a>

Represents a device object associated with a tape gateway.

## Contents
<a name="API_VTLDevice_Contents"></a>

 ** DeviceiSCSIAttributes **   <a name="StorageGateway-Type-VTLDevice-DeviceiSCSIAttributes"></a>
A list of iSCSI information about a VTL device.  
Type: [DeviceiSCSIAttributes](API_DeviceiSCSIAttributes.md) object  
Required: No

 ** VTLDeviceARN **   <a name="StorageGateway-Type-VTLDevice-VTLDeviceARN"></a>
Specifies the unique Amazon Resource Name (ARN) of the device (tape drive or media changer).  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** VTLDeviceProductIdentifier **   <a name="StorageGateway-Type-VTLDevice-VTLDeviceProductIdentifier"></a>
Specifies the model number of device that the VTL device emulates.  
Type: String  
Required: No

 ** VTLDeviceType **   <a name="StorageGateway-Type-VTLDevice-VTLDeviceType"></a>
Specifies the type of device that the VTL device emulates.  
Type: String  
Required: No

 ** VTLDeviceVendor **   <a name="StorageGateway-Type-VTLDevice-VTLDeviceVendor"></a>
Specifies the vendor of the device that the VTL device object emulates.  
Type: String  
Required: No

## See Also
<a name="API_VTLDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/VTLDevice) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/VTLDevice) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/VTLDevice) 