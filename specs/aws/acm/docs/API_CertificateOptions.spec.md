---
id: "@specs/aws/acm/docs/API_CertificateOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CertificateOptions"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# CertificateOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_CertificateOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CertificateOptions
<a name="API_CertificateOptions"></a>

Structure that contains options for your certificate. You can use this structure to specify whether to export your certificate.

Certificate transparency logging opt-out is no longer available. All public certificates are recorded in a certificate transparency log. For general information, see [Certificate Transparency Logging](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency).

You can export public ACM certificates to use with AWS services as well as outside AWS Cloud. For more information, see [AWS Certificate Manager exportable public certificate](https://docs.aws.amazon.com/acm/latest/userguide/acm-exportable-certificates.html).

## Contents
<a name="API_CertificateOptions_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CertificateTransparencyLoggingPreference **   <a name="ACM-Type-CertificateOptions-CertificateTransparencyLoggingPreference"></a>
This parameter has been deprecated. Certificate transparency logging opt-out is no longer available. All public certificates are recorded in a certificate transparency log.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** Export **   <a name="ACM-Type-CertificateOptions-Export"></a>
You can opt in to allow the export of your certificates by specifying `ENABLED`. You cannot update the value of `Export` after the the certificate is created.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

## See Also
<a name="API_CertificateOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/CertificateOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/CertificateOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/CertificateOptions) 