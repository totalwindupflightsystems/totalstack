---
id: "@specs/aws/rds/docs/API_CertificateDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CertificateDetails"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CertificateDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CertificateDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CertificateDetails
<a name="API_CertificateDetails"></a>

The details of the DB instance’s server certificate.

For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.

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
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CertificateDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CertificateDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CertificateDetails) 