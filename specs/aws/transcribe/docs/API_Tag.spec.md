---
id: "@specs/aws/transcribe/docs/API_Tag"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tag"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# Tag

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_Tag
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tag
<a name="API_Tag"></a>

Adds metadata, in the form of a key:value pair, to the specified resource.

For example, you could add the tag `Department:Sales` to a resource to indicate that it pertains to your organization's sales department. You can also use tags for tag-based access control.

To learn more about tagging, see [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html).

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="transcribe-Type-Tag-Key"></a>
The first part of a key:value pair that forms a tag associated with a given resource. For example, in the tag `Department:Sales`, the key is 'Department'.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

 ** Value **   <a name="transcribe-Type-Tag-Value"></a>
The second part of a key:value pair that forms a tag associated with a given resource. For example, in the tag `Department:Sales`, the value is 'Sales'.  
Note that you can set the value of a tag to an empty string, but you can't set the value of a tag to null. Omitting the tag value is the same as using an empty string.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/Tag) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/Tag) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/Tag) 