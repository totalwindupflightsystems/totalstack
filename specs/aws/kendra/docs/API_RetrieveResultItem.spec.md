---
id: "@specs/aws/kendra/docs/API_RetrieveResultItem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RetrieveResultItem"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# RetrieveResultItem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_RetrieveResultItem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RetrieveResultItem
<a name="API_RetrieveResultItem"></a>

A single retrieved relevant passage result.

## Contents
<a name="API_RetrieveResultItem_Contents"></a>

 ** Content **   <a name="kendra-Type-RetrieveResultItem-Content"></a>
The contents of the relevant passage.  
Type: String  
Required: No

 ** DocumentAttributes **   <a name="kendra-Type-RetrieveResultItem-DocumentAttributes"></a>
An array of document fields/attributes assigned to a document in the search results. For example, the document author (`_author`) or the source URI (`_source_uri`) of the document.  
Type: Array of [DocumentAttribute](API_DocumentAttribute.md) objects  
Required: No

 ** DocumentId **   <a name="kendra-Type-RetrieveResultItem-DocumentId"></a>
The identifier of the document.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** DocumentTitle **   <a name="kendra-Type-RetrieveResultItem-DocumentTitle"></a>
The title of the document.  
Type: String  
Required: No

 ** DocumentURI **   <a name="kendra-Type-RetrieveResultItem-DocumentURI"></a>
The URI of the original location of the document.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^(https?|ftp|file):\/\/([^\s]*)`   
Required: No

 ** Id **   <a name="kendra-Type-RetrieveResultItem-Id"></a>
The identifier of the relevant passage result.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 73.  
Required: No

 ** ScoreAttributes **   <a name="kendra-Type-RetrieveResultItem-ScoreAttributes"></a>
The confidence score bucket for a retrieved passage result. The confidence bucket provides a relative ranking that indicates how confident Amazon Kendra is that the response is relevant to the query.  
Type: [ScoreAttributes](API_ScoreAttributes.md) object  
Required: No

## See Also
<a name="API_RetrieveResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/RetrieveResultItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/RetrieveResultItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/RetrieveResultItem) 