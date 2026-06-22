---
id: "@specs/aws/batch/docs/API_ContainerDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ContainerDetail"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ContainerDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ContainerDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ContainerDetail
<a name="API_ContainerDetail"></a>

An object that represents the details of a container that's part of a job.

## Contents
<a name="API_ContainerDetail_Contents"></a>

 ** command **   <a name="Batch-Type-ContainerDetail-command"></a>
The command that's passed to the container.  
Type: Array of strings  
Required: No

 ** containerInstanceArn **   <a name="Batch-Type-ContainerDetail-containerInstanceArn"></a>
The Amazon Resource Name (ARN) of the container instance that the container is running on.  
Type: String  
Required: No

 ** enableExecuteCommand **   <a name="Batch-Type-ContainerDetail-enableExecuteCommand"></a>
Determines whether execute command functionality is turned on for this task. If `true`, execute command functionality is turned on all the containers in the task.  
Type: Boolean  
Required: No

 ** environment **   <a name="Batch-Type-ContainerDetail-environment"></a>
The environment variables to pass to a container.  
Environment variables cannot start with "`AWS_BATCH`". This naming convention is reserved for variables that AWS Batch sets.
Type: Array of [KeyValuePair](API_KeyValuePair.md) objects  
Required: No

 ** ephemeralStorage **   <a name="Batch-Type-ContainerDetail-ephemeralStorage"></a>
The amount of ephemeral storage allocated for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate.  
Type: [EphemeralStorage](API_EphemeralStorage.md) object  
Required: No

 ** executionRoleArn **   <a name="Batch-Type-ContainerDetail-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the execution role that AWS Batch can assume. For more information, see [Batch execution IAM role](https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html) in the * AWS Batch User Guide*.  
Type: String  
Required: No

 ** exitCode **   <a name="Batch-Type-ContainerDetail-exitCode"></a>
The exit code returned upon completion.  
Type: Integer  
Required: No

 ** fargatePlatformConfiguration **   <a name="Batch-Type-ContainerDetail-fargatePlatformConfiguration"></a>
The platform configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.  
Type: [FargatePlatformConfiguration](API_FargatePlatformConfiguration.md) object  
Required: No

 ** image **   <a name="Batch-Type-ContainerDetail-image"></a>
The image used to start the container.  
Type: String  
Required: No

 ** instanceType **   <a name="Batch-Type-ContainerDetail-instanceType"></a>
The instance type of the underlying host infrastructure of a multi-node parallel job.  
This parameter isn't applicable to jobs that are running on Fargate resources.
Type: String  
Required: No

 ** jobRoleArn **   <a name="Batch-Type-ContainerDetail-jobRoleArn"></a>
The Amazon Resource Name (ARN) that's associated with the job when run.  
Type: String  
Required: No

 ** linuxParameters **   <a name="Batch-Type-ContainerDetail-linuxParameters"></a>
Linux-specific modifications that are applied to the container, such as details for device mappings.  
Type: [LinuxParameters](API_LinuxParameters.md) object  
Required: No

 ** logConfiguration **   <a name="Batch-Type-ContainerDetail-logConfiguration"></a>
