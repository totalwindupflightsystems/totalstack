---
id: "@specs/aws/batch/docs/API_AttemptTaskContainerDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttemptTaskContainerDetails"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# AttemptTaskContainerDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_AttemptTaskContainerDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttemptTaskContainerDetails
<a name="API_AttemptTaskContainerDetails"></a>

An object that represents the details of a container that's part of a job attempt.

## Contents
<a name="API_AttemptTaskContainerDetails_Contents"></a>

 ** exitCode **   <a name="Batch-Type-AttemptTaskContainerDetails-exitCode"></a>
The exit code for the container’s attempt. A non-zero exit code is considered failed.  
Type: Integer  
Required: No

 ** logStreamName **   <a name="Batch-Type-AttemptTaskContainerDetails-logStreamName"></a>
The name of the Amazon CloudWatch Logs log stream that's associated with the container. The log group for AWS Batch jobs is `/aws/batch/job`. Each container attempt receives a log stream name when they reach the `RUNNING` status.  
Type: String  
Required: No

 ** name **   <a name="Batch-Type-AttemptTaskContainerDetails-name"></a>
The name of a container.  
Type: String  
Required: No

 ** networkInterfaces **   <a name="Batch-Type-AttemptTaskContainerDetails-networkInterfaces"></a>
The network interfaces that are associated with the job attempt.  
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects  
Required: No

 ** reason **   <a name="Batch-Type-AttemptTaskContainerDetails-reason"></a>
A short (255 max characters) string that's easy to understand and provides additional details for a running or stopped container.  
Type: String  
Required: No

## See Also
<a name="API_AttemptTaskContainerDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/AttemptTaskContainerDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/AttemptTaskContainerDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/AttemptTaskContainerDetails) 