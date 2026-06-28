---
id: "@specs/aws/fsx/docs/API_DiskIopsConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DiskIopsConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DiskIopsConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DiskIopsConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DiskIopsConfiguration
<a name="API_DiskIopsConfiguration"></a>

The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for NetApp ONTAP, Amazon FSx for Windows File Server, or FSx for OpenZFS file system. By default, Amazon FSx automatically provisions 3 IOPS per GB of storage capacity. You can provision additional IOPS per GB of storage. The configuration consists of the total number of provisioned SSD IOPS and how it is was provisioned, or the mode (by the customer or by Amazon FSx).

## Contents
<a name="API_DiskIopsConfiguration_Contents"></a>

 ** Iops **   <a name="FSx-Type-DiskIopsConfiguration-Iops"></a>
The total number of SSD IOPS provisioned for the file system.  
The minimum and maximum values for this property depend on the value of `HAPairs` and `StorageCapacity`. The minimum value is calculated as `StorageCapacity` \* 3 \* `HAPairs` (3 IOPS per GB of `StorageCapacity`). The maximum value is calculated as 200,000 \* `HAPairs`.  
Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `Iops` is outside of the minimum or maximum values.  
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 2400000.  
Required: No

 ** Mode **   <a name="FSx-Type-DiskIopsConfiguration-Mode"></a>
Specifies whether the file system is using the `AUTOMATIC` setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a `USER_PROVISIONED` value.  
Type: String  
Valid Values: `AUTOMATIC | USER_PROVISIONED`   
Required: No

## See Also
<a name="API_DiskIopsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DiskIopsConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DiskIopsConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DiskIopsConfiguration) 