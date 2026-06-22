---
id: "@specs/aws/acm/docs/API_CertificateSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CertificateSummary"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# CertificateSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_CertificateSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CertificateSummary
<a name="API_CertificateSummary"></a>

This structure is returned in the response object of [ListCertificates](API_ListCertificates.md) action. 

## Contents
<a name="API_CertificateSummary_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CertificateArn **   <a name="ACM-Type-CertificateSummary-CertificateArn"></a>
Amazon Resource Name (ARN) of the certificate. This is of the form:  
 `arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012`   
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: No

 ** CreatedAt **   <a name="ACM-Type-CertificateSummary-CreatedAt"></a>
The time at which the certificate was requested.  
Type: Timestamp  
Required: No

 ** DomainName **   <a name="ACM-Type-CertificateSummary-DomainName"></a>
Fully qualified domain name (FQDN), such as www.example.com or example.com, for the certificate.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`   
Required: No

 ** Exported **   <a name="ACM-Type-CertificateSummary-Exported"></a>
Indicates whether the certificate has been exported. This value exists only when the certificate type is `PRIVATE`.  
Type: Boolean  
Required: No

 ** ExportOption **   <a name="ACM-Type-CertificateSummary-ExportOption"></a>
Indicates if export is enabled for the certificate.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** ExtendedKeyUsages **   <a name="ACM-Type-CertificateSummary-ExtendedKeyUsages"></a>
Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID).   
Type: Array of strings  
Valid Values: `TLS_WEB_SERVER_AUTHENTICATION | TLS_WEB_CLIENT_AUTHENTICATION | CODE_SIGNING | EMAIL_PROTECTION | TIME_STAMPING | OCSP_SIGNING | IPSEC_END_SYSTEM | IPSEC_TUNNEL | IPSEC_USER | ANY | NONE | CUSTOM`   
Required: No

 ** HasAdditionalSubjectAlternativeNames **   <a name="ACM-Type-CertificateSummary-HasAdditionalSubjectAlternativeNames"></a>
When called by [ListCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html), indicates whether the full list of subject alternative names has been included in the response. If false, the response includes all of the subject alternative names included in the certificate. If true, the response only includes the first 100 subject alternative names included in the certificate. To display the full list of subject alternative names, use [DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html).  
Type: Boolean  
Required: No

 ** ImportedAt **   <a name="ACM-Type-CertificateSummary-ImportedAt"></a>
The date and time when the certificate was imported. This value exists only when the certificate type is `IMPORTED`.   
Type: Timestamp  
Required: No

 ** InUse **   <a name="ACM-Type-CertificateSummary-InUse"></a>
Indicates whether the certificate is currently in use by any AWS resources.  
Type: Boolean  
Required: No

 ** IssuedAt **   <a name="ACM-Type-CertificateSummary-IssuedAt"></a>
The time at which the certificate was issued. This value exists only when the certificate type is `AMAZON_ISSUED`.   
Type: Timestamp  
Required: No

 ** KeyAlgorithm **   <a name="ACM-Type-CertificateSummary-KeyAlgorithm"></a>
The algorithm that was used to generate the public-private key pair.  
Type: String  
Valid Values: `RSA_1024 | RSA_2048 | RSA_3072 | RSA_4096 | EC_prime256v1 | EC_secp384r1 | EC_secp521r1`   
Required: No

 ** KeyUsages **   <a name="ACM-Type-CertificateSummary-KeyUsages"></a>
A list of Key Usage X.509 v3 extension objects. Each object is a string value that identifies the purpose of the public key contained in the certificate. Possible extension values include DIGITAL\_SIGNATURE, KEY\_ENCHIPHERMENT, NON\_REPUDIATION, and more.  
Type: Array of strings  
Valid Values: `DIGITAL_SIGNATURE | NON_REPUDIATION | KEY_ENCIPHERMENT | DATA_ENCIPHERMENT | KEY_AGREEMENT | CERTIFICATE_SIGNING | CRL_SIGNING | ENCIPHER_ONLY | DECIPHER_ONLY | ANY | CUSTOM`   
Required: No

 ** ManagedBy **   <a name="ACM-Type-CertificateSummary-ManagedBy"></a>
Identifies the AWS service that manages the certificate issued by ACM.  
Type: String  
Valid Values: `CLOUDFRONT`   
Required: No

 ** NotAfter **   <a name="ACM-Type-CertificateSummary-NotAfter"></a>
The time after which the certificate is not valid.  
Type: Timestamp  
Required: No

 ** NotBefore **   <a name="ACM-Type-CertificateSummary-NotBefore"></a>
The time before which the certificate is not valid.  
Type: Timestamp  
Required: No

 ** RenewalEligibility **   <a name="ACM-Type-CertificateSummary-RenewalEligibility"></a>
Specifies whether the certificate is eligible for renewal. At this time, only exported private certificates can be renewed with the [RenewCertificate](API_RenewCertificate.md) command.  
Type: String  
Valid Values: `ELIGIBLE | INELIGIBLE`   
Required: No

 ** RevokedAt **   <a name="ACM-Type-CertificateSummary-RevokedAt"></a>
The time at which the certificate was revoked. This value exists only when the certificate status is `REVOKED`.   
Type: Timestamp  
Required: No

 ** Status **   <a name="ACM-Type-CertificateSummary-Status"></a>
The status of the certificate.  
A certificate enters status PENDING\_VALIDATION upon being requested, unless it fails for any of the reasons given in the troubleshooting topic [Certificate request fails](https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-failed.html). ACM makes repeated attempts to validate a certificate for 72 hours and then times out. If a certificate shows status FAILED or VALIDATION\_TIMED\_OUT, delete the request, correct the issue with [DNS validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html) or [Email validation](https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html), and try again. If validation succeeds, the certificate enters status ISSUED.   
Type: String  
Valid Values: `PENDING_VALIDATION | ISSUED | INACTIVE | EXPIRED | VALIDATION_TIMED_OUT | REVOKED | FAILED`   
Required: No

 ** SubjectAlternativeNameSummaries **   <a name="ACM-Type-CertificateSummary-SubjectAlternativeNameSummaries"></a>
One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website.   
When called by [ListCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html), this parameter will only return the first 100 subject alternative names included in the certificate. To display the full list of subject alternative names, use [DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html).  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`   
Required: No

 ** Type **   <a name="ACM-Type-CertificateSummary-Type"></a>
The source of the certificate. For certificates provided by ACM, this value is `AMAZON_ISSUED`. For certificates that you imported with [ImportCertificate](API_ImportCertificate.md), this value is `IMPORTED`. ACM does not provide [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) for imported certificates. For more information about the differences between certificates that you import and those that ACM provides, see [Importing Certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the * AWS Certificate Manager User Guide*.   
Type: String  
Valid Values: `IMPORTED | AMAZON_ISSUED | PRIVATE`   
Required: No

## See Also
<a name="API_CertificateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/CertificateSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/CertificateSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/CertificateSummary) 