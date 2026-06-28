---
id: "@specs/aws/network-firewall/docs/API_CIDRSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CIDRSummary"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# CIDRSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_CIDRSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CIDRSummary
<a name="API_CIDRSummary"></a>

Summarizes the CIDR blocks used by the IP set references in a firewall. Network Firewall calculates the number of CIDRs by taking an aggregated count of all CIDRs used by the IP sets you are referencing.

## Contents
<a name="API_CIDRSummary_Contents"></a>

 ** AvailableCIDRCount **   <a name="networkfirewall-Type-CIDRSummary-AvailableCIDRCount"></a>
The number of CIDR blocks available for use by the IP set references in a firewall.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1000000.  
Required: No

 ** IPSetReferences **   <a name="networkfirewall-Type-CIDRSummary-IPSetReferences"></a>
The list of the IP set references used by a firewall.  
Type: String to [IPSetMetadata](API_IPSetMetadata.md) object map  
Required: No

 ** UtilizedCIDRCount **   <a name="networkfirewall-Type-CIDRSummary-UtilizedCIDRCount"></a>
The number of CIDR blocks used by the IP set references in a firewall.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1000000.  
Required: No

## See Also
<a name="API_CIDRSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/CIDRSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/CIDRSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/CIDRSummary) 