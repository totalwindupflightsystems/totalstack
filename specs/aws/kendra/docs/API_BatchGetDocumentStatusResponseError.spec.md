---
id: "@specs/aws/kendra/docs/API_BatchGetDocumentStatusResponseError"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BatchGetDocumentStatusResponseError"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# BatchGetDocumentStatusResponseError

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_BatchGetDocumentStatusResponseError
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BatchGetDocumentStatusResponseError
<a name="API_BatchGetDocumentStatusResponseError"></a>

Provides a response when the status of a document could not be retrieved.

## Contents
<a name="API_BatchGetDocumentStatusResponseError_Contents"></a>

 ** DataSourceId **   <a name="kendra-Type-BatchGetDocumentStatusResponseError-DataSourceId"></a>
 The identifier of the data source connector that the failed document belongs to.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`   
Required: No

 ** DocumentId **   <a name="kendra-Type-BatchGetDocumentStatusResponseError-DocumentId"></a>
The identifier of the document whose status could not be retrieved.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** ErrorCode **   <a name="kendra-Type-BatchGetDocumentStatusResponseError-ErrorCode"></a>
Indicates the source of the error.  
Type: String  
Valid Values: `InternalError | InvalidRequest`   
Required: No

 ** ErrorMessage **   <a name="kendra-Type-BatchGetDocumentStatusResponseError-ErrorMessage"></a>
States that the API could not get the status of a document. This could be because the request is not valid or there is a system error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^\P{C}*$`   
Required: No

## See Also
<a name="API_BatchGetDocumentStatusResponseError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/BatchGetDocumentStatusResponseError) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/BatchGetDocumentStatusResponseError) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/BatchGetDocumentStatusResponseError) 