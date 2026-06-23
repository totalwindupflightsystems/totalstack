---
id: "@specs/aws/comprehend/docs/API_InvalidRequestDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InvalidRequestDetail"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# InvalidRequestDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_InvalidRequestDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InvalidRequestDetail
<a name="API_InvalidRequestDetail"></a>

Provides additional detail about why the request failed.

## Contents
<a name="API_InvalidRequestDetail_Contents"></a>

 ** Reason **   <a name="comprehend-Type-InvalidRequestDetail-Reason"></a>
Reason codes include the following values:  
+ DOCUMENT\_SIZE\_EXCEEDED - Document size is too large. Check the size of your file and resubmit the request.
+ UNSUPPORTED\_DOC\_TYPE - Document type is not supported. Check the file type and resubmit the request.
+ PAGE\_LIMIT\_EXCEEDED - Too many pages in the document. Check the number of pages in your file and resubmit the request.
+ TEXTRACT\_ACCESS\_DENIED - Access denied to Amazon Textract. Verify that your account has permission to use Amazon Textract API operations and resubmit the request.
+ NOT\_TEXTRACT\_JSON - Document is not Amazon Textract JSON format. Verify the format and resubmit the request.
+ MISMATCHED\_TOTAL\_PAGE\_COUNT - Check the number of pages in your file and resubmit the request.
+ INVALID\_DOCUMENT - Invalid document. Check the file and resubmit the request.
Type: String  
Valid Values: `DOCUMENT_SIZE_EXCEEDED | UNSUPPORTED_DOC_TYPE | PAGE_LIMIT_EXCEEDED | TEXTRACT_ACCESS_DENIED | NOT_TEXTRACT_JSON | MISMATCHED_TOTAL_PAGE_COUNT`   
Required: No

## See Also
<a name="API_InvalidRequestDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/InvalidRequestDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/InvalidRequestDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/InvalidRequestDetail) 