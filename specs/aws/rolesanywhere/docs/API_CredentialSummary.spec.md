---
id: "@specs/aws/rolesanywhere/docs/API_CredentialSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CredentialSummary"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# CredentialSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_CredentialSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CredentialSummary
<a name="API_CredentialSummary"></a>

A record of a presented X509 credential from a temporary credential request. 

## Contents
<a name="API_CredentialSummary_Contents"></a>

 ** enabled **   <a name="rolesanywhere-Type-CredentialSummary-enabled"></a>
Indicates whether the credential is enabled.  
Type: Boolean  
Required: No

 ** failed **   <a name="rolesanywhere-Type-CredentialSummary-failed"></a>
Indicates whether the temporary credential request was successful.   
Type: Boolean  
Required: No

 ** issuer **   <a name="rolesanywhere-Type-CredentialSummary-issuer"></a>
The fully qualified domain name of the issuing certificate for the presented end-entity certificate.  
Type: String  
Required: No

 ** seenAt **   <a name="rolesanywhere-Type-CredentialSummary-seenAt"></a>
The ISO-8601 time stamp of when the certificate was last used in a temporary credential request.  
Type: Timestamp  
Required: No

 ** serialNumber **   <a name="rolesanywhere-Type-CredentialSummary-serialNumber"></a>
The serial number of the certificate.  
Type: String  
Required: No

 ** x509CertificateData **   <a name="rolesanywhere-Type-CredentialSummary-x509CertificateData"></a>
The PEM-encoded data of the certificate.  
Type: String  
Required: No

## See Also
<a name="API_CredentialSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/CredentialSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/CredentialSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/CredentialSummary) 