---
id: "@specs/aws/kendra/docs/API_BatchPutDocumentResponseFailedDocument"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BatchPutDocumentResponseFailedDocument"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# BatchPutDocumentResponseFailedDocument

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_BatchPutDocumentResponseFailedDocument
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BatchPutDocumentResponseFailedDocument
<a name="API_BatchPutDocumentResponseFailedDocument"></a>

Provides information about a document that could not be indexed.

## Contents
<a name="API_BatchPutDocumentResponseFailedDocument_Contents"></a>

 ** DataSourceId **   <a name="kendra-Type-BatchPutDocumentResponseFailedDocument-DataSourceId"></a>
 The identifier of the data source connector that the failed document belongs to.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`   
Required: No

 ** ErrorCode **   <a name="kendra-Type-BatchPutDocumentResponseFailedDocument-ErrorCode"></a>
The type of error that caused the document to fail to be indexed.  
Type: String  
Valid Values: `InternalError | InvalidRequest`   
Required: No

 ** ErrorMessage **   <a name="kendra-Type-BatchPutDocumentResponseFailedDocument-ErrorMessage"></a>
A description of the reason why the document could not be indexed.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^\P{C}*$`   
Required: No

 ** Id **   <a name="kendra-Type-BatchPutDocumentResponseFailedDocument-Id"></a>
The identifier of the document.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_BatchPutDocumentResponseFailedDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/BatchPutDocumentResponseFailedDocument) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/BatchPutDocumentResponseFailedDocument) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/BatchPutDocumentResponseFailedDocument) 