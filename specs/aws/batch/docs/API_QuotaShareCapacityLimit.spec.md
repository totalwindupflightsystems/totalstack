---
id: "@specs/aws/batch/docs/API_QuotaShareCapacityLimit"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS QuotaShareCapacityLimit"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# QuotaShareCapacityLimit

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_QuotaShareCapacityLimit
> **target_lang:** meta — documentation tier. ALL sections preserved.



# QuotaShareCapacityLimit
<a name="API_QuotaShareCapacityLimit"></a>

Defines the capacity limit for a quota share, or the type and maximum quantity of a particular resource that can be allocated to jobs in the quota share without borrowing. 

## Contents
<a name="API_QuotaShareCapacityLimit_Contents"></a>

 ** capacityUnit **   <a name="Batch-Type-QuotaShareCapacityLimit-capacityUnit"></a>
The unit of compute capacity for the capacityLimit. For example, `ml.m5.large`.  
Type: String  
Required: Yes

 ** maxCapacity **   <a name="Batch-Type-QuotaShareCapacityLimit-maxCapacity"></a>
The maximum capacity available for the quota share. This value represents the maximum quantity of a resource that can be allocated to jobs in the quota share without borrowing.  
Type: Integer  
Required: Yes

## See Also
<a name="API_QuotaShareCapacityLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/QuotaShareCapacityLimit) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/QuotaShareCapacityLimit) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/QuotaShareCapacityLimit) 