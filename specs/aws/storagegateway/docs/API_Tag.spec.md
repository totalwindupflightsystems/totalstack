---
id: "@specs/aws/storagegateway/docs/API_Tag"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tag"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# Tag

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_Tag
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tag
<a name="API_Tag"></a>

A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: \+ - = . \_ : /.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="StorageGateway-Type-Tag-Key"></a>
Tag key. The key can't start with aws:.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`   
Required: Yes

 ** Value **   <a name="StorageGateway-Type-Tag-Value"></a>
Value of the tag key.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/Tag) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/Tag) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/Tag) 