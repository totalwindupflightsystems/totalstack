---
id: "@specs/aws/emr/docs/API_InstanceTypeConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceTypeConfig"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceTypeConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceTypeConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceTypeConfig
<a name="API_InstanceTypeConfig"></a>

An instance type configuration for each instance type in an instance fleet, which determines the Amazon EC2 instances Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities. When you use an allocation strategy, you can include a maximum of 30 instance type configurations for a fleet. For more information about how to use an allocation strategy, see [Configure Instance Fleets](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-fleet.html). Without an allocation strategy, you may specify a maximum of five instance type configurations for a fleet.

**Note**  
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

## Contents
<a name="API_InstanceTypeConfig_Contents"></a>

 ** InstanceType **   <a name="EMR-Type-InstanceTypeConfig-InstanceType"></a>
An Amazon EC2 instance type, such as `m3.xlarge`.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** BidPrice **   <a name="EMR-Type-InstanceTypeConfig-BidPrice"></a>
The bid price for each Amazon EC2 Spot Instance type as defined by `InstanceType`. Expressed in USD. If neither `BidPrice` nor `BidPriceAsPercentageOfOnDemandPrice` is provided, `BidPriceAsPercentageOfOnDemandPrice` defaults to 100%.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** BidPriceAsPercentageOfOnDemandPrice **   <a name="EMR-Type-InstanceTypeConfig-BidPriceAsPercentageOfOnDemandPrice"></a>
The bid price, as a percentage of On-Demand price, for each Amazon EC2 Spot Instance as defined by `InstanceType`. Expressed as a number (for example, 20 specifies 20%). If neither `BidPrice` nor `BidPriceAsPercentageOfOnDemandPrice` is provided, `BidPriceAsPercentageOfOnDemandPrice` defaults to 100%.  
Type: Double  
Valid Range: Minimum value of 0.0.  
Required: No

 ** Configurations **   <a name="EMR-Type-InstanceTypeConfig-Configurations"></a>
A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software that run on the cluster.  
Type: Array of [Configuration](API_Configuration.md) objects  
Required: No

 ** CustomAmiId **   <a name="EMR-Type-InstanceTypeConfig-CustomAmiId"></a>
The custom AMI ID to use for the instance type.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** EbsConfiguration **   <a name="EMR-Type-InstanceTypeConfig-EbsConfiguration"></a>
The configuration of Amazon Elastic Block Store (Amazon EBS) attached to each instance as defined by `InstanceType`.   
Type: [EbsConfiguration](API_EbsConfiguration.md) object  
Required: No

 ** Priority **   <a name="EMR-Type-InstanceTypeConfig-Priority"></a>
The priority at which Amazon EMR launches the Amazon EC2 instances with this instance type. Priority starts at 0, which is the highest priority. Amazon EMR considers the highest priority first.  
Type: Double  
Valid Range: Minimum value of 0.0.  
Required: No

 ** WeightedCapacity **   <a name="EMR-Type-InstanceTypeConfig-WeightedCapacity"></a>
The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in [InstanceFleetConfig](API_InstanceFleetConfig.md). This value is 1 for a master instance fleet, and must be 1 or greater for core and task instance fleets. Defaults to 1 if not specified.   
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_InstanceTypeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceTypeConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceTypeConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceTypeConfig) 