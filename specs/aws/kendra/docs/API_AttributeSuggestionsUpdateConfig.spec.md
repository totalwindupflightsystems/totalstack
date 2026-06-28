---
id: "@specs/aws/kendra/docs/API_AttributeSuggestionsUpdateConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttributeSuggestionsUpdateConfig"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# AttributeSuggestionsUpdateConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_AttributeSuggestionsUpdateConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttributeSuggestionsUpdateConfig
<a name="API_AttributeSuggestionsUpdateConfig"></a>

Updates the configuration information for the document fields/attributes that you want to base query suggestions on.

To deactivate using documents fields for query suggestions, set the mode to `INACTIVE`. You must also set `SuggestionTypes` as either `QUERY` or `DOCUMENT_ATTRIBUTES` and then call [GetQuerySuggestions](https://docs.aws.amazon.com/kendra/latest/dg/API_GetQuerySuggestions.html). If you set to `QUERY`, then Amazon Kendra uses the query history to base suggestions on. If you set to `DOCUMENT_ATTRIBUTES`, then Amazon Kendra uses the contents of document fields to base suggestions on.

## Contents
<a name="API_AttributeSuggestionsUpdateConfig_Contents"></a>

 ** AttributeSuggestionsMode **   <a name="kendra-Type-AttributeSuggestionsUpdateConfig-AttributeSuggestionsMode"></a>
You can set the mode to `ACTIVE` or `INACTIVE`. You must also set `SuggestionTypes` as either `QUERY` or `DOCUMENT_ATTRIBUTES` and then call [GetQuerySuggestions](https://docs.aws.amazon.com/kendra/latest/dg/API_GetQuerySuggestions.html). If `Mode` to use query history is set to `ENABLED` when calling [UpdateQuerySuggestionsConfig](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateQuerySuggestionsConfig.html) and `AttributeSuggestionsMode` to use fields/attributes is set to `ACTIVE`, and you haven't set your `SuggestionTypes` preference to `DOCUMENT_ATTRIBUTES`, then Amazon Kendra uses the query history.  
Type: String  
Valid Values: `ACTIVE | INACTIVE`   
Required: No

 ** SuggestableConfigList **   <a name="kendra-Type-AttributeSuggestionsUpdateConfig-SuggestableConfigList"></a>
The list of fields/attributes that you want to set as suggestible for query suggestions.  
Type: Array of [SuggestableConfig](API_SuggestableConfig.md) objects  
Required: No

## See Also
<a name="API_AttributeSuggestionsUpdateConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/AttributeSuggestionsUpdateConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/AttributeSuggestionsUpdateConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/AttributeSuggestionsUpdateConfig) 