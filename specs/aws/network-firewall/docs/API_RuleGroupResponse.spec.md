---
id: "@specs/aws/network-firewall/docs/API_RuleGroupResponse"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleGroupResponse"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# RuleGroupResponse

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_RuleGroupResponse
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleGroupResponse
<a name="API_RuleGroupResponse"></a>

The high-level properties of a rule group. This, along with the [RuleGroup](API_RuleGroup.md), define the rule group. You can retrieve all objects for a rule group by calling [DescribeRuleGroup](API_DescribeRuleGroup.md). 

## Contents
<a name="API_RuleGroupResponse_Contents"></a>

 ** RuleGroupArn **   <a name="networkfirewall-Type-RuleGroupResponse-RuleGroupArn"></a>
The Amazon Resource Name (ARN) of the rule group.  
If this response is for a create request that had `DryRun` set to `TRUE`, then this ARN is a placeholder that isn't attached to a valid resource.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** RuleGroupId **   <a name="networkfirewall-Type-RuleGroupResponse-RuleGroupId"></a>
The unique identifier for the rule group.   
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: Yes

 ** RuleGroupName **   <a name="networkfirewall-Type-RuleGroupResponse-RuleGroupName"></a>
The descriptive name of the rule group. You can't change the name of a rule group after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: Yes

 ** AnalysisResults **   <a name="networkfirewall-Type-RuleGroupResponse-AnalysisResults"></a>
The list of analysis results for `AnalyzeRuleGroup`. If you set `AnalyzeRuleGroup` to `TRUE` in [CreateRuleGroup](API_CreateRuleGroup.md), [UpdateRuleGroup](API_UpdateRuleGroup.md), or [DescribeRuleGroup](API_DescribeRuleGroup.md), Network Firewall analyzes the rule group and identifies the rules that might adversely effect your firewall's functionality. For example, if Network Firewall detects a rule that's routing traffic asymmetrically, which impacts the service's ability to properly process traffic, the service includes the rule in the list of analysis results.  
Type: Array of [AnalysisResult](API_AnalysisResult.md) objects  
Required: No

 ** Capacity **   <a name="networkfirewall-Type-RuleGroupResponse-Capacity"></a>
The maximum operating resources that this rule group can use. Rule group capacity is fixed at creation. When you update a rule group, you are limited to this capacity. When you reference a rule group from a firewall policy, Network Firewall reserves this capacity for the rule group.   
You can retrieve the capacity that would be required for a rule group before you create the rule group by calling [CreateRuleGroup](API_CreateRuleGroup.md) with `DryRun` set to `TRUE`.   
Type: Integer  
Required: No

 ** ConsumedCapacity **   <a name="networkfirewall-Type-RuleGroupResponse-ConsumedCapacity"></a>
The number of capacity units currently consumed by the rule group rules.   
Type: Integer  
Required: No

 ** Description **   <a name="networkfirewall-Type-RuleGroupResponse-Description"></a>
A description of the rule group.   
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$`   
Required: No

 ** EncryptionConfiguration **   <a name="networkfirewall-Type-RuleGroupResponse-EncryptionConfiguration"></a>
A complex type that contains the AWS KMS encryption configuration settings for your rule group.  
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object  
Required: No

 ** LastModifiedTime **   <a name="networkfirewall-Type-RuleGroupResponse-LastModifiedTime"></a>
The last time that the rule group was changed.  
Type: Timestamp  
Required: No

 ** NumberOfAssociations **   <a name="networkfirewall-Type-RuleGroupResponse-NumberOfAssociations"></a>
The number of firewall policies that use this rule group.  
Type: Integer  
Required: No

 ** RuleGroupStatus **   <a name="networkfirewall-Type-RuleGroupResponse-RuleGroupStatus"></a>
Detailed information about the current status of a rule group.   
Type: String  
Valid Values: `ACTIVE | DELETING | ERROR`   
Required: No

 ** SnsTopic **   <a name="networkfirewall-Type-RuleGroupResponse-SnsTopic"></a>
The Amazon Resource Name (ARN) of the Amazon Simple Notification Service SNS topic that's used to record changes to the managed rule group. You can subscribe to the SNS topic to receive notifications when the managed rule group is modified, such as for new versions and for version expiration. For more information, see the [Amazon Simple Notification Service Developer Guide.](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** SourceMetadata **   <a name="networkfirewall-Type-RuleGroupResponse-SourceMetadata"></a>
A complex type that contains metadata about the rule group that your own rule group is copied from. You can use the metadata to track the version updates made to the originating rule group.  
Type: [SourceMetadata](API_SourceMetadata.md) object  
Required: No

 ** SummaryConfiguration **   <a name="networkfirewall-Type-RuleGroupResponse-SummaryConfiguration"></a>
A complex type containing the currently selected rule option fields that will be displayed for rule summarization returned by [DescribeRuleGroupSummary](API_DescribeRuleGroupSummary.md).  
+ The `RuleOptions` specified in [SummaryConfiguration](API_SummaryConfiguration.md) 
+ Rule metadata organization preferences
Type: [SummaryConfiguration](API_SummaryConfiguration.md) object  
Required: No

 ** Tags **   <a name="networkfirewall-Type-RuleGroupResponse-Tags"></a>
The key:value pairs to associate with the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** Type **   <a name="networkfirewall-Type-RuleGroupResponse-Type"></a>
Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.   
Type: String  
Valid Values: `STATELESS | STATEFUL | STATEFUL_DOMAIN`   
Required: No

## See Also
<a name="API_RuleGroupResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/RuleGroupResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/RuleGroupResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/RuleGroupResponse) 