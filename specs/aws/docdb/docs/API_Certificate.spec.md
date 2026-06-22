---
id: "@specs/aws/docdb/docs/API_Certificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Certificate"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# Certificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_Certificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Certificate
<a name="API_Certificate"></a>

A certificate authority (CA) certificate for an AWS account.

## Contents
<a name="API_Certificate_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CertificateArn **   
The Amazon Resource Name (ARN) for the certificate.  
Example: `arn:aws:rds:us-east-1::cert:rds-ca-2019`   
Type: String  
Required: No

 ** CertificateIdentifier **   
The unique key that identifies a certificate.  
Example: `rds-ca-2019`   
Type: String  
Required: No

 ** CertificateType **   
The type of the certificate.  
Example: `CA`   
Type: String  
Required: No

 ** Thumbprint **   
The thumbprint of the certificate.  
Type: String  
Required: No

 ** ValidFrom **   
The starting date-time from which the certificate is valid.  
Example: `2019-07-31T17:57:09Z`   
Type: Timestamp  
Required: No

 ** ValidTill **   
The date-time after which the certificate is no longer valid.  
Example: `2024-07-31T17:57:09Z`   
Type: Timestamp  
Required: No

## See Also
<a name="API_Certificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/Certificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/Certificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/Certificate) 