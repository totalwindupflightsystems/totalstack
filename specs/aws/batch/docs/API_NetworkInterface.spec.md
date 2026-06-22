---
id: "@specs/aws/batch/docs/API_NetworkInterface"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NetworkInterface"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# NetworkInterface

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_NetworkInterface
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NetworkInterface
<a name="API_NetworkInterface"></a>

An object that represents the elastic network interface for a multi-node parallel job node.

## Contents
<a name="API_NetworkInterface_Contents"></a>

 ** attachmentId **   <a name="Batch-Type-NetworkInterface-attachmentId"></a>
The attachment ID for the network interface.  
Type: String  
Required: No

 ** ipv6Address **   <a name="Batch-Type-NetworkInterface-ipv6Address"></a>
The private IPv6 address for the network interface.  
Type: String  
Required: No

 ** privateIpv4Address **   <a name="Batch-Type-NetworkInterface-privateIpv4Address"></a>
The private IPv4 address for the network interface.  
Type: String  
Required: No

## See Also
<a name="API_NetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/NetworkInterface) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/NetworkInterface) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/NetworkInterface) 