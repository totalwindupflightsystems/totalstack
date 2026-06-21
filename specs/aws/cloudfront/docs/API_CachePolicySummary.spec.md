---
id: "@specs/aws/cloudfront/docs/API_CachePolicySummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CachePolicySummary"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CachePolicySummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CachePolicySummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CachePolicySummary
<a name="API_CachePolicySummary"></a>

Contains a cache policy.

## Contents
<a name="API_CachePolicySummary_Contents"></a>

 ** CachePolicy **   <a name="cloudfront-Type-CachePolicySummary-CachePolicy"></a>
The cache policy.  
Type: [CachePolicy](API_CachePolicy.md) object  
Required: Yes

 ** Type **   <a name="cloudfront-Type-CachePolicySummary-Type"></a>
The type of cache policy, either `managed` (created by AWS) or `custom` (created in this AWS account).  
Type: String  
Valid Values: `managed | custom`   
Required: Yes

## See Also
<a name="API_CachePolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CachePolicySummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CachePolicySummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CachePolicySummary) 