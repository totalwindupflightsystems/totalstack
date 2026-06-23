---
id: "@specs/aws/comprehend/docs/API_KeyPhrase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS KeyPhrase"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# KeyPhrase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_KeyPhrase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# KeyPhrase
<a name="API_KeyPhrase"></a>

Describes a key noun phrase.

## Contents
<a name="API_KeyPhrase_Contents"></a>

 ** BeginOffset **   <a name="comprehend-Type-KeyPhrase-BeginOffset"></a>
The zero-based offset from the beginning of the source text to the first character in the key phrase.  
Type: Integer  
Required: No

 ** EndOffset **   <a name="comprehend-Type-KeyPhrase-EndOffset"></a>
The zero-based offset from the beginning of the source text to the last character in the key phrase.  
Type: Integer  
Required: No

 ** Score **   <a name="comprehend-Type-KeyPhrase-Score"></a>
The level of confidence that Amazon Comprehend has in the accuracy of the detection.  
Type: Float  
Required: No

 ** Text **   <a name="comprehend-Type-KeyPhrase-Text"></a>
The text of a key noun phrase.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## See Also
<a name="API_KeyPhrase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/KeyPhrase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/KeyPhrase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/KeyPhrase) 