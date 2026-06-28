---
id: "@specs/aws/kendra/docs/API_ConfluenceBlogConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ConfluenceBlogConfiguration"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# ConfluenceBlogConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_ConfluenceBlogConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ConfluenceBlogConfiguration
<a name="API_ConfluenceBlogConfiguration"></a>

Configuration of blog settings for the Confluence data source. Blogs are always indexed unless filtered from the index by the `ExclusionPatterns` or `InclusionPatterns` fields in the `ConfluenceConfiguration` object.

## Contents
<a name="API_ConfluenceBlogConfiguration_Contents"></a>

 ** BlogFieldMappings **   <a name="kendra-Type-ConfluenceBlogConfiguration-BlogFieldMappings"></a>
Maps attributes or field names of Confluence blogs to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Confluence fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html). The Confluence data source field names must exist in your Confluence custom metadata.  
If you specify the `BlogFieldMappings` parameter, you must specify at least one field mapping.  
Type: Array of [ConfluenceBlogToIndexFieldMapping](API_ConfluenceBlogToIndexFieldMapping.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 9 items.  
Required: No

## See Also
<a name="API_ConfluenceBlogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/ConfluenceBlogConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/ConfluenceBlogConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/ConfluenceBlogConfiguration) 