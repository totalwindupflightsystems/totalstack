---
id: "@specs/aws/comprehend/docs/API_DocumentMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DocumentMetadata"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DocumentMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DocumentMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DocumentMetadata
<a name="API_DocumentMetadata"></a>

Information about the document, discovered during text extraction.

## Contents
<a name="API_DocumentMetadata_Contents"></a>

 ** ExtractedCharacters **   <a name="comprehend-Type-DocumentMetadata-ExtractedCharacters"></a>
List of pages in the document, with the number of characters extracted from each page.  
Type: Array of [ExtractedCharactersListItem](API_ExtractedCharactersListItem.md) objects  
Required: No

 ** Pages **   <a name="comprehend-Type-DocumentMetadata-Pages"></a>
Number of pages in the document.  
Type: Integer  
Required: No

## See Also
<a name="API_DocumentMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DocumentMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DocumentMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DocumentMetadata) 