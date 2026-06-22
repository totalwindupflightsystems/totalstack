---
id: "@specs/aws/batch/docs/API_LaunchTemplateSpecification"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LaunchTemplateSpecification"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# LaunchTemplateSpecification

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_LaunchTemplateSpecification
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LaunchTemplateSpecification
<a name="API_LaunchTemplateSpecification"></a>

An object that represents a launch template that's associated with a compute resource. You must specify either the launch template ID or launch template name in the request, but not both.

If security groups are specified using both the `securityGroupIds` parameter of `CreateComputeEnvironment` and the launch template, the values in the `securityGroupIds` parameter of `CreateComputeEnvironment` will be used.

**Note**  
This object isn't applicable to jobs that are running on Fargate resources.

## Contents
<a name="API_LaunchTemplateSpecification_Contents"></a>

 ** launchTemplateId **   <a name="Batch-Type-LaunchTemplateSpecification-launchTemplateId"></a>
The ID of the launch template.  
Type: String  
Required: No

 ** launchTemplateName **   <a name="Batch-Type-LaunchTemplateSpecification-launchTemplateName"></a>
The name of the launch template.  
Type: String  
Required: No

 ** overrides **   <a name="Batch-Type-LaunchTemplateSpecification-overrides"></a>
A launch template to use in place of the default launch template. You must specify either the launch template ID or launch template name in the request, but not both.  
You can specify up to ten (10) launch template overrides that are associated to unique instance types or families for each compute environment.  
To unset all override templates for a compute environment, you can pass an empty array to the [UpdateComputeEnvironment.overrides](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html) parameter, or not include the `overrides` parameter when submitting the `UpdateComputeEnvironment` API operation.
Type: Array of [LaunchTemplateSpecificationOverride](API_LaunchTemplateSpecificationOverride.md) objects  
Required: No

 ** userdataType **   <a name="Batch-Type-LaunchTemplateSpecification-userdataType"></a>
The EKS node initialization process to use. You only need to specify this value if you are using a custom AMI. The default value is `EKS_BOOTSTRAP_SH`. If *imageType* is a custom AMI based on EKS\_AL2023 or EKS\_AL2023\_NVIDIA then you must choose `EKS_NODEADM`.  
Type: String  
Valid Values: `EKS_BOOTSTRAP_SH | EKS_NODEADM`   
Required: No

 ** version **   <a name="Batch-Type-LaunchTemplateSpecification-version"></a>
The version number of the launch template, `$Default`, or `$Latest`.  
If the value is `$Default`, the default version of the launch template is used. If the value is `$Latest`, the latest version of the launch template is used.   
If the AMI ID that's used in a compute environment is from the launch template, the AMI isn't changed when the compute environment is updated. It's only changed if the `updateToLatestImageVersion` parameter for the compute environment is set to `true`. During an infrastructure update, if either `$Default` or `$Latest` is specified, AWS Batch re-evaluates the launch template version, and it might use a different version of the launch template. This is the case even if the launch template isn't specified in the update. When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the * AWS Batch User Guide*.
Default: `$Default`   
Latest: `$Latest`   
Type: String  
Required: No

## See Also
<a name="API_LaunchTemplateSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/LaunchTemplateSpecification) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/LaunchTemplateSpecification) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/LaunchTemplateSpecification) 