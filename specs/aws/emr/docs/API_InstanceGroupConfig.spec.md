---
id: "@specs/aws/emr/docs/API_InstanceGroupConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceGroupConfig"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceGroupConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceGroupConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceGroupConfig
<a name="API_InstanceGroupConfig"></a>

Configuration defining a new instance group.

## Contents
<a name="API_InstanceGroupConfig_Contents"></a>

 ** InstanceCount **   <a name="EMR-Type-InstanceGroupConfig-InstanceCount"></a>
Target number of instances for the instance group.  
Type: Integer  
Required: Yes

 ** InstanceRole **   <a name="EMR-Type-InstanceGroupConfig-InstanceRole"></a>
The role of the instance group in the cluster.  
Type: String  
Valid Values: `MASTER | CORE | TASK`   
Required: Yes

 ** InstanceType **   <a name="EMR-Type-InstanceGroupConfig-InstanceType"></a>
The Amazon EC2 instance type for all instances in the instance group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** AutoScalingPolicy **   <a name="EMR-Type-InstanceGroupConfig-AutoScalingPolicy"></a>
An automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates Amazon EC2 instances in response to the value of a CloudWatch metric. See [PutAutoScalingPolicy](API_PutAutoScalingPolicy.md).  
Type: [AutoScalingPolicy](API_AutoScalingPolicy.md) object  
Required: No

 ** BidPrice **   <a name="EMR-Type-InstanceGroupConfig-BidPrice"></a>
The bid price for each Amazon EC2 Spot Instance type as defined by `InstanceType`. Expressed in USD. If neither `BidPrice` nor `BidPriceAsPercentageOfOnDemandPrice` is provided, `BidPriceAsPercentageOfOnDemandPrice` defaults to 100%.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Configurations **   <a name="EMR-Type-InstanceGroupConfig-Configurations"></a>
Amazon EMR releases 4.x or later.
The list of configurations supplied for an Amazon EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).  
Type: Array of [Configuration](API_Configuration.md) objects  
Required: No

 ** CustomAmiId **   <a name="EMR-Type-InstanceGroupConfig-CustomAmiId"></a>
The custom AMI ID to use for the provisioned instance group.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** EbsConfiguration **   <a name="EMR-Type-InstanceGroupConfig-EbsConfiguration"></a>
EBS configurations that will be attached to each Amazon EC2 instance in the instance group.  
Type: [EbsConfiguration](API_EbsConfiguration.md) object  
Required: No

 ** Market **   <a name="EMR-Type-InstanceGroupConfig-Market"></a>
Market type of the Amazon EC2 instances used to create a cluster node.  
Type: String  
Valid Values: `ON_DEMAND | SPOT`   
Required: No

 ** Name **   <a name="EMR-Type-InstanceGroupConfig-Name"></a>
Friendly name given to the instance group.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

## See Also
<a name="API_InstanceGroupConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceGroupConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceGroupConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceGroupConfig) 