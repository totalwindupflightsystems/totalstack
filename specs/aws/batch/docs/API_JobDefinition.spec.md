---
id: "@specs/aws/batch/docs/API_JobDefinition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobDefinition"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# JobDefinition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_JobDefinition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobDefinition
<a name="API_JobDefinition"></a>

An object that represents an AWS Batch job definition.

## Contents
<a name="API_JobDefinition_Contents"></a>

 ** jobDefinitionArn **   <a name="Batch-Type-JobDefinition-jobDefinitionArn"></a>
The Amazon Resource Name (ARN) for the job definition.  
Type: String  
Required: Yes

 ** jobDefinitionName **   <a name="Batch-Type-JobDefinition-jobDefinitionName"></a>
The name of the job definition.  
Type: String  
Required: Yes

 ** revision **   <a name="Batch-Type-JobDefinition-revision"></a>
The revision of the job definition.  
Type: Integer  
Required: Yes

 ** type **   <a name="Batch-Type-JobDefinition-type"></a>
The type of job definition. It's either `container` or `multinode`. If the job is run on Fargate resources, then `multinode` isn't supported. For more information about multi-node parallel jobs, see [Creating a multi-node parallel job definition](https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html) in the * AWS Batch User Guide*.  
Type: String  
Required: Yes

 ** consumableResourceProperties **   <a name="Batch-Type-JobDefinition-consumableResourceProperties"></a>
Contains a list of consumable resources required by the job.  
Type: [ConsumableResourceProperties](API_ConsumableResourceProperties.md) object  
Required: No

 ** containerOrchestrationType **   <a name="Batch-Type-JobDefinition-containerOrchestrationType"></a>
The orchestration type of the compute environment. The valid values are `ECS` (default) or `EKS`.  
Type: String  
Valid Values: `ECS | EKS`   
Required: No

 ** containerProperties **   <a name="Batch-Type-JobDefinition-containerProperties"></a>
An object with properties specific to Amazon ECS-based jobs. When `containerProperties` is used in the job definition, it can't be used in addition to `eksProperties`, `ecsProperties`, or `nodeProperties`.  
Type: [ContainerProperties](API_ContainerProperties.md) object  
Required: No

 ** ecsProperties **   <a name="Batch-Type-JobDefinition-ecsProperties"></a>
An object that contains the properties for the Amazon ECS resources of a job.When `ecsProperties` is used in the job definition, it can't be used in addition to `containerProperties`, `eksProperties`, or `nodeProperties`.  
Type: [EcsProperties](API_EcsProperties.md) object  
Required: No

 ** eksProperties **   <a name="Batch-Type-JobDefinition-eksProperties"></a>
An object with properties that are specific to Amazon EKS-based jobs. When `eksProperties` is used in the job definition, it can't be used in addition to `containerProperties`, `ecsProperties`, or `nodeProperties`.  
Type: [EksProperties](API_EksProperties.md) object  
Required: No

 ** nodeProperties **   <a name="Batch-Type-JobDefinition-nodeProperties"></a>
An object with properties that are specific to multi-node parallel jobs. When `nodeProperties` is used in the job definition, it can't be used in addition to `containerProperties`, `ecsProperties`, or `eksProperties`.  
If the job runs on Fargate resources, don't specify `nodeProperties`. Use `containerProperties` instead.
Type: [NodeProperties](API_NodeProperties.md) object  
Required: No

 ** parameters **   <a name="Batch-Type-JobDefinition-parameters"></a>
Default parameters or parameter substitution placeholders that are set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a `SubmitJob` request override any corresponding parameter defaults from the job definition. For more information about specifying parameters, see [Job definition parameters](https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html) in the * AWS Batch User Guide*.  
Type: String to string map  
Required: No

 ** platformCapabilities **   <a name="Batch-Type-JobDefinition-platformCapabilities"></a>
The platform capabilities required by the job definition. If no value is specified, it defaults to `EC2`. Jobs run on Fargate resources specify `FARGATE`.  
Type: Array of strings  
Valid Values: `EC2 | FARGATE`   
Required: No

 ** propagateTags **   <a name="Batch-Type-JobDefinition-propagateTags"></a>
Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks when the tasks are created. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the `FAILED` state.  
Type: Boolean  
Required: No

 ** retryStrategy **   <a name="Batch-Type-JobDefinition-retryStrategy"></a>
The retry strategy to use for failed jobs that are submitted with this job definition.  
Type: [RetryStrategy](API_RetryStrategy.md) object  
Required: No

 ** schedulingPriority **   <a name="Batch-Type-JobDefinition-schedulingPriority"></a>
The scheduling priority of the job definition. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.  
Type: Integer  
Required: No

 ** status **   <a name="Batch-Type-JobDefinition-status"></a>
The status of the job definition.  
Type: String  
Required: No

 ** tags **   <a name="Batch-Type-JobDefinition-tags"></a>
The tags that are applied to the job definition.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** timeout **   <a name="Batch-Type-JobDefinition-timeout"></a>
The timeout time for jobs that are submitted with this job definition. After the amount of time you specify passes, AWS Batch terminates your jobs if they aren't finished.  
Type: [JobTimeout](API_JobTimeout.md) object  
Required: No

## See Also
<a name="API_JobDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/JobDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/JobDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/JobDefinition) 