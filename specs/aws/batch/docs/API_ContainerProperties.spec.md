---
id: "@specs/aws/batch/docs/API_ContainerProperties"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ContainerProperties"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ContainerProperties

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ContainerProperties
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ContainerProperties
<a name="API_ContainerProperties"></a>

Container properties are used for Amazon ECS based job definitions. These properties to describe the container that's launched as part of a job.

## Contents
<a name="API_ContainerProperties_Contents"></a>

 ** command **   <a name="Batch-Type-ContainerProperties-command"></a>
The command that's passed to the container. This parameter maps to `Cmd` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `COMMAND` parameter to [docker run](https://docs.docker.com/engine/reference/run/). For more information, see [https://docs.docker.com/engine/reference/builder/\#cmd](https://docs.docker.com/engine/reference/builder/#cmd).  
Type: Array of strings  
Required: No

 ** enableExecuteCommand **   <a name="Batch-Type-ContainerProperties-enableExecuteCommand"></a>
Determines whether execute command functionality is turned on for this task. If `true`, execute command functionality is turned on all the containers in the task.  
Type: Boolean  
Required: No

 ** environment **   <a name="Batch-Type-ContainerProperties-environment"></a>
The environment variables to pass to a container. This parameter maps to `Env` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--env` option to [docker run](https://docs.docker.com/engine/reference/run/).  
We don't recommend using plaintext environment variables for sensitive information, such as credential data.
Environment variables cannot start with "`AWS_BATCH`". This naming convention is reserved for variables that AWS Batch sets.
Type: Array of [KeyValuePair](API_KeyValuePair.md) objects  
Required: No

 ** ephemeralStorage **   <a name="Batch-Type-ContainerProperties-ephemeralStorage"></a>
The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate.  
Type: [EphemeralStorage](API_EphemeralStorage.md) object  
Required: No

 ** executionRoleArn **   <a name="Batch-Type-ContainerProperties-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the execution role that AWS Batch can assume. For jobs that run on Fargate resources, you must provide an execution role. For more information, see [AWS Batch execution IAM role](https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html) in the * AWS Batch User Guide*.  
Type: String  
Required: No

 ** fargatePlatformConfiguration **   <a name="Batch-Type-ContainerProperties-fargatePlatformConfiguration"></a>
The platform configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.  
Type: [FargatePlatformConfiguration](API_FargatePlatformConfiguration.md) object  
Required: No

 ** image **   <a name="Batch-Type-ContainerProperties-image"></a>
Required. The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with ` repository-url/image:tag `. It can be 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), underscores (\_), colons (:), periods (.), forward slashes (/), and number signs (\#). This parameter maps to `Image` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `IMAGE` parameter of [docker run](https://docs.docker.com/engine/reference/run/).  
Docker image architecture must match the processor architecture of the compute resources that they're scheduled on. For example, ARM-based Docker images can only run on ARM-based compute resources.
+ Images in Amazon ECR Public repositories use the full `registry/repository[:tag]` or `registry/repository[@digest]` naming conventions. For example, `public.ecr.aws/registry_alias/my-web-app:latest `.
+ Images in Amazon ECR repositories use the full registry and repository URI (for example, `123456789012.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`).
+ Images in official repositories on Docker Hub use a single name (for example, `ubuntu` or `mongo`).
+ Images in other repositories on Docker Hub are qualified with an organization name (for example, `amazon/amazon-ecs-agent`).
+ Images in other online repositories are qualified further by a domain name (for example, `quay.io/assemblyline/ubuntu`).
Type: String  
Required: No

 ** instanceType **   <a name="Batch-Type-ContainerProperties-instanceType"></a>
The instance type to use for a multi-node parallel job. All node groups in a multi-node parallel job must use the same instance type.  
This parameter isn't applicable to single-node container jobs or jobs that run on Fargate resources, and shouldn't be provided.
Type: String  
Required: No

 ** jobRoleArn **   <a name="Batch-Type-ContainerProperties-jobRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions. For more information, see [IAM roles for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.  
Type: String  
Required: No

 ** linuxParameters **   <a name="Batch-Type-ContainerProperties-linuxParameters"></a>
Linux-specific modifications that are applied to the container, such as details for device mappings.  
Type: [LinuxParameters](API_LinuxParameters.md) object  
Required: No

 ** logConfiguration **   <a name="Batch-Type-ContainerProperties-logConfiguration"></a>
The log configuration specification for the container.  
This parameter maps to `LogConfig` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--log-driver` option to [docker run](https://docs.docker.com/engine/reference/run/). By default, containers use the same logging driver that the Docker daemon uses. However the container might use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see [Configure logging drivers](https://docs.docker.com/engine/admin/logging/overview/) in the Docker documentation.  
 AWS Batch currently supports a subset of the logging drivers available to the Docker daemon (shown in the [LogConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html) data type).
This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`   
The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable before containers placed on that instance can use these log configuration options. For more information, see [Amazon ECS container agent configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: [LogConfiguration](API_LogConfiguration.md) object  
Required: No

 ** memory **   <a name="Batch-Type-ContainerProperties-memory"></a>
This parameter is deprecated, use `resourceRequirements` to specify the memory requirements for the job definition. It's not supported for jobs running on Fargate resources. For jobs that run on Amazon EC2 resources, it specifies the memory hard limit (in MiB) for a container. If your container attempts to exceed the specified number, it's terminated. You must specify at least 4 MiB of memory for a job using this parameter. The memory hard limit can be specified in several places. It must be specified for each node at least once.  
Type: Integer  
Required: No

 ** mountPoints **   <a name="Batch-Type-ContainerProperties-mountPoints"></a>
The mount points for data volumes in your container. This parameter maps to `Volumes` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--volume` option to [docker run](https://docs.docker.com/engine/reference/run/).  
Type: Array of [MountPoint](API_MountPoint.md) objects  
Required: No

 ** networkConfiguration **   <a name="Batch-Type-ContainerProperties-networkConfiguration"></a>
The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.  
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object  
Required: No

 ** privileged **   <a name="Batch-Type-ContainerProperties-privileged"></a>
When this parameter is true, the container is given elevated permissions on the host container instance (similar to the `root` user). This parameter maps to `Privileged` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--privileged` option to [docker run](https://docs.docker.com/engine/reference/run/). The default value is false.  
This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided, or specified as false.
Type: Boolean  
Required: No

 ** readonlyRootFilesystem **   <a name="Batch-Type-ContainerProperties-readonlyRootFilesystem"></a>
When this parameter is true, the container is given read-only access to its root file system. This parameter maps to `ReadonlyRootfs` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--read-only` option to `docker run`.  
Type: Boolean  
Required: No

 ** repositoryCredentials **   <a name="Batch-Type-ContainerProperties-repositoryCredentials"></a>
The private repository authentication credentials to use.  
Type: [RepositoryCredentials](API_RepositoryCredentials.md) object  
Required: No

 ** resourceRequirements **   <a name="Batch-Type-ContainerProperties-resourceRequirements"></a>
The type and amount of resources to assign to a container. The supported resources include `GPU`, `MEMORY`, and `VCPU`.  
Type: Array of [ResourceRequirement](API_ResourceRequirement.md) objects  
Required: No

 ** runtimePlatform **   <a name="Batch-Type-ContainerProperties-runtimePlatform"></a>
An object that represents the compute environment architecture for AWS Batch jobs on Fargate.  
Type: [RuntimePlatform](API_RuntimePlatform.md) object  
Required: No

 ** secrets **   <a name="Batch-Type-ContainerProperties-secrets"></a>
The secrets for the container. For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the * AWS Batch User Guide*.  
Type: Array of [Secret](API_Secret.md) objects  
Required: No

 ** ulimits **   <a name="Batch-Type-ContainerProperties-ulimits"></a>
A list of `ulimits` to set in the container. This parameter maps to `Ulimits` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--ulimit` option to [docker run](https://docs.docker.com/engine/reference/run/).  
This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.
Type: Array of [Ulimit](API_Ulimit.md) objects  
Required: No

 ** user **   <a name="Batch-Type-ContainerProperties-user"></a>
The user name to use inside the container. This parameter maps to `User` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--user` option to [docker run](https://docs.docker.com/engine/reference/run/).  
Type: String  
Required: No

 ** vcpus **   <a name="Batch-Type-ContainerProperties-vcpus"></a>
This parameter is deprecated, use `resourceRequirements` to specify the vCPU requirements for the job definition. It's not supported for jobs running on Fargate resources. For jobs running on Amazon EC2 resources, it specifies the number of vCPUs reserved for the job.  
Each vCPU is equivalent to 1,024 CPU shares. This parameter maps to `CpuShares` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--cpu-shares` option to [docker run](https://docs.docker.com/engine/reference/run/). The number of vCPUs must be specified but can be specified in several places. You must specify it at least once for each node.  
Type: Integer  
Required: No

 ** volumes **   <a name="Batch-Type-ContainerProperties-volumes"></a>
A list of data volumes used in a job.  
Type: Array of [Volume](API_Volume.md) objects  
Required: No

## See Also
<a name="API_ContainerProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ContainerProperties) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ContainerProperties) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ContainerProperties) 