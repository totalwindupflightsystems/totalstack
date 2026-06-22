---
id: "@specs/aws/acm/docs/API_AcmCertificateMetadataFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AcmCertificateMetadataFilter"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# AcmCertificateMetadataFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_AcmCertificateMetadataFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AcmCertificateMetadataFilter
<a name="API_AcmCertificateMetadataFilter"></a>

Filters certificates by ACM metadata.

## Contents
<a name="API_AcmCertificateMetadataFilter_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Exported **   <a name="ACM-Type-AcmCertificateMetadataFilter-Exported"></a>
Filter by whether the certificate has been exported.  
Type: Boolean  
Required: No

 ** ExportOption **   <a name="ACM-Type-AcmCertificateMetadataFilter-ExportOption"></a>
Filter by certificate export option.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** InUse **   <a name="ACM-Type-AcmCertificateMetadataFilter-InUse"></a>
Filter by whether the certificate is in use.  
Type: Boolean  
Required: No

 ** ManagedBy **   <a name="ACM-Type-AcmCertificateMetadataFilter-ManagedBy"></a>
Filter by the entity that manages the certificate.  
Type: String  
Valid Values: `CLOUDFRONT`   
Required: No

 ** RenewalStatus **   <a name="ACM-Type-AcmCertificateMetadataFilter-RenewalStatus"></a>
Filter by certificate renewal status.  
Type: String  
Valid Values: `PENDING_AUTO_RENEWAL | PENDING_VALIDATION | SUCCESS | FAILED`   
Required: No

 ** Status **   <a name="ACM-Type-AcmCertificateMetadataFilter-Status"></a>
Filter by certificate status.  
Type: String  
Valid Values: `PENDING_VALIDATION | ISSUED | INACTIVE | EXPIRED | VALIDATION_TIMED_OUT | REVOKED | FAILED`   
Required: No

 ** Type **   <a name="ACM-Type-AcmCertificateMetadataFilter-Type"></a>
Filter by certificate type.  
Type: String  
Valid Values: `IMPORTED | AMAZON_ISSUED | PRIVATE`   
Required: No

 ** ValidationMethod **   <a name="ACM-Type-AcmCertificateMetadataFilter-ValidationMethod"></a>
Filter by validation method.  
Type: String  
Valid Values: `EMAIL | DNS | HTTP`   
Required: No

## See Also
<a name="API_AcmCertificateMetadataFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/AcmCertificateMetadataFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/AcmCertificateMetadataFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/AcmCertificateMetadataFilter) 