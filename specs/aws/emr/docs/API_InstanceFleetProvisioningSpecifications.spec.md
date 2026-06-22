---
id: "@specs/aws/emr/docs/API_InstanceFleetProvisioningSpecifications"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceFleetProvisioningSpecifications"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceFleetProvisioningSpecifications

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceFleetProvisioningSpecifications
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceFleetProvisioningSpecifications
<a name="API_InstanceFleetProvisioningSpecifications"></a>

The launch specification for On-Demand and Spot Instances in the fleet.

**Note**  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand and Spot instance allocation strategies are available in Amazon EMR releases 5.12.1 and later.

## Contents
<a name="API_InstanceFleetProvisioningSpecifications_Contents"></a>

 ** OnDemandSpecification **   <a name="EMR-Type-InstanceFleetProvisioningSpecifications-OnDemandSpecification"></a>
 The launch specification for On-Demand Instances in the instance fleet, which determines the allocation strategy and capacity reservation options.  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand Instances allocation strategy is available in Amazon EMR releases 5.12.1 and later.
Type: [OnDemandProvisioningSpecification](API_OnDemandProvisioningSpecification.md) object  
Required: No

 ** SpotSpecification **   <a name="EMR-Type-InstanceFleetProvisioningSpecifications-SpotSpecification"></a>
The launch specification for Spot instances in the fleet, which determines the allocation strategy, defined duration, and provisioning timeout behavior.  
Type: [SpotProvisioningSpecification](API_SpotProvisioningSpecification.md) object  
Required: No

## See Also
<a name="API_InstanceFleetProvisioningSpecifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceFleetProvisioningSpecifications) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceFleetProvisioningSpecifications) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceFleetProvisioningSpecifications) 