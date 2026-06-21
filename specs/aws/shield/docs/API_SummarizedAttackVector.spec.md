---
id: "@specs/aws/shield/docs/API_SummarizedAttackVector"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SummarizedAttackVector"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# SummarizedAttackVector

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_SummarizedAttackVector
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SummarizedAttackVector
<a name="API_SummarizedAttackVector"></a>

A summary of information about the attack.

## Contents
<a name="API_SummarizedAttackVector_Contents"></a>

 ** VectorType **   <a name="AWSShield-Type-SummarizedAttackVector-VectorType"></a>
The attack type, for example, SNMP reflection or SYN flood.  
Type: String  
Required: Yes

 ** VectorCounters **   <a name="AWSShield-Type-SummarizedAttackVector-VectorCounters"></a>
The list of counters that describe the details of the attack.  
Type: Array of [SummarizedCounter](API_SummarizedCounter.md) objects  
Required: No

## See Also
<a name="API_SummarizedAttackVector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/SummarizedAttackVector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/SummarizedAttackVector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/SummarizedAttackVector) 