---
id: "@specs/aws/batch/docs/API_AttemptContainerDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttemptContainerDetail"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# AttemptContainerDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_AttemptContainerDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttemptContainerDetail
<a name="API_AttemptContainerDetail"></a>

An object that represents the details of a container that's part of a job attempt.

## Contents
<a name="API_AttemptContainerDetail_Contents"></a>

 ** containerInstanceArn **   <a name="Batch-Type-AttemptContainerDetail-containerInstanceArn"></a>
The Amazon Resource Name (ARN) of the Amazon ECS container instance that hosts the job attempt.  
Type: String  
Required: No

 ** exitCode **   <a name="Batch-Type-AttemptContainerDetail-exitCode"></a>
The exit code for the job attempt. A non-zero exit code is considered failed.  
Type: Integer  
Required: No

 ** logStreamName **   <a name="Batch-Type-AttemptContainerDetail-logStreamName"></a>
The name of the CloudWatch Logs log stream that's associated with the container. The log group for AWS Batch jobs is `/aws/batch/job`. Each container attempt receives a log stream name when they reach the `RUNNING` status.  
Type: String  
Required: No

 ** networkInterfaces **   <a name="Batch-Type-AttemptContainerDetail-networkInterfaces"></a>
The network interfaces that are associated with the job attempt.  
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects  
Required: No

 ** reason **   <a name="Batch-Type-AttemptContainerDetail-reason"></a>
A short (255 max characters) human-readable string to provide additional details for a running or stopped container.  
Type: String  
Required: No

 ** taskArn **   <a name="Batch-Type-AttemptContainerDetail-taskArn"></a>
The Amazon Resource Name (ARN) of the Amazon ECS task that's associated with the job attempt. Each container attempt receives a task ARN when they reach the `STARTING` status.  
Type: String  
Required: No

## See Also
<a name="API_AttemptContainerDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/AttemptContainerDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/AttemptContainerDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/AttemptContainerDetail) 