---
id: "@specs/aws/redshift/docs/API_HsmClientCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HsmClientCertificate"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# HsmClientCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_HsmClientCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HsmClientCertificate
<a name="API_HsmClientCertificate"></a>

Returns information about an HSM client certificate. The certificate is stored in a secure Hardware Storage Module (HSM), and used by the Amazon Redshift cluster to encrypt data files.

## Contents
<a name="API_HsmClientCertificate_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** HsmClientCertificateIdentifier **   
The identifier of the HSM client certificate.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** HsmClientCertificatePublicKey **   
The public key that the Amazon Redshift cluster will use to connect to the HSM. You must register the public key in the HSM.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Tags.Tag.N **   
The list of tags for the HSM client certificate.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## See Also
<a name="API_HsmClientCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/HsmClientCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/HsmClientCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/HsmClientCertificate) 