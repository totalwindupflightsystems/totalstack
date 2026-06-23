---
id: "@specs/aws/comprehend/docs/API_ErrorsListItem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ErrorsListItem"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# ErrorsListItem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_ErrorsListItem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ErrorsListItem
<a name="API_ErrorsListItem"></a>

Text extraction encountered one or more page-level errors in the input document.

The `ErrorCode` contains one of the following values:
+ TEXTRACT\_BAD\_PAGE - Amazon Textract cannot read the page. For more information about page limits in Amazon Textract, see [ Page Quotas in Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/limits-document.html).
+ TEXTRACT\_PROVISIONED\_THROUGHPUT\_EXCEEDED - The number of requests exceeded your throughput limit. For more information about throughput quotas in Amazon Textract, see [ Default quotas in Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/limits-quotas-explained.html).
+ PAGE\_CHARACTERS\_EXCEEDED - Too many text characters on the page (10,000 characters maximum).
+ PAGE\_SIZE\_EXCEEDED - The maximum page size is 10 MB.
+ INTERNAL\_SERVER\_ERROR - The request encountered a service issue. Try the API request again.

## Contents
<a name="API_ErrorsListItem_Contents"></a>

 ** ErrorCode **   <a name="comprehend-Type-ErrorsListItem-ErrorCode"></a>
Error code for the cause of the error.  
Type: String  
Valid Values: `TEXTRACT_BAD_PAGE | TEXTRACT_PROVISIONED_THROUGHPUT_EXCEEDED | PAGE_CHARACTERS_EXCEEDED | PAGE_SIZE_EXCEEDED | INTERNAL_SERVER_ERROR`   
Required: No

 ** ErrorDocumentType **   <a name="comprehend-Type-ErrorsListItem-ErrorDocumentType"></a>
The type of the document associated with the error.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** ErrorMessage **   <a name="comprehend-Type-ErrorsListItem-ErrorMessage"></a>
Text message explaining the reason for the error.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** Page **   <a name="comprehend-Type-ErrorsListItem-Page"></a>
Page number where the error occurred.  
Type: Integer  
Required: No

## See Also
<a name="API_ErrorsListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/ErrorsListItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/ErrorsListItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/ErrorsListItem) 