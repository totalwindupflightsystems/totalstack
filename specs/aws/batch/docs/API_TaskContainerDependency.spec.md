---
id: "@specs/aws/batch/docs/API_TaskContainerDependency"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TaskContainerDependency"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# TaskContainerDependency

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_TaskContainerDependency
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TaskContainerDependency
<a name="API_TaskContainerDependency"></a>

A list of containers that this task depends on.

## Contents
<a name="API_TaskContainerDependency_Contents"></a>

 ** condition **   <a name="Batch-Type-TaskContainerDependency-condition"></a>
The dependency condition of the container. The following are the available conditions and their behavior:  
+  `START` - This condition emulates the behavior of links and volumes today. It validates that a dependent container is started before permitting other containers to start. 
+  `COMPLETE` - This condition validates that a dependent container runs to completion (exits) before permitting other containers to start. This can be useful for nonessential containers that run a script and then exit. This condition can't be set on an essential container. 
+  `SUCCESS` - This condition is the same as `COMPLETE`, but it also requires that the container exits with a zero status. This condition can't be set on an essential container. 
Type: String  
Required: No

 ** containerName **   <a name="Batch-Type-TaskContainerDependency-containerName"></a>
A unique identifier for the container.  
Type: String  
Required: No

## See Also
<a name="API_TaskContainerDependency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/TaskContainerDependency) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/TaskContainerDependency) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/TaskContainerDependency) 