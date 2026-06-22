---
id: "@specs/aws/acm/docs/API_AcmCertificateMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AcmCertificateMetadata"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# AcmCertificateMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_AcmCertificateMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AcmCertificateMetadata
<a name="API_AcmCertificateMetadata"></a>

Contains ACM-specific metadata about a certificate.

## Contents
<a name="API_AcmCertificateMetadata_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CreatedAt **   <a name="ACM-Type-AcmCertificateMetadata-CreatedAt"></a>
The time at which the certificate was requested.  
Type: Timestamp  
Required: No

 ** Exported **   <a name="ACM-Type-AcmCertificateMetadata-Exported"></a>
Indicates whether the certificate has been exported.  
Type: Boolean  
Required: No

 ** ExportOption **   <a name="ACM-Type-AcmCertificateMetadata-ExportOption"></a>
Indicates whether the certificate can be exported.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** ImportedAt **   <a name="ACM-Type-AcmCertificateMetadata-ImportedAt"></a>
The date and time when the certificate was imported. This value exists only when the certificate type is `IMPORTED`.   
Type: Timestamp  
Required: No

 ** InUse **   <a name="ACM-Type-AcmCertificateMetadata-InUse"></a>
Indicates whether the certificate is currently in use by an AWS service.  
Type: Boolean  
Required: No

 ** IssuedAt **   <a name="ACM-Type-AcmCertificateMetadata-IssuedAt"></a>
The time at which the certificate was issued. This value exists only when the certificate type is `AMAZON_ISSUED`.   
Type: Timestamp  
Required: No

 ** ManagedBy **   <a name="ACM-Type-AcmCertificateMetadata-ManagedBy"></a>
Identifies the AWS service that manages the certificate issued by ACM.  
Type: String  
Valid Values: `CLOUDFRONT`   
Required: No

 ** RenewalEligibility **   <a name="ACM-Type-AcmCertificateMetadata-RenewalEligibility"></a>
Specifies whether the certificate is eligible for renewal. At this time, only exported private certificates can be renewed with the [RenewCertificate](API_RenewCertificate.md) command.  
Type: String  
Valid Values: `ELIGIBLE | INELIGIBLE`   
Required: No

 ** RenewalStatus **   <a name="ACM-Type-AcmCertificateMetadata-RenewalStatus"></a>
The renewal status of the certificate.  
Type: String  
Valid Values: `PENDING_AUTO_RENEWAL | PENDING_VALIDATION | SUCCESS | FAILED`   
Required: No

 ** RevokedAt **   <a name="ACM-Type-AcmCertificateMetadata-RevokedAt"></a>
The time at which the certificate was revoked. This value exists only when the certificate status is `REVOKED`.   
Type: Timestamp  
Required: No

 ** Status **   <a name="ACM-Type-AcmCertificateMetadata-Status"></a>
The status of the certificate.  
A certificate enters status PENDING\_VALIDATION upon being requested, unless it fails for any of the reasons given in the troubleshooting topic [Certificate request fails](https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-failed.html). ACM makes repeated attempts to validate a certificate for 72 hours and then times out. If a certificate shows status FAILED or VALIDATION\_TIMED\_OUT, delete the request, correct the issue with [DNS validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html) or [Email validation](https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html), and try again. If validation succeeds, the certificate enters status ISSUED.   
Type: String  
Valid Values: `PENDING_VALIDATION | ISSUED | INACTIVE | EXPIRED | VALIDATION_TIMED_OUT | REVOKED | FAILED`   
Required: No

 ** Type **   <a name="ACM-Type-AcmCertificateMetadata-Type"></a>
The source of the certificate. For certificates provided by ACM, this value is `AMAZON_ISSUED`. For certificates that you imported with [ImportCertificate](API_ImportCertificate.md), this value is `IMPORTED`. ACM does not provide [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) for imported certificates. For more information about the differences between certificates that you import and those that ACM provides, see [Importing Certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the * AWS Certificate Manager User Guide*.   
Type: String  
Valid Values: `IMPORTED | AMAZON_ISSUED | PRIVATE`   
Required: No

 ** ValidationMethod **   <a name="ACM-Type-AcmCertificateMetadata-ValidationMethod"></a>
Specifies the domain validation method.  
Type: String  
Valid Values: `EMAIL | DNS | HTTP`   
Required: No

## See Also
<a name="API_AcmCertificateMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/AcmCertificateMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/AcmCertificateMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/AcmCertificateMetadata) 