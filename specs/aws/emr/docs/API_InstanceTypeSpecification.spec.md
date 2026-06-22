---
id: "@specs/aws/emr/docs/API_InstanceTypeSpecification"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceTypeSpecification"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceTypeSpecification

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceTypeSpecification
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceTypeSpecification
<a name="API_InstanceTypeSpecification"></a>

The configuration specification for each instance type in an instance fleet.

**Note**  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

## Contents
<a name="API_InstanceTypeSpecification_Contents"></a>

 ** BidPrice **   <a name="EMR-Type-InstanceTypeSpecification-BidPrice"></a>
The bid price for each Amazon EC2 Spot Instance type as defined by `InstanceType`. Expressed in USD. If neither `BidPrice` nor `BidPriceAsPercentageOfOnDemandPrice` is provided, `BidPriceAsPercentageOfOnDemandPrice` defaults to 100%.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** BidPriceAsPercentageOfOnDemandPrice **   <a name="EMR-Type-InstanceTypeSpecification-BidPriceAsPercentageOfOnDemandPrice"></a>
The bid price, as a percentage of On-Demand price, for each Amazon EC2 Spot Instance as defined by `InstanceType`. Expressed as a number (for example, 20 specifies 20%).  
Type: Double  
Valid Range: Minimum value of 0.0.  
Required: No

 ** Configurations **   <a name="EMR-Type-InstanceTypeSpecification-Configurations"></a>
A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR.  
Type: Array of [Configuration](API_Configuration.md) objects  
Required: No

 ** CustomAmiId **   <a name="EMR-Type-InstanceTypeSpecification-CustomAmiId"></a>
The custom AMI ID to use for the instance type.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** EbsBlockDevices **   <a name="EMR-Type-InstanceTypeSpecification-EbsBlockDevices"></a>
The configuration of Amazon Elastic Block Store (Amazon EBS) attached to each instance as defined by `InstanceType`.  
Type: Array of [EbsBlockDevice](API_EbsBlockDevice.md) objects  
Required: No

 ** EbsOptimized **   <a name="EMR-Type-InstanceTypeSpecification-EbsOptimized"></a>
Evaluates to `TRUE` when the specified `InstanceType` is EBS-optimized.  
Type: Boolean  
Required: No

 ** InstanceType **   <a name="EMR-Type-InstanceTypeSpecification-InstanceType"></a>
The Amazon EC2 instance type, for example `m3.xlarge`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Priority **   <a name="EMR-Type-InstanceTypeSpecification-Priority"></a>
The priority at which Amazon EMR launches the Amazon EC2 instances with this instance type. Priority starts at 0, which is the highest priority. Amazon EMR considers the highest priority first.  
Type: Double  
Valid Range: Minimum value of 0.0.  
Required: No

 ** WeightedCapacity **   <a name="EMR-Type-InstanceTypeSpecification-WeightedCapacity"></a>
The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in [InstanceFleetConfig](API_InstanceFleetConfig.md). Capacity values represent performance characteristics such as vCPUs, memory, or I/O. If not specified, the default value is 1.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_InstanceTypeSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceTypeSpecification) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceTypeSpecification) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceTypeSpecification) 