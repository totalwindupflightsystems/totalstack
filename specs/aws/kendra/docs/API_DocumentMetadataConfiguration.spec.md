---
id: "@specs/aws/kendra/docs/API_DocumentMetadataConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DocumentMetadataConfiguration"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# DocumentMetadataConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_DocumentMetadataConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DocumentMetadataConfiguration
<a name="API_DocumentMetadataConfiguration"></a>

Specifies the properties, such as relevance tuning and searchability, of an index field.

## Contents
<a name="API_DocumentMetadataConfiguration_Contents"></a>

 ** Name **   <a name="kendra-Type-DocumentMetadataConfiguration-Name"></a>
The name of the index field.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 30.  
Required: Yes

 ** Type **   <a name="kendra-Type-DocumentMetadataConfiguration-Type"></a>
The data type of the index field.   
Type: String  
Valid Values: `STRING_VALUE | STRING_LIST_VALUE | LONG_VALUE | DATE_VALUE`   
Required: Yes

 ** Relevance **   <a name="kendra-Type-DocumentMetadataConfiguration-Relevance"></a>
Provides tuning parameters to determine how the field affects the search results.  
Type: [Relevance](API_Relevance.md) object  
Required: No

 ** Search **   <a name="kendra-Type-DocumentMetadataConfiguration-Search"></a>
Provides information about how the field is used during a search.  
Type: [Search](API_Search.md) object  
Required: No

## See Also
<a name="API_DocumentMetadataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/DocumentMetadataConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/DocumentMetadataConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/DocumentMetadataConfiguration) 