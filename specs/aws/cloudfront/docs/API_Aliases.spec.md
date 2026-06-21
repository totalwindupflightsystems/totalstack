---
id: "@specs/aws/cloudfront/docs/API_Aliases"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Aliases"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# Aliases

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_Aliases
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Aliases
<a name="API_Aliases"></a>

A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.

## Contents
<a name="API_Aliases_Contents"></a>

 ** Quantity **   <a name="cloudfront-Type-Aliases-Quantity"></a>
The number of CNAME aliases, if any, that you want to associate with this distribution.  
Type: Integer  
Required: Yes

 ** Items **   <a name="cloudfront-Type-Aliases-Items"></a>
A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.  
Type: Array of strings  
Required: No

## See Also
<a name="API_Aliases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/Aliases) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/Aliases) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/Aliases) 