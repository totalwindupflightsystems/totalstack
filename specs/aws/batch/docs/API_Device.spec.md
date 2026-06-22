---
id: "@specs/aws/batch/docs/API_Device"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Device"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# Device

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_Device
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Device
<a name="API_Device"></a>

An object that represents a container instance host device.

**Note**  
This object isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.

## Contents
<a name="API_Device_Contents"></a>

 ** hostPath **   <a name="Batch-Type-Device-hostPath"></a>
The path for the device on the host container instance.  
Type: String  
Required: Yes

 ** containerPath **   <a name="Batch-Type-Device-containerPath"></a>
The path inside the container that's used to expose the host device. By default, the `hostPath` value is used.  
Type: String  
Required: No

 ** permissions **   <a name="Batch-Type-Device-permissions"></a>
The explicit permissions to provide to the container for the device. By default, the container has permissions for `read`, `write`, and `mknod` for the device.  
Type: Array of strings  
Valid Values: `READ | WRITE | MKNOD`   
Required: No

## See Also
<a name="API_Device_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/Device) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/Device) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/Device) 