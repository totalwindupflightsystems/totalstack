---
id: "@specs/aws/network-firewall/docs/API_Flow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Flow"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# Flow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_Flow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Flow
<a name="API_Flow"></a>

Any number of arrays, where each array is a single flow identified in the scope of the operation. If multiple flows were in the scope of the operation, multiple `Flows` arrays are returned.

## Contents
<a name="API_Flow_Contents"></a>

 ** Age **   <a name="networkfirewall-Type-Flow-Age"></a>
Returned as info about age of the flows identified by the flow operation.  
Type: Integer  
Required: No

 ** ByteCount **   <a name="networkfirewall-Type-Flow-ByteCount"></a>
Returns the number of bytes received or transmitted in a specific flow.  
Type: Long  
Required: No

 ** DestinationAddress **   <a name="networkfirewall-Type-Flow-DestinationAddress"></a>
A single IP address specification. This is used in the [MatchAttributes](API_MatchAttributes.md) source and destination specifications.  
Type: [Address](API_Address.md) object  
Required: No

 ** DestinationPort **   <a name="networkfirewall-Type-Flow-DestinationPort"></a>
The destination port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994`. To match with any port, specify `ANY`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^.*$`   
Required: No

 ** PacketCount **   <a name="networkfirewall-Type-Flow-PacketCount"></a>
Returns the total number of data packets received or transmitted in a flow.  
Type: Integer  
Required: No

 ** Protocol **   <a name="networkfirewall-Type-Flow-Protocol"></a>
The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 12.  
Pattern: `^.*$`   
Required: No

 ** SourceAddress **   <a name="networkfirewall-Type-Flow-SourceAddress"></a>
A single IP address specification. This is used in the [MatchAttributes](API_MatchAttributes.md) source and destination specifications.  
Type: [Address](API_Address.md) object  
Required: No

 ** SourcePort **   <a name="networkfirewall-Type-Flow-SourcePort"></a>
The source port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994`. To match with any port, specify `ANY`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^.*$`   
Required: No

## See Also
<a name="API_Flow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/Flow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/Flow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/Flow) 