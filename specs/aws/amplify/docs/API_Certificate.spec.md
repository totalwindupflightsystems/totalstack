---
id: "@specs/aws/amplify/docs/API_Certificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Certificate"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# Certificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_Certificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Certificate
<a name="API_Certificate"></a>

Describes the current SSL/TLS certificate that is in use for the domain. If you are using `CreateDomainAssociation` to create a new domain association, `Certificate` describes the new certificate that you are creating.

## Contents
<a name="API_Certificate_Contents"></a>

 ** type **   <a name="amplify-Type-Certificate-type"></a>
The type of SSL/TLS certificate that you want to use.  
Specify `AMPLIFY_MANAGED` to use the default certificate that Amplify provisions for you.  
Specify `CUSTOM` to use your own certificate that you have already added to AWS Certificate Manager in your AWS account. Make sure you request (or import) the certificate in the US East (N. Virginia) Region (us-east-1). For more information about using ACM, see [Importing certificates into AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *ACM User guide*.  
Type: String  
Valid Values: `AMPLIFY_MANAGED | CUSTOM`   
Required: Yes

 ** certificateVerificationDNSRecord **   <a name="amplify-Type-Certificate-certificateVerificationDNSRecord"></a>
The DNS record for certificate verification.  
Type: String  
Length Constraints: Maximum length of 1000.  
Required: No

 ** customCertificateArn **   <a name="amplify-Type-Certificate-customCertificateArn"></a>
The Amazon resource name (ARN) for a custom certificate that you have already added to AWS Certificate Manager in your AWS account.   
This field is required only when the certificate type is `CUSTOM`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `^arn:aws:acm:[a-z0-9-]+:\d{12}:certificate\/.+$`   
Required: No

## See Also
<a name="API_Certificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/Certificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/Certificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/Certificate) 