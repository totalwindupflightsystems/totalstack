---
id: "@specs/aws/network-firewall/docs/API_Summary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Summary"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# Summary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_Summary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Summary
<a name="API_Summary"></a>

A complex type containing summaries of security protections provided by a rule group.

Network Firewall extracts this information from selected fields in the rule group's Suricata rules, based on your [SummaryConfiguration](API_SummaryConfiguration.md) settings.

## Contents
<a name="API_Summary_Contents"></a>

 ** RuleSummaries **   <a name="networkfirewall-Type-Summary-RuleSummaries"></a>
An array of [RuleSummary](API_RuleSummary.md) objects containing individual rule details that had been configured by the rulegroup's SummaryConfiguration.  
Type: Array of [RuleSummary](API_RuleSummary.md) objects  
Required: No

## See Also
<a name="API_Summary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/Summary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/Summary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/Summary) 