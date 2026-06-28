---
id: "@specs/aws/network-firewall/docs/API_TCPFlagField"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TCPFlagField"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# TCPFlagField

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_TCPFlagField
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TCPFlagField
<a name="API_TCPFlagField"></a>

TCP flags and masks to inspect packets for, used in stateless rules [MatchAttributes](API_MatchAttributes.md) settings.

## Contents
<a name="API_TCPFlagField_Contents"></a>

 ** Flags **   <a name="networkfirewall-Type-TCPFlagField-Flags"></a>
Used in conjunction with the `Masks` setting to define the flags that must be set and flags that must not be set in order for the packet to match. This setting can only specify values that are also specified in the `Masks` setting.  
For the flags that are specified in the masks setting, the following must be true for the packet to match:   
+ The ones that are set in this flags setting must be set in the packet. 
+ The ones that are not set in this flags setting must also not be set in the packet. 
Type: Array of strings  
Valid Values: `FIN | SYN | RST | PSH | ACK | URG | ECE | CWR`   
Required: Yes

 ** Masks **   <a name="networkfirewall-Type-TCPFlagField-Masks"></a>
The set of flags to consider in the inspection. To inspect all flags in the valid values list, leave this with no setting.  
Type: Array of strings  
Valid Values: `FIN | SYN | RST | PSH | ACK | URG | ECE | CWR`   
Required: No

## See Also
<a name="API_TCPFlagField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/TCPFlagField) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/TCPFlagField) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/TCPFlagField) 