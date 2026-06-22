---
id: "@specs/aws/emr/docs/API_ScriptBootstrapActionConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ScriptBootstrapActionConfig"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ScriptBootstrapActionConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ScriptBootstrapActionConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ScriptBootstrapActionConfig
<a name="API_ScriptBootstrapActionConfig"></a>

Configuration of the script to run during a bootstrap action.

## Contents
<a name="API_ScriptBootstrapActionConfig_Contents"></a>

 ** Path **   <a name="EMR-Type-ScriptBootstrapActionConfig-Path"></a>
Location in Amazon S3 of the script to run during a bootstrap action.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** Args **   <a name="EMR-Type-ScriptBootstrapActionConfig-Args"></a>
A list of command line arguments to pass to the bootstrap action script.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

## See Also
<a name="API_ScriptBootstrapActionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ScriptBootstrapActionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ScriptBootstrapActionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ScriptBootstrapActionConfig) 