---
id: "@specs/aws/cloudtrail/docs/API_ResourceTag"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ResourceTag"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# ResourceTag

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_ResourceTag
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ResourceTag
<a name="API_ResourceTag"></a>

A resource tag.

## Contents
<a name="API_ResourceTag_Contents"></a>

 ** ResourceId **   <a name="awscloudtrail-Type-ResourceTag-ResourceId"></a>
Specifies the ARN of the resource.  
Type: String  
Required: No

 ** TagsList **   <a name="awscloudtrail-Type-ResourceTag-TagsList"></a>
A list of tags.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Maximum number of 200 items.  
Required: No

## See Also
<a name="API_ResourceTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ResourceTag) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ResourceTag) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ResourceTag) 