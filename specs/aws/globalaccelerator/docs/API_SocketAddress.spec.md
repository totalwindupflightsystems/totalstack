---
id: "@specs/aws/globalaccelerator/docs/API_SocketAddress"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SocketAddress"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# SocketAddress

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_SocketAddress
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SocketAddress
<a name="API_SocketAddress"></a>

An IP address/port combination.

## Contents
<a name="API_SocketAddress_Contents"></a>

 ** IpAddress **   <a name="globalaccelerator-Type-SocketAddress-IpAddress"></a>
The IP address for the socket address.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** Port **   <a name="globalaccelerator-Type-SocketAddress-Port"></a>
The port for the socket address.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

## See Also
<a name="API_SocketAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/SocketAddress) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/SocketAddress) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/SocketAddress) 