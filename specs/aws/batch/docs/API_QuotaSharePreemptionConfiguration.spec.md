---
id: "@specs/aws/batch/docs/API_QuotaSharePreemptionConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS QuotaSharePreemptionConfiguration"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# QuotaSharePreemptionConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_QuotaSharePreemptionConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# QuotaSharePreemptionConfiguration
<a name="API_QuotaSharePreemptionConfiguration"></a>

Specifies the preemption behavior for jobs in a quota share.

## Contents
<a name="API_QuotaSharePreemptionConfiguration_Contents"></a>

 ** inSharePreemption **   <a name="Batch-Type-QuotaSharePreemptionConfiguration-inSharePreemption"></a>
Specifies whether jobs within a quota share can be preempted by another, higher priority job in the same quota share.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: Yes

## See Also
<a name="API_QuotaSharePreemptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/QuotaSharePreemptionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/QuotaSharePreemptionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/QuotaSharePreemptionConfiguration) 