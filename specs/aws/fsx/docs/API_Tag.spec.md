---
id: "@specs/aws/fsx/docs/API_Tag"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tag"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# Tag

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_Tag
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tag
<a name="API_Tag"></a>

Specifies a key-value pair for a resource tag.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="FSx-Type-Tag-Key"></a>
A value that specifies the `TagKey`, the name of the tag. Tag keys must be unique for the resource to which they are attached.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`   
Required: Yes

 ** Value **   <a name="FSx-Type-Tag-Value"></a>
A value that specifies the `TagValue`, the value assigned to the corresponding tag key. Tag values can be null and don't have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`   
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/Tag) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/Tag) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/Tag) 