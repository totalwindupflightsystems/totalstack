---
id: "@specs/aws/emr/docs/API_Tag"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tag"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# Tag

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_Tag
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tag
<a name="API_Tag"></a>

A key-value pair containing user-defined metadata that you can associate with an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see [Tag Clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html). 

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="EMR-Type-Tag-Key"></a>
A user-defined key, which is the minimum required information for a valid tag. For more information, see [Tag](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html).   
Type: String  
Required: No

 ** Value **   <a name="EMR-Type-Tag-Value"></a>
A user-defined value, which is optional in a tag. For more information, see [Tag Clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html).   
Type: String  
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/Tag) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/Tag) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/Tag) 