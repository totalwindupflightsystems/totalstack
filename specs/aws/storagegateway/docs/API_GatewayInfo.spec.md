---
id: "@specs/aws/storagegateway/docs/API_GatewayInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GatewayInfo"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# GatewayInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_GatewayInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GatewayInfo
<a name="API_GatewayInfo"></a>

Describes a gateway object.

## Contents
<a name="API_GatewayInfo_Contents"></a>

 ** DeprecationDate **   <a name="StorageGateway-Type-GatewayInfo-DeprecationDate"></a>
Date after which this gateway will not receive software updates for new features and bug fixes.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25.  
Required: No

 ** Ec2InstanceId **   <a name="StorageGateway-Type-GatewayInfo-Ec2InstanceId"></a>
The ID of the Amazon EC2 instance that was used to launch the gateway.  
Type: String  
Required: No

 ** Ec2InstanceRegion **   <a name="StorageGateway-Type-GatewayInfo-Ec2InstanceRegion"></a>
The AWS Region where the Amazon EC2 instance is located.  
Type: String  
Required: No

 ** GatewayARN **   <a name="StorageGateway-Type-GatewayInfo-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** GatewayId **   <a name="StorageGateway-Type-GatewayInfo-GatewayId"></a>
The unique identifier assigned to your gateway during activation. This ID becomes part of the gateway Amazon Resource Name (ARN), which you use as input for other operations.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 30.  
Required: No

 ** GatewayName **   <a name="StorageGateway-Type-GatewayInfo-GatewayName"></a>
The name of the gateway.  
Type: String  
Required: No

 ** GatewayOperationalState **   <a name="StorageGateway-Type-GatewayInfo-GatewayOperationalState"></a>
The state of the gateway.  
Valid Values: `DISABLED` \| `ACTIVE`   
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 25.  
Required: No

 ** GatewayType **   <a name="StorageGateway-Type-GatewayInfo-GatewayType"></a>
The type of the gateway.  
Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/).
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 20.  
Required: No

 ** HostEnvironment **   <a name="StorageGateway-Type-GatewayInfo-HostEnvironment"></a>
The type of hardware or software platform on which the gateway is running.  
Tape Gateway is no longer available on Snow Family devices.
Type: String  
Valid Values: `VMWARE | HYPER-V | EC2 | KVM | OTHER | SNOWBALL`   
Required: No

 ** HostEnvironmentId **   <a name="StorageGateway-Type-GatewayInfo-HostEnvironmentId"></a>
A unique identifier for the specific instance of the host platform running the gateway. This value is only available for certain host environments, and its format depends on the host environment type.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

 ** SoftwareVersion **   <a name="StorageGateway-Type-GatewayInfo-SoftwareVersion"></a>
The version number of the software running on the gateway appliance.  
Type: String  
Required: No

## See Also
<a name="API_GatewayInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/GatewayInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/GatewayInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/GatewayInfo) 