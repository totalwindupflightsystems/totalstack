---
id: "@specs/aws/cloudfront/docs/API_ActiveTrustedSigners"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActiveTrustedSigners"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ActiveTrustedSigners

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ActiveTrustedSigners
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActiveTrustedSigners
<a name="API_ActiveTrustedSigners"></a>

A list of AWS accounts and the active CloudFront key pairs in each account that CloudFront can use to verify the signatures of signed URLs and signed cookies.

## Contents
<a name="API_ActiveTrustedSigners_Contents"></a>

 ** Enabled **   <a name="cloudfront-Type-ActiveTrustedSigners-Enabled"></a>
This field is `true` if any of the AWS accounts in the list are configured as trusted signers. If not, this field is `false`.  
Type: Boolean  
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-ActiveTrustedSigners-Quantity"></a>
The number of AWS accounts in the list.  
Type: Integer  
Required: Yes

 ** Items **   <a name="cloudfront-Type-ActiveTrustedSigners-Items"></a>
A list of AWS accounts and the identifiers of active CloudFront key pairs in each account that CloudFront can use to verify the signatures of signed URLs and signed cookies.  
Type: Array of [Signer](API_Signer.md) objects  
Required: No

## See Also
<a name="API_ActiveTrustedSigners_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ActiveTrustedSigners) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ActiveTrustedSigners) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ActiveTrustedSigners) 