---
id: "@specs/aws/emr/docs/API_PlacementType"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PlacementType"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# PlacementType

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_PlacementType
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PlacementType
<a name="API_PlacementType"></a>

The Amazon EC2 Availability Zone configuration of the cluster (job flow).

## Contents
<a name="API_PlacementType_Contents"></a>

 ** AvailabilityZone **   <a name="EMR-Type-PlacementType-AvailabilityZone"></a>
The Amazon EC2 Availability Zone for the cluster. `AvailabilityZone` is used for uniform instance groups, while `AvailabilityZones` (plural) is used for instance fleets.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** AvailabilityZones **   <a name="EMR-Type-PlacementType-AvailabilityZones"></a>
When multiple Availability Zones are specified, Amazon EMR evaluates them and launches instances in the optimal Availability Zone. `AvailabilityZones` is used for instance fleets, while `AvailabilityZone` (singular) is used for uniform instance groups.  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

## See Also
<a name="API_PlacementType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/PlacementType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/PlacementType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/PlacementType) 