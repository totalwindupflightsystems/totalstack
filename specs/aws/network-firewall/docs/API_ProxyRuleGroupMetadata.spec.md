---
id: "@specs/aws/network-firewall/docs/API_ProxyRuleGroupMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProxyRuleGroupMetadata"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ProxyRuleGroupMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ProxyRuleGroupMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProxyRuleGroupMetadata
<a name="API_ProxyRuleGroupMetadata"></a>

High-level information about a proxy rule group, returned by operations like create and describe. You can use the information provided in the metadata to retrieve and manage a proxy rule group. You can retrieve all objects for a proxy rule group by calling [DescribeProxyRuleGroup](API_DescribeProxyRuleGroup.md). 

## Contents
<a name="API_ProxyRuleGroupMetadata_Contents"></a>

 ** Arn **   <a name="networkfirewall-Type-ProxyRuleGroupMetadata-Arn"></a>
The Amazon Resource Name (ARN) of a proxy rule group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** Name **   <a name="networkfirewall-Type-ProxyRuleGroupMetadata-Name"></a>
The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## See Also
<a name="API_ProxyRuleGroupMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyRuleGroupMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyRuleGroupMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyRuleGroupMetadata) 