---
id: "@specs/aws/shield/docs/API_SubResourceSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SubResourceSummary"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# SubResourceSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_SubResourceSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SubResourceSummary
<a name="API_SubResourceSummary"></a>

The attack information for the specified SubResource.

## Contents
<a name="API_SubResourceSummary_Contents"></a>

 ** AttackVectors **   <a name="AWSShield-Type-SubResourceSummary-AttackVectors"></a>
The list of attack types and associated counters.  
Type: Array of [SummarizedAttackVector](API_SummarizedAttackVector.md) objects  
Required: No

 ** Counters **   <a name="AWSShield-Type-SubResourceSummary-Counters"></a>
The counters that describe the details of the attack.  
Type: Array of [SummarizedCounter](API_SummarizedCounter.md) objects  
Required: No

 ** Id **   <a name="AWSShield-Type-SubResourceSummary-Id"></a>
The unique identifier (ID) of the `SubResource`.  
Type: String  
Required: No

 ** Type **   <a name="AWSShield-Type-SubResourceSummary-Type"></a>
The `SubResource` type.  
Type: String  
Valid Values: `IP | URL`   
Required: No

## See Also
<a name="API_SubResourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/SubResourceSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/SubResourceSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/SubResourceSummary) 