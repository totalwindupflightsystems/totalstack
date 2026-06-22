---
id: "@specs/aws/batch/docs/API_JobQueueDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobQueueDetail"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# JobQueueDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_JobQueueDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobQueueDetail
<a name="API_JobQueueDetail"></a>

An object that represents the details for an AWS Batch job queue.

## Contents
<a name="API_JobQueueDetail_Contents"></a>

 ** computeEnvironmentOrder **   <a name="Batch-Type-JobQueueDetail-computeEnvironmentOrder"></a>
The compute environments that are attached to the job queue and the order that job placement is preferred. Compute environments are selected for job placement in ascending order.  
Type: Array of [ComputeEnvironmentOrder](API_ComputeEnvironmentOrder.md) objects  
Required: Yes

 ** jobQueueArn **   <a name="Batch-Type-JobQueueDetail-jobQueueArn"></a>
The Amazon Resource Name (ARN) of the job queue.  
Type: String  
Required: Yes

 ** jobQueueName **   <a name="Batch-Type-JobQueueDetail-jobQueueName"></a>
The job queue name.  
Type: String  
Required: Yes

 ** priority **   <a name="Batch-Type-JobQueueDetail-priority"></a>
The priority of the job queue. Job queue priority determines the order that job queues are evaluated when multiple queues dispatch jobs within a shared compute environment. A higher value for `priority` indicates a higher priority. Queues are evaluated in cycles, in descending order by priority. For example, a job queue with a priority value of `10` is evaluated before a queue with a priority value of `1`. All of the compute environments must be either Amazon EC2 (`EC2` or `SPOT`) or Fargate (`FARGATE` or `FARGATE_SPOT`). Amazon EC2 and Fargate compute environments can't be mixed.  
Job queue priority doesn't guarantee that a particular job executes before a job in a lower priority queue. Jobs added to higher priority queues during the queue evaluation cycle might not be evaluated until the next cycle. A job is dispatched from a queue only if resources are available when the queue is evaluated. If there are insufficient resources available at that time, the cycle proceeds to the next queue. This means that jobs added to higher priority queues might have to wait for jobs in multiple lower priority queues to complete before they are dispatched. You can use job dependencies to control the order for jobs from queues with different priorities. For more information, see [Job Dependencies](https://docs.aws.amazon.com/batch/latest/userguide/job_dependencies.html) in the * AWS Batch User Guide*.
Type: Integer  
Required: Yes

 ** state **   <a name="Batch-Type-JobQueueDetail-state"></a>
Describes the ability of the queue to accept new jobs. If the job queue state is `ENABLED`, it can accept jobs. If the job queue state is `DISABLED`, new jobs can't be added to the queue, but jobs already in the queue can finish.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: Yes

 ** jobQueueType **   <a name="Batch-Type-JobQueueDetail-jobQueueType"></a>
The type of job queue. For service jobs that run on SageMaker Training, this value is `SAGEMAKER_TRAINING`. For regular container jobs, this value is `EKS`, `ECS`, or `ECS_FARGATE` depending on the compute environment.  
Type: String  
Valid Values: `EKS | ECS | ECS_FARGATE | SAGEMAKER_TRAINING`   
Required: No

 ** jobStateTimeLimitActions **   <a name="Batch-Type-JobQueueDetail-jobStateTimeLimitActions"></a>
The set of actions that AWS Batch perform on jobs that remain at the head of the job queue in the specified state longer than specified times. AWS Batch will perform each action after `maxTimeSeconds` has passed.  
Type: Array of [JobStateTimeLimitAction](API_JobStateTimeLimitAction.md) objects  
Required: No

 ** schedulingPolicyArn **   <a name="Batch-Type-JobQueueDetail-schedulingPolicyArn"></a>
The Amazon Resource Name (ARN) of the scheduling policy. The format is `aws:Partition:batch:Region:Account:scheduling-policy/Name `. For example, `aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy`.  
Type: String  
Required: No

 ** serviceEnvironmentOrder **   <a name="Batch-Type-JobQueueDetail-serviceEnvironmentOrder"></a>
The order of the service environment associated with the job queue. Job queues with a higher priority are evaluated first when associated with the same service environment.  
Type: Array of [ServiceEnvironmentOrder](API_ServiceEnvironmentOrder.md) objects  
Required: No

 ** status **   <a name="Batch-Type-JobQueueDetail-status"></a>
The status of the job queue (for example, `CREATING` or `VALID`).  
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | DELETED | VALID | INVALID`   
Required: No

 ** statusReason **   <a name="Batch-Type-JobQueueDetail-statusReason"></a>
A short, human-readable string to provide additional details for the current status of the job queue.  
Type: String  
Required: No

 ** tags **   <a name="Batch-Type-JobQueueDetail-tags"></a>
The tags that are applied to the job queue. For more information, see [Tagging your AWS Batch resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html) in * AWS Batch User Guide*.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

## See Also
<a name="API_JobQueueDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/JobQueueDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/JobQueueDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/JobQueueDetail) 