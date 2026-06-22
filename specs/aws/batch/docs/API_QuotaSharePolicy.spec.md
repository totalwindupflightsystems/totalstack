---
id: "@specs/aws/batch/docs/API_QuotaSharePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS QuotaSharePolicy"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# QuotaSharePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_QuotaSharePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# QuotaSharePolicy
<a name="API_QuotaSharePolicy"></a>

The quota share scheduling policy details for a job queue.

## Contents
<a name="API_QuotaSharePolicy_Contents"></a>

 ** idleResourceAssignmentStrategy **   <a name="Batch-Type-QuotaSharePolicy-idleResourceAssignmentStrategy"></a>
The strategy that determines how idle resources are assigned to quota shares that are borrowing capacity. Currently, only `FIFO` is supported.  
Type: String  
Valid Values: `FIFO`   
Required: Yes

## See Also
<a name="API_QuotaSharePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/QuotaSharePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/QuotaSharePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/QuotaSharePolicy) 