---
id: "@specs/aws/emr/docs/API_SupportedProductConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SupportedProductConfig"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# SupportedProductConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_SupportedProductConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SupportedProductConfig
<a name="API_SupportedProductConfig"></a>

The list of supported product configurations that allow user-supplied arguments. Amazon EMR accepts these arguments and forwards them to the corresponding installation script as bootstrap action arguments.

## Contents
<a name="API_SupportedProductConfig_Contents"></a>

 ** Args **   <a name="EMR-Type-SupportedProductConfig-Args"></a>
The list of user-supplied arguments.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Name **   <a name="EMR-Type-SupportedProductConfig-Name"></a>
The name of the product configuration.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

## See Also
<a name="API_SupportedProductConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SupportedProductConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SupportedProductConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SupportedProductConfig) 