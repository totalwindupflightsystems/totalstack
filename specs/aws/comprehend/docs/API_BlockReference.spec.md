---
id: "@specs/aws/comprehend/docs/API_BlockReference"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BlockReference"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# BlockReference

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_BlockReference
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BlockReference
<a name="API_BlockReference"></a>

A reference to a block. 

## Contents
<a name="API_BlockReference_Contents"></a>

 ** BeginOffset **   <a name="comprehend-Type-BlockReference-BeginOffset"></a>
Offset of the start of the block within its parent block.  
Type: Integer  
Required: No

 ** BlockId **   <a name="comprehend-Type-BlockReference-BlockId"></a>
Unique identifier for the block.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** ChildBlocks **   <a name="comprehend-Type-BlockReference-ChildBlocks"></a>
List of child blocks within this block.  
Type: Array of [ChildBlock](API_ChildBlock.md) objects  
Required: No

 ** EndOffset **   <a name="comprehend-Type-BlockReference-EndOffset"></a>
Offset of the end of the block within its parent block.  
Type: Integer  
Required: No

## See Also
<a name="API_BlockReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/BlockReference) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/BlockReference) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/BlockReference) 