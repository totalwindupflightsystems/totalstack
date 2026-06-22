---
id: "@specs/aws/batch/docs/API_LaunchTemplateSpecificationOverride"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LaunchTemplateSpecificationOverride"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# LaunchTemplateSpecificationOverride

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_LaunchTemplateSpecificationOverride
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LaunchTemplateSpecificationOverride
<a name="API_LaunchTemplateSpecificationOverride"></a>

An object that represents a launch template to use in place of the default launch template. You must specify either the launch template ID or launch template name in the request, but not both.

If security groups are specified using both the `securityGroupIds` parameter of `CreateComputeEnvironment` and the launch template, the values in the `securityGroupIds` parameter of `CreateComputeEnvironment` will be used.

You can define up to ten (10) overrides for each compute environment.

**Note**  
This object isn't applicable to jobs that are running on Fargate resources.

**Note**  
To unset all override templates for a compute environment, you can pass an empty array to the [UpdateComputeEnvironment.overrides](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html) parameter, or not include the `overrides` parameter when submitting the `UpdateComputeEnvironment` API operation.

## Contents
<a name="API_LaunchTemplateSpecificationOverride_Contents"></a>

 ** launchTemplateId **   <a name="Batch-Type-LaunchTemplateSpecificationOverride-launchTemplateId"></a>
The ID of the launch template.  
 **Note:** If you specify the `launchTemplateId` you can't specify the `launchTemplateName` as well.  
Type: String  
Required: No

 ** launchTemplateName **   <a name="Batch-Type-LaunchTemplateSpecificationOverride-launchTemplateName"></a>
The name of the launch template.  
 **Note:** If you specify the `launchTemplateName` you can't specify the `launchTemplateId` as well.  
Type: String  
Required: No

 ** targetInstanceTypes **   <a name="Batch-Type-LaunchTemplateSpecificationOverride-targetInstanceTypes"></a>
The instance type or family that this override launch template should be applied to.  
This parameter is required when defining a launch template override.  
Information included in this parameter must meet the following requirements:  
+ Must be a valid Amazon EC2 instance type or family.
+ The following AWS Batch `InstanceTypes` are not allowed: `optimal`, `default_x86_64`, and `default_arm64`.
+  `targetInstanceTypes` can target only instance types and families that are included within the [https://docs.aws.amazon.com/batch/latest/APIReference/API_ComputeResource.html#Batch-Type-ComputeResource-instanceTypes](https://docs.aws.amazon.com/batch/latest/APIReference/API_ComputeResource.html#Batch-Type-ComputeResource-instanceTypes) set. `targetInstanceTypes` doesn't need to include all of the instances from the `instanceType` set, but at least a subset. For example, if `ComputeResource.instanceTypes` includes `[m5, g5]`, `targetInstanceTypes` can include `[m5.2xlarge]` and `[m5.large]` but not `[c5.large]`.
+  `targetInstanceTypes` included within the same launch template override or across launch template overrides can't overlap for the same compute environment. For example, you can't define one launch template override to target an instance family and another define an instance type within this same family.
Type: Array of strings  
Required: No

 ** userdataType **   <a name="Batch-Type-LaunchTemplateSpecificationOverride-userdataType"></a>
The EKS node initialization process to use. You only need to specify this value if you are using a custom AMI. The default value is `EKS_BOOTSTRAP_SH`. If *imageType* is a custom AMI based on EKS\_AL2023 or EKS\_AL2023\_NVIDIA then you must choose `EKS_NODEADM`.  
Type: String  
Valid Values: `EKS_BOOTSTRAP_SH | EKS_NODEADM`   
Required: No

 ** version **   <a name="Batch-Type-LaunchTemplateSpecificationOverride-version"></a>
The version number of the launch template, `$Default`, or `$Latest`.  
If the value is `$Default`, the default version of the launch template is used. If the value is `$Latest`, the latest version of the launch template is used.   
If the AMI ID that's used in a compute environment is from the launch template, the AMI isn't changed when the compute environment is updated. It's only changed if the `updateToLatestImageVersion` parameter for the compute environment is set to `true`. During an infrastructure update, if either `$Default` or `$Latest` is specified, AWS Batch re-evaluates the launch template version, and it might use a different version of the launch template. This is the case even if the launch template isn't specified in the update. When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the * AWS Batch User Guide*.
Default: `$Default`   
Latest: `$Latest`   
Type: String  
Required: No

## See Also
<a name="API_LaunchTemplateSpecificationOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/LaunchTemplateSpecificationOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/LaunchTemplateSpecificationOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/LaunchTemplateSpecificationOverride) 