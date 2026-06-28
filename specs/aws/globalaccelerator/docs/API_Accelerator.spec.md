---
id: "@specs/aws/globalaccelerator/docs/API_Accelerator"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Accelerator"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# Accelerator

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_Accelerator
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Accelerator
<a name="API_Accelerator"></a>

An accelerator is a complex type that includes one or more listeners that process inbound connections and then direct traffic to one or more endpoint groups, each of which includes endpoints, such as load balancers.

## Contents
<a name="API_Accelerator_Contents"></a>

 ** AcceleratorArn **   <a name="globalaccelerator-Type-Accelerator-AcceleratorArn"></a>
The Amazon Resource Name (ARN) of the accelerator.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** CreatedTime **   <a name="globalaccelerator-Type-Accelerator-CreatedTime"></a>
The date and time that the accelerator was created.  
Type: Timestamp  
Required: No

 ** DnsName **   <a name="globalaccelerator-Type-Accelerator-DnsName"></a>
The Domain Name System (DNS) name that Global Accelerator creates that points to an accelerator's static IPv4 addresses.  
The naming convention for the DNS name for an accelerator is the following: A lowercase letter a, followed by a 16-bit random hex string, followed by .awsglobalaccelerator.com. For example: a1234567890abcdef.awsglobalaccelerator.com.  
If you have a dual-stack accelerator, you also have a second DNS name, `DualStackDnsName`, that points to both the A record and the AAAA record for all four static addresses for the accelerator: two IPv4 addresses and two IPv6 addresses.  
For more information about the default DNS name, see [ Support for DNS addressing in Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/dns-addressing-custom-domains.dns-addressing.html) in the * AWS Global Accelerator Developer Guide*.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** DualStackDnsName **   <a name="globalaccelerator-Type-Accelerator-DualStackDnsName"></a>
The Domain Name System (DNS) name that Global Accelerator creates that points to a dual-stack accelerator's four static IP addresses: two IPv4 addresses and two IPv6 addresses.  
The naming convention for the dual-stack DNS name is the following: A lowercase letter a, followed by a 16-bit random hex string, followed by .dualstack.awsglobalaccelerator.com. For example: a1234567890abcdef.dualstack.awsglobalaccelerator.com.  
Note: Global Accelerator also assigns a default DNS name, `DnsName`, to your accelerator that points just to the static IPv4 addresses.   
For more information, see [ Support for DNS addressing in Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html#about-accelerators.dns-addressing) in the * AWS Global Accelerator Developer Guide*.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** Enabled **   <a name="globalaccelerator-Type-Accelerator-Enabled"></a>
Indicates whether the accelerator is enabled. The value is true or false. The default value is true.   
If the value is set to true, the accelerator cannot be deleted. If set to false, accelerator can be deleted.  
Type: Boolean  
Required: No

 ** Events **   <a name="globalaccelerator-Type-Accelerator-Events"></a>
A history of changes that you make to an accelerator in Global Accelerator.  
Type: Array of [AcceleratorEvent](API_AcceleratorEvent.md) objects  
Required: No

 ** IpAddressType **   <a name="globalaccelerator-Type-Accelerator-IpAddressType"></a>
The IP address type that an accelerator supports. For a standard accelerator, the value can be IPV4 or DUAL\_STACK.  
Type: String  
Valid Values: `IPV4 | DUAL_STACK`   
Required: No

 ** IpSets **   <a name="globalaccelerator-Type-Accelerator-IpSets"></a>
The static IP addresses that Global Accelerator associates with the accelerator.  
Type: Array of [IpSet](API_IpSet.md) objects  
Required: No

 ** LastModifiedTime **   <a name="globalaccelerator-Type-Accelerator-LastModifiedTime"></a>
The date and time that the accelerator was last modified.  
Type: Timestamp  
Required: No

 ** Name **   <a name="globalaccelerator-Type-Accelerator-Name"></a>
The name of the accelerator. The name must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** Status **   <a name="globalaccelerator-Type-Accelerator-Status"></a>
Describes the deployment status of the accelerator.  
Type: String  
Valid Values: `DEPLOYED | IN_PROGRESS`   
Required: No

## See Also
<a name="API_Accelerator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/Accelerator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/Accelerator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/Accelerator) 