---
id: "@specs/aws/network-firewall/docs/API_AnalysisResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AnalysisResult"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# AnalysisResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_AnalysisResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AnalysisResult
<a name="API_AnalysisResult"></a>

The analysis result for Network Firewall's stateless rule group analyzer. Every time you call [CreateRuleGroup](API_CreateRuleGroup.md), [UpdateRuleGroup](API_UpdateRuleGroup.md), or [DescribeRuleGroup](API_DescribeRuleGroup.md) on a stateless rule group, Network Firewall analyzes the stateless rule groups in your account and identifies the rules that might adversely effect your firewall's functionality. For example, if Network Firewall detects a rule that's routing traffic asymmetrically, which impacts the service's ability to properly process traffic, the service includes the rule in a list of analysis results.

The `AnalysisResult` data type is not related to traffic analysis reports you generate using [StartAnalysisReport](API_StartAnalysisReport.md). For information on traffic analysis report results, see [AnalysisTypeReportResult](API_AnalysisTypeReportResult.md).

## Contents
<a name="API_AnalysisResult_Contents"></a>

 ** AnalysisDetail **   <a name="networkfirewall-Type-AnalysisResult-AnalysisDetail"></a>
Provides analysis details for the identified rule.  
Type: String  
Required: No

 ** IdentifiedRuleIds **   <a name="networkfirewall-Type-AnalysisResult-IdentifiedRuleIds"></a>
The priority number of the stateless rules identified in the analysis.  
Type: Array of strings  
Required: No

 ** IdentifiedType **   <a name="networkfirewall-Type-AnalysisResult-IdentifiedType"></a>
The types of rule configurations that Network Firewall analyzes your rule groups for. Network Firewall analyzes stateless rule groups for the following types of rule configurations:  
+  `STATELESS_RULE_FORWARDING_ASYMMETRICALLY` 

  Cause: One or more stateless rules with the action `pass` or `forward` are forwarding traffic asymmetrically. Specifically, the rule's set of source IP addresses or their associated port numbers, don't match the set of destination IP addresses or their associated port numbers.

  To mitigate: Make sure that there's an existing return path. For example, if the rule allows traffic from source 10.1.0.0/24 to destination 20.1.0.0/24, you should allow return traffic from source 20.1.0.0/24 to destination 10.1.0.0/24.
+  `STATELESS_RULE_CONTAINS_TCP_FLAGS` 

  Cause: At least one stateless rule with the action `pass` or`forward` contains TCP flags that are inconsistent in the forward and return directions.

  To mitigate: Prevent asymmetric routing issues caused by TCP flags by following these actions:
  + Remove unnecessary TCP flag inspections from the rules.
  + If you need to inspect TCP flags, check that the rules correctly account for changes in TCP flags throughout the TCP connection cycle, for example `SYN` and `ACK` flags used in a 3-way TCP handshake.
Type: String  
Valid Values: `STATELESS_RULE_FORWARDING_ASYMMETRICALLY | STATELESS_RULE_CONTAINS_TCP_FLAGS`   
Required: No

## See Also
<a name="API_AnalysisResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/AnalysisResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/AnalysisResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/AnalysisResult) 