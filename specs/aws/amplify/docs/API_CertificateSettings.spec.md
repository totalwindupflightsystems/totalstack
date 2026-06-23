---
id: "@specs/aws/amplify/docs/API_CertificateSettings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CertificateSettings"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# CertificateSettings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_CertificateSettings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CertificateSettings
<a name="API_CertificateSettings"></a>

The type of SSL/TLS certificate to use for your custom domain. If a certificate type isn't specified, Amplify uses the default `AMPLIFY_MANAGED` certificate.

## Contents
<a name="API_CertificateSettings_Contents"></a>

 ** type **   <a name="amplify-Type-CertificateSettings-type"></a>
The certificate type.  
Specify `AMPLIFY_MANAGED` to use the default certificate that Amplify provisions for you.  
Specify `CUSTOM` to use your own certificate that you have already added to AWS Certificate Manager in your AWS account. Make sure you request (or import) the certificate in the US East (N. Virginia) Region (us-east-1). For more information about using ACM, see [Importing certificates into AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *ACM User guide*.  
Type: String  
Valid Values: `AMPLIFY_MANAGED | CUSTOM`   
Required: Yes

 ** customCertificateArn **   <a name="amplify-Type-CertificateSettings-customCertificateArn"></a>
The Amazon resource name (ARN) for the custom certificate that you have already added to AWS Certificate Manager in your AWS account.  
This field is required only when the certificate type is `CUSTOM`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `^arn:aws:acm:[a-z0-9-]+:\d{12}:certificate\/.+$`   
Required: No

## See Also
<a name="API_CertificateSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/CertificateSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/CertificateSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/CertificateSettings) 