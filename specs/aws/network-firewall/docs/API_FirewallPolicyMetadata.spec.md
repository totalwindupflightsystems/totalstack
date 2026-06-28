---
id: "@specs/aws/network-firewall/docs/API_FirewallPolicyMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FirewallPolicyMetadata"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# FirewallPolicyMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_FirewallPolicyMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FirewallPolicyMetadata
<a name="API_FirewallPolicyMetadata"></a>

High-level information about a firewall policy, returned by operations like create and describe. You can use the information provided in the metadata to retrieve and manage a firewall policy. You can retrieve all objects for a firewall policy by calling [DescribeFirewallPolicy](API_DescribeFirewallPolicy.md). 

## Contents
<a name="API_FirewallPolicyMetadata_Contents"></a>

 ** Arn **   <a name="networkfirewall-Type-FirewallPolicyMetadata-Arn"></a>
The Amazon Resource Name (ARN) of the firewall policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** Name **   <a name="networkfirewall-Type-FirewallPolicyMetadata-Name"></a>
The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## See Also
<a name="API_FirewallPolicyMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FirewallPolicyMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FirewallPolicyMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FirewallPolicyMetadata) 