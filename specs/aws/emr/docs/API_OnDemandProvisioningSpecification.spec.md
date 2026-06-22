---
id: "@specs/aws/emr/docs/API_OnDemandProvisioningSpecification"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OnDemandProvisioningSpecification"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# OnDemandProvisioningSpecification

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_OnDemandProvisioningSpecification
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OnDemandProvisioningSpecification
<a name="API_OnDemandProvisioningSpecification"></a>

 The launch specification for On-Demand Instances in the instance fleet, which determines the allocation strategy. 

**Note**  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand Instances allocation strategy is available in Amazon EMR releases 5.12.1 and later.

## Contents
<a name="API_OnDemandProvisioningSpecification_Contents"></a>

 ** AllocationStrategy **   <a name="EMR-Type-OnDemandProvisioningSpecification-AllocationStrategy"></a>
Specifies the strategy to use in launching On-Demand instance fleets. Available options are `lowest-price` and `prioritized`. `lowest-price` specifies to launch the instances with the lowest price first, and `prioritized` specifies that Amazon EMR should launch the instances with the highest priority first. The default is `lowest-price`.  
Type: String  
Valid Values: `lowest-price | prioritized`   
Required: Yes

 ** CapacityReservationOptions **   <a name="EMR-Type-OnDemandProvisioningSpecification-CapacityReservationOptions"></a>
The launch specification for On-Demand instances in the instance fleet, which determines the allocation strategy.  
Type: [OnDemandCapacityReservationOptions](API_OnDemandCapacityReservationOptions.md) object  
Required: No

## See Also
<a name="API_OnDemandProvisioningSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/OnDemandProvisioningSpecification) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/OnDemandProvisioningSpecification) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/OnDemandProvisioningSpecification) 