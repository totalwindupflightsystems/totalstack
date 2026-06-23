---
id: "@specs/aws/comprehend/docs/API_DocumentClassifierDocuments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DocumentClassifierDocuments"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DocumentClassifierDocuments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DocumentClassifierDocuments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DocumentClassifierDocuments
<a name="API_DocumentClassifierDocuments"></a>

The location of the training documents. This parameter is required in a request to create a semi-structured document classification model.

## Contents
<a name="API_DocumentClassifierDocuments_Contents"></a>

 ** S3Uri **   <a name="comprehend-Type-DocumentClassifierDocuments-S3Uri"></a>
The S3 URI location of the training documents specified in the S3Uri CSV file.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: Yes

 ** TestS3Uri **   <a name="comprehend-Type-DocumentClassifierDocuments-TestS3Uri"></a>
The S3 URI location of the test documents included in the TestS3Uri CSV file. This field is not required if you do not specify a test CSV file.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: No

## See Also
<a name="API_DocumentClassifierDocuments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DocumentClassifierDocuments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DocumentClassifierDocuments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DocumentClassifierDocuments) 