---
id: "@specs/aws/emr/docs/API_SecurityConfigurationSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SecurityConfigurationSummary"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# SecurityConfigurationSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_SecurityConfigurationSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SecurityConfigurationSummary
<a name="API_SecurityConfigurationSummary"></a>

The creation date and time, and name, of a security configuration.

## Contents
<a name="API_SecurityConfigurationSummary_Contents"></a>

 ** CreationDateTime **   <a name="EMR-Type-SecurityConfigurationSummary-CreationDateTime"></a>
The date and time the security configuration was created.  
Type: Timestamp  
Required: No

 ** Name **   <a name="EMR-Type-SecurityConfigurationSummary-Name"></a>
The name of the security configuration.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

## See Also
<a name="API_SecurityConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SecurityConfigurationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SecurityConfigurationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SecurityConfigurationSummary) 