---
id: "@specs/aws/batch/docs/API_NodePropertyOverride"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NodePropertyOverride"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# NodePropertyOverride

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_NodePropertyOverride
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NodePropertyOverride
<a name="API_NodePropertyOverride"></a>

The object that represents any node overrides to a job definition that's used in a [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) API operation.

## Contents
<a name="API_NodePropertyOverride_Contents"></a>

 ** targetNodes **   <a name="Batch-Type-NodePropertyOverride-targetNodes"></a>
The range of nodes, using node index values, that's used to override. A range of `0:3` indicates nodes with index values of `0` through `3`. If the starting range value is omitted (`:n`), then `0` is used to start the range. If the ending range value is omitted (`n:`), then the highest possible node index is used to end the range.  
Type: String  
Required: Yes

 ** consumableResourcePropertiesOverride **   <a name="Batch-Type-NodePropertyOverride-consumableResourcePropertiesOverride"></a>
An object that contains overrides for the consumable resources of a job.  
Type: [ConsumableResourceProperties](API_ConsumableResourceProperties.md) object  
Required: No

 ** containerOverrides **   <a name="Batch-Type-NodePropertyOverride-containerOverrides"></a>
The overrides that are sent to a node range.  
Type: [ContainerOverrides](API_ContainerOverrides.md) object  
Required: No

 ** ecsPropertiesOverride **   <a name="Batch-Type-NodePropertyOverride-ecsPropertiesOverride"></a>
An object that contains the properties that you want to replace for the existing Amazon ECS resources of a job.  
Type: [EcsPropertiesOverride](API_EcsPropertiesOverride.md) object  
Required: No

 ** eksPropertiesOverride **   <a name="Batch-Type-NodePropertyOverride-eksPropertiesOverride"></a>
An object that contains the properties that you want to replace for the existing Amazon EKS resources of a job.  
Type: [EksPropertiesOverride](API_EksPropertiesOverride.md) object  
Required: No

 ** instanceTypes **   <a name="Batch-Type-NodePropertyOverride-instanceTypes"></a>
An object that contains the instance types that you want to replace for the existing resources of a job.  
Type: Array of strings  
Required: No

## See Also
<a name="API_NodePropertyOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/NodePropertyOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/NodePropertyOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/NodePropertyOverride) 