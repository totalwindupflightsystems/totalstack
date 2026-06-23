---
id: "@specs/aws/comprehend/docs/API_DocumentClass"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DocumentClass"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DocumentClass

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DocumentClass
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DocumentClass
<a name="API_DocumentClass"></a>

Specifies the class that categorizes the document being analyzed

## Contents
<a name="API_DocumentClass_Contents"></a>

 ** Name **   <a name="comprehend-Type-DocumentClass-Name"></a>
The name of the class.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** Page **   <a name="comprehend-Type-DocumentClass-Page"></a>
Page number in the input document. This field is present in the response only if your request includes the `Byte` parameter.   
Type: Integer  
Required: No

 ** Score **   <a name="comprehend-Type-DocumentClass-Score"></a>
The confidence score that Amazon Comprehend has this class correctly attributed.  
Type: Float  
Required: No

## See Also
<a name="API_DocumentClass_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DocumentClass) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DocumentClass) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DocumentClass) 