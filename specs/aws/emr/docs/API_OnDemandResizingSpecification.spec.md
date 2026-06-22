---
id: "@specs/aws/emr/docs/API_OnDemandResizingSpecification"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OnDemandResizingSpecification"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# OnDemandResizingSpecification

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_OnDemandResizingSpecification
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OnDemandResizingSpecification
<a name="API_OnDemandResizingSpecification"></a>

The resize specification for On-Demand Instances in the instance fleet, which contains the resize timeout period. 

## Contents
<a name="API_OnDemandResizingSpecification_Contents"></a>

 ** AllocationStrategy **   <a name="EMR-Type-OnDemandResizingSpecification-AllocationStrategy"></a>
Specifies the allocation strategy to use to launch On-Demand instances during a resize. The default is `lowest-price`.  
Type: String  
Valid Values: `lowest-price | prioritized`   
Required: No

 ** CapacityReservationOptions **   <a name="EMR-Type-OnDemandResizingSpecification-CapacityReservationOptions"></a>
Describes the strategy for using unused Capacity Reservations for fulfilling On-Demand capacity.  
Type: [OnDemandCapacityReservationOptions](API_OnDemandCapacityReservationOptions.md) object  
Required: No

 ** TimeoutDurationMinutes **   <a name="EMR-Type-OnDemandResizingSpecification-TimeoutDurationMinutes"></a>
On-Demand resize timeout in minutes. If On-Demand Instances are not provisioned within this time, the resize workflow stops. The minimum value is 5 minutes, and the maximum value is 10,080 minutes (7 days). The timeout applies to all resize workflows on the Instance Fleet. The resize could be triggered by Amazon EMR Managed Scaling or by the customer (via Amazon EMR Console, Amazon EMR CLI modify-instance-fleet or Amazon EMR SDK ModifyInstanceFleet API) or by Amazon EMR due to Amazon EC2 Spot Reclamation.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_OnDemandResizingSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/OnDemandResizingSpecification) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/OnDemandResizingSpecification) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/OnDemandResizingSpecification) 