---
id: "@specs/aws/batch/docs/API_ComputeEnvironmentDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ComputeEnvironmentDetail"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ComputeEnvironmentDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ComputeEnvironmentDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ComputeEnvironmentDetail
<a name="API_ComputeEnvironmentDetail"></a>

An object that represents an AWS Batch compute environment.

## Contents
<a name="API_ComputeEnvironmentDetail_Contents"></a>

 ** computeEnvironmentArn **   <a name="Batch-Type-ComputeEnvironmentDetail-computeEnvironmentArn"></a>
The Amazon Resource Name (ARN) of the compute environment.  
Type: String  
Required: Yes

 ** computeEnvironmentName **   <a name="Batch-Type-ComputeEnvironmentDetail-computeEnvironmentName"></a>
The name of the compute environment. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).  
Type: String  
Required: Yes

 ** computeResources **   <a name="Batch-Type-ComputeEnvironmentDetail-computeResources"></a>
The compute resources defined for the compute environment. For more information, see [Compute environments](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html) in the * AWS Batch User Guide*.  
Type: [ComputeResource](API_ComputeResource.md) object  
Required: No

 ** containerOrchestrationType **   <a name="Batch-Type-ComputeEnvironmentDetail-containerOrchestrationType"></a>
The orchestration type of the compute environment. The valid values are `ECS` (default) or `EKS`.  
Type: String  
Valid Values: `ECS | EKS`   
Required: No

 ** context **   <a name="Batch-Type-ComputeEnvironmentDetail-context"></a>
Reserved.  
Type: String  
Required: No

 ** ecsClusterArn **   <a name="Batch-Type-ComputeEnvironmentDetail-ecsClusterArn"></a>
The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster that the compute environment uses.  
Type: String  
Required: No

 ** eksConfiguration **   <a name="Batch-Type-ComputeEnvironmentDetail-eksConfiguration"></a>
The configuration for the Amazon EKS cluster that supports the AWS Batch compute environment. Only specify this parameter if the `containerOrchestrationType` is `EKS`.  
Type: [EksConfiguration](API_EksConfiguration.md) object  
Required: No

 ** serviceRole **   <a name="Batch-Type-ComputeEnvironmentDetail-serviceRole"></a>
The service role that's associated with the compute environment that allows AWS Batch to make calls to AWS API operations on your behalf. For more information, see [Batch service IAM role](https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html) in the * AWS Batch User Guide*.  
Type: String  
Required: No

 ** state **   <a name="Batch-Type-ComputeEnvironmentDetail-state"></a>
The state of the compute environment. The valid values are `ENABLED` or `DISABLED`.  
If the state is `ENABLED`, then the AWS Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically based on the job queue demand.  
If the state is `DISABLED`, then the AWS Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a `STARTING` or `RUNNING` state continue to progress normally. Managed compute environments in the `DISABLED` state don't scale out.   
Compute environments in a `DISABLED` state may continue to incur billing charges, for example, if they have running instances due to jobs that are still executing or a non-zero `minvCpus` setting. To prevent additional charges, disable and delete the compute environment.
When an instance is idle, the instance scales down to the `minvCpus` value. However, the instance size doesn't change. For example, consider a `c5.8xlarge` instance with a `minvCpus` value of `4` and a `desiredvCpus` value of `36`. This instance doesn't scale down to a `c5.large` instance.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** status **   <a name="Batch-Type-ComputeEnvironmentDetail-status"></a>
The current status of the compute environment (for example, `CREATING` or `VALID`).  
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | DELETED | VALID | INVALID`   
Required: No

 ** statusReason **   <a name="Batch-Type-ComputeEnvironmentDetail-statusReason"></a>
A short, human-readable string to provide additional details for the current status of the compute environment.  
Type: String  
Required: No

 ** tags **   <a name="Batch-Type-ComputeEnvironmentDetail-tags"></a>
The tags applied to the compute environment.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** type **   <a name="Batch-Type-ComputeEnvironmentDetail-type"></a>
The type of the compute environment: `MANAGED` or `UNMANAGED`. For more information, see [Compute environments](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html) in the * AWS Batch User Guide*.  
Type: String  
Valid Values: `MANAGED | UNMANAGED`   
Required: No

 ** unmanagedvCpus **   <a name="Batch-Type-ComputeEnvironmentDetail-unmanagedvCpus"></a>
The maximum number of VCPUs expected to be used for an unmanaged compute environment.  
Type: Integer  
Required: No

 ** updatePolicy **   <a name="Batch-Type-ComputeEnvironmentDetail-updatePolicy"></a>
Specifies the infrastructure update policy for the compute environment. For more information about infrastructure updates, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the * AWS Batch User Guide*.  
Type: [UpdatePolicy](API_UpdatePolicy.md) object  
Required: No

 ** uuid **   <a name="Batch-Type-ComputeEnvironmentDetail-uuid"></a>
Unique identifier for the compute environment.  
Type: String  
Required: No

## See Also
<a name="API_ComputeEnvironmentDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ComputeEnvironmentDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ComputeEnvironmentDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ComputeEnvironmentDetail) 