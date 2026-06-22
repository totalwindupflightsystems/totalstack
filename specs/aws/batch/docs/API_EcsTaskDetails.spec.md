---
id: "@specs/aws/batch/docs/API_EcsTaskDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EcsTaskDetails"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EcsTaskDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EcsTaskDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EcsTaskDetails
<a name="API_EcsTaskDetails"></a>

The details of a task definition that describes the container and volume definitions of an Amazon ECS task.

## Contents
<a name="API_EcsTaskDetails_Contents"></a>

 ** containerInstanceArn **   <a name="Batch-Type-EcsTaskDetails-containerInstanceArn"></a>
The Amazon Resource Name (ARN) of the container instance that hosts the task.  
Type: String  
Required: No

 ** containers **   <a name="Batch-Type-EcsTaskDetails-containers"></a>
A list of containers that are included in the `taskProperties` list.  
Type: Array of [TaskContainerDetails](API_TaskContainerDetails.md) objects  
Required: No

 ** enableExecuteCommand **   <a name="Batch-Type-EcsTaskDetails-enableExecuteCommand"></a>
Determines whether execute command functionality is turned on for this task. If `true`, execute command functionality is turned on all the containers in the task.  
Type: Boolean  
Required: No

 ** ephemeralStorage **   <a name="Batch-Type-EcsTaskDetails-ephemeralStorage"></a>
The amount of ephemeral storage allocated for the task.  
Type: [EphemeralStorage](API_EphemeralStorage.md) object  
Required: No

 ** executionRoleArn **   <a name="Batch-Type-EcsTaskDetails-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the execution role that AWS Batch can assume. For more information, see [Batch execution IAM role](https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html) in the * AWS Batch User Guide*.  
Type: String  
Required: No

 ** ipcMode **   <a name="Batch-Type-EcsTaskDetails-ipcMode"></a>
The IPC resource namespace to use for the containers in the task. The valid values are `host`, `task`, or `none`. For more information see `ipcMode` in [EcsTaskProperties](https://docs.aws.amazon.com/batch/latest/APIReference/API_EcsTaskProperties.html).  
Type: String  
Required: No

 ** networkConfiguration **   <a name="Batch-Type-EcsTaskDetails-networkConfiguration"></a>
The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.  
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object  
Required: No

 ** pidMode **   <a name="Batch-Type-EcsTaskDetails-pidMode"></a>
The process namespace to use for the containers in the task. The valid values are `host`, or `task`. For more information see `pidMode` in [EcsTaskProperties](https://docs.aws.amazon.com/batch/latest/APIReference/API_EcsTaskProperties.html).  
Type: String  
Required: No

 ** platformVersion **   <a name="Batch-Type-EcsTaskDetails-platformVersion"></a>
The Fargate platform version where the jobs are running.  
Type: String  
Required: No

 ** runtimePlatform **   <a name="Batch-Type-EcsTaskDetails-runtimePlatform"></a>
An object that represents the compute environment architecture for AWS Batch jobs on Fargate.  
Type: [RuntimePlatform](API_RuntimePlatform.md) object  
Required: No

 ** taskArn **   <a name="Batch-Type-EcsTaskDetails-taskArn"></a>
The ARN of the Amazon ECS task.  
Type: String  
Required: No

 ** taskRoleArn **   <a name="Batch-Type-EcsTaskDetails-taskRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions. For more information, see [IAM roles for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.  
This is object is comparable to [ContainerProperties:jobRoleArn](https://docs.aws.amazon.com/batch/latest/APIReference/API_ContainerProperties.html).
Type: String  
Required: No

 ** volumes **   <a name="Batch-Type-EcsTaskDetails-volumes"></a>
A list of data volumes used in a job.  
Type: Array of [Volume](API_Volume.md) objects  
Required: No

## See Also
<a name="API_EcsTaskDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EcsTaskDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EcsTaskDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EcsTaskDetails) 