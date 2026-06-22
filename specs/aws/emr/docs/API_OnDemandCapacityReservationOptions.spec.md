---
id: "@specs/aws/emr/docs/API_OnDemandCapacityReservationOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OnDemandCapacityReservationOptions"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# OnDemandCapacityReservationOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_OnDemandCapacityReservationOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OnDemandCapacityReservationOptions
<a name="API_OnDemandCapacityReservationOptions"></a>

Describes the strategy for using unused Capacity Reservations for fulfilling On-Demand capacity.

## Contents
<a name="API_OnDemandCapacityReservationOptions_Contents"></a>

 ** CapacityReservationPreference **   <a name="EMR-Type-OnDemandCapacityReservationOptions-CapacityReservationPreference"></a>
Indicates the instance's Capacity Reservation preferences. Possible preferences include:  
+  `open` - The instance can run in any open Capacity Reservation that has matching attributes (instance type, platform, Availability Zone).
+  `none` - The instance avoids running in a Capacity Reservation even if one is available. The instance runs as an On-Demand Instance.
Type: String  
Valid Values: `open | none`   
Required: No

 ** CapacityReservationResourceGroupArn **   <a name="EMR-Type-OnDemandCapacityReservationOptions-CapacityReservationResourceGroupArn"></a>
The ARN of the Capacity Reservation resource group in which to run the instance.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** UsageStrategy **   <a name="EMR-Type-OnDemandCapacityReservationOptions-UsageStrategy"></a>
Indicates whether to use unused Capacity Reservations for fulfilling On-Demand capacity.  
If you specify `use-capacity-reservations-first`, the fleet uses unused Capacity Reservations to fulfill On-Demand capacity up to the target On-Demand capacity. If multiple instance pools have unused Capacity Reservations, the On-Demand allocation strategy (`lowest-price`) is applied. If the number of unused Capacity Reservations is less than the On-Demand target capacity, the remaining On-Demand target capacity is launched according to the On-Demand allocation strategy (`lowest-price`).  
If you do not specify a value, the fleet fulfills the On-Demand capacity according to the chosen On-Demand allocation strategy.  
Type: String  
Valid Values: `use-capacity-reservations-first`   
Required: No

## See Also
<a name="API_OnDemandCapacityReservationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/OnDemandCapacityReservationOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/OnDemandCapacityReservationOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/OnDemandCapacityReservationOptions) 