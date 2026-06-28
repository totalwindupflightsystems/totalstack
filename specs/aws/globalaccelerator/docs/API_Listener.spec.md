---
id: "@specs/aws/globalaccelerator/docs/API_Listener"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Listener"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# Listener

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_Listener
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Listener
<a name="API_Listener"></a>

A complex type for a listener.

## Contents
<a name="API_Listener_Contents"></a>

 ** ClientAffinity **   <a name="globalaccelerator-Type-Listener-ClientAffinity"></a>
Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Client affinity gives you control over whether to always route each client to the same specific endpoint.  
 AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is `NONE`, Global Accelerator uses the "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address, destination port, and protocol—to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes.   
If you want a given client to always be routed to the same endpoint, set client affinity to `SOURCE_IP` instead. When you use the `SOURCE_IP` setting, Global Accelerator uses the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to select the hash value.  
The default value is `NONE`.  
Type: String  
Valid Values: `NONE | SOURCE_IP`   
Required: No

 ** ListenerArn **   <a name="globalaccelerator-Type-Listener-ListenerArn"></a>
The Amazon Resource Name (ARN) of the listener.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** PortRanges **   <a name="globalaccelerator-Type-Listener-PortRanges"></a>
The list of port ranges for the connections from clients to the accelerator.  
Type: Array of [PortRange](API_PortRange.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** Protocol **   <a name="globalaccelerator-Type-Listener-Protocol"></a>
The protocol for the connections from clients to the accelerator.  
Type: String  
Valid Values: `TCP | UDP`   
Required: No

## See Also
<a name="API_Listener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/Listener) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/Listener) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/Listener) 