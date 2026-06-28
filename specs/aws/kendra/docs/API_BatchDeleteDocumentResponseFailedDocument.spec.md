---
id: "@specs/aws/kendra/docs/API_BatchDeleteDocumentResponseFailedDocument"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BatchDeleteDocumentResponseFailedDocument"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# BatchDeleteDocumentResponseFailedDocument

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_BatchDeleteDocumentResponseFailedDocument
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BatchDeleteDocumentResponseFailedDocument
<a name="API_BatchDeleteDocumentResponseFailedDocument"></a>

Provides information about documents that could not be removed from an index by the `BatchDeleteDocument` API.

## Contents
<a name="API_BatchDeleteDocumentResponseFailedDocument_Contents"></a>

 ** DataSourceId **   <a name="kendra-Type-BatchDeleteDocumentResponseFailedDocument-DataSourceId"></a>
 The identifier of the data source connector that the document belongs to.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`   
Required: No

 ** ErrorCode **   <a name="kendra-Type-BatchDeleteDocumentResponseFailedDocument-ErrorCode"></a>
The error code for why the document couldn't be removed from the index.  
Type: String  
Valid Values: `InternalError | InvalidRequest`   
Required: No

 ** ErrorMessage **   <a name="kendra-Type-BatchDeleteDocumentResponseFailedDocument-ErrorMessage"></a>
An explanation for why the document couldn't be removed from the index.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^\P{C}*$`   
Required: No

 ** Id **   <a name="kendra-Type-BatchDeleteDocumentResponseFailedDocument-Id"></a>
The identifier of the document that couldn't be removed from the index.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_BatchDeleteDocumentResponseFailedDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/BatchDeleteDocumentResponseFailedDocument) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/BatchDeleteDocumentResponseFailedDocument) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/BatchDeleteDocumentResponseFailedDocument) 