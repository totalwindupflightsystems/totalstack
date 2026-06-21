---
id: "@specs/aws/cloudtrail/docs/API_Tag"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tag"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# Tag

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_Tag
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tag
<a name="API_Tag"></a>

A custom key-value pair associated with a resource such as a CloudTrail trail, event data store, dashboard, or channel.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="awscloudtrail-Type-Tag-Key"></a>
The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

 ** Value **   <a name="awscloudtrail-Type-Tag-Value"></a>
The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Tag) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Tag) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Tag) 