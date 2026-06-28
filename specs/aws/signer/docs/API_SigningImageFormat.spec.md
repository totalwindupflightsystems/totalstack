---
id: "@specs/aws/signer/docs/API_SigningImageFormat"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SigningImageFormat"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# SigningImageFormat

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_SigningImageFormat
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SigningImageFormat
<a name="API_SigningImageFormat"></a>

The image format of a AWS Signer platform or profile.

## Contents
<a name="API_SigningImageFormat_Contents"></a>

 ** defaultFormat **   <a name="signer-Type-SigningImageFormat-defaultFormat"></a>
The default format of a signing image.  
Type: String  
Valid Values: `JSON | JSONEmbedded | JSONDetached`   
Required: Yes

 ** supportedFormats **   <a name="signer-Type-SigningImageFormat-supportedFormats"></a>
The supported formats of a signing image.  
Type: Array of strings  
Valid Values: `JSON | JSONEmbedded | JSONDetached`   
Required: Yes

## See Also
<a name="API_SigningImageFormat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/SigningImageFormat) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/SigningImageFormat) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/SigningImageFormat) 