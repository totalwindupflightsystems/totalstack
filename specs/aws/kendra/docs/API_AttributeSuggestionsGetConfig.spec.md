---
id: "@specs/aws/kendra/docs/API_AttributeSuggestionsGetConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttributeSuggestionsGetConfig"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# AttributeSuggestionsGetConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_AttributeSuggestionsGetConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttributeSuggestionsGetConfig
<a name="API_AttributeSuggestionsGetConfig"></a>

Provides the configuration information for the document fields/attributes that you want to base query suggestions on.

## Contents
<a name="API_AttributeSuggestionsGetConfig_Contents"></a>

 ** AdditionalResponseAttributes **   <a name="kendra-Type-AttributeSuggestionsGetConfig-AdditionalResponseAttributes"></a>
The list of additional document field/attribute keys or field names to include in the response. You can use additional fields to provide extra information in the response. Additional fields are not used to based suggestions on.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`   
Required: No

 ** AttributeFilter **   <a name="kendra-Type-AttributeSuggestionsGetConfig-AttributeFilter"></a>
Filters the search results based on document fields/attributes.  
Type: [AttributeFilter](API_AttributeFilter.md) object  
Required: No

 ** SuggestionAttributes **   <a name="kendra-Type-AttributeSuggestionsGetConfig-SuggestionAttributes"></a>
The list of document field/attribute keys or field names to use for query suggestions. If the content within any of the fields match what your user starts typing as their query, then the field content is returned as a query suggestion.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`   
Required: No

 ** UserContext **   <a name="kendra-Type-AttributeSuggestionsGetConfig-UserContext"></a>
Applies user context filtering so that only users who are given access to certain documents see these document in their search results.  
Type: [UserContext](API_UserContext.md) object  
Required: No

## See Also
<a name="API_AttributeSuggestionsGetConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/AttributeSuggestionsGetConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/AttributeSuggestionsGetConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/AttributeSuggestionsGetConfig) 