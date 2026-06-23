---
id: "@specs/aws/comprehend/docs/API_DocumentTypeListItem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DocumentTypeListItem"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DocumentTypeListItem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DocumentTypeListItem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DocumentTypeListItem
<a name="API_DocumentTypeListItem"></a>

Document type for each page in the document.

## Contents
<a name="API_DocumentTypeListItem_Contents"></a>

 ** Page **   <a name="comprehend-Type-DocumentTypeListItem-Page"></a>
Page number.  
Type: Integer  
Required: No

 ** Type **   <a name="comprehend-Type-DocumentTypeListItem-Type"></a>
Document type.  
Type: String  
Valid Values: `NATIVE_PDF | SCANNED_PDF | MS_WORD | IMAGE | PLAIN_TEXT | TEXTRACT_DETECT_DOCUMENT_TEXT_JSON | TEXTRACT_ANALYZE_DOCUMENT_JSON`   
Required: No

## See Also
<a name="API_DocumentTypeListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DocumentTypeListItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DocumentTypeListItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DocumentTypeListItem) 