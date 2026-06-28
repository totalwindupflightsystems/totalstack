---
id: "@specs/aws/storagegateway/docs/API_EndpointNetworkConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EndpointNetworkConfiguration"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# EndpointNetworkConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_EndpointNetworkConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EndpointNetworkConfiguration
<a name="API_EndpointNetworkConfiguration"></a>

Specifies network configuration information for the gateway associated with the Amazon FSx file system.

## Contents
<a name="API_EndpointNetworkConfiguration_Contents"></a>

 ** IpAddresses **   <a name="StorageGateway-Type-EndpointNetworkConfiguration-IpAddresses"></a>
A list of gateway IP addresses on which the associated Amazon FSx file system is available.  
If multiple file systems are associated with this gateway, this field is required.
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 7. Maximum length of 15.  
Pattern: `^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}`   
Required: No

## See Also
<a name="API_EndpointNetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/EndpointNetworkConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/EndpointNetworkConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/EndpointNetworkConfiguration) 