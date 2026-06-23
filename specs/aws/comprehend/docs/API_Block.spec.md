---
id: "@specs/aws/comprehend/docs/API_Block"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Block"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# Block

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_Block
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Block
<a name="API_Block"></a>

Information about each word or line of text in the input document.

For additional information, see [Block](https://docs.aws.amazon.com/textract/latest/dg/API_Block.html) in the Amazon Textract API reference.

## Contents
<a name="API_Block_Contents"></a>

 ** BlockType **   <a name="comprehend-Type-Block-BlockType"></a>
The block represents a line of text or one word of text.  
+ WORD - A word that's detected on a document page. A word is one or more ISO basic Latin script characters that aren't separated by spaces.
+ LINE - A string of tab-delimited, contiguous words that are detected on a document page
Type: String  
Valid Values: `LINE | WORD`   
Required: No

 ** Geometry **   <a name="comprehend-Type-Block-Geometry"></a>
Co-ordinates of the rectangle or polygon that contains the text.  
Type: [Geometry](API_Geometry.md) object  
Required: No

 ** Id **   <a name="comprehend-Type-Block-Id"></a>
Unique identifier for the block.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** Page **   <a name="comprehend-Type-Block-Page"></a>
Page number where the block appears.  
Type: Integer  
Required: No

 ** Relationships **   <a name="comprehend-Type-Block-Relationships"></a>
A list of child blocks of the current block. For example, a LINE object has child blocks for each WORD block that's part of the line of text.   
Type: Array of [RelationshipsListItem](API_RelationshipsListItem.md) objects  
Required: No

 ** Text **   <a name="comprehend-Type-Block-Text"></a>
The word or line of text extracted from the block.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## See Also
<a name="API_Block_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/Block) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/Block) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/Block) 