---
id: "@specs/aws/batch/docs/API_ContainerOverrides"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ContainerOverrides"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ContainerOverrides

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ContainerOverrides
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ContainerOverrides
<a name="API_ContainerOverrides"></a>

The overrides that should be sent to a container.

For information about using AWS Batch overrides when you connect event sources to targets, see [BatchContainerOverrides](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_BatchContainerOverrides.html).

## Contents
<a name="API_ContainerOverrides_Contents"></a>

 ** command **   <a name="Batch-Type-ContainerOverrides-command"></a>
The command to send to the container that overrides the default command from the Docker image or the job definition.  
This parameter can't contain an empty string.
Type: Array of strings  
Required: No

 ** environment **   <a name="Batch-Type-ContainerOverrides-environment"></a>
The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.  
Environment variables cannot start with "`AWS_BATCH`". This naming convention is reserved for variables that AWS Batch sets.
Type: Array of [KeyValuePair](API_KeyValuePair.md) objects  
Required: No

 ** instanceType **   <a name="Batch-Type-ContainerOverrides-instanceType"></a>
The instance type to use for a multi-node parallel job.  
This parameter isn't applicable to single-node container jobs or jobs that run on Fargate resources, and shouldn't be provided.
Type: String  
Required: No

 ** memory **   <a name="Batch-Type-ContainerOverrides-memory"></a>
This parameter is deprecated, use `resourceRequirements` to override the memory requirements specified in the job definition. It's not supported for jobs running on Fargate resources. For jobs that run on Amazon EC2 resources, it overrides the `memory` parameter set in the job definition, but doesn't override any memory requirement that's specified in the `resourceRequirements` structure in the job definition. To override memory requirements that are specified in the `resourceRequirements` structure in the job definition, `resourceRequirements` must be specified in the `SubmitJob` request, with `type` set to `MEMORY` and `value` set to the new value. For more information, see [Can't override job definition resource requirements](https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#override-resource-requirements) in the * AWS Batch User Guide*.  
Type: Integer  
Required: No

 ** resourceRequirements **   <a name="Batch-Type-ContainerOverrides-resourceRequirements"></a>
The type and amount of resources to assign to a container. This overrides the settings in the job definition. The supported resources include `GPU`, `MEMORY`, and `VCPU`.  
Type: Array of [ResourceRequirement](API_ResourceRequirement.md) objects  
Required: No

 ** vcpus **   <a name="Batch-Type-ContainerOverrides-vcpus"></a>
This parameter is deprecated, use `resourceRequirements` to override the `vcpus` parameter that's set in the job definition. It's not supported for jobs running on Fargate resources. For jobs that run on Amazon EC2 resources, it overrides the `vcpus` parameter set in the job definition, but doesn't override any vCPU requirement specified in the `resourceRequirements` structure in the job definition. To override vCPU requirements that are specified in the `resourceRequirements` structure in the job definition, `resourceRequirements` must be specified in the `SubmitJob` request, with `type` set to `VCPU` and `value` set to the new value. For more information, see [Can't override job definition resource requirements](https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#override-resource-requirements) in the * AWS Batch User Guide*.  
Type: Integer  
Required: No

## See Also
<a name="API_ContainerOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ContainerOverrides) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ContainerOverrides) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ContainerOverrides) 