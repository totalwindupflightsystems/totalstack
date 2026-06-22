---
id: "@specs/aws/batch/docs/API_FairshareCapacityUsage"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FairshareCapacityUsage"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# FairshareCapacityUsage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_FairshareCapacityUsage
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FairshareCapacityUsage
<a name="API_FairshareCapacityUsage"></a>

The capacity usage for a fairshare scheduling job queue.

## Contents
<a name="API_FairshareCapacityUsage_Contents"></a>

 ** capacityUnit **   <a name="Batch-Type-FairshareCapacityUsage-capacityUnit"></a>
The unit of measure for the capacity usage. For compute jobs, this is `VCPU` for Amazon EC2 and `cpu` for Amazon EKS. For service jobs, this is the instance type.  
Type: String  
Required: No

 ** quantity **   <a name="Batch-Type-FairshareCapacityUsage-quantity"></a>
The quantity of capacity being used, measured in the units specified by `capacityUnit`.  
Type: Double  
Required: No

## See Also
<a name="API_FairshareCapacityUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/FairshareCapacityUsage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/FairshareCapacityUsage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/FairshareCapacityUsage) 