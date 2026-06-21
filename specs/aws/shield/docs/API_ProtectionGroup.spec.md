---
id: "@specs/aws/shield/docs/API_ProtectionGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProtectionGroup"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# ProtectionGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_ProtectionGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProtectionGroup
<a name="API_ProtectionGroup"></a>

A grouping of protected resources that you and AWS Shield Advanced can monitor as a collective. This resource grouping improves the accuracy of detection and reduces false positives. 

## Contents
<a name="API_ProtectionGroup_Contents"></a>

 ** Aggregation **   <a name="AWSShield-Type-ProtectionGroup-Aggregation"></a>
Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events.  
+  `Sum` - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.
+  `Mean` - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.
+  `Max` - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront distributions and origin resources for CloudFront distributions.
Type: String  
Valid Values: `SUM | MEAN | MAX`   
Required: Yes

 ** Members **   <a name="AWSShield-Type-ProtectionGroup-Members"></a>
The ARNs (Amazon Resource Names) of the resources to include in the protection group. You must set this when you set `Pattern` to `ARBITRARY` and you must not set it for any other `Pattern` setting.   
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10000 items.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** Pattern **   <a name="AWSShield-Type-ProtectionGroup-Pattern"></a>
The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource ARNs (Amazon Resource Names), or include all resources of a specified resource type.  
Type: String  
Valid Values: `ALL | ARBITRARY | BY_RESOURCE_TYPE`   
Required: Yes

 ** ProtectionGroupId **   <a name="AWSShield-Type-ProtectionGroup-ProtectionGroupId"></a>
The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `[a-zA-Z0-9\\-]*`   
Required: Yes

 ** ProtectionGroupArn **   <a name="AWSShield-Type-ProtectionGroup-ProtectionGroupArn"></a>
The ARN (Amazon Resource Name) of the protection group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*`   
Required: No

 ** ResourceType **   <a name="AWSShield-Type-ProtectionGroup-ResourceType"></a>
The resource type to include in the protection group. All protected resources of this type are included in the protection group. You must set this when you set `Pattern` to `BY_RESOURCE_TYPE` and you must not set it for any other `Pattern` setting.   
Type: String  
Valid Values: `CLOUDFRONT_DISTRIBUTION | ROUTE_53_HOSTED_ZONE | ELASTIC_IP_ALLOCATION | CLASSIC_LOAD_BALANCER | APPLICATION_LOAD_BALANCER | GLOBAL_ACCELERATOR`   
Required: No

## See Also
<a name="API_ProtectionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/ProtectionGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/ProtectionGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/ProtectionGroup) 