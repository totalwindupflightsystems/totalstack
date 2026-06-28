---
id: "@specs/aws/network-firewall/docs/API_PortRange"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PortRange"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# PortRange

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_PortRange
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PortRange
<a name="API_PortRange"></a>

A single port range specification. This is used for source and destination port ranges in the stateless rule [MatchAttributes](API_MatchAttributes.md), `SourcePorts`, and `DestinationPorts` settings. 

## Contents
<a name="API_PortRange_Contents"></a>

 ** FromPort **   <a name="networkfirewall-Type-PortRange-FromPort"></a>
The lower limit of the port range. This must be less than or equal to the `ToPort` specification.   
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 65535.  
Required: Yes

 ** ToPort **   <a name="networkfirewall-Type-PortRange-ToPort"></a>
The upper limit of the port range. This must be greater than or equal to the `FromPort` specification.   
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 65535.  
Required: Yes

## See Also
<a name="API_PortRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/PortRange) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/PortRange) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/PortRange) 