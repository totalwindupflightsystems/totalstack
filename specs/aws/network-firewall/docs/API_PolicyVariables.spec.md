---
id: "@specs/aws/network-firewall/docs/API_PolicyVariables"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PolicyVariables"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# PolicyVariables

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_PolicyVariables
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PolicyVariables
<a name="API_PolicyVariables"></a>

Contains variables that you can use to override default Suricata settings in your firewall policy.

## Contents
<a name="API_PolicyVariables_Contents"></a>

 ** RuleVariables **   <a name="networkfirewall-Type-PolicyVariables-RuleVariables"></a>
The IPv4 or IPv6 addresses in CIDR notation to use for the Suricata `HOME_NET` variable. If your firewall uses an inspection VPC, you might want to override the `HOME_NET` variable with the CIDRs of your home networks. If you don't override `HOME_NET` with your own CIDRs, Network Firewall by default uses the CIDR of your inspection VPC.  
Type: String to [IPSet](API_IPSet.md) object map  
Key Length Constraints: Minimum length of 1. Maximum length of 32.  
Key Pattern: `^[A-Za-z][A-Za-z0-9_]*$`   
Required: No

## See Also
<a name="API_PolicyVariables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/PolicyVariables) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/PolicyVariables) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/PolicyVariables) 