---
id: "@specs/aws/comprehend/docs/API_RelationshipsListItem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RelationshipsListItem"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# RelationshipsListItem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_RelationshipsListItem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RelationshipsListItem
<a name="API_RelationshipsListItem"></a>

List of child blocks for the current block.

## Contents
<a name="API_RelationshipsListItem_Contents"></a>

 ** Ids **   <a name="comprehend-Type-RelationshipsListItem-Ids"></a>
Identifers of the child blocks.  
Type: Array of strings  
Length Constraints: Minimum length of 1.  
Required: No

 ** Type **   <a name="comprehend-Type-RelationshipsListItem-Type"></a>
Only supported relationship is a child relationship.  
Type: String  
Valid Values: `CHILD`   
Required: No

## See Also
<a name="API_RelationshipsListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/RelationshipsListItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/RelationshipsListItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/RelationshipsListItem) 