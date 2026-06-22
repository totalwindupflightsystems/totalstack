---
id: "@specs/aws/acm/docs/API_CertificateDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CertificateDetail"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# CertificateDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_CertificateDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CertificateDetail
<a name="API_CertificateDetail"></a>

Contains metadata about an ACM certificate. This structure is returned in the response to a [DescribeCertificate](API_DescribeCertificate.md) request. 

## Contents
<a name="API_CertificateDetail_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CertificateArn **   <a name="ACM-Type-CertificateDetail-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate. For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: No

 ** CertificateAuthorityArn **   <a name="ACM-Type-CertificateDetail-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) of the private certificate authority (CA) that issued the certificate. This has the following format:   
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012`   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: No

 ** CreatedAt **   <a name="ACM-Type-CertificateDetail-CreatedAt"></a>
The time at which the certificate was requested.  
Type: Timestamp  
Required: No

 ** DomainName **   <a name="ACM-Type-CertificateDetail-DomainName"></a>
The fully qualified domain name for the certificate, such as www.example.com or example.com.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`   
Required: No

 ** DomainValidationOptions **   <a name="ACM-Type-CertificateDetail-DomainValidationOptions"></a>
Contains information about the initial validation of each domain name that occurs as a result of the [RequestCertificate](API_RequestCertificate.md) request. This field exists only when the certificate type is `AMAZON_ISSUED`.   
Type: Array of [DomainValidation](API_DomainValidation.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Required: No

 ** ExtendedKeyUsages **   <a name="ACM-Type-CertificateDetail-ExtendedKeyUsages"></a>
Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID).   
Type: Array of [ExtendedKeyUsage](API_ExtendedKeyUsage.md) objects  
Required: No

 ** FailureReason **   <a name="ACM-Type-CertificateDetail-FailureReason"></a>
