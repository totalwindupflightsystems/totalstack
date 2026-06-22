---
id: "@specs/aws/emr/docs/API_BlockPublicAccessConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BlockPublicAccessConfiguration"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# BlockPublicAccessConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_BlockPublicAccessConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BlockPublicAccessConfiguration
<a name="API_BlockPublicAccessConfiguration"></a>

A configuration for Amazon EMR block public access. When `BlockPublicSecurityGroupRules` is set to `true`, Amazon EMR prevents cluster creation if one of the cluster's security groups has a rule that allows inbound traffic from 0.0.0.0/0 or ::/0 on a port, unless the port is specified as an exception using `PermittedPublicSecurityGroupRuleRanges`.

## Contents
<a name="API_BlockPublicAccessConfiguration_Contents"></a>

 ** BlockPublicSecurityGroupRules **   <a name="EMR-Type-BlockPublicAccessConfiguration-BlockPublicSecurityGroupRules"></a>
Indicates whether Amazon EMR block public access is enabled (`true`) or disabled (`false`). By default, the value is `false` for accounts that have created Amazon EMR clusters before July 2019. For accounts created after this, the default is `true`.  
Type: Boolean  
Required: Yes

 ** PermittedPublicSecurityGroupRuleRanges **   <a name="EMR-Type-BlockPublicAccessConfiguration-PermittedPublicSecurityGroupRuleRanges"></a>
Specifies ports and port ranges that are permitted to have security group rules that allow inbound traffic from all public sources. For example, if Port 23 (Telnet) is specified for `PermittedPublicSecurityGroupRuleRanges`, Amazon EMR allows cluster creation if a security group associated with the cluster has a rule that allows inbound traffic on Port 23 from IPv4 0.0.0.0/0 or IPv6 port ::/0 as the source.  
By default, Port 22, which is used for SSH access to the cluster Amazon EC2 instances, is in the list of `PermittedPublicSecurityGroupRuleRanges`.  
Type: Array of [PortRange](API_PortRange.md) objects  
Required: No

## See Also
<a name="API_BlockPublicAccessConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/BlockPublicAccessConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/BlockPublicAccessConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/BlockPublicAccessConfiguration) 