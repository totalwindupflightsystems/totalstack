---
id: "@specs/aws/globalaccelerator/docs/API_DestinationPortMapping"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DestinationPortMapping"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# DestinationPortMapping

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_DestinationPortMapping
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DestinationPortMapping
<a name="API_DestinationPortMapping"></a>

The port mappings for a specified endpoint IP address (destination).

## Contents
<a name="API_DestinationPortMapping_Contents"></a>

 ** AcceleratorArn **   <a name="globalaccelerator-Type-DestinationPortMapping-AcceleratorArn"></a>
The Amazon Resource Name (ARN) of the custom routing accelerator that you have port mappings for.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** AcceleratorSocketAddresses **   <a name="globalaccelerator-Type-DestinationPortMapping-AcceleratorSocketAddresses"></a>
The IP address/port combinations (sockets) that map to a given destination socket address.  
Type: Array of [SocketAddress](API_SocketAddress.md) objects  
Required: No

 ** DestinationSocketAddress **   <a name="globalaccelerator-Type-DestinationPortMapping-DestinationSocketAddress"></a>
The endpoint IP address/port combination for traffic received on the accelerator socket address.  
Type: [SocketAddress](API_SocketAddress.md) object  
Required: No

 ** DestinationTrafficState **   <a name="globalaccelerator-Type-DestinationPortMapping-DestinationTrafficState"></a>
Indicates whether or not a port mapping destination can receive traffic. The value is either ALLOW, if traffic is allowed to the destination, or DENY, if traffic is not allowed to the destination.  
Type: String  
Valid Values: `ALLOW | DENY`   
Required: No

 ** EndpointGroupArn **   <a name="globalaccelerator-Type-DestinationPortMapping-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** EndpointGroupRegion **   <a name="globalaccelerator-Type-DestinationPortMapping-EndpointGroupRegion"></a>
The AWS Region for the endpoint group.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** EndpointId **   <a name="globalaccelerator-Type-DestinationPortMapping-EndpointId"></a>
The ID for the virtual private cloud (VPC) subnet.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** IpAddressType **   <a name="globalaccelerator-Type-DestinationPortMapping-IpAddressType"></a>
The IP address type that an accelerator supports. For a custom routing accelerator, the value must be IPV4.  
Type: String  
Valid Values: `IPV4 | DUAL_STACK`   
Required: No

## See Also
<a name="API_DestinationPortMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/DestinationPortMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/DestinationPortMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/DestinationPortMapping) 