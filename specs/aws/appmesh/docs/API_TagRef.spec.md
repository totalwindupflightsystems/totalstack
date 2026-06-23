---
id: "@specs/aws/appmesh/docs/API_TagRef"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TagRef"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# TagRef

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_TagRef
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TagRef
<a name="API_TagRef"></a>

Optional metadata that you apply to a resource to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.

## Contents
<a name="API_TagRef_Contents"></a>

 ** key **   <a name="appmesh-Type-TagRef-key"></a>
One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

 ** value **   <a name="appmesh-Type-TagRef-value"></a>
The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: Yes

## See Also
<a name="API_TagRef_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/TagRef) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/TagRef) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/TagRef) 