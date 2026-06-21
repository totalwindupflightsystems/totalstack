---
id: "@specs/aws/cloudfront/docs/API_CacheBehaviors"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CacheBehaviors"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CacheBehaviors

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CacheBehaviors
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CacheBehaviors
<a name="API_CacheBehaviors"></a>

A complex type that contains zero or more `CacheBehavior` elements.

## Contents
<a name="API_CacheBehaviors_Contents"></a>

 ** Quantity **   <a name="cloudfront-Type-CacheBehaviors-Quantity"></a>
The number of cache behaviors for this distribution.  
Type: Integer  
Required: Yes

 ** Items **   <a name="cloudfront-Type-CacheBehaviors-Items"></a>
Optional: A complex type that contains cache behaviors for this distribution. If `Quantity` is `0`, you can omit `Items`.  
Type: Array of [CacheBehavior](API_CacheBehavior.md) objects  
Required: No

## See Also
<a name="API_CacheBehaviors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CacheBehaviors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CacheBehaviors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CacheBehaviors) 