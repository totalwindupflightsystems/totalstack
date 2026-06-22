---
id: "@specs/aws/acm/docs/API_RenewalSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RenewalSummary"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# RenewalSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_RenewalSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RenewalSummary
<a name="API_RenewalSummary"></a>

Contains information about the status of ACM's [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) for the certificate. This structure exists only when the certificate type is `AMAZON_ISSUED`.

## Contents
<a name="API_RenewalSummary_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DomainValidationOptions **   <a name="ACM-Type-RenewalSummary-DomainValidationOptions"></a>
Contains information about the validation of each domain name in the certificate, as it pertains to ACM's [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html). This is different from the initial validation that occurs as a result of the [RequestCertificate](API_RequestCertificate.md) request. This field exists only when the certificate type is `AMAZON_ISSUED`.  
Type: Array of [DomainValidation](API_DomainValidation.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Required: Yes

 ** RenewalStatus **   <a name="ACM-Type-RenewalSummary-RenewalStatus"></a>
The status of ACM's [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) of the certificate.  
Type: String  
Valid Values: `PENDING_AUTO_RENEWAL | PENDING_VALIDATION | SUCCESS | FAILED`   
Required: Yes

 ** UpdatedAt **   <a name="ACM-Type-RenewalSummary-UpdatedAt"></a>
The time at which the renewal summary was last updated.  
Type: Timestamp  
Required: Yes

 ** RenewalStatusReason **   <a name="ACM-Type-RenewalSummary-RenewalStatusReason"></a>
The reason that a renewal request was unsuccessful.  
Type: String  
Valid Values: `NO_AVAILABLE_CONTACTS | ADDITIONAL_VERIFICATION_REQUIRED | DOMAIN_NOT_ALLOWED | INVALID_PUBLIC_DOMAIN | DOMAIN_VALIDATION_DENIED | CAA_ERROR | PCA_LIMIT_EXCEEDED | PCA_INVALID_ARN | PCA_INVALID_STATE | PCA_REQUEST_FAILED | PCA_NAME_CONSTRAINTS_VALIDATION | PCA_RESOURCE_NOT_FOUND | PCA_INVALID_ARGS | PCA_INVALID_DURATION | PCA_ACCESS_DENIED | SLR_NOT_FOUND | OTHER`   
Required: No

## See Also
<a name="API_RenewalSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/RenewalSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/RenewalSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/RenewalSummary) 