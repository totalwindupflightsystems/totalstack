---
id: "@specs/aws/acm/docs/API_CertificateSearchResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CertificateSearchResult"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# CertificateSearchResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_CertificateSearchResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CertificateSearchResult
<a name="API_CertificateSearchResult"></a>

Contains information about a certificate returned by the [SearchCertificates](API_SearchCertificates.md) action. This structure includes the certificate ARN, X.509 attributes, and ACM metadata.

## Contents
<a name="API_CertificateSearchResult_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CertificateArn **   <a name="ACM-Type-CertificateSearchResult-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: No

 ** CertificateMetadata **   <a name="ACM-Type-CertificateSearchResult-CertificateMetadata"></a>
ACM-specific metadata about the certificate.  
Type: [CertificateMetadata](API_CertificateMetadata.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** X509Attributes **   <a name="ACM-Type-CertificateSearchResult-X509Attributes"></a>
X.509 certificate attributes such as subject, issuer, and validity period.  
Type: [X509Attributes](API_X509Attributes.md) object  
Required: No

## See Also
<a name="API_CertificateSearchResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/CertificateSearchResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/CertificateSearchResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/CertificateSearchResult) 