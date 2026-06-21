---
id: "@specs/aws/shield/docs/API_Tag"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tag"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# Tag

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_Tag
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tag
<a name="API_Tag"></a>

A tag associated with an AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing or other management. Typically, the tag key represents a category, such as "environment", and the tag value represents a specific value within that category, such as "test," "development," or "production". Or you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="AWSShield-Type-Tag-Key"></a>
Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as "customer." Tag keys are case-sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

 ** Value **   <a name="AWSShield-Type-Tag-Value"></a>
Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as "companyA" or "companyB." Tag values are case-sensitive.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/Tag) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/Tag) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/Tag) 