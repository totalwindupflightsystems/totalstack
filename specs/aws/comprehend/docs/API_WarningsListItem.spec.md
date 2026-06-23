---
id: "@specs/aws/comprehend/docs/API_WarningsListItem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS WarningsListItem"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# WarningsListItem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_WarningsListItem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# WarningsListItem
<a name="API_WarningsListItem"></a>

The system identified one of the following warnings while processing the input document:
+ The document to classify is plain text, but the classifier is a native document model.
+ The document to classify is semi-structured, but the classifier is a plain-text model.

## Contents
<a name="API_WarningsListItem_Contents"></a>

 ** Page **   <a name="comprehend-Type-WarningsListItem-Page"></a>
Page number in the input document.  
Type: Integer  
Required: No

 ** WarnCode **   <a name="comprehend-Type-WarningsListItem-WarnCode"></a>
The type of warning.  
Type: String  
Valid Values: `INFERENCING_PLAINTEXT_WITH_NATIVE_TRAINED_MODEL | INFERENCING_NATIVE_DOCUMENT_WITH_PLAINTEXT_TRAINED_MODEL`   
Required: No

 ** WarnMessage **   <a name="comprehend-Type-WarningsListItem-WarnMessage"></a>
Text message associated with the warning.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## See Also
<a name="API_WarningsListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/WarningsListItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/WarningsListItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/WarningsListItem) 