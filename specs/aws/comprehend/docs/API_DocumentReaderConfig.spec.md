---
id: "@specs/aws/comprehend/docs/API_DocumentReaderConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DocumentReaderConfig"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DocumentReaderConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DocumentReaderConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DocumentReaderConfig
<a name="API_DocumentReaderConfig"></a>

Provides configuration parameters to override the default actions for extracting text from PDF documents and image files. 

 By default, Amazon Comprehend performs the following actions to extract text from files, based on the input file type: 
+  **Word files** - Amazon Comprehend parser extracts the text. 
+  **Digital PDF files** - Amazon Comprehend parser extracts the text. 
+  **Image files and scanned PDF files** - Amazon Comprehend uses the Amazon Textract `DetectDocumentText` API to extract the text. 

 `DocumentReaderConfig` does not apply to plain text files or Word files.

 For image files and PDF documents, you can override these default actions using the fields listed below. For more information, see [ Setting text extraction options](https://docs.aws.amazon.com/comprehend/latest/dg/idp-set-textract-options.html) in the Comprehend Developer Guide. 

## Contents
<a name="API_DocumentReaderConfig_Contents"></a>

 ** DocumentReadAction **   <a name="comprehend-Type-DocumentReaderConfig-DocumentReadAction"></a>
This field defines the Amazon Textract API operation that Amazon Comprehend uses to extract text from PDF files and image files. Enter one of the following values:  
+  `TEXTRACT_DETECT_DOCUMENT_TEXT` - The Amazon Comprehend service uses the `DetectDocumentText` API operation. 
+  `TEXTRACT_ANALYZE_DOCUMENT` - The Amazon Comprehend service uses the `AnalyzeDocument` API operation. 
Type: String  
Valid Values: `TEXTRACT_DETECT_DOCUMENT_TEXT | TEXTRACT_ANALYZE_DOCUMENT`   
Required: Yes

 ** DocumentReadMode **   <a name="comprehend-Type-DocumentReaderConfig-DocumentReadMode"></a>
Determines the text extraction actions for PDF files. Enter one of the following values:  
+  `SERVICE_DEFAULT` - use the Amazon Comprehend service defaults for PDF files.
+  `FORCE_DOCUMENT_READ_ACTION` - Amazon Comprehend uses the Textract API specified by DocumentReadAction for all PDF files, including digital PDF files. 
Type: String  
Valid Values: `SERVICE_DEFAULT | FORCE_DOCUMENT_READ_ACTION`   
Required: No

 ** FeatureTypes **   <a name="comprehend-Type-DocumentReaderConfig-FeatureTypes"></a>
Specifies the type of Amazon Textract features to apply. If you chose `TEXTRACT_ANALYZE_DOCUMENT` as the read action, you must specify one or both of the following values:  
+  `TABLES` - Returns additional information about any tables that are detected in the input document. 
+  `FORMS` - Returns additional information about any forms that are detected in the input document. 
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Valid Values: `TABLES | FORMS`   
Required: No

## See Also
<a name="API_DocumentReaderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DocumentReaderConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DocumentReaderConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DocumentReaderConfig) 