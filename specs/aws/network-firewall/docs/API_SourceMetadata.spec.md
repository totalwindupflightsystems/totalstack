---
id: "@specs/aws/network-firewall/docs/API_SourceMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SourceMetadata"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# SourceMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_SourceMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SourceMetadata
<a name="API_SourceMetadata"></a>

High-level information about the managed rule group that your own rule group is copied from. You can use the the metadata to track version updates made to the originating rule group. You can retrieve all objects for a rule group by calling [DescribeRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeRuleGroup.html).

## Contents
<a name="API_SourceMetadata_Contents"></a>

 ** SourceArn **   <a name="networkfirewall-Type-SourceMetadata-SourceArn"></a>
The Amazon Resource Name (ARN) of the rule group that your own rule group is copied from.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** SourceUpdateToken **   <a name="networkfirewall-Type-SourceMetadata-SourceUpdateToken"></a>
The update token of the AWS managed rule group that your own rule group is copied from. To determine the update token for the managed rule group, call [DescribeRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeRuleGroup.html#networkfirewall-DescribeRuleGroup-response-UpdateToken).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: No

## See Also
<a name="API_SourceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/SourceMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/SourceMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/SourceMetadata) 