---
id: "@specs/aws/batch/docs/API_NodeOverrides"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NodeOverrides"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# NodeOverrides

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_NodeOverrides
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NodeOverrides
<a name="API_NodeOverrides"></a>

An object that represents any node overrides to a job definition that's used in a [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) API operation.

**Note**  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs. Rather, use `containerOverrides` instead.

## Contents
<a name="API_NodeOverrides_Contents"></a>

 ** nodePropertyOverrides **   <a name="Batch-Type-NodeOverrides-nodePropertyOverrides"></a>
The node property overrides for the job.  
Type: Array of [NodePropertyOverride](API_NodePropertyOverride.md) objects  
Required: No

 ** numNodes **   <a name="Batch-Type-NodeOverrides-numNodes"></a>
The number of nodes to use with a multi-node parallel job. This value overrides the number of nodes that are specified in the job definition. To use this override, you must meet the following conditions:  
+ There must be at least one node range in your job definition that has an open upper boundary, such as `:` or `n:`.
+ The lower boundary of the node range that's specified in the job definition must be fewer than the number of nodes specified in the override.
+ The main node index that's specified in the job definition must be fewer than the number of nodes specified in the override.
Type: Integer  
Required: No

## See Also
<a name="API_NodeOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/NodeOverrides) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/NodeOverrides) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/NodeOverrides) 