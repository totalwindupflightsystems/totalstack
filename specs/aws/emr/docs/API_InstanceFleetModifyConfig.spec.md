---
id: "@specs/aws/emr/docs/API_InstanceFleetModifyConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceFleetModifyConfig"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceFleetModifyConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceFleetModifyConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceFleetModifyConfig
<a name="API_InstanceFleetModifyConfig"></a>

Configuration parameters for an instance fleet modification request.

**Note**  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

## Contents
<a name="API_InstanceFleetModifyConfig_Contents"></a>

 ** InstanceFleetId **   <a name="EMR-Type-InstanceFleetModifyConfig-InstanceFleetId"></a>
A unique identifier for the instance fleet.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

 ** Context **   <a name="EMR-Type-InstanceFleetModifyConfig-Context"></a>
Reserved.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** InstanceTypeConfigs **   <a name="EMR-Type-InstanceFleetModifyConfig-InstanceTypeConfigs"></a>
An array of InstanceTypeConfig objects that specify how Amazon EMR provisions Amazon EC2 instances when it fulfills On-Demand and Spot capacities. For more information, see [InstanceTypeConfig](https://docs.aws.amazon.com/emr/latest/APIReference/API_InstanceTypeConfig.html).  
Type: Array of [InstanceTypeConfig](API_InstanceTypeConfig.md) objects  
Required: No

 ** ResizeSpecifications **   <a name="EMR-Type-InstanceFleetModifyConfig-ResizeSpecifications"></a>
The resize specification for the instance fleet.  
Type: [InstanceFleetResizingSpecifications](API_InstanceFleetResizingSpecifications.md) object  
Required: No

 ** TargetOnDemandCapacity **   <a name="EMR-Type-InstanceFleetModifyConfig-TargetOnDemandCapacity"></a>
The target capacity of On-Demand units for the instance fleet. For more information see [InstanceFleetConfig:TargetOnDemandCapacity](API_InstanceFleetConfig.md#EMR-Type-InstanceFleetConfig-TargetOnDemandCapacity).  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** TargetSpotCapacity **   <a name="EMR-Type-InstanceFleetModifyConfig-TargetSpotCapacity"></a>
The target capacity of Spot units for the instance fleet. For more information, see [InstanceFleetConfig:TargetSpotCapacity](API_InstanceFleetConfig.md#EMR-Type-InstanceFleetConfig-TargetSpotCapacity).  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_InstanceFleetModifyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceFleetModifyConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceFleetModifyConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceFleetModifyConfig) 