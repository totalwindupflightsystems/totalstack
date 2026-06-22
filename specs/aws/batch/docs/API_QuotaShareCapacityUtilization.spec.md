---
id: "@specs/aws/batch/docs/API_QuotaShareCapacityUtilization"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS QuotaShareCapacityUtilization"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# QuotaShareCapacityUtilization

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_QuotaShareCapacityUtilization
> **target_lang:** meta — documentation tier. ALL sections preserved.



# QuotaShareCapacityUtilization
<a name="API_QuotaShareCapacityUtilization"></a>

The capacity utilization for a specific quota share, including the quota share name and its current usage.

## Contents
<a name="API_QuotaShareCapacityUtilization_Contents"></a>

 ** capacityUsage **   <a name="Batch-Type-QuotaShareCapacityUtilization-capacityUsage"></a>
The capacity usage information for this quota share, including the units of compute capacity and quantity being used.  
Type: Array of [QuotaShareCapacityUsage](API_QuotaShareCapacityUsage.md) objects  
Required: No

 ** quotaShareName **   <a name="Batch-Type-QuotaShareCapacityUtilization-quotaShareName"></a>
The name of the quota share.  
Type: String  
Required: No

## See Also
<a name="API_QuotaShareCapacityUtilization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/QuotaShareCapacityUtilization) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/QuotaShareCapacityUtilization) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/QuotaShareCapacityUtilization) 