---
id: "@specs/aws/acm/docs/API_CertificateMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CertificateMetadata"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# CertificateMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_CertificateMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CertificateMetadata
<a name="API_CertificateMetadata"></a>

Contains metadata about a certificate. Currently supports ACM certificate metadata.

## Contents
<a name="API_CertificateMetadata_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AcmCertificateMetadata **   <a name="ACM-Type-CertificateMetadata-AcmCertificateMetadata"></a>
Metadata for an ACM certificate.  
Type: [AcmCertificateMetadata](API_AcmCertificateMetadata.md) object  
Required: No

## See Also
<a name="API_CertificateMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/CertificateMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/CertificateMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/CertificateMetadata) 