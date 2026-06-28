---
id: "@specs/aws/network-firewall/docs/API_FlowTimeouts"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FlowTimeouts"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# FlowTimeouts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_FlowTimeouts
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FlowTimeouts
<a name="API_FlowTimeouts"></a>

Describes the amount of time that can pass without any traffic sent through the firewall before the firewall determines that the connection is idle and Network Firewall removes the flow entry from its flow table. When you update this value, existing connections will be treated according to your stream exception policy configuration. 

## Contents
<a name="API_FlowTimeouts_Contents"></a>

 ** TcpIdleTimeoutSeconds **   <a name="networkfirewall-Type-FlowTimeouts-TcpIdleTimeoutSeconds"></a>
The number of seconds that can pass without any TCP traffic sent through the firewall before the firewall determines that the connection is idle. After the idle timeout passes, data packets are dropped, however, the next TCP SYN packet is considered a new flow and is processed by the firewall. Clients or targets can use TCP keepalive packets to reset the idle timeout.   
You can define the `TcpIdleTimeoutSeconds` value to be between 60 and 6000 seconds. If no value is provided, it defaults to 350 seconds.   
Type: Integer  
Required: No

## See Also
<a name="API_FlowTimeouts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FlowTimeouts) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FlowTimeouts) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FlowTimeouts) 