---
id: "@specs/aws/batch/docs/API_EksContainerOverride"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksContainerOverride"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksContainerOverride

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksContainerOverride
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksContainerOverride
<a name="API_EksContainerOverride"></a>

Object representing any Kubernetes overrides to a job definition that's used in a [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) API operation.

## Contents
<a name="API_EksContainerOverride_Contents"></a>

 ** args **   <a name="Batch-Type-EksContainerOverride-args"></a>
The arguments to the entrypoint to send to the container that overrides the default arguments from the Docker image or the job definition. For more information, see [Dockerfile reference: CMD](https://docs.docker.com/engine/reference/builder/#cmd) and [Define a command an arguments for a pod](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) in the *Kubernetes documentation*.  
Type: Array of strings  
Required: No

 ** command **   <a name="Batch-Type-EksContainerOverride-command"></a>
The command to send to the container that overrides the default command from the Docker image or the job definition.  
Type: Array of strings  
Required: No

 ** env **   <a name="Batch-Type-EksContainerOverride-env"></a>
The environment variables to send to the container. You can add new environment variables, which are added to the container at launch. Or, you can override the existing environment variables from the Docker image or the job definition.  
Environment variables cannot start with "`AWS_BATCH`". This naming convention is reserved for variables that AWS Batch sets.
Type: Array of [EksContainerEnvironmentVariable](API_EksContainerEnvironmentVariable.md) objects  
Required: No

 ** image **   <a name="Batch-Type-EksContainerOverride-image"></a>
The override of the Docker image that's used to start the container.  
Type: String  
Required: No

 ** name **   <a name="Batch-Type-EksContainerOverride-name"></a>
A pointer to the container that you want to override. The name must match a unique container name that you wish to override.  
Type: String  
Required: No

 ** resources **   <a name="Batch-Type-EksContainerOverride-resources"></a>
The type and amount of resources to assign to a container. These override the settings in the job definition. The supported resources include `memory`, `cpu`, and `nvidia.com/gpu`. For more information, see [Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the *Kubernetes documentation*.  
Type: [EksContainerResourceRequirements](API_EksContainerResourceRequirements.md) object  
Required: No

## See Also
<a name="API_EksContainerOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksContainerOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksContainerOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksContainerOverride) 