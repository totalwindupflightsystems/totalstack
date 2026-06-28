---
id: "@specs/aws/kendra/docs/API_FacetResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FacetResult"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# FacetResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_FacetResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FacetResult
<a name="API_FacetResult"></a>

The facet values for the documents in the response.

## Contents
<a name="API_FacetResult_Contents"></a>

 ** DocumentAttributeKey **   <a name="kendra-Type-FacetResult-DocumentAttributeKey"></a>
The key for the facet values. This is the same as the `DocumentAttributeKey` provided in the query.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`   
Required: No

 ** DocumentAttributeValueCountPairs **   <a name="kendra-Type-FacetResult-DocumentAttributeValueCountPairs"></a>
An array of key/value pairs, where the key is the value of the attribute and the count is the number of documents that share the key value.  
Type: Array of [DocumentAttributeValueCountPair](API_DocumentAttributeValueCountPair.md) objects  
Required: No

 ** DocumentAttributeValueType **   <a name="kendra-Type-FacetResult-DocumentAttributeValueType"></a>
The data type of the facet value. This is the same as the type defined for the index field when it was created.  
Type: String  
Valid Values: `STRING_VALUE | STRING_LIST_VALUE | LONG_VALUE | DATE_VALUE`   
Required: No

## See Also
<a name="API_FacetResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/FacetResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/FacetResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/FacetResult) 