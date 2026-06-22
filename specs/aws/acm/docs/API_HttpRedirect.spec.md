---
id: "@specs/aws/acm/docs/API_HttpRedirect"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HttpRedirect"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# HttpRedirect

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_HttpRedirect
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HttpRedirect
<a name="API_HttpRedirect"></a>

Contains information for HTTP-based domain validation of certificates requested through Amazon CloudFront and issued by ACM. This field exists only when the certificate type is `AMAZON_ISSUED` and the validation method is `HTTP`.

## Contents
<a name="API_HttpRedirect_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** RedirectFrom **   <a name="ACM-Type-HttpRedirect-RedirectFrom"></a>
The URL including the domain to be validated. The certificate authority sends `GET` requests here during validation.  
Type: String  
Required: No

 ** RedirectTo **   <a name="ACM-Type-HttpRedirect-RedirectTo"></a>
The URL hosting the validation token. `RedirectFrom` must return this content or redirect here.  
Type: String  
Required: No

## See Also
<a name="API_HttpRedirect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/HttpRedirect) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/HttpRedirect) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/HttpRedirect) 