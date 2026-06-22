---
id: "@specs/aws/batch/docs/API_EcsTaskProperties"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EcsTaskProperties"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EcsTaskProperties

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EcsTaskProperties
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EcsTaskProperties
<a name="API_EcsTaskProperties"></a>

The properties for a task definition that describes the container and volume definitions of an Amazon ECS task. You can specify which Docker images to use, the required resources, and other configurations related to launching the task definition through an Amazon ECS service or task.

## Contents
<a name="API_EcsTaskProperties_Contents"></a>

 ** containers **   <a name="Batch-Type-EcsTaskProperties-containers"></a>
This object is a list of containers.  
Type: Array of [TaskContainerProperties](API_TaskContainerProperties.md) objects  
Required: Yes

 ** enableExecuteCommand **   <a name="Batch-Type-EcsTaskProperties-enableExecuteCommand"></a>
Determines whether execute command functionality is turned on for this task. If `true`, execute command functionality is turned on all the containers in the task.  
Type: Boolean  
Required: No

 ** ephemeralStorage **   <a name="Batch-Type-EcsTaskProperties-ephemeralStorage"></a>
The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate.  
Type: [EphemeralStorage](API_EphemeralStorage.md) object  
Required: No

 ** executionRoleArn **   <a name="Batch-Type-EcsTaskProperties-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the execution role that AWS Batch can assume. For jobs that run on Fargate resources, you must provide an execution role. For more information, see [AWS Batch execution IAM role](https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html) in the * AWS Batch User Guide*.  
Type: String  
Required: No

 ** ipcMode **   <a name="Batch-Type-EcsTaskProperties-ipcMode"></a>
The IPC resource namespace to use for the containers in the task. The valid values are `host`, `task`, or `none`.  
If `host` is specified, all containers within the tasks that specified the `host` IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance.  
If `task` is specified, all containers within the specified `task` share the same IPC resources.  
If `none` is specified, the IPC resources within the containers of a task are private, and are not shared with other containers in a task or on the container instance.   
If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance. For more information, see [IPC settings](https://docs.docker.com/engine/reference/run/#ipc-settings---ipc) in the Docker run reference.  
Type: String  
Required: No

 ** networkConfiguration **   <a name="Batch-Type-EcsTaskProperties-networkConfiguration"></a>
The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.  
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object  
Required: No

 ** pidMode **   <a name="Batch-Type-EcsTaskProperties-pidMode"></a>
The process namespace to use for the containers in the task. The valid values are `host` or `task`. For example, monitoring sidecars might need `pidMode` to access information about other containers running in the same task.  
If `host` is specified, all containers within the tasks that specified the `host` PID mode on the same container instance share the process namespace with the host Amazon EC2 instance.  
If `task` is specified, all containers within the specified task share the same process namespace.  
If no value is specified, the default is a private namespace for each container. For more information, see [PID settings](https://docs.docker.com/engine/reference/run/#pid-settings---pid) in the Docker run reference.  
Type: String  
Required: No

 ** platformVersion **   <a name="Batch-Type-EcsTaskProperties-platformVersion"></a>
The Fargate platform version where the jobs are running. A platform version is specified only for jobs that are running on Fargate resources. If one isn't specified, the `LATEST` platform version is used by default. This uses a recent, approved version of the Fargate platform for compute resources. For more information, see [AWS Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide*.  
Type: String  
Required: No

 ** runtimePlatform **   <a name="Batch-Type-EcsTaskProperties-runtimePlatform"></a>
An object that represents the compute environment architecture for AWS Batch jobs on Fargate.  
Type: [RuntimePlatform](API_RuntimePlatform.md) object  
Required: No

 ** taskRoleArn **   <a name="Batch-Type-EcsTaskProperties-taskRoleArn"></a>
The Amazon Resource Name (ARN) that's associated with the Amazon ECS task.  
This is object is comparable to [ContainerProperties:jobRoleArn](https://docs.aws.amazon.com/batch/latest/APIReference/API_ContainerProperties.html).
Type: String  
Required: No

 ** volumes **   <a name="Batch-Type-EcsTaskProperties-volumes"></a>
A list of volumes that are associated with the job.  
Type: Array of [Volume](API_Volume.md) objects  
Required: No

## See Also
<a name="API_EcsTaskProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EcsTaskProperties) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EcsTaskProperties) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EcsTaskProperties) 