The reason the certificate request failed. This value exists only when the certificate status is `FAILED`. For more information, see [Certificate Request Failed](https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting.html#troubleshooting-failed) in the * AWS Certificate Manager User Guide*.   
Type: String  
Valid Values: `NO_AVAILABLE_CONTACTS | ADDITIONAL_VERIFICATION_REQUIRED | DOMAIN_NOT_ALLOWED | INVALID_PUBLIC_DOMAIN | DOMAIN_VALIDATION_DENIED | CAA_ERROR | PCA_LIMIT_EXCEEDED | PCA_INVALID_ARN | PCA_INVALID_STATE | PCA_REQUEST_FAILED | PCA_NAME_CONSTRAINTS_VALIDATION | PCA_RESOURCE_NOT_FOUND | PCA_INVALID_ARGS | PCA_INVALID_DURATION | PCA_ACCESS_DENIED | SLR_NOT_FOUND | OTHER`   
Required: No

 ** ImportedAt **   <a name="ACM-Type-CertificateDetail-ImportedAt"></a>
The date and time when the certificate was imported. This value exists only when the certificate type is `IMPORTED`.   
Type: Timestamp  
Required: No

 ** InUseBy **   <a name="ACM-Type-CertificateDetail-InUseBy"></a>
A list of ARNs for the AWS resources that are using the certificate. A certificate can be used by multiple AWS resources.   
Type: Array of strings  
Required: No

 ** IssuedAt **   <a name="ACM-Type-CertificateDetail-IssuedAt"></a>
The time at which the certificate was issued. This value exists only when the certificate type is `AMAZON_ISSUED`.   
Type: Timestamp  
Required: No

 ** Issuer **   <a name="ACM-Type-CertificateDetail-Issuer"></a>
The name of the certificate authority that issued and signed the certificate.  
Type: String  
Required: No

 ** KeyAlgorithm **   <a name="ACM-Type-CertificateDetail-KeyAlgorithm"></a>
The algorithm that was used to generate the public-private key pair.  
Type: String  
Valid Values: `RSA_1024 | RSA_2048 | RSA_3072 | RSA_4096 | EC_prime256v1 | EC_secp384r1 | EC_secp521r1`   
Required: No

 ** KeyUsages **   <a name="ACM-Type-CertificateDetail-KeyUsages"></a>
A list of Key Usage X.509 v3 extension objects. Each object is a string value that identifies the purpose of the public key contained in the certificate. Possible extension values include DIGITAL\_SIGNATURE, KEY\_ENCHIPHERMENT, NON\_REPUDIATION, and more.  
Type: Array of [KeyUsage](API_KeyUsage.md) objects  
Required: No

 ** ManagedBy **   <a name="ACM-Type-CertificateDetail-ManagedBy"></a>
Identifies the AWS service that manages the certificate issued by ACM.  
Type: String  
Valid Values: `CLOUDFRONT`   
Required: No

 ** NotAfter **   <a name="ACM-Type-CertificateDetail-NotAfter"></a>
The time after which the certificate is not valid.  
Type: Timestamp  
Required: No

 ** NotBefore **   <a name="ACM-Type-CertificateDetail-NotBefore"></a>
The time before which the certificate is not valid.  
Type: Timestamp  
Required: No

 ** Options **   <a name="ACM-Type-CertificateDetail-Options"></a>
Contains the certificate options. Certificate transparency logging opt-out is no longer available. All public certificates are recorded in a certificate transparency log.  
Type: [CertificateOptions](API_CertificateOptions.md) object  
Required: No

 ** RenewalEligibility **   <a name="ACM-Type-CertificateDetail-RenewalEligibility"></a>
Specifies whether the certificate is eligible for renewal. At this time, only exported private certificates can be renewed with the [RenewCertificate](API_RenewCertificate.md) command.  
Type: String  
Valid Values: `ELIGIBLE | INELIGIBLE`   
Required: No

 ** RenewalSummary **   <a name="ACM-Type-CertificateDetail-RenewalSummary"></a>
Contains information about the status of ACM's [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) for the certificate. This field exists only when the certificate type is `AMAZON_ISSUED`.  
Type: [RenewalSummary](API_RenewalSummary.md) object  
Required: No

 ** RevocationReason **   <a name="ACM-Type-CertificateDetail-RevocationReason"></a>
The reason the certificate was revoked. This value exists only when the certificate status is `REVOKED`.   
Type: String  
Valid Values: `UNSPECIFIED | KEY_COMPROMISE | CA_COMPROMISE | AFFILIATION_CHANGED | SUPERCEDED | SUPERSEDED | CESSATION_OF_OPERATION | CERTIFICATE_HOLD | REMOVE_FROM_CRL | PRIVILEGE_WITHDRAWN | A_A_COMPROMISE`   
Required: No

 ** RevokedAt **   <a name="ACM-Type-CertificateDetail-RevokedAt"></a>
The time at which the certificate was revoked. This value exists only when the certificate status is `REVOKED`.   
Type: Timestamp  
Required: No

 ** Serial **   <a name="ACM-Type-CertificateDetail-Serial"></a>
The serial number of the certificate.  
Type: String  
Required: No

 ** SignatureAlgorithm **   <a name="ACM-Type-CertificateDetail-SignatureAlgorithm"></a>
The algorithm that was used to sign the certificate.  
Type: String  
Required: No

 ** Status **   <a name="ACM-Type-CertificateDetail-Status"></a>
The status of the certificate.  
A certificate enters status PENDING\_VALIDATION upon being requested, unless it fails for any of the reasons given in the troubleshooting topic [Certificate request fails](https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-failed.html). ACM makes repeated attempts to validate a certificate for 72 hours and then times out. If a certificate shows status FAILED or VALIDATION\_TIMED\_OUT, delete the request, correct the issue with [DNS validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html) or [Email validation](https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html), and try again. If validation succeeds, the certificate enters status ISSUED.   
Type: String  
Valid Values: `PENDING_VALIDATION | ISSUED | INACTIVE | EXPIRED | VALIDATION_TIMED_OUT | REVOKED | FAILED`   
Required: No

 ** Subject **   <a name="ACM-Type-CertificateDetail-Subject"></a>
The name of the entity that is associated with the public key contained in the certificate.  
Type: String  
Required: No

 ** SubjectAlternativeNames **   <a name="ACM-Type-CertificateDetail-SubjectAlternativeNames"></a>
One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website.   
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`   
Required: No

 ** Type **   <a name="ACM-Type-CertificateDetail-Type"></a>
The source of the certificate. For certificates provided by ACM, this value is `AMAZON_ISSUED`. For certificates that you imported with [ImportCertificate](API_ImportCertificate.md), this value is `IMPORTED`. ACM does not provide [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) for imported certificates. For more information about the differences between certificates that you import and those that ACM provides, see [Importing Certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the * AWS Certificate Manager User Guide*.   
Type: String  
Valid Values: `IMPORTED | AMAZON_ISSUED | PRIVATE`   
Required: No

## See Also
<a name="API_CertificateDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/CertificateDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/CertificateDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/CertificateDetail) 