---
id: "@specs/aws/batch/docs/API_NodeRangeProperty"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NodeRangeProperty"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# NodeRangeProperty

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_NodeRangeProperty
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NodeRangeProperty
<a name="API_NodeRangeProperty"></a>

This is an object that represents the properties of the node range for a multi-node parallel job.

## Contents
<a name="API_NodeRangeProperty_Contents"></a>

 ** targetNodes **   <a name="Batch-Type-NodeRangeProperty-targetNodes"></a>
The range of nodes, using node index values. A range of `0:3` indicates nodes with index values of `0` through `3`. If the starting range value is omitted (`:n`), then `0` is used to start the range. If the ending range value is omitted (`n:`), then the highest possible node index is used to end the range. Your accumulative node ranges must account for all nodes (`0:n`). You can nest node ranges (for example, `0:10` and `4:5`). In this case, the `4:5` range properties override the `0:10` properties.  
Type: String  
Required: Yes

 ** consumableResourceProperties **   <a name="Batch-Type-NodeRangeProperty-consumableResourceProperties"></a>
Contains a list of consumable resources required by a job.  
Type: [ConsumableResourceProperties](API_ConsumableResourceProperties.md) object  
Required: No

 ** container **   <a name="Batch-Type-NodeRangeProperty-container"></a>
The container details for the node range.  
Type: [ContainerProperties](API_ContainerProperties.md) object  
Required: No

 ** ecsProperties **   <a name="Batch-Type-NodeRangeProperty-ecsProperties"></a>
This is an object that represents the properties of the node range for a multi-node parallel job.  
Type: [EcsProperties](API_EcsProperties.md) object  
Required: No

 ** eksProperties **   <a name="Batch-Type-NodeRangeProperty-eksProperties"></a>
This is an object that represents the properties of the node range for a multi-node parallel job.  
Type: [EksProperties](API_EksProperties.md) object  
Required: No

 ** instanceTypes **   <a name="Batch-Type-NodeRangeProperty-instanceTypes"></a>
The instance types of the underlying host infrastructure of a multi-node parallel job.  
This parameter isn't applicable to jobs that are running on Fargate resources.  
In addition, this list object is currently limited to one element.
Type: Array of strings  
Required: No

## See Also
<a name="API_NodeRangeProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/NodeRangeProperty) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/NodeRangeProperty) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/NodeRangeProperty) 