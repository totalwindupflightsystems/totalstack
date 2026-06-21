---
id: "@specs/aws/cloudtrail/docs/API_Resource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Resource"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# Resource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_Resource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Resource
<a name="API_Resource"></a>

Specifies the type and name of a resource referenced by an event.

## Contents
<a name="API_Resource_Contents"></a>

 ** ResourceName **   <a name="awscloudtrail-Type-Resource-ResourceName"></a>
The name of the resource referenced by the event returned. These are user-created names whose values will depend on the environment. For example, the resource name might be "auto-scaling-test-group" for an Auto Scaling Group or "i-1234567" for an EC2 Instance.  
Type: String  
Required: No

 ** ResourceType **   <a name="awscloudtrail-Type-Resource-ResourceType"></a>
The type of a resource referenced by the event returned. When the resource type cannot be determined, null is returned. Some examples of resource types are: **Instance** for EC2, **Trail** for CloudTrail, **DBInstance** for Amazon RDS, and **AccessKey** for IAM. To learn more about how to look up and filter events by the resource types supported for a service, see [Filtering CloudTrail Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-console.html#filtering-cloudtrail-events).  
Type: String  
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Resource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Resource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Resource) 