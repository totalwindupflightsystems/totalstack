---
id: "@specs/aws/emr/docs/API_InstanceFleetResizingSpecifications"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceFleetResizingSpecifications"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceFleetResizingSpecifications

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceFleetResizingSpecifications
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceFleetResizingSpecifications
<a name="API_InstanceFleetResizingSpecifications"></a>

The resize specification for On-Demand and Spot Instances in the fleet.

## Contents
<a name="API_InstanceFleetResizingSpecifications_Contents"></a>

 ** OnDemandResizeSpecification **   <a name="EMR-Type-InstanceFleetResizingSpecifications-OnDemandResizeSpecification"></a>
The resize specification for On-Demand Instances in the instance fleet, which contains the allocation strategy, capacity reservation options, and the resize timeout period.   
Type: [OnDemandResizingSpecification](API_OnDemandResizingSpecification.md) object  
Required: No

 ** SpotResizeSpecification **   <a name="EMR-Type-InstanceFleetResizingSpecifications-SpotResizeSpecification"></a>
The resize specification for Spot Instances in the instance fleet, which contains the allocation strategy and the resize timeout period.   
Type: [SpotResizingSpecification](API_SpotResizingSpecification.md) object  
Required: No

## See Also
<a name="API_InstanceFleetResizingSpecifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceFleetResizingSpecifications) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceFleetResizingSpecifications) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceFleetResizingSpecifications) 