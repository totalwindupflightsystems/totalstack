---
id: "@specs/aws/cloudfront/docs/API_ConflictingAlias"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ConflictingAlias"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ConflictingAlias

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ConflictingAlias
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ConflictingAlias
<a name="API_ConflictingAlias"></a>

An alias (also called a CNAME) and the CloudFront standard distribution and AWS account ID that it's associated with. The standard distribution and account IDs are partially hidden, which allows you to identify the standard distributions and accounts that you own, and helps to protect the information of ones that you don't own.

## Contents
<a name="API_ConflictingAlias_Contents"></a>

 ** AccountId **   <a name="cloudfront-Type-ConflictingAlias-AccountId"></a>
The (partially hidden) ID of the AWS account that owns the standard distribution that's associated with the alias.  
Type: String  
Required: No

 ** Alias **   <a name="cloudfront-Type-ConflictingAlias-Alias"></a>
An alias (also called a CNAME).  
Type: String  
Required: No

 ** DistributionId **   <a name="cloudfront-Type-ConflictingAlias-DistributionId"></a>
The (partially hidden) ID of the CloudFront standard distribution associated with the alias.  
Type: String  
Required: No

## See Also
<a name="API_ConflictingAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ConflictingAlias) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ConflictingAlias) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ConflictingAlias) 