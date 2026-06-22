---
id: "@specs/aws/docdb/docs/API_CertificateDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CertificateDetails"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# CertificateDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_CertificateDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CertificateDetails
<a name="API_CertificateDetails"></a>

Returns the details of the DB instance’s server certificate.

For more information, see [Updating Your Amazon DocumentDB TLS Certificates](https://docs.aws.amazon.com/documentdb/latest/devguide/ca_cert_rotation.html) and [ Encrypting Data in Transit](https://docs.aws.amazon.com/documentdb/latest/devguide/security.encryption.ssl.html) in the *Amazon DocumentDB Developer Guide*.

## Contents
<a name="API_CertificateDetails_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CAIdentifier **   
The CA identifier of the CA certificate used for the DB instance's server certificate.  
Type: String  
Required: No

 ** ValidTill **   
The expiration date of the DB instance’s server certificate.  
Type: Timestamp  
Required: No

## See Also
<a name="API_CertificateDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/CertificateDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/CertificateDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/CertificateDetails) 