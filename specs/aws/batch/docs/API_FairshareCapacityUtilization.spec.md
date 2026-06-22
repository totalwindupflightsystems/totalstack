---
id: "@specs/aws/batch/docs/API_FairshareCapacityUtilization"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FairshareCapacityUtilization"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# FairshareCapacityUtilization

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_FairshareCapacityUtilization
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FairshareCapacityUtilization
<a name="API_FairshareCapacityUtilization"></a>

The capacity utilization for a specific share in a fairshare scheduling job queue, including the share identifier and its current usage.

## Contents
<a name="API_FairshareCapacityUtilization_Contents"></a>

 ** capacityUsage **   <a name="Batch-Type-FairshareCapacityUtilization-capacityUsage"></a>
The capacity usage information for this share, including the unit of measure and quantity being used. This is `VCPU` for Amazon EC2 and `cpu` for Amazon EKS.  
Type: Array of [FairshareCapacityUsage](API_FairshareCapacityUsage.md) objects  
Required: No

 ** shareIdentifier **   <a name="Batch-Type-FairshareCapacityUtilization-shareIdentifier"></a>
The share identifier for the fairshare scheduling job queue.  
Type: String  
Required: No

## See Also
<a name="API_FairshareCapacityUtilization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/FairshareCapacityUtilization) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/FairshareCapacityUtilization) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/FairshareCapacityUtilization) 