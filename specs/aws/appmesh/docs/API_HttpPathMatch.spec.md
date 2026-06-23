---
id: "@specs/aws/appmesh/docs/API_HttpPathMatch"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HttpPathMatch"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# HttpPathMatch

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_HttpPathMatch
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HttpPathMatch
<a name="API_HttpPathMatch"></a>

An object representing the path to match in the request.

## Contents
<a name="API_HttpPathMatch_Contents"></a>

 ** exact **   <a name="appmesh-Type-HttpPathMatch-exact"></a>
The exact path to match on.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** regex **   <a name="appmesh-Type-HttpPathMatch-regex"></a>
The regex used to match the path.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

## See Also
<a name="API_HttpPathMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HttpPathMatch) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HttpPathMatch) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HttpPathMatch) 