The log configuration specification for the container.  
This parameter maps to `LogConfig` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--log-driver` option to [docker run](https://docs.docker.com/engine/reference/run/). By default, containers use the same logging driver that the Docker daemon uses. However, the container might use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance. Or, alternatively, it must be configured on a different log server for remote logging options. For more information on the options for different supported log drivers, see [Configure logging drivers](https://docs.docker.com/engine/admin/logging/overview/) in the Docker documentation.  
 AWS Batch currently supports a subset of the logging drivers available to the Docker daemon (shown in the [LogConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html) data type). Additional log drivers might be available in future releases of the Amazon ECS container agent.
This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`   
The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable before containers placed on that instance can use these log configuration options. For more information, see [Amazon ECS container agent configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: [LogConfiguration](API_LogConfiguration.md) object  
Required: No

 ** logStreamName **   <a name="Batch-Type-ContainerDetail-logStreamName"></a>
The name of the Amazon CloudWatch Logs log stream that's associated with the container. The log group for AWS Batch jobs is `/aws/batch/job`. Each container attempt receives a log stream name when they reach the `RUNNING` status.  
Type: String  
Required: No

 ** memory **   <a name="Batch-Type-ContainerDetail-memory"></a>
For jobs running on Amazon EC2 resources that didn't specify memory requirements using `resourceRequirements`, the number of MiB of memory reserved for the job. For other jobs, including all run on Fargate resources, see `resourceRequirements`.  
Type: Integer  
Required: No

 ** mountPoints **   <a name="Batch-Type-ContainerDetail-mountPoints"></a>
The mount points for data volumes in your container.  
Type: Array of [MountPoint](API_MountPoint.md) objects  
Required: No

 ** networkConfiguration **   <a name="Batch-Type-ContainerDetail-networkConfiguration"></a>
The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.  
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object  
Required: No

 ** networkInterfaces **   <a name="Batch-Type-ContainerDetail-networkInterfaces"></a>
The network interfaces that are associated with the job.  
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects  
Required: No

 ** privileged **   <a name="Batch-Type-ContainerDetail-privileged"></a>
When this parameter is true, the container is given elevated permissions on the host container instance (similar to the `root` user). The default value is `false`.  
This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided, or specified as `false`.
Type: Boolean  
Required: No

 ** readonlyRootFilesystem **   <a name="Batch-Type-ContainerDetail-readonlyRootFilesystem"></a>
When this parameter is true, the container is given read-only access to its root file system. This parameter maps to `ReadonlyRootfs` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--read-only` option to [https://docs.docker.com/engine/reference/commandline/run/](https://docs.docker.com/engine/reference/commandline/run/).  
Type: Boolean  
Required: No

 ** reason **   <a name="Batch-Type-ContainerDetail-reason"></a>
A short (255 max characters) human-readable string to provide additional details for a running or stopped container.  
Type: String  
Required: No

 ** repositoryCredentials **   <a name="Batch-Type-ContainerDetail-repositoryCredentials"></a>
The private repository authentication credentials to use.  
Type: [RepositoryCredentials](API_RepositoryCredentials.md) object  
Required: No

 ** resourceRequirements **   <a name="Batch-Type-ContainerDetail-resourceRequirements"></a>
The type and amount of resources to assign to a container. The supported resources include `GPU`, `MEMORY`, and `VCPU`.  
Type: Array of [ResourceRequirement](API_ResourceRequirement.md) objects  
Required: No

 ** runtimePlatform **   <a name="Batch-Type-ContainerDetail-runtimePlatform"></a>
An object that represents the compute environment architecture for AWS Batch jobs on Fargate.  
Type: [RuntimePlatform](API_RuntimePlatform.md) object  
Required: No

 ** secrets **   <a name="Batch-Type-ContainerDetail-secrets"></a>
The secrets to pass to the container. For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the * AWS Batch User Guide*.  
Type: Array of [Secret](API_Secret.md) objects  
Required: No

 ** taskArn **   <a name="Batch-Type-ContainerDetail-taskArn"></a>
The Amazon Resource Name (ARN) of the Amazon ECS task that's associated with the container job. Each container attempt receives a task ARN when they reach the `STARTING` status.  
Type: String  
Required: No

 ** ulimits **   <a name="Batch-Type-ContainerDetail-ulimits"></a>
A list of `ulimit` values to set in the container. This parameter maps to `Ulimits` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--ulimit` option to [docker run](https://docs.docker.com/engine/reference/run/).  
This parameter isn't applicable to jobs that are running on Fargate resources.
Type: Array of [Ulimit](API_Ulimit.md) objects  
Required: No

 ** user **   <a name="Batch-Type-ContainerDetail-user"></a>
The user name to use inside the container. This parameter maps to `User` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--user` option to [docker run](https://docs.docker.com/engine/reference/run/).  
Type: String  
Required: No

 ** vcpus **   <a name="Batch-Type-ContainerDetail-vcpus"></a>
The number of vCPUs reserved for the container. For jobs that run on Amazon EC2 resources, you can specify the vCPU requirement for the job using `resourceRequirements`, but you can't specify the vCPU requirements in both the `vcpus` and `resourceRequirements` object. This parameter maps to `CpuShares` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--cpu-shares` option to [docker run](https://docs.docker.com/engine/reference/run/). Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU. This is required but can be specified in several places. It must be specified for each node at least once.  
This parameter isn't applicable to jobs that run on Fargate resources. For jobs that run on Fargate resources, you must specify the vCPU requirement for the job using `resourceRequirements`.
Type: Integer  
Required: No

 ** volumes **   <a name="Batch-Type-ContainerDetail-volumes"></a>
A list of volumes that are associated with the job.  
Type: Array of [Volume](API_Volume.md) objects  
Required: No

## See Also
<a name="API_ContainerDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ContainerDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ContainerDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ContainerDetail) 