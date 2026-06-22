---
id: "@specs/aws/emr/docs/API_BootstrapActionConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BootstrapActionConfig"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# BootstrapActionConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_BootstrapActionConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BootstrapActionConfig
<a name="API_BootstrapActionConfig"></a>

Configuration of a bootstrap action.

## Contents
<a name="API_BootstrapActionConfig_Contents"></a>

 ** Name **   <a name="EMR-Type-BootstrapActionConfig-Name"></a>
The name of the bootstrap action.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** ScriptBootstrapAction **   <a name="EMR-Type-BootstrapActionConfig-ScriptBootstrapAction"></a>
The script run by the bootstrap action.  
Type: [ScriptBootstrapActionConfig](API_ScriptBootstrapActionConfig.md) object  
Required: Yes

## See Also
<a name="API_BootstrapActionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/BootstrapActionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/BootstrapActionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/BootstrapActionConfig) 