---
id: "@specs/aws/batch/docs/API_EksContainer"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksContainer"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksContainer

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksContainer
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksContainer
<a name="API_EksContainer"></a>

EKS container properties are used in job definitions for Amazon EKS based job definitions to describe the properties for a container node in the pod that's launched as part of a job. This can't be specified for Amazon ECS based job definitions.

## Contents
<a name="API_EksContainer_Contents"></a>

 ** image **   <a name="Batch-Type-EksContainer-image"></a>
The Docker image used to start the container.  
Type: String  
Required: Yes

 ** args **   <a name="Batch-Type-EksContainer-args"></a>
An array of arguments to the entrypoint. If this isn't specified, the `CMD` of the container image is used. This corresponds to the `args` member in the [Entrypoint](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint) portion of the [Pod](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/) in Kubernetes. Environment variable references are expanded using the container's environment.  
If the referenced environment variable doesn't exist, the reference in the command isn't changed. For example, if the reference is to "`$(NAME1)`" and the `NAME1` environment variable doesn't exist, the command string will remain "`$(NAME1)`." `$$` is replaced with `$`, and the resulting string isn't expanded. For example, `$$(VAR_NAME)` is passed as `$(VAR_NAME)` whether or not the `VAR_NAME` environment variable exists. For more information, see [Dockerfile reference: CMD](https://docs.docker.com/engine/reference/builder/#cmd) and [Define a command and arguments for a pod](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) in the *Kubernetes documentation*.  
Type: Array of strings  
Required: No

 ** command **   <a name="Batch-Type-EksContainer-command"></a>
The entrypoint for the container. This isn't run within a shell. If this isn't specified, the `ENTRYPOINT` of the container image is used. Environment variable references are expanded using the container's environment.  
If the referenced environment variable doesn't exist, the reference in the command isn't changed. For example, if the reference is to "`$(NAME1)`" and the `NAME1` environment variable doesn't exist, the command string will remain "`$(NAME1)`." `$$` is replaced with `$` and the resulting string isn't expanded. For example, `$$(VAR_NAME)` will be passed as `$(VAR_NAME)` whether or not the `VAR_NAME` environment variable exists. The entrypoint can't be updated. For more information, see [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint) in the *Dockerfile reference* and [Define a command and arguments for a container](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) and [Entrypoint](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint) in the *Kubernetes documentation*.  
Type: Array of strings  
Required: No

 ** env **   <a name="Batch-Type-EksContainer-env"></a>
The environment variables to pass to a container.  
Environment variables cannot start with "`AWS_BATCH`". This naming convention is reserved for variables that AWS Batch sets.
Type: Array of [EksContainerEnvironmentVariable](API_EksContainerEnvironmentVariable.md) objects  
Required: No

 ** imagePullPolicy **   <a name="Batch-Type-EksContainer-imagePullPolicy"></a>
The image pull policy for the container. Supported values are `Always`, `IfNotPresent`, and `Never`. This parameter defaults to `IfNotPresent`. However, if the `:latest` tag is specified, it defaults to `Always`. For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images) in the *Kubernetes documentation*.  
Type: String  
Required: No

 ** name **   <a name="Batch-Type-EksContainer-name"></a>
The name of the container. If the name isn't specified, the default name "`Default`" is used. Each container in a pod must have a unique name.  
Type: String  
Required: No

 ** resources **   <a name="Batch-Type-EksContainer-resources"></a>
The type and amount of resources to assign to a container. The supported resources include `memory`, `cpu`, and `nvidia.com/gpu`. For more information, see [Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the *Kubernetes documentation*.  
Type: [EksContainerResourceRequirements](API_EksContainerResourceRequirements.md) object  
Required: No

 ** securityContext **   <a name="Batch-Type-EksContainer-securityContext"></a>
The security context for a job. For more information, see [Configure a security context for a pod or container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) in the *Kubernetes documentation*.  
Type: [EksContainerSecurityContext](API_EksContainerSecurityContext.md) object  
Required: No

 ** volumeMounts **   <a name="Batch-Type-EksContainer-volumeMounts"></a>
The volume mounts for the container. AWS Batch supports `emptyDir`, `hostPath`, and `secret` volume types. For more information about volumes and volume mounts in Kubernetes, see [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) in the *Kubernetes documentation*.  
Type: Array of [EksContainerVolumeMount](API_EksContainerVolumeMount.md) objects  
Required: No

## See Also
<a name="API_EksContainer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksContainer) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksContainer) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksContainer) 