---
id: "@specs/aws/redshift/docs/API_Association"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Association"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# Association

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_Association
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Association
<a name="API_Association"></a>

Contains information about the custom domain name association.

## Contents
<a name="API_Association_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CertificateAssociations.CertificateAssociation.N **   
A list of all associated clusters and domain names tied to a specific certificate.  
Type: Array of [CertificateAssociation](API_CertificateAssociation.md) objects  
Required: No

 ** CustomDomainCertificateArn **   
The Amazon Resource Name (ARN) for the certificate associated with the custom domain.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** CustomDomainCertificateExpiryDate **   
The expiration date for the certificate.  
Type: Timestamp  
Required: No

## See Also
<a name="API_Association_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/Association) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/Association) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/Association) 