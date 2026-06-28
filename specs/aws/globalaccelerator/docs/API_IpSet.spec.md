---
id: "@specs/aws/globalaccelerator/docs/API_IpSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS IpSet"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# IpSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_IpSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# IpSet
<a name="API_IpSet"></a>

A complex type for the set of IP addresses for an accelerator.

## Contents
<a name="API_IpSet_Contents"></a>

 ** IpAddresses **   <a name="globalaccelerator-Type-IpSet-IpAddresses"></a>
The array of IP addresses in the IP address set. An IP address set can have a maximum of two IP addresses.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2 items.  
Length Constraints: Maximum length of 45.  
Required: No

 ** IpAddressFamily **   <a name="globalaccelerator-Type-IpSet-IpAddressFamily"></a>
The types of IP addresses included in this IP set.   
Type: String  
Valid Values: `IPv4 | IPv6`   
Required: No

 ** IpFamily **   <a name="globalaccelerator-Type-IpSet-IpFamily"></a>
IpFamily is deprecated and has been replaced by IpAddressFamily.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## See Also
<a name="API_IpSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/IpSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/IpSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/IpSet) 