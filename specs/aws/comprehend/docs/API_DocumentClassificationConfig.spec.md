---
id: "@specs/aws/comprehend/docs/API_DocumentClassificationConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DocumentClassificationConfig"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DocumentClassificationConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DocumentClassificationConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DocumentClassificationConfig
<a name="API_DocumentClassificationConfig"></a>

Configuration required for a document classification model.

## Contents
<a name="API_DocumentClassificationConfig_Contents"></a>

 ** Mode **   <a name="comprehend-Type-DocumentClassificationConfig-Mode"></a>
Classification mode indicates whether the documents are `MULTI_CLASS` or `MULTI_LABEL`.  
Type: String  
Valid Values: `MULTI_CLASS | MULTI_LABEL`   
Required: Yes

 ** Labels **   <a name="comprehend-Type-DocumentClassificationConfig-Labels"></a>
One or more labels to associate with the custom classifier.  
Type: Array of strings  
Array Members: Maximum number of 1000 items.  
Length Constraints: Maximum length of 5000.  
Pattern: `^\P{C}*$`   
Required: No

## See Also
<a name="API_DocumentClassificationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DocumentClassificationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DocumentClassificationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DocumentClassificationConfig) 