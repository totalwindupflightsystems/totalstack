---
id: "@specs/aws/storagegateway/docs/API_NetworkInterface"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NetworkInterface"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# NetworkInterface

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_NetworkInterface
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NetworkInterface
<a name="API_NetworkInterface"></a>

Describes a gateway's network interface.

## Contents
<a name="API_NetworkInterface_Contents"></a>

 ** Ipv4Address **   <a name="StorageGateway-Type-NetworkInterface-Ipv4Address"></a>
The Internet Protocol version 4 (IPv4) address of the interface.  
Type: String  
Required: No

 ** Ipv6Address **   <a name="StorageGateway-Type-NetworkInterface-Ipv6Address"></a>
The Internet Protocol version 6 (IPv6) address of the interface.  
This element returns IPv6 addresses for all gateway types except FSx File Gateway.
Type: String  
Required: No

 ** MacAddress **   <a name="StorageGateway-Type-NetworkInterface-MacAddress"></a>
The Media Access Control (MAC) address of the interface.  
This is currently unsupported and will not be returned in output.
Type: String  
Required: No

## See Also
<a name="API_NetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/NetworkInterface) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/NetworkInterface) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/NetworkInterface) 