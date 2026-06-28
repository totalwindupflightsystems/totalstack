---
id: "@specs/aws/network-firewall/docs/API_FirewallPolicyResponse"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FirewallPolicyResponse"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# FirewallPolicyResponse

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_FirewallPolicyResponse
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FirewallPolicyResponse
<a name="API_FirewallPolicyResponse"></a>

The high-level properties of a firewall policy. This, along with the [FirewallPolicy](API_FirewallPolicy.md), define the policy. You can retrieve all objects for a firewall policy by calling [DescribeFirewallPolicy](API_DescribeFirewallPolicy.md). 

## Contents
<a name="API_FirewallPolicyResponse_Contents"></a>

 ** FirewallPolicyArn **   <a name="networkfirewall-Type-FirewallPolicyResponse-FirewallPolicyArn"></a>
The Amazon Resource Name (ARN) of the firewall policy.  
If this response is for a create request that had `DryRun` set to `TRUE`, then this ARN is a placeholder that isn't attached to a valid resource.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** FirewallPolicyId **   <a name="networkfirewall-Type-FirewallPolicyResponse-FirewallPolicyId"></a>
The unique identifier for the firewall policy.   
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: Yes

 ** FirewallPolicyName **   <a name="networkfirewall-Type-FirewallPolicyResponse-FirewallPolicyName"></a>
The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: Yes

 ** ConsumedStatefulDomainCapacity **   <a name="networkfirewall-Type-FirewallPolicyResponse-ConsumedStatefulDomainCapacity"></a>
The total number of domain name specifications across all domain list rule groups in the firewall policy that use the `stateful-domain-rulegroup` resource type.  
Type: Integer  
Required: No

 ** ConsumedStatefulRuleCapacity **   <a name="networkfirewall-Type-FirewallPolicyResponse-ConsumedStatefulRuleCapacity"></a>
The number of capacity units currently consumed by the policy's stateful rules.  
Type: Integer  
Required: No

 ** ConsumedStatelessRuleCapacity **   <a name="networkfirewall-Type-FirewallPolicyResponse-ConsumedStatelessRuleCapacity"></a>
The number of capacity units currently consumed by the policy's stateless rules.  
Type: Integer  
Required: No

 ** Description **   <a name="networkfirewall-Type-FirewallPolicyResponse-Description"></a>
A description of the firewall policy.  
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$`   
Required: No

 ** EncryptionConfiguration **   <a name="networkfirewall-Type-FirewallPolicyResponse-EncryptionConfiguration"></a>
A complex type that contains the AWS KMS encryption configuration settings for your firewall policy.  
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object  
Required: No

 ** FirewallPolicyStatus **   <a name="networkfirewall-Type-FirewallPolicyResponse-FirewallPolicyStatus"></a>
The current status of the firewall policy. You can retrieve this for a firewall policy by calling [DescribeFirewallPolicy](API_DescribeFirewallPolicy.md) and providing the firewall policy's name or ARN.  
Type: String  
Valid Values: `ACTIVE | DELETING | ERROR`   
Required: No

 ** LastModifiedTime **   <a name="networkfirewall-Type-FirewallPolicyResponse-LastModifiedTime"></a>
The last time that the firewall policy was changed.  
Type: Timestamp  
Required: No

 ** NumberOfAssociations **   <a name="networkfirewall-Type-FirewallPolicyResponse-NumberOfAssociations"></a>
The number of firewalls that are associated with this firewall policy.  
Type: Integer  
Required: No

 ** Tags **   <a name="networkfirewall-Type-FirewallPolicyResponse-Tags"></a>
The key:value pairs to associate with the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## See Also
<a name="API_FirewallPolicyResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FirewallPolicyResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FirewallPolicyResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FirewallPolicyResponse) 