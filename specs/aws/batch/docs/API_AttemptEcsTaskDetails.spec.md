---
id: "@specs/aws/batch/docs/API_AttemptEcsTaskDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttemptEcsTaskDetails"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# AttemptEcsTaskDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_AttemptEcsTaskDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttemptEcsTaskDetails
<a name="API_AttemptEcsTaskDetails"></a>

An object that represents the details of a task.

## Contents
<a name="API_AttemptEcsTaskDetails_Contents"></a>

 ** containerInstanceArn **   <a name="Batch-Type-AttemptEcsTaskDetails-containerInstanceArn"></a>
The Amazon Resource Name (ARN) of the container instance that hosts the task.  
Type: String  
Required: No

 ** containers **   <a name="Batch-Type-AttemptEcsTaskDetails-containers"></a>
A list of containers that are included in the `taskProperties` list.  
Type: Array of [AttemptTaskContainerDetails](API_AttemptTaskContainerDetails.md) objects  
Required: No

 ** taskArn **   <a name="Batch-Type-AttemptEcsTaskDetails-taskArn"></a>
The ARN of the Amazon ECS task.  
Type: String  
Required: No

## See Also
<a name="API_AttemptEcsTaskDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/AttemptEcsTaskDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/AttemptEcsTaskDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/AttemptEcsTaskDetails) 