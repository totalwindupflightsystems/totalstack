---
id: "@specs/aws/kendra/docs/API_Document"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Document"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# Document

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_Document
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Document
<a name="API_Document"></a>

A document in an index.

## Contents
<a name="API_Document_Contents"></a>

 ** Id **   <a name="kendra-Type-Document-Id"></a>
A identifier of the document in the index.  
Note, each document ID must be unique per index. You cannot create a data source to index your documents with their unique IDs and then use the `BatchPutDocument` API to index the same documents, or vice versa. You can delete a data source and then use the `BatchPutDocument` API to index the same documents, or vice versa.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

 ** AccessControlConfigurationId **   <a name="kendra-Type-Document-AccessControlConfigurationId"></a>
The identifier of the access control configuration that you want to apply to the document.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `[a-zA-Z0-9-]+`   
Required: No

 ** AccessControlList **   <a name="kendra-Type-Document-AccessControlList"></a>
Information on principals (users and/or groups) and which documents they should have access to. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.  
Type: Array of [Principal](API_Principal.md) objects  
Required: No

 ** Attributes **   <a name="kendra-Type-Document-Attributes"></a>
Custom attributes to apply to the document. Use the custom attributes to provide additional information for searching, to provide facets for refining searches, and to provide additional information in the query response.  
For example, 'DataSourceId' and 'DataSourceSyncJobId' are custom attributes that provide information on the synchronization of documents running on a data source. Note, 'DataSourceSyncJobId' could be an optional custom attribute as Amazon Kendra will use the ID of a running sync job.  
Type: Array of [DocumentAttribute](API_DocumentAttribute.md) objects  
Required: No

 ** Blob **   <a name="kendra-Type-Document-Blob"></a>
The contents of the document.   
Documents passed to the `Blob` parameter must be base64 encoded. Your code might not need to encode the document file bytes if you're using an AWS SDK to call Amazon Kendra APIs. If you are calling the Amazon Kendra endpoint directly using REST, you must base64 encode the contents before sending.  
Type: Base64-encoded binary data object  
Required: No

 ** ContentType **   <a name="kendra-Type-Document-ContentType"></a>
The file type of the document in the `Blob` field.  
If you want to index snippets or subsets of HTML documents instead of the entirety of the HTML documents, you must add the `HTML` start and closing tags (`<HTML>content</HTML>`) around the content.  
Type: String  
Valid Values: `PDF | HTML | MS_WORD | PLAIN_TEXT | PPT | RTF | XML | XSLT | MS_EXCEL | CSV | JSON | MD`   
Required: No

 ** HierarchicalAccessControlList **   <a name="kendra-Type-Document-HierarchicalAccessControlList"></a>
The list of [principal](https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html) lists that define the hierarchy for which documents users should have access to.  
Type: Array of [HierarchicalPrincipal](API_HierarchicalPrincipal.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 30 items.  
Required: No

 ** S3Path **   <a name="kendra-Type-Document-S3Path"></a>
Information required to find a specific file in an Amazon S3 bucket.  
Type: [S3Path](API_S3Path.md) object  
Required: No

 ** Title **   <a name="kendra-Type-Document-Title"></a>
The title of the document.  
Type: String  
Required: No

## See Also
<a name="API_Document_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/Document) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/Document) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/Document) 