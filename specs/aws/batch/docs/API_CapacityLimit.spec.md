---
id: "@specs/aws/batch/docs/API_CapacityLimit"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CapacityLimit"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# CapacityLimit

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_CapacityLimit
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CapacityLimit
<a name="API_CapacityLimit"></a>

Defines the type and maximum quantity of resources that can be allocated to service jobs in a service environment.

## Contents
<a name="API_CapacityLimit_Contents"></a>

 ** capacityUnit **   <a name="Batch-Type-CapacityLimit-capacityUnit"></a>
The unit of measure for the capacity limit, which defines how `maxCapacity` is interpreted. For `SAGEMAKER_TRAINING` jobs in a quota management enabled service environment, specify the [instance type](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceConfig.html#sagemaker-Type-ResourceConfig-InstanceType) (for example, `ml.m5.large`). Otherwise, use `NUM_INSTANCES`.  
Type: String  
Required: No

 ** maxCapacity **   <a name="Batch-Type-CapacityLimit-maxCapacity"></a>
The maximum capacity available for the service environment. For a quota management enabled service environment, this value represents the maximum quantity of a particular resource type (specified by `capacityUnit`) that can be allocated to service jobs. For other service environments, this value represents the maximum quantity of all resources that can be allocated to service jobs.  
For example, if `maxCapacity=50` and `capacityUnit=NUM_INSTANCES`, you can run up to 50 instances concurrently. If you run 5 SageMaker Training jobs that each use 10 instances, a subsequent job requiring 10 instances waits in the queue until capacity is available. In a quota management enabled service environment with `capacityUnit=ml.m5.large`, only `ml.m5.large` instances count against this limit, and jobs requiring other instance types wait until a matching capacity limit is configured.  
Type: Integer  
Required: No

## See Also
<a name="API_CapacityLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/CapacityLimit) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/CapacityLimit) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/CapacityLimit) 