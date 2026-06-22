---
id: "@specs/aws/emr/docs/API_PlacementGroupConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PlacementGroupConfig"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# PlacementGroupConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_PlacementGroupConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PlacementGroupConfig
<a name="API_PlacementGroupConfig"></a>

Placement group configuration for an Amazon EMR cluster. The configuration specifies the placement strategy that can be applied to instance roles during cluster creation.

To use this configuration, consider attaching managed policy AmazonElasticMapReducePlacementGroupPolicy to the Amazon EMR role.

## Contents
<a name="API_PlacementGroupConfig_Contents"></a>

 ** InstanceRole **   <a name="EMR-Type-PlacementGroupConfig-InstanceRole"></a>
Role of the instance in the cluster.  
Starting with Amazon EMR release 5.23.0, the only supported instance role is `MASTER`.  
Type: String  
Valid Values: `MASTER | CORE | TASK`   
Required: Yes

 ** PlacementStrategy **   <a name="EMR-Type-PlacementGroupConfig-PlacementStrategy"></a>
Amazon EC2 Placement Group strategy associated with instance role.  
Starting with Amazon EMR release 5.23.0, the only supported placement strategy is `SPREAD` for the `MASTER` instance role.  
Type: String  
Valid Values: `SPREAD | PARTITION | CLUSTER | NONE`   
Required: No

## See Also
<a name="API_PlacementGroupConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/PlacementGroupConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/PlacementGroupConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/PlacementGroupConfig) 