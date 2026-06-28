---
id: "@specs/aws/globalaccelerator/docs/API_CustomRoutingAccelerator"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CustomRoutingAccelerator"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# CustomRoutingAccelerator

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_CustomRoutingAccelerator
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CustomRoutingAccelerator
<a name="API_CustomRoutingAccelerator"></a>

Attributes of a custom routing accelerator.

## Contents
<a name="API_CustomRoutingAccelerator_Contents"></a>

 ** AcceleratorArn **   <a name="globalaccelerator-Type-CustomRoutingAccelerator-AcceleratorArn"></a>
The Amazon Resource Name (ARN) of the custom routing accelerator.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** CreatedTime **   <a name="globalaccelerator-Type-CustomRoutingAccelerator-CreatedTime"></a>
The date and time that the accelerator was created.  
Type: Timestamp  
Required: No

 ** DnsName **   <a name="globalaccelerator-Type-CustomRoutingAccelerator-DnsName"></a>
The Domain Name System (DNS) name that Global Accelerator creates that points to an accelerator's static IPv4 addresses.   
The naming convention for the DNS name is the following: A lowercase letter a, followed by a 16-bit random hex string, followed by .awsglobalaccelerator.com. For example: a1234567890abcdef.awsglobalaccelerator.com.  
If you have a dual-stack accelerator, you also have a second DNS name, `DualStackDnsName`, that points to both the A record and the AAAA record for all four static addresses for the accelerator: two IPv4 addresses and two IPv6 addresses.  
For more information about the default DNS name, see [ Support for DNS addressing in Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/dns-addressing-custom-domains.dns-addressing.html) in the * AWS Global Accelerator Developer Guide*.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** Enabled **   <a name="globalaccelerator-Type-CustomRoutingAccelerator-Enabled"></a>
Indicates whether the accelerator is enabled. The value is true or false. The default value is true.   
If the value is set to true, the accelerator cannot be deleted. If set to false, accelerator can be deleted.  
Type: Boolean  
Required: No

 ** IpAddressType **   <a name="globalaccelerator-Type-CustomRoutingAccelerator-IpAddressType"></a>
The IP address type that an accelerator supports. For a custom routing accelerator, the value must be IPV4.  
Type: String  
Valid Values: `IPV4 | DUAL_STACK`   
Required: No

 ** IpSets **   <a name="globalaccelerator-Type-CustomRoutingAccelerator-IpSets"></a>
The static IP addresses that Global Accelerator associates with the accelerator.  
Type: Array of [IpSet](API_IpSet.md) objects  
Required: No

 ** LastModifiedTime **   <a name="globalaccelerator-Type-CustomRoutingAccelerator-LastModifiedTime"></a>
The date and time that the accelerator was last modified.  
Type: Timestamp  
Required: No

 ** Name **   <a name="globalaccelerator-Type-CustomRoutingAccelerator-Name"></a>
The name of the accelerator. The name must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** Status **   <a name="globalaccelerator-Type-CustomRoutingAccelerator-Status"></a>
Describes the deployment status of the accelerator.  
Type: String  
Valid Values: `DEPLOYED | IN_PROGRESS`   
Required: No

## See Also
<a name="API_CustomRoutingAccelerator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CustomRoutingAccelerator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CustomRoutingAccelerator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CustomRoutingAccelerator) 