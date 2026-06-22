---
id: "@specs/aws/batch/docs/API_QueueSnapshotCapacityUsage"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS QueueSnapshotCapacityUsage"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# QueueSnapshotCapacityUsage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_QueueSnapshotCapacityUsage
> **target_lang:** meta — documentation tier. ALL sections preserved.



# QueueSnapshotCapacityUsage
<a name="API_QueueSnapshotCapacityUsage"></a>

The configured capacity usage for a job queue snapshot, including the unit of measure and quantity of resources being used.

## Contents
<a name="API_QueueSnapshotCapacityUsage_Contents"></a>

 ** capacityUnit **   <a name="Batch-Type-QueueSnapshotCapacityUsage-capacityUnit"></a>
The unit of measure for the capacity usage. For compute jobs, this is `VCPU` for Amazon EC2 and `cpu` for Amazon EKS. For service jobs, this is the instance type.  
Type: String  
Required: No

 ** quantity **   <a name="Batch-Type-QueueSnapshotCapacityUsage-quantity"></a>
The quantity of capacity being used in the queue snapshot, measured in the units specified by `capacityUnit`.  
Type: Double  
Required: No

## See Also
<a name="API_QueueSnapshotCapacityUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/QueueSnapshotCapacityUsage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/QueueSnapshotCapacityUsage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/QueueSnapshotCapacityUsage) 