---
id: "@specs/aws/network-firewall/docs/API_IPSetMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS IPSetMetadata"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# IPSetMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_IPSetMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# IPSetMetadata
<a name="API_IPSetMetadata"></a>

General information about the IP set.

## Contents
<a name="API_IPSetMetadata_Contents"></a>

 ** ResolvedCIDRCount **   <a name="networkfirewall-Type-IPSetMetadata-ResolvedCIDRCount"></a>
Describes the total number of CIDR blocks currently in use by the IP set references in a firewall. To determine how many CIDR blocks are available for you to use in a firewall, you can call `AvailableCIDRCount`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1000000.  
Required: No

## See Also
<a name="API_IPSetMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/IPSetMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/IPSetMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/IPSetMetadata) 