---
id: "@specs/aws/acm/docs/API_CertificateFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CertificateFilter"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# CertificateFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_CertificateFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CertificateFilter
<a name="API_CertificateFilter"></a>

Defines a filter for searching certificates by ARN, X.509 attributes, or ACM metadata.

## Contents
<a name="API_CertificateFilter_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AcmCertificateMetadataFilter **   <a name="ACM-Type-CertificateFilter-AcmCertificateMetadataFilter"></a>
Filter by ACM certificate metadata.  
Type: [AcmCertificateMetadataFilter](API_AcmCertificateMetadataFilter.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** CertificateArn **   <a name="ACM-Type-CertificateFilter-CertificateArn"></a>
Filter by certificate ARN.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: No

 ** X509AttributeFilter **   <a name="ACM-Type-CertificateFilter-X509AttributeFilter"></a>
Filter by X.509 certificate attributes.  
Type: [X509AttributeFilter](API_X509AttributeFilter.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_CertificateFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/CertificateFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/CertificateFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/CertificateFilter) 