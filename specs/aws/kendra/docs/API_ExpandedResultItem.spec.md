---
id: "@specs/aws/kendra/docs/API_ExpandedResultItem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExpandedResultItem"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# ExpandedResultItem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_ExpandedResultItem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExpandedResultItem
<a name="API_ExpandedResultItem"></a>

 A single expanded result in a collapsed group of search results.

An expanded result item contains information about an expanded result document within a collapsed group of search results. This includes the original location of the document, a list of attributes assigned to the document, and relevant text from the document that satisfies the query. 

## Contents
<a name="API_ExpandedResultItem_Contents"></a>

 ** DocumentAttributes **   <a name="kendra-Type-ExpandedResultItem-DocumentAttributes"></a>
An array of document attributes assigned to a document in the search results. For example, the document author ("\_author") or the source URI ("\_source\_uri") of the document.  
Type: Array of [DocumentAttribute](API_DocumentAttribute.md) objects  
Required: No

 ** DocumentExcerpt **   <a name="kendra-Type-ExpandedResultItem-DocumentExcerpt"></a>
Provides text and information about where to highlight the text.  
Type: [TextWithHighlights](API_TextWithHighlights.md) object  
Required: No

 ** DocumentId **   <a name="kendra-Type-ExpandedResultItem-DocumentId"></a>
The idenitifier of the document.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** DocumentTitle **   <a name="kendra-Type-ExpandedResultItem-DocumentTitle"></a>
Provides text and information about where to highlight the text.  
Type: [TextWithHighlights](API_TextWithHighlights.md) object  
Required: No

 ** DocumentURI **   <a name="kendra-Type-ExpandedResultItem-DocumentURI"></a>
The URI of the original location of the document.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^(https?|ftp|file):\/\/([^\s]*)`   
Required: No

 ** Id **   <a name="kendra-Type-ExpandedResultItem-Id"></a>
The identifier for the expanded result.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 73.  
Required: No

## See Also
<a name="API_ExpandedResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/ExpandedResultItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/ExpandedResultItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/ExpandedResultItem) 