---
id: "@specs/aws/batch/docs/API_TaskContainerOverrides"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TaskContainerOverrides"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# TaskContainerOverrides

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_TaskContainerOverrides
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TaskContainerOverrides
<a name="API_TaskContainerOverrides"></a>

The overrides that should be sent to a container.

For information about using AWS Batch overrides when you connect event sources to targets, see [BatchContainerOverrides](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_BatchContainerOverrides.html).

## Contents
<a name="API_TaskContainerOverrides_Contents"></a>

 ** command **   <a name="Batch-Type-TaskContainerOverrides-command"></a>
The command to send to the container that overrides the default command from the Docker image or the job definition.  
This parameter can't contain an empty string.
Type: Array of strings  
Required: No

 ** environment **   <a name="Batch-Type-TaskContainerOverrides-environment"></a>
The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.  
Environment variables cannot start with `AWS_BATCH`. This naming convention is reserved for variables that AWS Batch sets.
Type: Array of [KeyValuePair](API_KeyValuePair.md) objects  
Required: No

 ** name **   <a name="Batch-Type-TaskContainerOverrides-name"></a>
A pointer to the container that you want to override. The container's name provides a unique identifier for the container being used.  
Type: String  
Required: No

 ** resourceRequirements **   <a name="Batch-Type-TaskContainerOverrides-resourceRequirements"></a>
The type and amount of resources to assign to a container. This overrides the settings in the job definition. The supported resources include `GPU`, `MEMORY`, and `VCPU`.  
Type: Array of [ResourceRequirement](API_ResourceRequirement.md) objects  
Required: No

## See Also
<a name="API_TaskContainerOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/TaskContainerOverrides) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/TaskContainerOverrides) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/TaskContainerOverrides) 