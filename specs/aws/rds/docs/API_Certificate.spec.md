---
id: "@specs/aws/rds/docs/API_Certificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Certificate"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# Certificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_Certificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Certificate
<a name="API_Certificate"></a>

A CA certificate for an AWS account.

For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.

## Contents
<a name="API_Certificate_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CertificateArn **   
The Amazon Resource Name (ARN) for the certificate.  
Type: String  
Required: No

 ** CertificateIdentifier **   
The unique key that identifies a certificate.  
Type: String  
Required: No

 ** CertificateType **   
The type of the certificate.  
Type: String  
Required: No

 ** CustomerOverride **   
Indicates whether there is an override for the default certificate identifier.  
Type: Boolean  
Required: No

 ** CustomerOverrideValidTill **   
If there is an override for the default certificate identifier, when the override expires.  
Type: Timestamp  
Required: No

 ** Thumbprint **   
The thumbprint of the certificate.  
Type: String  
Required: No

 ** ValidFrom **   
The starting date from which the certificate is valid.  
Type: Timestamp  
Required: No

 ** ValidTill **   
The final date that the certificate continues to be valid.  
Type: Timestamp  
Required: No

## See Also
<a name="API_Certificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/Certificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/Certificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/Certificate) 