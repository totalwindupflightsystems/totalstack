---
id: "@specs/aws/shield/docs/API_AttackDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttackDetail"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# AttackDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_AttackDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttackDetail
<a name="API_AttackDetail"></a>

The details of a DDoS attack.

## Contents
<a name="API_AttackDetail_Contents"></a>

 ** AttackCounters **   <a name="AWSShield-Type-AttackDetail-AttackCounters"></a>
List of counters that describe the attack for the specified time period.  
Type: Array of [SummarizedCounter](API_SummarizedCounter.md) objects  
Required: No

 ** AttackId **   <a name="AWSShield-Type-AttackDetail-AttackId"></a>
The unique identifier (ID) of the attack.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\\-]*`   
Required: No

 ** AttackProperties **   <a name="AWSShield-Type-AttackDetail-AttackProperties"></a>
The array of objects that provide details of the AWS Shield event.   
For infrastructure layer events (L3 and L4 events), you can view metrics for top contributors in Amazon CloudWatch metrics. For more information, see [AWS Shield metrics and alarms](https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html#set-ddos-alarms) in the * AWS WAF Developer Guide*.   
Type: Array of [AttackProperty](API_AttackProperty.md) objects  
Required: No

 ** EndTime **   <a name="AWSShield-Type-AttackDetail-EndTime"></a>
The time the attack ended, in Unix time in seconds.   
Type: Timestamp  
Required: No

 ** Mitigations **   <a name="AWSShield-Type-AttackDetail-Mitigations"></a>
List of mitigation actions taken for the attack.  
Type: Array of [Mitigation](API_Mitigation.md) objects  
Required: No

 ** ResourceArn **   <a name="AWSShield-Type-AttackDetail-ResourceArn"></a>
The ARN (Amazon Resource Name) of the resource that was attacked.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*`   
Required: No

 ** StartTime **   <a name="AWSShield-Type-AttackDetail-StartTime"></a>
The time the attack started, in Unix time in seconds.   
Type: Timestamp  
Required: No

 ** SubResources **   <a name="AWSShield-Type-AttackDetail-SubResources"></a>
If applicable, additional detail about the resource being attacked, for example, IP address or URL.  
Type: Array of [SubResourceSummary](API_SubResourceSummary.md) objects  
Required: No

## See Also
<a name="API_AttackDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/AttackDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/AttackDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/AttackDetail) 