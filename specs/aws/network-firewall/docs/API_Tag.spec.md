---
id: "@specs/aws/network-firewall/docs/API_Tag"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tag"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# Tag

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_Tag
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tag
<a name="API_Tag"></a>

A key:value pair associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource. 

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="networkfirewall-Type-Tag-Key"></a>
The part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as "customer." Tag keys are case-sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^.*$`   
Required: Yes

 ** Value **   <a name="networkfirewall-Type-Tag-Value"></a>
The part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as "companyA" or "companyB." Tag values are case-sensitive.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `^.*$`   
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/Tag) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/Tag) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/Tag) 