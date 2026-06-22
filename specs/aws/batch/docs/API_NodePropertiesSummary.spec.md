---
id: "@specs/aws/batch/docs/API_NodePropertiesSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NodePropertiesSummary"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# NodePropertiesSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_NodePropertiesSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NodePropertiesSummary
<a name="API_NodePropertiesSummary"></a>

An object that represents the properties of a node that's associated with a multi-node parallel job.

## Contents
<a name="API_NodePropertiesSummary_Contents"></a>

 ** isMainNode **   <a name="Batch-Type-NodePropertiesSummary-isMainNode"></a>
Specifies whether the current node is the main node for a multi-node parallel job.  
Type: Boolean  
Required: No

 ** nodeIndex **   <a name="Batch-Type-NodePropertiesSummary-nodeIndex"></a>
The node index for the node. Node index numbering begins at zero. This index is also available on the node with the `AWS_BATCH_JOB_NODE_INDEX` environment variable.  
Type: Integer  
Required: No

 ** numNodes **   <a name="Batch-Type-NodePropertiesSummary-numNodes"></a>
The number of nodes that are associated with a multi-node parallel job.  
Type: Integer  
Required: No

## See Also
<a name="API_NodePropertiesSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/NodePropertiesSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/NodePropertiesSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/NodePropertiesSummary) 