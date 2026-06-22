---
id: "@specs/aws/batch/docs/API_JobCapacityUsageSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobCapacityUsageSummary"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# JobCapacityUsageSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_JobCapacityUsageSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobCapacityUsageSummary
<a name="API_JobCapacityUsageSummary"></a>

The capacity usage for a job, including the unit of measure and quantity of resources being used.

## Contents
<a name="API_JobCapacityUsageSummary_Contents"></a>

 ** capacityUnit **   <a name="Batch-Type-JobCapacityUsageSummary-capacityUnit"></a>
The unit of measure for the capacity usage. This is `VCPU` for Amazon EC2 and `cpu` for Amazon EKS.  
Type: String  
Required: No

 ** quantity **   <a name="Batch-Type-JobCapacityUsageSummary-quantity"></a>
The quantity of capacity being used by the job, measured in the units specified by `capacityUnit`.  
Type: Double  
Required: No

## See Also
<a name="API_JobCapacityUsageSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/JobCapacityUsageSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/JobCapacityUsageSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/JobCapacityUsageSummary) 