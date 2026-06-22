---
id: "@specs/aws/batch/docs/API_NodeDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NodeDetails"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# NodeDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_NodeDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NodeDetails
<a name="API_NodeDetails"></a>

An object that represents the details of a multi-node parallel job node.

## Contents
<a name="API_NodeDetails_Contents"></a>

 ** isMainNode **   <a name="Batch-Type-NodeDetails-isMainNode"></a>
Specifies whether the current node is the main node for a multi-node parallel job.  
Type: Boolean  
Required: No

 ** nodeIndex **   <a name="Batch-Type-NodeDetails-nodeIndex"></a>
The node index for the node. Node index numbering starts at zero. This index is also available on the node with the `AWS_BATCH_JOB_NODE_INDEX` environment variable.  
Type: Integer  
Required: No

## See Also
<a name="API_NodeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/NodeDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/NodeDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/NodeDetails) 