---
id: "@specs/aws/batch/docs/API_NodeProperties"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NodeProperties"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# NodeProperties

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_NodeProperties
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NodeProperties
<a name="API_NodeProperties"></a>

An object that represents the node properties of a multi-node parallel job.

**Note**  
Node properties can't be specified for Amazon EKS based job definitions.

## Contents
<a name="API_NodeProperties_Contents"></a>

 ** mainNode **   <a name="Batch-Type-NodeProperties-mainNode"></a>
Specifies the node index for the main node of a multi-node parallel job. This node index value must be fewer than the number of nodes.  
Type: Integer  
Required: Yes

 ** nodeRangeProperties **   <a name="Batch-Type-NodeProperties-nodeRangeProperties"></a>
A list of node ranges and their properties that are associated with a multi-node parallel job.  
Type: Array of [NodeRangeProperty](API_NodeRangeProperty.md) objects  
Required: Yes

 ** numNodes **   <a name="Batch-Type-NodeProperties-numNodes"></a>
The number of nodes that are associated with a multi-node parallel job.  
Type: Integer  
Required: Yes

## See Also
<a name="API_NodeProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/NodeProperties) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/NodeProperties) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/NodeProperties) 