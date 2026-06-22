---
id: "@specs/aws/batch/docs/API_SchedulingPolicyDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SchedulingPolicyDetail"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# SchedulingPolicyDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_SchedulingPolicyDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SchedulingPolicyDetail
<a name="API_SchedulingPolicyDetail"></a>

An object that represents a scheduling policy.

## Contents
<a name="API_SchedulingPolicyDetail_Contents"></a>

 ** arn **   <a name="Batch-Type-SchedulingPolicyDetail-arn"></a>
The Amazon Resource Name (ARN) of the scheduling policy. An example is `arn:aws:batch:us-east-1:123456789012:scheduling-policy/HighPriority `.  
Type: String  
Required: Yes

 ** name **   <a name="Batch-Type-SchedulingPolicyDetail-name"></a>
The name of the fair-share scheduling policy.  
Type: String  
Required: Yes

 ** fairsharePolicy **   <a name="Batch-Type-SchedulingPolicyDetail-fairsharePolicy"></a>
The fair-share scheduling policy details.  
Type: [FairsharePolicy](API_FairsharePolicy.md) object  
Required: No

 ** quotaSharePolicy **   <a name="Batch-Type-SchedulingPolicyDetail-quotaSharePolicy"></a>
The quota share scheduling policy details.  
Type: [QuotaSharePolicy](API_QuotaSharePolicy.md) object  
Required: No

 ** tags **   <a name="Batch-Type-SchedulingPolicyDetail-tags"></a>
The tags that you apply to the fair-share scheduling policy to categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in * AWS General Reference*.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

## See Also
<a name="API_SchedulingPolicyDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/SchedulingPolicyDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/SchedulingPolicyDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/SchedulingPolicyDetail) 