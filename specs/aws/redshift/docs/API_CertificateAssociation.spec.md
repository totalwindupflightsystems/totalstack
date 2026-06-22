---
id: "@specs/aws/redshift/docs/API_CertificateAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CertificateAssociation"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CertificateAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CertificateAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CertificateAssociation
<a name="API_CertificateAssociation"></a>

A cluster ID and custom domain name tied to a specific certificate. These are typically returned in a list.

## Contents
<a name="API_CertificateAssociation_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** ClusterIdentifier **   
The cluster identifier for the certificate association.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** CustomDomainName **   
The custom domain name for the certificate association.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_CertificateAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CertificateAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CertificateAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CertificateAssociation) 