---
id: "@specs/aws/cloudfront/docs/API_ActiveTrustedKeyGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActiveTrustedKeyGroups"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ActiveTrustedKeyGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ActiveTrustedKeyGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActiveTrustedKeyGroups
<a name="API_ActiveTrustedKeyGroups"></a>

A list of key groups, and the public keys in each key group, that CloudFront can use to verify the signatures of signed URLs and signed cookies.

## Contents
<a name="API_ActiveTrustedKeyGroups_Contents"></a>

 ** Enabled **   <a name="cloudfront-Type-ActiveTrustedKeyGroups-Enabled"></a>
This field is `true` if any of the key groups have public keys that CloudFront can use to verify the signatures of signed URLs and signed cookies. If not, this field is `false`.  
Type: Boolean  
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-ActiveTrustedKeyGroups-Quantity"></a>
The number of key groups in the list.  
Type: Integer  
Required: Yes

 ** Items **   <a name="cloudfront-Type-ActiveTrustedKeyGroups-Items"></a>
A list of key groups, including the identifiers of the public keys in each key group that CloudFront can use to verify the signatures of signed URLs and signed cookies.  
Type: Array of [KGKeyPairIds](API_KGKeyPairIds.md) objects  
Required: No

## See Also
<a name="API_ActiveTrustedKeyGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ActiveTrustedKeyGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ActiveTrustedKeyGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ActiveTrustedKeyGroups) 