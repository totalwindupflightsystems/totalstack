---
id: "@specs/aws/network-firewall/docs/API_FlowFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FlowFilter"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# FlowFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_FlowFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FlowFilter
<a name="API_FlowFilter"></a>

Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.

## Contents
<a name="API_FlowFilter_Contents"></a>

 ** DestinationAddress **   <a name="networkfirewall-Type-FlowFilter-DestinationAddress"></a>
A single IP address specification. This is used in the [MatchAttributes](API_MatchAttributes.md) source and destination specifications.  
Type: [Address](API_Address.md) object  
Required: No

 ** DestinationPort **   <a name="networkfirewall-Type-FlowFilter-DestinationPort"></a>
The destination port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994`. To match with any port, specify `ANY`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^.*$`   
Required: No

 ** Protocols **   <a name="networkfirewall-Type-FlowFilter-Protocols"></a>
The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 12.  
Pattern: `^.*$`   
Required: No

 ** SourceAddress **   <a name="networkfirewall-Type-FlowFilter-SourceAddress"></a>
A single IP address specification. This is used in the [MatchAttributes](API_MatchAttributes.md) source and destination specifications.  
Type: [Address](API_Address.md) object  
Required: No

 ** SourcePort **   <a name="networkfirewall-Type-FlowFilter-SourcePort"></a>
The source port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994`. To match with any port, specify `ANY`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^.*$`   
Required: No

## See Also
<a name="API_FlowFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FlowFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FlowFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FlowFilter) 