---
id: "@specs/aws/kendra/docs/API_AttributeSuggestionsDescribeConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttributeSuggestionsDescribeConfig"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# AttributeSuggestionsDescribeConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_AttributeSuggestionsDescribeConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttributeSuggestionsDescribeConfig
<a name="API_AttributeSuggestionsDescribeConfig"></a>

Gets information on the configuration of document fields/attributes that you want to base query suggestions on. To change your configuration, use [AttributeSuggestionsUpdateConfig](https://docs.aws.amazon.com/kendra/latest/dg/API_AttributeSuggestionsUpdateConfig.html) and then call [UpdateQuerySuggestionsConfig](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateQuerySuggestionsConfig.html).

## Contents
<a name="API_AttributeSuggestionsDescribeConfig_Contents"></a>

 ** AttributeSuggestionsMode **   <a name="kendra-Type-AttributeSuggestionsDescribeConfig-AttributeSuggestionsMode"></a>
The mode is set to either `ACTIVE` or `INACTIVE`. If the `Mode` for query history is set to `ENABLED` when calling [UpdateQuerySuggestionsConfig](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateQuerySuggestionsConfig.html) and `AttributeSuggestionsMode` to use fields/attributes is set to `ACTIVE`, and you haven't set your `SuggestionTypes` preference to `DOCUMENT_ATTRIBUTES`, then Amazon Kendra uses the query history.  
Type: String  
Valid Values: `ACTIVE | INACTIVE`   
Required: No

 ** SuggestableConfigList **   <a name="kendra-Type-AttributeSuggestionsDescribeConfig-SuggestableConfigList"></a>
The list of fields/attributes that you want to set as suggestible for query suggestions.  
Type: Array of [SuggestableConfig](API_SuggestableConfig.md) objects  
Required: No

## See Also
<a name="API_AttributeSuggestionsDescribeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/AttributeSuggestionsDescribeConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/AttributeSuggestionsDescribeConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/AttributeSuggestionsDescribeConfig) 