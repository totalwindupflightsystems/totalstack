---
id: "@specs/aws/emr/docs/API_InstanceGroupDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InstanceGroupDetail"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# InstanceGroupDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_InstanceGroupDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InstanceGroupDetail
<a name="API_InstanceGroupDetail"></a>

Detailed information about an instance group.

## Contents
<a name="API_InstanceGroupDetail_Contents"></a>

 ** CreationDateTime **   <a name="EMR-Type-InstanceGroupDetail-CreationDateTime"></a>
The date/time the instance group was created.  
Type: Timestamp  
Required: Yes

 ** InstanceRequestCount **   <a name="EMR-Type-InstanceGroupDetail-InstanceRequestCount"></a>
Target number of instances to run in the instance group.  
Type: Integer  
Required: Yes

 ** InstanceRole **   <a name="EMR-Type-InstanceGroupDetail-InstanceRole"></a>
Instance group role in the cluster  
Type: String  
Valid Values: `MASTER | CORE | TASK`   
Required: Yes

 ** InstanceRunningCount **   <a name="EMR-Type-InstanceGroupDetail-InstanceRunningCount"></a>
Actual count of running instances.  
Type: Integer  
Required: Yes

 ** InstanceType **   <a name="EMR-Type-InstanceGroupDetail-InstanceType"></a>
Amazon EC2 instance type.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** Market **   <a name="EMR-Type-InstanceGroupDetail-Market"></a>
Market type of the Amazon EC2 instances used to create a cluster node.  
Type: String  
Valid Values: `ON_DEMAND | SPOT`   
Required: Yes

 ** State **   <a name="EMR-Type-InstanceGroupDetail-State"></a>
State of instance group. The following values are no longer supported: STARTING, TERMINATED, and FAILED.  
Type: String  
Valid Values: `PROVISIONING | BOOTSTRAPPING | RUNNING | RECONFIGURING | RESIZING | SUSPENDED | TERMINATING | TERMINATED | ARRESTED | SHUTTING_DOWN | ENDED`   
Required: Yes

 ** BidPrice **   <a name="EMR-Type-InstanceGroupDetail-BidPrice"></a>
The bid price for each Amazon EC2 Spot Instance type as defined by `InstanceType`. Expressed in USD. If neither `BidPrice` nor `BidPriceAsPercentageOfOnDemandPrice` is provided, `BidPriceAsPercentageOfOnDemandPrice` defaults to 100%.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** CustomAmiId **   <a name="EMR-Type-InstanceGroupDetail-CustomAmiId"></a>
The custom AMI ID to use for the provisioned instance group.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** EndDateTime **   <a name="EMR-Type-InstanceGroupDetail-EndDateTime"></a>
The date/time the instance group was terminated.  
Type: Timestamp  
Required: No

 ** InstanceGroupId **   <a name="EMR-Type-InstanceGroupDetail-InstanceGroupId"></a>
Unique identifier for the instance group.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** LastStateChangeReason **   <a name="EMR-Type-InstanceGroupDetail-LastStateChangeReason"></a>
Details regarding the state of the instance group.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Name **   <a name="EMR-Type-InstanceGroupDetail-Name"></a>
Friendly name for the instance group.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** ReadyDateTime **   <a name="EMR-Type-InstanceGroupDetail-ReadyDateTime"></a>
The date/time the instance group was available to the cluster.  
Type: Timestamp  
Required: No

 ** StartDateTime **   <a name="EMR-Type-InstanceGroupDetail-StartDateTime"></a>
The date/time the instance group was started.  
Type: Timestamp  
Required: No

## See Also
<a name="API_InstanceGroupDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceGroupDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceGroupDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceGroupDetail) 