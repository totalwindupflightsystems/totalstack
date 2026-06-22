---
id: "@specs/aws/emr/docs/API_UsernamePassword"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UsernamePassword"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# UsernamePassword

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_UsernamePassword
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UsernamePassword
<a name="API_UsernamePassword"></a>

The username and password that you use to connect to cluster endpoints.

## Contents
<a name="API_UsernamePassword_Contents"></a>

 ** Password **   <a name="EMR-Type-UsernamePassword-Password"></a>
The password associated with the temporary credentials that you use to connect to cluster endpoints.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Username **   <a name="EMR-Type-UsernamePassword-Username"></a>
The username associated with the temporary credentials that you use to connect to cluster endpoints.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

## See Also
<a name="API_UsernamePassword_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/UsernamePassword) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/UsernamePassword) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/UsernamePassword) 