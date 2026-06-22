---
id: "@specs/aws/acm/docs/API_DomainValidation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DomainValidation"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# DomainValidation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_DomainValidation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DomainValidation
<a name="API_DomainValidation"></a>

Contains information about the validation of each domain name in the certificate.

## Contents
<a name="API_DomainValidation_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DomainName **   <a name="ACM-Type-DomainValidation-DomainName"></a>
A fully qualified domain name (FQDN) in the certificate. For example, `www.example.com` or `example.com`.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`   
Required: Yes

 ** HttpRedirect **   <a name="ACM-Type-DomainValidation-HttpRedirect"></a>
Contains information for HTTP-based domain validation of certificates requested through Amazon CloudFront and issued by ACM. This field exists only when the certificate type is `AMAZON_ISSUED` and the validation method is `HTTP`.  
Type: [HttpRedirect](API_HttpRedirect.md) object  
Required: No

 ** ResourceRecord **   <a name="ACM-Type-DomainValidation-ResourceRecord"></a>
Contains the CNAME record that you add to your DNS database for domain validation. For more information, see [Use DNS to Validate Domain Ownership](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html).  
The CNAME information that you need does not include the name of your domain. If you include your domain name in the DNS database CNAME record, validation fails. For example, if the name is `_a79865eb4cd1a6ab990a45779b4e0b96.yourdomain.com`, only `_a79865eb4cd1a6ab990a45779b4e0b96` must be used.
Type: [ResourceRecord](API_ResourceRecord.md) object  
Required: No

 ** ValidationDomain **   <a name="ACM-Type-DomainValidation-ValidationDomain"></a>
The domain name that ACM used to send domain validation emails.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`   
Required: No

 ** ValidationEmails **   <a name="ACM-Type-DomainValidation-ValidationEmails"></a>
A list of email addresses that ACM used to send domain validation emails.  
Type: Array of strings  
Required: No

 ** ValidationMethod **   <a name="ACM-Type-DomainValidation-ValidationMethod"></a>
Specifies the domain validation method.  
Type: String  
Valid Values: `EMAIL | DNS | HTTP`   
Required: No

 ** ValidationStatus **   <a name="ACM-Type-DomainValidation-ValidationStatus"></a>
The validation status of the domain name. This can be one of the following values:  
+  `PENDING_VALIDATION` 
+  ``SUCCESS
+  ``FAILED
Type: String  
Valid Values: `PENDING_VALIDATION | SUCCESS | FAILED`   
Required: No

## See Also
<a name="API_DomainValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/DomainValidation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/DomainValidation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/DomainValidation) 